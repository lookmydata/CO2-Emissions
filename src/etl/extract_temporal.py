import pandas as pd


def E_desastres_naturales():
    return pd.read_csv('datasets/desastres_naturales/Climate-related_Disasters_Frequency.csv')


def E_energyco2():
    return pd.read_csv("datasets/energyco2.csv")


def E_consumo_energia():
    return pd.read_csv("datasets/energy_consumption/owid-energy-consumption-source.csv")


def E_energia_estadistica_mensual():
    return pd.read_csv("datasets/energia_estadistica_mensual/MES_0522.csv")
