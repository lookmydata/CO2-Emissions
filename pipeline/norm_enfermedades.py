import pandas as pd
def getdatafemale():
    return pd.read_csv("datasets/enfermedades/lung_cancer_number_of_new_female_cases.csv")
def getdatamale():
    return pd.read_csv("datasets/enfermedades/lung_cancer_number_of_new_male_cases.csv")

def norm_enfermedades(dfm,dff):
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
    dfm = dfm.fillna(0) #paso los nulos a 0 ya que en los csv hay promedio de personas con cancer de pulmon en tal lugar

    dff = dff.rename(columns={'country' :'pais'})
    dfm = dfm.rename(columns={'country' :'pais'}) #renombro columna

    dff = dff.melt(id_vars='pais', var_name='anio', value_name='casos')
    dfm = dfm.melt(id_vars='pais', var_name='anio', value_name='casos') #el .melt salvador xd

    dff = cambiaraint(dff)
    dfm = cambiaraint(dfm) # paso a INT los promedios ya que no puede haber 2,3 personas con cancer de pulmon

    dff = dff.rename(columns={'casos' :'casos F'})
    dfm = dfm.rename(columns={'casos' :'Casos M'})

    df_final = pd.merge(dff,dfm,how='outer',on=['pais','anio'])
    
    return df_final

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
