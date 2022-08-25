from urllib.request import urlopen
from requests_html import HTMLSession,AsyncHTMLSession
from zipfile import ZipFile
from io import BytesIO
import wget

url3 = 'https://datasets.wri.org/dataset/globalpowerplantdatabase'
xpath3 = '/html/body/div[2]/div/div[2]/div/article/div/section/ul/li[1]/div/a'
folder3 = 'pipeline'
url = "https://github.com/owid/energy-data"


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

data = loadData()

#La clase loadData() contiene métodos para diferentes Datasets:
# getPowerPlantsData(url,xpath,folder)
#   url: str - url que contiene el link de descarga
#   xpath: str - xpath del link de descarga. Salvo que la página se modifique, se mantiene constante
#   folder: str - carpeta del sistema de archivos donde se guardará el csv del dataset

# getEnergyData(url,folder)
#   url: str - url que contiene el link de descarga
#   folder: str - carpeta del sistema de archivos donde se guardará el csv del dataset