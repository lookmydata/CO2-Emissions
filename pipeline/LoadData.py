from urllib.request import urlopen
from requests_html import HTMLSession,AsyncHTMLSession
from zipfile import ZipFile
from io import BytesIO
import wget, requests
import pandas as pd

url_powerPlantsData = 'https://datasets.wri.org/dataset/globalpowerplantdatabase'
xpath_powerPlantsData = '/html/body/div[2]/div/div[2]/div/article/div/section/ul/li[1]/div/a'
folder3 = 'pipeline'
url_energyData = "https://github.com/owid/energy-data"
url_climateDisasters =  "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_11_1_Physical_Risks_Climate_related_disasters_frequency/FeatureServer/0/query?where=1%3D1&outFields=Country,ISO3,Indicator,Source,F1980,F1981,F1982,F1983,F1984,F1985,F1986,F1987,F1988,F1989,F1990,F1991,F1992,F1993,F1994,F1995,F1996,F1997,F1998,F1999,F2000,F2001,F2002,F2003,F2004,F2005,F2006,F2007,F2008,F2009,F2010,F2011,F2012,F2013,F2014,F2015,F2016,F2017,F2018,F2019,F2020,F2021&outSR=4326&f=json"


class loadData():

    def getPowerPlantsData(self,url,xpath,folder):
        self.url = url
        self.xpath = xpath
        self.folder = folder

        folder = "../"+folder
        s = HTMLSession()
        r = s.get(url)
        r.html.render(sleep=1,reload=False)
        data = r.html.xpath(xpath,first=True)
        link = list(data.absolute_links)[0]
        if 'zip' in link:
            response = urlopen(link)
            zipfile = ZipFile(BytesIO(response.read()))
            for item in zipfile.namelist():
                if 'csv' in item:
                    file_name = item
            zipfile.extract(file_name,path=folder)
        else:
            wget.download(link,out=folder)
        return

    def getEnergyData(self,url,folder):
        self.url = url
        self.folder = folder
        s = HTMLSession()
        r = s.get(url)
        links = r.html.find('a')            
        for item in links:
            if item.text == 'CSV':
                link=list(item.absolute_links)[0]
        wget.download(link,out=folder) 
        return
    
    def getClimateDisastersData(self,url):
        self.url = url
        response = requests.get(url).json()
        df5 = pd.DataFrame()
        for i in range(0,len(response['features'])):
            df = pd.DataFrame.from_dict([response['features'][i]['attributes']])
            data=(df5,df)
            df5=pd.concat(data)
        return df5
    

data = loadData()


#La clase loadData() contiene métodos para diferentes Datasets:
# getPowerPlantsData(url,xpath,folder)
#   url: str - url que contiene el link de descarga
#   xpath: str - xpath del link de descarga. Salvo que la página se modifique, se mantiene constante
#   folder: str - carpeta del sistema de archivos donde se guardará el csv del dataset

# getEnergyData(url,folder)
#   url: str - url que contiene el link de descarga
#   folder: str - carpeta del sistema de archivos donde se guardará el csv del dataset