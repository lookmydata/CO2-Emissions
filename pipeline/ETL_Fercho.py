# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3.10.6 64-bit
#     language: python
#     name: python3
# ---

import pandas as pd
import re
import requests

dic_cols = {
    "country": "pais",
    "type": "tipo",
    "year": "anio",
    "consumption": "cons",
    "production": "produccion",
    "gdp": "pbi",
    "population": "poblacion",
    "intensity": "intensidad",
    "emission": "emision_co2",
    "indicator": "indicador",
    "fuel": "combustible",
    "wind": "eolica",
    "electricity": "elec",
    "energy": "energia",
    "iso_code": "pais_iso",
    "share": "participacion",
    "renewable": "renovable",
    "oil": "petroleo",
    "change": "cambio",
    "coal": "carbon",
    "time": "periodo",
    "product": "producto",
    "value": "valor",
    "unit": "unidad",
    "iso3": "pais_iso",
    "source": "fuente",
}


# +
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


def dropBeforeYear(df, year):
    lista = ["year", "anio", "año"]
    for column in df.columns:
        if column.lower() in lista:
            df = df[df[column] >= year].reset_index(drop=True)
    return df


# -

# **EnergyCO2**

dataset = pd.read_csv(r"..\energyco2.csv")
df = pd.DataFrame(dataset)

# Dropeo la columna Unnamed: 0 que no contiene informacion

df = df.drop(columns="Unnamed: 0")


# Le paso una serie y un tipo para chequear si los elementos de la serie pertenecen a esa clase o no
def chequeoTipo(serie, clase):
    pertenece = False
    lista = []
    for item in serie:
        if isinstance(item, clase):
            pertenece = True
        else:
            lista.append(item)
    if len(lista) > 0:
        return lista
    else:
        return pertenece


# +
# for item in df.columns:
#     for i in range(0,df.shape[0]):
#         if df[i,item]:
#             print(f"{item}:{type(df[item][i])}")
# -

chequeoTipo(df["CO2_emission"], float)

# Todos los features tienen elementos de las clases adecuadas para sus datos

# Renombro columnas usando snake_case en español según definido por el equipo de trabajo

# Una vez que ya chequee que cada columna tenga el tipo de dato adecuado, puedo usar esa condicion para chequear todas las columnas y convertir a float de dos digitos

for columna in df.columns:
    if isinstance(df[columna][1], float):
        df[columna] = df[columna].round(2)

# <hr>

# <h1>Climate Related Disasters Frequency</h1>
# <h2><i>Version CSV</i></h2>

dataset = pd.read_csv(
    r"..\desastres_naturales\Climate-related_Disasters_Frequency.csv"
)
df2 = pd.DataFrame(dataset)

df2.head(2)

df2 = df2.drop(columns=["ObjectId", "ISO2", "Code", "Unit"])

# Convierto NaN en ceros (en este caso se trata de frecuencias)

df2.iloc[:, 5:] = df2.iloc[:, 5:].fillna(0)

# Aplico la funcion para renombrar columnas nomCols usando el diccionario creado, dic_cols

nomCols(df2, dic_cols)

df2.iloc[:, 5:] = df2.iloc[:, 5:].fillna(0)
for column in df2.columns:
    if re.search("f\d{2,}", column):
        nom = column.split("f")[1]
        df2[column] = df2[column].round(2)
        df2.rename(columns={column: nom}, inplace=True)

df2.indicador.unique()

# Recorto los datos de la columna indicador para mostrar unicamente los descriptores

df2["indicador"] = df2["indicador"].apply(lambda x: x.split(": ")[1])

df2.to_parquet(
    r"..\desastres_naturales\Climate-related_Disasters_Frequency_normalizado.parquet"
)

# <hr>

# <h1>OWID-Energy-Consumption-Source</h1>

dataset = pd.read_csv(
    r"..\energy_consumption\owid-energy-consumption-source.csv"
)
df3 = pd.DataFrame(dataset)

df3.head()

for i in range(3, 128):
    if chequeoTipo(df3.iloc[:, i], float):
        continue
    else:
        print(f"{df3.iloc[0:1,i]}")

# Renombro columnas y me quedo con datos de 1980 en adelante

nomCols(df3, dic_cols)
df3 = dropBeforeYear(df3, 1980)

for columna in df3.columns:
    if isinstance(df3[columna][2], float):
        df3[columna] = df3[columna].round(2)

df3.shape

df3.dropna(thresh=4)

# Elijo columnas que brindan informacion de cambio y 'per_capita' (no necesito esa info en el analisis planteado e igualmente puedo calcularlo con los demás datos de ser necesario)

lista = []
for column in df3.columns:
    if (
        "_pct" in column
        or "cambio" in column
        or "per_capita" in column
        or "_participacion_" in column
    ):
        lista.append(column)

df3 = df3.drop(columns=lista)

df3.head()

df3.to_parquet(
    r"..\energy_consumption\owid-energy-consumption-source_normalizado.parquet"
)

# <hr>

# <h1>Energia Estadistica Mensual</h1>

dataset = pd.read_csv(r"..\energia_estadistica_mensual\MES_0522.csv")
df4 = pd.DataFrame(dataset)

df4.head(1)

nomCols(df4, dic_cols)

df4.shape

df4.dropna(subset="valor", inplace=True)

df4.isna().sum()

pertenece = False
lista = []
for item in df4.iloc[:, 4]:
    if isinstance(item, float):
        pertenece = True
    else:
        lista.append((item, df4.columns[i]))
if len(lista) > 0:
    print(lista)
else:
    print(pertenece)

df4["periodo"] = pd.to_datetime(df4["periodo"])
df4["valor"] = df4["valor"].round(2)
df4["anio"] = df4["periodo"].dt.year
df4["mes"] = df4["periodo"].dt.month

df4 = df4[["anio", "mes", "pais", "balance", "producto", "valor"]].sort_values(
    by=["anio", "mes"]
)
df4.rename(columns={"valor": "cons_energia_gwh"}, inplace=True)


df4.to_parquet(
    r"C:\Users\ferch\Desktop\Henry\Proyecto Grupal\CO2-Emissions\datasets\energia_estadistica_mensual\MES_O522_normalizado.parquet"
)

# <h1>Climate Related Disasters Frequency</h1>
# <h2>Versión API</h2>

url = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_11_1_Physical_Risks_Climate_related_disasters_frequency/FeatureServer/0/query?where=1%3D1&outFields=Country,ISO3,Indicator,Source,F1980,F1981,F1982,F1983,F1984,F1985,F1986,F1987,F1988,F1989,F1990,F1991,F1992,F1993,F1994,F1995,F1996,F1997,F1998,F1999,F2000,F2001,F2002,F2003,F2004,F2005,F2006,F2007,F2008,F2009,F2010,F2011,F2012,F2013,F2014,F2015,F2016,F2017,F2018,F2019,F2020,F2021&outSR=4326&f=json"
response = requests.get(url).json()

df5 = pd.DataFrame()

lista = [item for item in response["features"][0]["attributes"].keys()]

for i in range(0, len(response["features"])):
    df = pd.DataFrame.from_dict([response["features"][i]["attributes"]])
    data = (df5, df)
    df5 = pd.concat(data)

df5.reset_index(drop=True, inplace=True)

nomCols(df5, dic_cols)

df5.iloc[:, 5:]

# Cambio nombres de columnas y aplico un fillna sobre los campos de frecuencias para luego aplicar un round

for column in df5.columns:
    if re.search("f\d{2,}", column):
        df5[column] = df5[column].fillna(0)
        nom = column.split("f")[1]
        df5[column] = df5[column].round(2)
        df5.rename(columns={column: nom}, inplace=True)

df5["indicador"] = df2["indicador"].apply(lambda x: x.split(": ")[1])

df6 = df5.groupby(by="pais").sum().transpose()

df5.head()
