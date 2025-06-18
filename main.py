import time
import scraper
import data_file_mgr as dfm
import streamlit as st

URL = "https://programmer100.pythonanywhere.com/"

if __name__ == "__main__":
    dfm.initiate_file()
    while True:
        extracted_temp = scraper.extraction(URL)
        dfm.save_to_file(extracted_temp)
        time.sleep(2)