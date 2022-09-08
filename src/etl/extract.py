import os
import requests
import pandas as pd

from requests_html import HTMLSession
from zipfile import ZipFile
from pathlib import Path
from src import PROJECT_PATH


folder3 = "pipeline"
url_energyData = "https://github.com/owid/energy-data"
url_climateDisasters = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_11_1_Physical_Risks_Climate_related_disasters_frequency/FeatureServer/0/query?where=1%3D1&outFields=Country,ISO3,Indicator,Source,F1980,F1981,F1982,F1983,F1984,F1985,F1986,F1987,F1988,F1989,F1990,F1991,F1992,F1993,F1994,F1995,F1996,F1997,F1998,F1999,F2000,F2001,F2002,F2003,F2004,F2005,F2006,F2007,F2008,F2009,F2010,F2011,F2012,F2013,F2014,F2015,F2016,F2017,F2018,F2019,F2020,F2021&outSR=4326&f=json"


class Extract:

    def plantas_energia(self, csv=True):
        """
        Descarga el csv de powerPlantsData

        Parameters
        ----------
        url: str
            url que contiene el link de descarga
        xpath: str
            xpath del link de descarga. Salvo que la página se modifique, se mantiene constante
        folder: str
            carpeta del sistema de archivos donde se guardará el csv del dataset

        Examples
        --------
        >>> data = loadData()
        >>> data.getp....(url=url)
        """
        if csv:
            return pd.read_csv(
                'datasets/global_power_plant/global_power_plant_database.csv'
            ).to_json()

        url = "https://datasets.wri.org/dataset/globalpowerplantdatabase"
        xpath = "/html/body/div[2]/div/div[2]/div/article/div/section/ul/li[1]/div/a"

        s = HTMLSession()
        r = s.get(url)
        r.html.render(sleep=1, reload=False)
        data = r.html.xpath(xpath, first=True)
        link = list(data.absolute_links)[0]
        response = requests.get(link, allow_redirects=True)
        path = os.path.join(Path(__file__).parent, "../../datasets/global_power_plant/gpp.zip")
        print(PROJECT_PATH)
        with open(path, 'wb') as file:
            file.write(response.content)
            with ZipFile(path, 'r') as zobj:
               for file_name in zobj.namelist():
                   if file_name.endswith('.csv'):
                       zobj.extract(file_name, Path(path).parent)


    def energiaco2(self, url=None, folder=None, csv=True):
        """
        url: str - url que contiene el link de descarga
        folder: str - carpeta del sistema de archivos donde se guardará el csv del dataset
        """

        if csv:
            return pd.read_csv('datasets/energyco2.csv').to_json()

        self.url = url
        self.folder = folder
        s = HTMLSession()
        r = s.get(url)
        links = r.html.find("a")
        for item in links:
            if item.text == "CSV":
                link = list(item.absolute_links)[0]
        wget.download(link, out=folder)
        

    def desastres_naturales(self, url=None, csv=True):
        if csv:
            return pd.read_csv('datasets/desastres_naturales/Climate-related_Disasters_Frequency.csv')

        self.url = url
        response = requests.get(url).json()
        df5 = pd.DataFrame()
        for i in range(0, len(response["features"])):
            df = pd.DataFrame.from_dict(
                [response["features"][i]["attributes"]]
            )
            data = (df5, df)
            df5 = pd.concat(data)
        return df5


    def consumo_energia(self):
        return pd.read_csv('datasets/energy_consumption/owid-energy-consumption-source.csv').to_json()


    def energia_estadistica_mensual(self):
        return pd.read_csv('datasets/energia_estadistica_mensual/MES_0522.csv').to_json()


    def cancer_female(self):
        return pd.read_csv('datasets/enfermedades/lung_cancer_number_of_new_female_cases.csv').to_json()


    def cancer_male(self):
        return pd.read_csv('datasets/enfermedades/lung_cancer_number_of_new_male_cases.csv').to_json()


    def energia_renovable(self):
        return pd.read_csv('datasets/energias_renovables/gtfrenewableenergydata.csv').to_json()
