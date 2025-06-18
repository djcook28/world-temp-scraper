import requests
import selectorlib

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extraction(url):
    source = scrape(url)
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temp"]
    return value