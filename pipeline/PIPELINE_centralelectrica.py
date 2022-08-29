import pandas as pd

def listcol_df(dataframe):
    return dataframe.columns.to_list()


def gppdb():
    dataframe = pd.read_csv(
        "../datasets/global_power_plant_database.csv", low_memory=False
    )
    df = dataframe.copy()

    dict_cols = {
        "country_long": "pais",
        "country": "codigo_iso",
        "name": "nombre",
        "gppd_idnr": "ID_central_electrica",
        "capacity_mw": "capacidad_MW",
        "latitude": "latitud",
        "longitude": "longitud",
        "primary_fuel": "energia_primaria",
        "other_fuel1": "otra_energia1",
        "other_fuel2": "otra_energia2",
        "other_fuel3": "otra_energia3",
        "commissioning_year": "año_apertura",
        "owner": "dueño",
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

    a = listcol_df(df)
    del a[18:25]
    df1 = pd.melt(df, id_vars=a, var_name="anio", value_name="GWh_x_anio")

    dropiar = [
        "ID_central_electrica",
        "otra_energia2",
        "otra_energia3",
        "dueño",
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


# central=gppdb()
# central.to_parquet('../datasets/NORMALIZADO_central_electrica.parquet')
