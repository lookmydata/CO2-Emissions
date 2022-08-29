import pandas as pd


# def rename_columns(data: pd.DataFrame):

# funcion valen
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

dic_cols = {
    "country": "pais", #1       
    "type": "tipo",
    "year": "anio",
    "consumption": "cons",
    "production": "produccion",
    "gdp": "pbi",
    "population": "poblacion",
    "intensity": "intensidad",
    "emission": "emision",
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

# funciones fercho
class Transform(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        return super(Transform, self).__init__(*args, **kwargs)

    @property
    def _constructor(self):
        return Transform

    def rename_columns(self, columns_dict):
        """
        Rename the columns by substrings
        """
        data = self.copy()
        columns = '$$'.join(data.columns).lower()
        for key, value in columns_dict.items():
            columns = columns.replace(key, value)
        data = data.rename(
            columns=dict(zip(data.columns, columns.split('$$')))
        )
        return data

    def drop_before_year(self, year):
        """
        Drop all rows less than selected year
        """
        data = self.copy()
        column = "anio"
        assert column in data.columns, "No se encuentra la columna 'anio'. Renombralas y vuelve a intentar"
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


energyco2 = pd.read_csv("../../datasets/energyco2.csv")

def transform_energyco2(data):
    return (
        Transform(data)
        .drop(columns="Unnamed: 0")
        .rename_columns(dic_cols)
        .drop_before_year(2000)
    )

print(transform_energyco2(energyco2))
