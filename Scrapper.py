import requests
from bs4 import BeautifulSoup
import time
import json

# URL base (puedes cambiarla según la enfermedad/planta)
url = "https://www.plantwise.org/KnowledgeBank/factsheetforlink.aspx?fsid=123456&lang=en"  # reemplaza el ID

headers = {
    "User-Agent": "Mozilla/5.0"
}

def extraer_info(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    ficha = {}

    # Título de la enfermedad
    titulo = soup.find("h1")
    if titulo:
        ficha["titulo"] = titulo.get_text(strip=True)

    # Buscar secciones por encabezado (como "Symptoms")
    secciones = soup.find_all("h2")
    for sec in secciones:
        texto = sec.get_text(strip=True).lower()
        if "symptom" in texto:
            sintomas = sec.find_next_sibling("p")
            if sintomas:
                ficha["sintomas"] = sintomas.get_text(strip=True)
    
    return ficha

# Llamada
url_ficha = "https://www.plantwise.org/KnowledgeBank/factsheetforlink.aspx?fsid=20380&lang=en"
datos = extraer_info(url_ficha)
print(json.dumps(datos, indent=2))
