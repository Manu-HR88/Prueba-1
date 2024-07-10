import streamlit as st
import openpyxl
import requests
from io import BytesIO
import os
from datetime import datetime

# URL del archivo en GitHub
url = 'https://github.com/Manu-HR88/Prueba-1/raw/main/template.xlsx'

# Descargar el archivo desde GitHub
@st.cache_data
def download_template(url):
    response = requests.get(url)
    response.raise_for_status()  # Asegurarse de que la solicitud fue exitosa
    return BytesIO(response.content)

# Cargar la plantilla de Excel desde el archivo descargado
def load_workbook():
    file_stream = download_template(url)
    return openpyxl.load_workbook(file_stream)

# Guardar datos en celdas específicas
def save_to_excel(name, age, gender):
    wb = load_workbook()
    sheet = wb.active
    sheet['A1'] = name  # Guardar nombre en celda A1
    sheet['B1'] = age   # Guardar edad en celda B1
    sheet['C1'] = gender # Guardar género en celda C1
    
    # Generar un nombre de archivo único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f'output_{timestamp}.xlsx'
    
    # Guardar en el directorio actual (asegúrate de tener permisos)
    wb.save(output_filename)
    
    return output_filename

# Crear la interfaz de usuario
st.title("Formulario de Información")

name = st.text_input("Nombre")
age = st.number_input("Edad", min_value=0, max_value=120, step=1)
gender = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])

if st.button("Guardar"):
    output_filename = save_to_excel(name, age, gender)
    st.success(f"Datos guardados en {output_filename}")
