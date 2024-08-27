from load_data_poo import Cload_data

name_schema = 'dwh'
table_name ='tb_pkmn_clean'
table_file = 'tb_pokemon_clean.csv'

if __name__ == '__main__':
  etl_carga = Cload_data(name_schema,table_name,table_file)
  #etl_carga.process()
  etl_carga.process_copy()
