from sqlalchemy import create_engine
import pandas as pd
import os
import config as config
import numpy as np
from sqlalchemy import text
import logging


def tasks_info_query_regular_data(env_name, start_date, end_date):
    engine1 = create_engine(
        f"mysql+pymysql://{config.MYSQL_CRED[env_name]['username']}:{config.MYSQL_CRED[env_name]['password']}@"
        f"{config.MYSQL_CRED[env_name]['host']}/db",
        connect_args={'ssl': {'ssl-mode': f'{os.getcwd()}/RapidSSLCABundle.pem'}})

    connection1 = engine1.connect()

    query = connection1.execute(text(f'select a.owner as owner_id, tasks.status,a.name as group_name, '
                                     f'p.env_id as all_tasks \n'
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
        f'and tasks.mocked = 0 \n'), '+' '{exception_query}')

    result = query.fetchall()
    df = pd.DataFrame(result)
    return df


def process_regular_data_billing_groups(df):
    try:
        if True:
            df.loc[:, 'completed'] = np.where(df['status'] == 'COMPLETED', 1, 0)
            df.loc[:, 'failed'] = np.where(df['status'] == 'FAILED', 1, 0)
            df.loc[:, 'aborted'] = np.where(df['status'] == 'ABORTED', 1, 0)

            gather = df.groupby(['billing_group_name']).agg({'all_tasks': 'count', 'completed': 'sum', 'failed': 'sum',
                                                             'aborted': 'sum'})
            final = gather.reset_index()

        return final
    except KeyError:
        logging.info(msg="In the selected period, there were no task runs on for regular Client billing group")


def create_report(file, start_date, end_date, env_name):
    subdir = "reports"

    if not os.path.exists(subdir):
        os.mkdir(subdir)

    file_path = os.path.join(subdir, f'Regular report for {start_date}-{end_date} on {env_name} env.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'r') as existing_file:
            existing_content = existing_file.read()
            logging.warn(msg="This report already exist. Please find it at {file_path}")
            return existing_content
    else:
        if file is not None and isinstance(file, pd.DataFrame):
            file.to_excel(file_path, index=True, startrow=1)
            logging.info(msg=f"Please find the report at {file_path}")
        else:
            logging.info(msg="The file contains no results for selected period")


