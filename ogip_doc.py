from bs4 import BeautifulSoup
from astropy.io import fits
import requests

def check_ogip_web_docs(ofwgurl="https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/ofwg_recomm.html"):
    """
    
    :return: 
    """
    # this scans through documents listed on
    # https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/ofwg_recomm.html
    # and retrieves:
    #    document name (ogip/92-007 or whatever), title, location, authors, version number, last update
    req = requests.get (ofwgurl)
    soup = BeautifulSoup(req.text,'lxml')
    l = soup.find_all('a')
    links =[x.get('href') for x in l]
    return


if __name__ == "__main__":
    check_ogip_web_docs()