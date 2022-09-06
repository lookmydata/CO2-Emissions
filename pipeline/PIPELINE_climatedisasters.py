# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3.9.1 64-bit
#     language: python
#     name: python3
# ---

import pandas as pd

df=pd.read_csv('../datasets/desastres_naturales/Climate-related_Disasters_Frequency_normalizado.csv',sep=';')
print(df)

<<<<<<< HEAD
# +
col=['Unnamed: 0','objectid','iso2','code','unidad','fuente']

df.drop(columns=col,inplace=True)
# +
cols=['pais','pais_iso','indicador']

df1=pd.melt(df,id_vars=cols,var_name='anio',value_name='frecuencia')

#df1.to_csv('../datasets/desastres_naturales/Climate-related_Disasters_Frequency_normalizado.csv',sep=';',index=False)
=======
def extract_cd():
    return pd.read_csv('datasets/desastres_naturales/Climate-related_Disasters_Frequency.csv')

dic_cols = {'country':'pais','type':'tipo','year':'anio','consumption':'cons','production':'produccion','gdp':'pbi','population':'poblacion','intensity':'intensidad','emission':'emision_co2','indicator':'indicador','fuel':'combustible','wind':'eolica','electricity':'elec','energy':'energia','iso_code':'pais_iso','share':'participacion','renewable':'renovable','oil':'petroleo','change':'cambio','coal':'carbon','time':'periodo','product':'producto','value':'valor','unit':'unidad','iso3':'pais_iso','source':'fuente'}

def transform_cd():
    df=extract_cd()
    nomCols(df,dic_cols)
    df = df.drop(columns=['objectid','iso2','code','unidad','fuente'])
    df.iloc[:,5:] = df.iloc[:,5:].fillna(0)
    for column in df.columns:
        if re.search('f\d{2,}', column):
            nom = column.split('f')[1]
            df[column]=df[column].round(2)
            df.rename(columns={column:nom},inplace=True)

    df['indicador'] = df['indicador'].apply(lambda x: x.split(': ')[1])

    cols=['pais','pais_iso','indicador']
    df1=pd.melt(df,id_vars=cols,var_name='anio',value_name='frecuencia')
    df1["frecuencia"] = df1.frecuencia.replace(np.nan, 0)

    return df1
    # df1.to_csv('datasets/desastres_naturales/Climate-related_Disasters_Frequency_normalizado.csv',sep=';',index=False)
>>>>>>> 7886e4c (c.disasters_pline)
