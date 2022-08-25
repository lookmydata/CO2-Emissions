import pandas as pd

def gtf_norm(dataframe):

    copy=dataframe.copy()
    dict_cols = {'Series Code':'codigo_info','Country Name':'pais','Country Code':'codigo_iso','1990 [YR1990]': '1990', '1991 [YR1991]': '1991', '1992 [YR1992]': '1992', '1993 [YR1993]': '1993', '1994 [YR1994]': '1994', '1995 [YR1995]': '1995', 
    '1996 [YR1996]': '1996', '1997 [YR1997]': '1997', '1998 [YR1998]': '1998', '1999 [YR1999]': '1999', '2000 [YR2000]': '2000', '2001 [YR2001]': '2001',
    '2002 [YR2002]': '2002', '2003 [YR2003]': '2003', '2004 [YR2004]': '2004', '2005 [YR2005]': '2005', '2006 [YR2006]': '2006', '2007 [YR2007]': '2007', 
    '2008 [YR2008]': '2008', '2009 [YR2009]': '2009', '2010 [YR2010]': '2010', '2011 [YR2011]': '2011', '2012 [YR2012]': '2012', '2013 [YR2013]': '2013', '2014 [YR2014]': '2014'}

    copy.rename(columns=dict_cols,inplace=True)
    copy.drop(columns='Series Name',inplace=True)

    df1=pd.melt(copy,id_vars=['pais','codigo_info','codigo_iso'],var_name='anio',value_name='valor')

    ci_norm=df1.codigo_info.to_list()
    ci_fin=[]
    for i in ci_norm:
        a=i.split('_')
        ci_fin.append(a[0])
    se=pd.Series(ci_fin)
    df1['info_codigo']=se
    df1.drop(columns='codigo_info',inplace=True)

    tf=df1.valor.to_list()
    tff=[]
    for i in tf:
        if i!='..':
            tff.append(round(float(i),2))
        else:
            tff.append(i)
            
    se1=pd.Series(tff)
    df1['valor']=se1
    df1['valor']=df1.valor.replace('..',None)
    df1['anio']=df1.anio.astype(int)

    return df1

energy_access=gtf_norm(pd.read_csv('../datasets/energias_renovables/gtfenergyaccessdata.csv'))
# energy_access.to_parquet('../datasets/energias_renovables/NORMALIZADO_acceso_a_electricidad.parquet')
energy_intensity=gtf_norm(pd.read_csv('../datasets/energias_renovables/gtfprimaryenergyintensitydata.csv'))
# energy_intensity.to_parquet('../datasets/energias_renovables/NORMALIZADO_intensidad_electricidad_primaria.parquet')

renewable_energy=gtf_norm(pd.read_csv('../datasets/energias_renovables/gtfrenewableenergydata.csv'))
# renewable_energy.to_parquet('../datasets/energias_renovables/NORMALIZADO_data_energia_renovable.parquet')