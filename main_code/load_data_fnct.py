import sys
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
sys.path.append('/Users/edugonzo/Desktop/GitRepos_work/pandas_pkmn/config_param')
import myconfig # pyright: ignore[reportMissingImports]

db_params = {
                'host': myconfig.v_host,
                'database': myconfig.v_database,
                'user': myconfig.v_user,
                'password': myconfig.v_password,
                'port' : myconfig.v_port
                }
                
str_conn = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/defaultdb?sslmode=require"
   