import pandas as pd
from pipeline.PIPELINE_renewableenergy import tools

t=tools()

def pp_extract():
    return t.readcsv(
        "datasets/global_power_plant_database.csv"
    ).copy()

def pp_transform(data):
    df = data
    dict_cols = {
        "country_long": "pais",
        "country": "codigo_iso",
        "name": "nombre",
        "capacity_mw": "capacidad_MW",
        "latitude": "latitud",
        "longitude": "longitud",
        "primary_fuel": "energia_primaria",
        "other_fuel1": "otra_energia1",
        "commissioning_year": "año_apertura",
        "year_of_capacity_data": "año_capacidad_reportada",
        "generation_gwh_2013": 2013,
        "generation_gwh_2014": 2014,
        "generation_gwh_2015": 2015,
        "generation_gwh_2016": 2016,
        "generation_gwh_2017": 2017,
        "generation_gwh_2018": 2018,
        "generation_gwh_2019": 2019,
    }
    df.rename(columns=dict_cols, inplace=True)

    a = t.listar(df.columns)
    del a[18:25]
    df1 = pd.melt(df, id_vars=a, var_name="anio", value_name="GWh_x_anio")

    dropiar = [
        "gppd_idnr",
        "other_fuel2",
        "other_fuel3",
        "owner",
        "source",
        "url",
        "geolocation_source",
        "wepp_id",
        "generation_data_source",
        "estimated_generation_gwh_2013",
        "estimated_generation_gwh_2014",
        "estimated_generation_gwh_2015",
        "estimated_generation_gwh_2016",
        "estimated_generation_gwh_2017",
        "estimated_generation_note_2013",
        "estimated_generation_note_2014",
        "estimated_generation_note_2015",
        "estimated_generation_note_2016",
        "estimated_generation_note_2017",
    ]
    df1.drop(columns=dropiar, inplace=True)

    return df1
