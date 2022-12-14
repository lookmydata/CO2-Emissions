import pandas as pd
import numpy as np
from pyarrow import TransformInputStream

from src.etl.common import STANDARD_COLUMNS
from pipeline.PIPELINE_renewableenergy import gtf_transform
from pipeline.PIPELINE_powerplant import pp_transform
from pipeline.norm_enfermedades import NormEnfermedades


# funcion valen
# def gppdb():
#     dataframe = pd.read_csv(
#         "../datasets/global_power_plant_database.csv", low_memory=False
#     )
#     df = dataframe.copy()
# 
#     dict_cols = {
#         "country_long": "pais",
#         "country": "codigo_iso",
#         "name": "nombre",
#         "gppd_idnr": "ID_central_electrica",
#         "capacity_mv": "capacidad_mv",
#         "latitude": "latitud",
#         "longitude": "longitud",
#         "primary_fuel": "combustible_primario",
#         "other_fuel1": "otra_energia1",
#         "other_fuel2": "otra_energia2",
#         "other_fuel3": "otra_energia3",
#         "commissioning_year": "año_apertura",
#         "owner": "dueño",
#         "year_of_capacity_data": "año_capacidad_reportada",
#         "generation_gwh_2013": "2013",
#         "generation_gwh_2014": "2014",
#         "generation_gwh_2015": "2015",
#         "generation_gwh_2016": "2016",
#         "generation_gwh_2017": "2017",
#         "generation_gwh_2018": "2018",
#         "generation_gwh_2019": "2019",
#     }
#     df.rename(columns=dict_cols, inplace=True)


# dataset = pd.read_csv(
#     "../../datasets/desastres_naturales/Climate-related_Disasters_Frequency.csv"
# )
# print(dataset.columns)


# dataset = pd.read_csv(
#     "../../datasets/energy_consumption/owid-energy-consumption-source.csv"
# )

# print(dataset.columns)


# Climate disasters


class Transform(pd.DataFrame):

    def __init__(self, *args, **kwargs):
        return super(Transform, self).__init__(*args, **kwargs)


    @property
    def _constructor(self):
        return Transform


    def rename_by_substring(self):
        """
        Rename the columns by substrings
        """
        data = self.copy()
        data.columns = data.columns.str.strip().str.lower()
        columns = "$$".join(data.columns)
        for key, value in STANDARD_COLUMNS.items():
            columns = columns.replace(key, value)
        data = data.rename(
            columns=dict(zip(data.columns, columns.split("$$")))
        )
        return data


    def rename_columns(self, *args, **kwargs):
        data = self.copy()
        data.columns = data.columns.str.strip().str.lower()
        if args or kwargs:
            return data.rename(*args, **kwargs)
        else:
            return data.rename(columns=STANDARD_COLUMNS)


    def drop_before_year(self, year):
        """
        Drop all rows less than selected year
        """
        data = self.copy()
        column = "anio"
        assert (
            column in data.columns
        ), "No se encuentra la columna 'anio'. Renombralas y vuelve a intentar"
        return data[data[column] >= year].reset_index(drop=True)


    def type_checker(self, column, clase):
        """
        Check all types of dataset
        """
        pertenece = False
        lista = []
        for item in self.data[column]:
            if isinstance(item, clase):
                pertenece = True
            else:
                lista.append(item)
        if len(lista) > 0:
            return lista
        else:
            return pertenece


    def fillna_col(self, column, value):
        data = self.copy()
        data[column] = data[column].fillna(value)
        return data


    def apply_split(self, column, char, position=0):
        data = self.copy()
        data[column] = data[column].apply(lambda x: x.split(char)[position])
        return data


    def map_column(self, column, *args, **kwargs):
        data = self.copy()
        data[column] = data[column].apply(*args, **kwargs)
        return data


    def replace_string(self, column, *args, **kwargs):
        data = self.copy()
        data[column] = data[column].replace(*args, **kwargs, regex=True)
        return data


    def to_datetime(self, column):
        data = self.copy()
        data[column] = pd.to_datetime(data[column])
        return data


    def create_column(self, name, sentence):
        data = self.copy()
        data[name] = eval(sentence)
        return data


    @classmethod
    def desastres_naturales(cls, data):
        data = pd.read_json(data)
        return (
            cls(data)
            .drop(columns=["ObjectId", "ISO2", "Code", "Unit"])
            .melt(
                id_vars=["Country", "ISO3", "Indicator", "Source"],
                var_name="anio",
                value_name="frecuencia",
            )
            .fillna_col("frecuencia", 0)
            .rename_columns()
            .replace_string("anio", "F", "")
            .apply_split("indicador", ": ", 1)
            .apply_split("pais", ",")
            .astype(
                {
                    "anio": np.int32,
                    "frecuencia": np.float32,
                    "pais": "string",
                    "pais_iso": "string",
                    "indicador": "string",
                    "fuente": "string",
                }
            )
        ).to_json()


    @classmethod
    def energiaco2(cls, data):
        data = pd.read_json(data)
        return (
            cls(data)
            .drop(columns="Unnamed: 0")
            .rename_columns()
            .round(2)
        ).to_json()

    
    @classmethod
    def consumo_energia(cls, data):
        data = pd.read_json(data)
        return (
            cls(data)
            .drop([
                    c
                    for c in data.columns
                    if "_pct" in c
                    or "change" in c
                    or "per_capita" in c
                    or "share" in c
                ], axis=1
            )
            .rename_columns()
            .rename_by_substring()
            .drop_before_year(1980)
            .round(2)
            .dropna(thresh=4)
            # .astype(
            #     {
            #         "pais": "string",
            #         "pais_iso": "string",
            #     }
            # )
        ).to_json()


    @classmethod
    def energia_estadistica_mensual(cls, data):
        data = pd.read_json(data)
        return (
            cls(data)
            .rename_columns()
            .dropna(subset="valor")
            .to_datetime("periodo")
            .round(2)
            .create_column("anio", "data['periodo'].dt.year")
            .create_column("mes", "data['periodo'].dt.month")
            .drop(columns=["periodo"])
            .rename_columns(columns={"valor": "cons_energia_gwh"})
        ).to_json()

    
    @classmethod
    def energia_renovable(cls, data):
        df = pd.read_json(data)
        return gtf_transform(df).to_json()


    @classmethod
    def plantas_energia(cls, data):
        df = pd.read_json(data)
        return pp_transform(df).to_json()


    @classmethod
    def cancer_male(cls, data):
        data = pd.read_json(data)
        return NormEnfermedades().transform(data, sex='M').to_json()


    @classmethod
    def cancer_female(cls, data):
        data = pd.read_json(data)
        return NormEnfermedades().transform(data, sex='F').to_json()


    @classmethod
    def lung_cancer(cls, *args):
        data = [pd.read_json(a) for a in args]
        return pd.merge(*data, how='outer', on=['pais','anio']).to_json()
