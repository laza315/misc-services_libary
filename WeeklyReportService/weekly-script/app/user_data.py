from sqlalchemy import create_engine
import pandas as pd
import os
import config as config
import numpy as np
from sqlalchemy import text
import logging


def tasks_info_query(env_name, start_date, end_date):

    engine1 = create_engine(
        f"mysql+pymysql://{config.MYSQL_CRED[env_name]['username']}:{config.MYSQL_CRED[env_name]['password']}@{config.MYSQL_CRED[env_name]['host']}/db",
        connect_args={'ssl': {'ssl-mode': f'{os.getcwd()}/RapidSSLCABundle.pem'}})

    connection1 = engine1.connect()

# TODO: Update query with other bg groups on other envs which shouldn't be monitored, if need it
    query1 = connection1.execute(text(
        f'select a.owner as owner_id, tasks.status,a.name as group_name, p.env_id as all_tasks \n'
        f'from contexts tcc join funding_source_transactions bb on \n'
        f'bb.id = tcc.funding_source_transactions \n'
        f'JOIN fs fs ON fst.fs = fs.id \n'
        f'JOIN fsat on fsat.fs_id=fs.id join fstags on fstags.id=fsat.tag \n'
        f'JOIN tasks on task_id=.tasks.platform_id \n'
        f'JOIN task_execution_status on tasks.state = task_execution_status.id \n'
        f'where (left(from_unixtime(tasks.time_finished/1000), 19) >= "{start_date}") \n'
        f'and left(from_unixtime(tasks.time_finished/1000), 19) < "{end_date}" \n'
        f'and fsat.tag_id = 11 and fs.active = 1 \n'
        f'and tasks.is_bedb_task = 0 \n'
        f'and tasks.mocked = 0 \n'
    ))

    result = query1.fetchall()
    df = pd.DataFrame(result)
    return df


def process_client_billing_groups(df, env_name):
    distinct_divs = df['div_id'].unique()
    result_dfs = []
    for div in distinct_divs:
        postgree_conn = create_engine(f"postgresql+psycopg2://{config.POSTGRES_CRED[env_name]['username']}:{config.POSTGRES_CRED[env_name]['password']}@{config.POSTGRES_CRED[platform_name]['host']}/db")

        with postgree_conn.connect() as postgree_connection:
            result2 = postgree_connection.execute(text(
                        f"select client.id as ent_id, client.name as ent_name, organization.public_id as div_id, organization.name as div_name \n"
                        f"from client_account join organization on client_account.id = organization.client_account_id \n"
                        f"where organization.public_id in ('{div}')"))

            query2 = result2.fetchall()
            df2 = pd.DataFrame(query2)
            merged_df = pd.merge(df, df2, on='div_id')

            if not df2.empty:
                ent_name = merged_df['ent_name'].iloc[0]
                merged_df['client_name'] = ent_name
                merged_df['completed'] = np.where(merged_df['status'] == 'COMPLETED', 1, 0)
                merged_df['failed'] = np.where(merged_df['status'] == 'FAILED', 1, 0)
                merged_df['aborted'] = np.where(merged_df['status'] == 'ABORTED', 1, 0)
            elif df2.empty:
                logging.warn(msg='There is no client')

            result_dfs.append(merged_df)

    if result_dfs:
        final_result_df = pd.concat(result_dfs, ignore_index=True)

        result_summary = final_result_df.groupby(['client_name', 'billing_group_name']).agg({
            'all_tasks': 'count',
            'completed': 'sum',
            'failed': 'sum',
            'aborted': 'sum'
        })

        final = result_summary.groupby(['client_name']).agg({
            'all_tasks': 'sum',
            'completed': 'sum',
            'failed': 'sum',
            'aborted': 'sum'
        })

        final = final.reset_index()

        return final


def create_report(file, start_date, end_date, env_name):
    subdir = "reports"

    if not os.path.exists(subdir):
        os.mkdir(subdir)

    file_path = os.path.join(subdir, f'Client report for {start_date}-{end_date} on {env_name} env.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'r') as existing_file:
            existing_content = existing_file.read()
            logging.info(msg=f"This report already exist. Please find it at {file_path}")
            return existing_content
    else:
        if file is not None and isinstance(file, pd.DataFrame):
            file.to_excel(file_path, index=True, startrow=1)
            logging.info(msg=f"Please find the report at {file_path}")
        else:
            logging.info(msg="The file contains no results for selected period")


