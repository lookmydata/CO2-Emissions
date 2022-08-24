from urllib.request import urlopen
from requests_html import HTMLSession
from zipfile import ZipFile
from io import BytesIO


url = 'https://datasets.wri.org/dataset/globalpowerplantdatabase'
xpath = '/html/body/div[2]/div/div[2]/div/article/div/section/ul/li[1]/div/a'

def getData(url,xpath):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1,reload=False)
    data = r.html.xpath(xpath,first=True)
    link = list(data.absolute_links)[0]
    response = urlopen(link)
    zipfile = ZipFile(BytesIO(response.read()))
    for item in zipfile.namelist():
        if 'csv' in item:
            file_name = item
    zipfile.extract(file_name,path="../pipeline")

getData(url,xpath)

