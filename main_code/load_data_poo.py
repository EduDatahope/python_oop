# POO Example

import sys
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
sys.path.append('/Users/edugonzo/Desktop/GitRepos_work/pandas_pkmn/config_param')
import myconfig # pyright: ignore[reportMissingImports]

class Cload_data:


    def __init__(self , cschema:str , ctable_name:str , ctable_file:str):
        self.cschema=cschema
        self.ctable_name=ctable_name
        self.ctable_file=ctable_file
    
    def process(self):
            
            print('---- inicializando proceso------')
            db_params = {
                'host': myconfig.v_host,
                'database': myconfig.v_database,
                'user': myconfig.v_user,
                'password': myconfig.v_password,
                'port' : myconfig.v_port
                }
                
            str_conn = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/defaultdb?sslmode=require"
                
            conn = psycopg2.connect(str_conn)
            db = create_engine(str_conn)
            conn_eng = db.connect()
            conn.autocommit = True
            cur = conn.cursor()

            full_file = myconfig.v_path + self.ctable_file
            v_query = 'SET search_path TO ' + self.cschema
            print(v_query)
            cur.execute(v_query)

            v_query = 'truncate table ' + self.ctable_name
            print(v_query)
            cur.execute(v_query)

            print('---- fin 1::succes truncate----')

            df = pd.read_csv( full_file , sep=';')
            df.to_sql(name=self.ctable_name,con=conn_eng,if_exists='append',schema=self.cschema,index=False)
            print('---- fin 2::succes load dataframe----')

            conn.close()

    def process_copy(self):
            
            print('---- inicializando proceso copy------')
            db_params = {
                'host': myconfig.v_host,
                'database': myconfig.v_database,
                'user': myconfig.v_user,
                'password': myconfig.v_password,
                'port' : myconfig.v_port
                }
                
            str_conn = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/defaultdb?sslmode=require"
                
            conn = psycopg2.connect(str_conn)
            db = create_engine(str_conn)
            conn_eng = db.connect()
            conn.autocommit = True
            cur = conn.cursor()

            full_file = myconfig.v_path + self.ctable_file
            v_query = 'SET search_path TO ' + self.cschema
            print(v_query)
            cur.execute(v_query) 

            print(' ----------- Import usin sql cursor -------- : succes')

            with open(full_file, 'r') as f:
            # Notice that we don't need the csv module.
                 next(f) # Skip the header row.
                 cur.copy_from(f, self.ctable_name, sep=';')