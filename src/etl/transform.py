import pandas as pd
import numpy as np
import re


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
STANDARD_COLUMNS = {
    "country": "pais",
    "energy_type": "tipo_energia",
    "year": "anio",
    "energy_consumption": "consumo_energia",
    "energy_production": "produccion_energia",
    "gdp": "pbi",
    "population": "poblacion",
    "energy_intensity_per_capita": "intensidad_energia_per_capita",
    "energy_intensity_by_gdp": "intensidad_energia_por_pbi",
    "co2_emission": "emision_co2",
    "iso3": "pais_iso",
    "iso_code": "pais_iso",
    "indicator": "indicador",
    "source": "fuente",
    # Substrings
    "fuel": "combustible",
    "wind": "eolica",
    "electricity": "elec",
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
}
STANDARD_COUNTRIES = {
    'AFG': 'Afghanistan',
    'ALB': 'Albania',
    'DZA': 'Algeria',
    'ASM': 'American Samoa',
    'AGO': 'Angola',
    'ATA': 'Antarctica',
    'ATG': 'Antigua and Barbuda',
    'ARG': 'Argentina',
    'ARM': 'Armenia',
    'ABW': 'Aruba',
    'AUS': 'Australia',
    'AUT': 'Austria',
    'AZE': 'Azerbaijan',
    'BHS': 'Bahamas',
    'BHR': 'Bahrain',
    'BGD': 'Bangladesh',
    'BRB': 'Barbados',
    'BLR': 'Belarus',
    'BEL': 'Belgium',
    'BLZ': 'Belize',
    'BEN': 'Benin',
    'BMU': 'Bermuda',
    'BTN': 'Bhutan',
    'BOL': 'Bolivia',
    'BIH': 'Bosnia and Herzegovina',
    'BWA': 'Botswana',
    'BRA': 'Brazil',
    'VGB': 'British Virgin Islands',
    'BRN': 'Brunei',
    'BGR': 'Bulgaria',
    'BFA': 'Burkina Faso',
    'BDI': 'Burundi',
    'KHM': 'Cambodia',
    'CMR': 'Cameroon',
    'CAN': 'Canada',
    'CPV': 'Cape Verde',
    'CYM': 'Cayman Islands',
    'CAF': 'Central African Republic',
    'TCD': 'Chad',
    'CHL': 'Chile',
    'CHN': 'China',
    'COL': 'Colombia',
    'COM': 'Comoros',
    'COG': 'Congo',
    'COK': 'Cook Islands',
    'CRI': 'Costa Rica',
    'CIV': "Cote d'Ivoire",
    'HRV': 'Croatia',
    'CUB': 'Cuba',
    'CYP': 'Cyprus',
    'CZE': 'Czechia',
    'COD': 'Democratic Republic of Congo',
    'DNK': 'Denmark',
    'DJI': 'Djibouti',
    'DMA': 'Dominica',
    'DOM': 'Dominican Republic',
    'ECU': 'Ecuador',
    'EGY': 'Egypt',
    'SLV': 'El Salvador',
    'GNQ': 'Equatorial Guinea',
    'ERI': 'Eritrea',
    'EST': 'Estonia',
    'SWZ': 'Eswatini',
    'ETH': 'Ethiopia',
    'FRO': 'Faeroe Islands',
    'FLK': 'Falkland Islands',
    'FJI': 'Fiji',
    'FIN': 'Finland',
    'FRA': 'France',
    'GUF': 'French Guiana',
    'PYF': 'French Polynesia',
    'GAB': 'Gabon',
    'GMB': 'Gambia',
    'GEO': 'Georgia',
    'DEU': 'Germany',
    'GHA': 'Ghana',
    'GIB': 'Gibraltar',
    'GRC': 'Greece',
    'GRL': 'Greenland',
    'GRD': 'Grenada',
    'GLP': 'Guadeloupe',
    'GUM': 'Guam',
    'GTM': 'Guatemala',
    'GIN': 'Guinea',
    'GNB': 'Guinea-Bissau',
    'GUY': 'Guyana',
    'HTI': 'Haiti',
    'HND': 'Honduras',
    'HKG': 'Hong Kong',
    'HUN': 'Hungary',
    'ISL': 'Iceland',
    'IND': 'India',
    'IDN': 'Indonesia',
    'IRN': 'Iran',
    'IRQ': 'Iraq',
    'IRL': 'Ireland',
    'ISR': 'Israel',
    'ITA': 'Italy',
    'JAM': 'Jamaica',
    'JPN': 'Japan',
    'JOR': 'Jordan',
    'KAZ': 'Kazakhstan',
    'KEN': 'Kenya',
    'KIR': 'Kiribati',
    'KWT': 'Kuwait',
    'KGZ': 'Kyrgyzstan',
    'LAO': 'Laos',
    'LVA': 'Latvia',
    'LBN': 'Lebanon',
    'LSO': 'Lesotho',
    'LBR': 'Liberia',
    'LBY': 'Libya',
    'LTU': 'Lithuania',
    'LUX': 'Luxembourg',
    'MAC': 'Macao',
    'MDG': 'Madagascar',
    'MWI': 'Malawi',
    'MYS': 'Malaysia',
    'MDV': 'Maldives',
    'MLI': 'Mali',
    'MLT': 'Malta',
    'MTQ': 'Martinique',
    'MRT': 'Mauritania',
    'MUS': 'Mauritius',
    'MEX': 'Mexico',
    'FSM': 'Micronesia (country)',
    'MDA': 'Moldova',
    'MNG': 'Mongolia',
    'MNE': 'Montenegro',
    'MSR': 'Montserrat',
    'MAR': 'Morocco',
    'MOZ': 'Mozambique',
    'MMR': 'Myanmar',
    'NAM': 'Namibia',
    'NRU': 'Nauru',
    'NPL': 'Nepal',
    'NLD': 'Netherlands',
    'ANT': 'Netherlands Antilles',
    'NCL': 'New Caledonia',
    'NZL': 'New Zealand',
    'NIC': 'Nicaragua',
    'NER': 'Niger',
    'NGA': 'Nigeria',
    'NIU': 'Niue',
    'PRK': 'North Korea',
    'MKD': 'North Macedonia',
    'MNP': 'Northern Mariana Islands',
    'NOR': 'Norway',
    'OMN': 'Oman',
    'PAK': 'Pakistan',
    'PSE': 'Palestine',
    'PAN': 'Panama',
    'PNG': 'Papua New Guinea',
    'PRY': 'Paraguay',
    'PER': 'Peru',
    'PHL': 'Philippines',
    'POL': 'Poland',
    'PRT': 'Portugal',
    'PRI': 'Puerto Rico',
    'QAT': 'Qatar',
    'REU': 'Reunion',
    'ROU': 'Romania',
    'RUS': 'Russia',
    'RWA': 'Rwanda',
    'SHN': 'Saint Helena',
    'KNA': 'Saint Kitts and Nevis',
    'LCA': 'Saint Lucia',
    'SPM': 'Saint Pierre and Miquelon',
    'VCT': 'Saint Vincent and the Grenadines',
    'WSM': 'Samoa',
    'STP': 'Sao Tome and Principe',
    'SAU': 'Saudi Arabia',
    'SEN': 'Senegal',
    'SRB': 'Serbia',
    'SYC': 'Seychelles',
    'SLE': 'Sierra Leone',
    'SGP': 'Singapore',
    'SVK': 'Slovakia',
    'SVN': 'Slovenia',
    'SLB': 'Solomon Islands',
    'SOM': 'Somalia',
    'ZAF': 'South Africa',
    'KOR': 'South Korea',
    'SSD': 'South Sudan',
    'ESP': 'Spain',
    'LKA': 'Sri Lanka',
    'SDN': 'Sudan',
    'SUR': 'Suriname',
    'SWE': 'Sweden',
    'CHE': 'Switzerland',
    'SYR': 'Syria',
    'TWN': 'Taiwan',
    'TJK': 'Tajikistan',
    'TZA': 'Tanzania',
    'THA': 'Thailand',
    'TLS': 'Timor',
    'TGO': 'Togo',
    'TON': 'Tonga',
    'TTO': 'Trinidad and Tobago',
    'TUN': 'Tunisia',
    'TUR': 'Turkey',
    'TKM': 'Turkmenistan',
    'TCA': 'Turks and Caicos Islands',
    'TUV': 'Tuvalu',
    'UGA': 'Uganda',
    'UKR': 'Ukraine',
    'ARE': 'United Arab Emirates',
    'GBR': 'United Kingdom',
    'USA': 'United States',
    'VIR': 'United States Virgin Islands',
    'URY': 'Uruguay',
    'UZB': 'Uzbekistan',
    'VUT': 'Vanuatu',
    'VEN': 'Venezuela',
    'VNM': 'Vietnam',
    'ESH': 'Western Sahara',
    'YEM': 'Yemen',
    'ZMB': 'Zambia',
    'ZWE': 'Zimbabwe'}


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


# -----------------------------------------------------------------------------------------


# TRANSFORMACION FERCHO -- REALIZADO

# REALIZADO
def T_desastres_naturales(data) -> pd.DataFrame:
    return (
        Transform(data)
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
    )


# df = pd.read_csv(
#     '../../datasets/desastres_naturales/Climate-related_Disasters_Frequency.csv'
# )
# data = T_desastres_naturales(df)
# print(data)


# REALIZADO
def T_energyco2(data) -> pd.DataFrame:
    return Transform(data).drop(columns="Unnamed: 0").rename_columns().round(2)

# df = pd.read_csv("../../datasets/energyco2.csv")
# data = T_energyco2(df)
# print(data.columns)


# REALIZADO
def T_consumo_energia(data) -> pd.DataFrame:
    return (
        Transform(data)
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
    )


# dataset = pd.read_csv(
#     "../../datasets/energy_consumption/owid-energy-consumption-source.csv"
# )
# data = T_consumo_energia(dataset)
# print(data)


# REALIZADO
def T_energia_estadistica_mensual(data) -> pd.DataFrame:
    return (
        Transform(data)
        .rename_columns()
        .dropna(subset="valor")
        .to_datetime("periodo")
        .round(2)
        .create_column("anio", "data['periodo'].dt.year")
        .create_column("mes", "data['periodo'].dt.month")
        .drop(columns=["periodo"])
        .rename_columns(columns={"valor": "cons_energia_gwh"})
    )


# dataset = pd.read_csv("../../datasets/energia_estadistica_mensual/MES_0522.csv")
# data = T_energia_estadistica_mensual(dataset)
# print(data)
