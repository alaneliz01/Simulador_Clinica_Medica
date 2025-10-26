# ===============================================
# REPORTES DE CITAS MÉDICAS
# ===============================================

import pandas as pd       # Para trabajar con tablas (DataFrames)
import time               # Para pausar un momento los mensajes
import os                 # Para manejar rutas de archivos
from datetime import datetime  # Para obtener la fecha actual

# Función para limpiar la pantalla (opcional)
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# -------------------------------------------------------
# CARGAR Y LIMPIAR DATOS
# -------------------------------------------------------
def cargar_y_limpiar_citas():
    """Carga el archivo CSV y organiza las citas por fecha y hora."""
    try:
        citas = pd.read_csv('citas_medicas.csv')

        if citas.empty:
            return pd.DataFrame()

        # Convertir las fechas a tipo datetime y ordenar
        citas['Fecha_cita'] = pd.to_datetime(citas['Fecha_cita'], errors='coerce')
        citas = citas.sort_values(by=['Fecha_cita', 'Hora_cita']).reset_index(drop=True)
        return citas

    except FileNotFoundError:
        print('Error: No se encontró el archivo "citas_medicas.csv".')
        time.sleep(2)
        return None

# -------------------------------------------------------
# GENERAR REPORTE EN EXCEL
# -------------------------------------------------------
def generar_reporte_excel(citas, nombre_archivo):
    """Genera un reporte en Excel."""
    try:
        citas['Fecha_cita'] = citas['Fecha_cita'].dt.strftime('%d-%m-%Y')

        citas.to_excel(nombre_archivo, index=False)
        ruta = os.path.abspath(nombre_archivo)

        print(f'\nReporte Excel creado con éxito: {ruta}')
        time.sleep(2)

    except Exception as e:
        print(f'Error al generar el reporte: {e}')
        time.sleep(3)

# -------------------------------------------------------
# GENERAR REPORTE EN CSV
# -------------------------------------------------------
def generar_reporte_csv(citas, nombre_archivo):
    """Genera un reporte en formato CSV."""
    try:
        citas['Fecha_cita'] = citas['Fecha_cita'].dt.strftime('%d-%m-%Y')

        citas.to_csv(nombre_archivo, index=False, encoding='utf-8')
        ruta = os.path.abspath(nombre_archivo)

        print(f'\nReporte CSV creado con éxito: {ruta}')
        time.sleep(2)

    except Exception as e:
        print(f'Error al generar el reporte: {e}')
        time.sleep(3)

# -------------------------------------------------------
# MENÚ PRINCIPAL DE REPORTES
# -------------------------------------------------------
def reportes():
    """Muestra el menú de reportes."""
    citas = cargar_y_limpiar_citas()

    if citas is None or citas.empty:
        print('No hay datos disponibles para generar reportes.')
        time.sleep(2)
        return

    fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")

    while True:
        limpiar()
        print("""
===============================
======= Módulo Reportes ======
===============================
1. Generar Reporte en Excel
2. Generar Reporte en CSV
3. Regresar al Menú Principal
===============================
""")

        opcion = input("\nElige una opción: ").strip()
        fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")

        if opcion == '1':
            archivo = f'reporte_citas_{fecha_actual}.xlsx'
            generar_reporte_excel(citas, archivo)

        elif opcion == '2':
            archivo = f'reporte_citas_{fecha_actual}.csv'
            generar_reporte_csv(citas, archivo)

        elif opcion == '3':
            limpiar()
            print("Regresando al menú principal...")
            time.sleep(1)
            break

        else:
            print("Opción inválida. Intenta de nuevo.")
            time.sleep(1)
