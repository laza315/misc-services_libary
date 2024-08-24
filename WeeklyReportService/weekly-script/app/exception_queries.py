from sqlalchemy import create_engine
import pandas as pd
import os
import config as config
from sqlalchemy import text


def tasks_info_query_exception(env_name):
    engine1 = create_engine(
        f"mysql+pymysql://{config.MYSQL_CRED[env_name]['username']}:{config.MYSQL_CRED[env_name]['password']}@{config.MYSQL_CRED[env_name]['host']}/db",
        connect_args={'ssl': {'ssl-mode': f'{os.getcwd()}/RapidSSLCABundle.pem'}})

    # Test the connection
    connection1 = engine1.connect()

    query = connection1.execute(text(f'{exception_query}'))

    result = query.fetchall()
    df = pd.DataFrame(result)
    return df




