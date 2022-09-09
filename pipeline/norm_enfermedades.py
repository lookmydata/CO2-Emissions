import pandas as pd
from typing import Literal


def getdatafemale():
    return pd.read_parquet("datasets/enfermedades/lung_cancer_number_of_new_female_cases.parquet")


def getdatamale():
    return pd.read_parquet("datasets/enfermedades/lung_cancer_number_of_new_male_cases.parquet")


class NormEnfermedades:

    def __init__(self) -> None:
        pass


    def __to_int(self, data):
        i = 0
        for i in range(len(data)):
            if type(data['casos'][i]) == str:
                if "k" in data['casos'][i]:
                    data['casos'][i] = round(float(data['casos'][i].split("k")[0])*1000)
            data['casos'][i] = round(float(data['casos'][i]))
            i = i+1
        return data


    def transform(self, df, sex: Literal['M', 'F']):
        df = df.fillna(0) #paso los nulos a 0 ya que en los csv hay promedio de personas con cancer de pulmon en tal lugar
        df = df.rename(columns={'country' :'pais'}) #renombro columna
        df = df.melt(id_vars='pais', var_name='anio', value_name='casos') #el .melt salvador xd
        df = self.__to_int(df) # paso a INT los promedios ya que no puede haber 2,3 personas con cancer de pulmon
        df = df.rename(columns={'casos' :f'casos {sex}'})
        return df


    def fusion(self, dff, dfm):
        return pd.merge(dff, dfm, how='outer', on=['pais','anio'])
        

def E_enf(dff):
    def cambiaraint (dataframe):
        i = 0
        for i in range(len(dataframe)):
            if type(dataframe['casos'][i]) == str:
                if "k" in dataframe['casos'][i]:
                    dataframe['casos'][i] = round(float(dataframe['casos'][i].split("k")[0])*1000)
            dataframe['casos'][i] = round(float(dataframe['casos'][i]))
            i = i+1
        return dataframe
    dff = dff.fillna(0)

    dff = dff.rename(columns={'country' :'pais'})
    
    dff = dff.melt(id_vars='pais', var_name='anio', value_name='casos')

    dff = cambiaraint(dff)

    dff = dff.rename(columns={'casos' :'casos F'})
    
    return dff
