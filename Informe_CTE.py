import streamlit as st
from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import wbgapi as wb
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
from datetime import datetime
import re
import nltk
import plotly.graph_objects as go
import plotly.express as px
nltk.download('stopwords')
nltk.download('punkt')


st.markdown("<h1 style='text-align: center; color: orange;'>REPORTE   DEL  CTE</h1>", unsafe_allow_html=True)

carga_df1 = st.file_uploader("Selecciona archivo formulario de Diálogo con supervisores")

if carga_df1 is not None:
    df_dialogos = pd.read_csv(carga_df1)
    st.write(df_dialogos)
