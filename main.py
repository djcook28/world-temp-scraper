import time
import pandas as pd
import scraper
#import data_file_mgr as dfm
import db_mgr
import streamlit as st
import pandas as pd
import datetime

URL = "https://programmer100.pythonanywhere.com/"

def extract_and_save():
    extracted_temp = float(scraper.extraction(URL))

    current_time = datetime.datetime.now()
    current_time = datetime.datetime.strftime(current_time, "%y-%m-%d-%H-%M-%S")

    #dfm.save_to_file(current_time, extracted_temp)
    db_mgr.save(current_time, extracted_temp)
    new_row = {"dates": current_time, "temperatures": extracted_temp}
    return new_row

#if(dfm.initiate_file()):
#    extract_and_save()
df = db_mgr.load()
df = pd.DataFrame(df, columns=["dates", "temperatures"])

#df = pd.read_csv("temp.txt")
chart = st.line_chart(df, x="dates", y="temperatures")

while True:
    new_row = extract_and_save()

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    chart.add_rows(pd.DataFrame([new_row]))

    time.sleep(2)
