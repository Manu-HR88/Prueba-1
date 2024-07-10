import streamlit as st
import openpyxl
import requests
from io import BytesIO
from datetime import datetime

# URL del archivo en GitHub (reemplaza con tu propia URL)
url = 'https://github.com/tu_usuario/tu_repositorio/raw/main/template.xlsx'

# Descargar el archivo desde GitHub
@st.cache_data
def download_template(url):
    response = requests.get(url)
    response.raise_for_status()  # Asegurarse de que la solicitud fue exitosa
    return BytesIO(response.content)

# Verificar si el contenido es un archivo Excel válido
def is_valid_excel(file_stream):
    try:
        wb = openpyxl.load_workbook(file_stream)
        return True
    except Exception as e:
        st.error(f"Error al cargar el archivo de Excel: {e}")
        return False

# Cargar la plantilla de Excel desde el archivo descargado
def load_workbook():
    file_stream = download_template(url)
    if is_valid_excel(file_stream):
        return openpyxl.load_workbook(file_stream)
    else:
        st.error("El archivo descargado no es un archivo de Excel válido.")
        return None

# Guardar datos en celdas específicas
def save_to_excel(name, age, gender):
    wb = load_workbook()
    if wb:
        sheet = wb.active
        sheet['A1'] = name  # Guardar nombre en celda A1
        sheet['B1'] = age   # Guardar edad en celda B1
        sheet['C1'] = gender # Guardar género en celda C1
        
        # Generar un archivo en memoria
        output = BytesIO()
        wb.save(output)
        output.seek(0)  # Regresar al inicio del archivo
        
        return output
    else:
        return None

# Crear la interfaz de usuario
st.title("Formulario de Información")

name = st.text_input("Nombre")
age = st.number_input("Edad", min_value=0, max_value=120, step=1)
gender = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])

if st.button("Guardar"):
    excel_file = save_to_excel(name, age, gender)
    if excel_file:
        st.success("Datos guardados exitosamente.")
        st.download_button(
            label="Descargar archivo Excel",
            data=excel_file,
            file_name=f"datos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.error("No se pudo guardar el archivo de Excel.")

# Mostrar versiones de las bibliotecas utilizadas
st.write(f"Versión de openpyxl: {openpyxl.__version__}")
st.write(f"Versión de requests: {requests.__version__}")
