import pandas as pd
import numpy as np
import re

def nomCols(df, dic):
    for column in df.columns:
        df.rename(columns={column: column.lower()}, inplace=True)
    for column in df.columns:
        for key in dic.keys():
            if column == key:
                nom = column.replace(column, dic[key])
                df.rename(columns={column: nom}, inplace=True)
            elif key in column:
                nom = column.replace(key, dic[key])
                df.rename(columns={column: nom}, inplace=True)
    return df

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
    df['pais'] = df['pais'].apply(lambda x: x.split(', ')[0])

    cols=['pais','pais_iso','indicador']
    df1=pd.melt(df,id_vars=cols,var_name='anio',value_name='frecuencia')
    df1["frecuencia"] = df1.frecuencia.replace(np.nan, 0)
    
    # df1.to_csv('datasets/desastres_naturales/Climate-related_Disasters_Frequency_normalizado.csv',sep=';',index=False)
    return df1