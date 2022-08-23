from PIPELINE_centralelectrica import gppdb

def get_tabla_pais():
    df1=gppdb()
    tabla_pais=df1[['codigo_iso','pais']].copy().drop_duplicates()
    return tabla_pais

# tabla=get_tabla_pais()
# tabla.to_parquet('../datasets/tabla_pais.parquet')