import time
import pandas as pd
import scraper
import data_file_mgr as dfm
import streamlit as st
import pandas
import datetime

URL = "https://programmer100.pythonanywhere.com/"

def extract_and_save():
    extracted_temp = float(scraper.extraction(URL))

    current_time = datetime.datetime.now()
    current_time = datetime.datetime.strftime(current_time, "%y-%m-%d-%H-%M-%S")

    dfm.save_to_file(current_time, extracted_temp)
    new_row = {"dates": current_time, "temperature": extracted_temp}
    return new_row

if(dfm.initiate_file()):
    extract_and_save()

df = pandas.read_csv("temp.txt")
chart = st.line_chart(df, x="dates", y="temperature")

while True:
    new_row = extract_and_save()

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    chart.add_rows(pd.DataFrame([new_row]))

    time.sleep(2)
