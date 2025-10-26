# ===============================================
# SISTEMA SIMPLE DE CITAS MÉDICAS 
# ===============================================

import pandas as pd
import time
import os
from datetime import datetime

# -------------------------------------------------------
# Función para limpiar la pantalla
# -------------------------------------------------------
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# -------------------------------------------------------
# Cargar datos iniciales
# -------------------------------------------------------
def cargar_datos_iniciales():
    limpiar()
    pacientes = pd.DataFrame()
    citas = []

    # Cargar pacientes
    try:
        pacientes = pd.read_csv('pacientes.csv')
    except FileNotFoundError:
        print('Error: No se encontró "pacientes.csv"')
        time.sleep(2)
        return None, None
    except pd.errors.EmptyDataError:
        print('Advertencia: El archivo pacientes.csv está vacío.')

    # Cargar citas existentes (si hay archivo)
    if os.path.exists('citas_medicas.csv'):
        try:
            df = pd.read_csv('citas_medicas.csv')
            if not df.empty and all(col in df.columns for col in ['Nombre', 'Fecha_cita', 'Hora_cita']):
                citas = df.to_dict('records')
                print(f"Se cargaron {len(citas)} citas existentes.")
        except pd.errors.EmptyDataError:
            print("Archivo citas_medicas.csv vacío. Se iniciará vacío.")
        except Exception as e:
            print(f"Error al cargar citas: {e}")

    time.sleep(1)
    return pacientes, citas

# -------------------------------------------------------
# Guardar citas
# -------------------------------------------------------
def guardar_citas(citas_list):
    limpiar()
    if citas_list:
        df = pd.DataFrame(citas_list)
        # Crear columna temporal de fecha+hora para ordenar
        df['FechaHora'] = pd.to_datetime(df['Fecha_cita'] + ' ' + df['Hora_cita'], dayfirst=True, errors='coerce')
        df = df.sort_values(by='FechaHora').drop(columns=['FechaHora'])
        df.to_csv('citas_medicas.csv', index=False)
        print(f'Se guardaron {len(citas_list)} citas.')
    else:
        pd.DataFrame(columns=['Nombre', 'Fecha_cita', 'Hora_cita']).to_csv('citas_medicas.csv', index=False)
        print('No hay citas. Archivo vacío guardado.')
    time.sleep(2)

# -------------------------------------------------------
# Registrar cita
# -------------------------------------------------------
def registrar_cita(pacientes, citas):
    limpiar()
    print("=== Registrar Cita ===")

    if pacientes.empty:
        print('No hay pacientes registrados.')
        time.sleep(2)
        return

    print('\nPacientes:')
    for i, row in pacientes[['Nombre', 'Edad', 'Teléfono']].iterrows():
        print(f"{i+1}. {row['Nombre']} | Edad: {row['Edad']} | Tel: {row['Teléfono']}")

    seleccion = input('\nElija el número del paciente (o R para regresar): ').strip()
    if seleccion.lower() == 'r':
        return

    try:
        indice = int(seleccion) - 1
        if 0 <= indice < len(pacientes):
            nombre = pacientes.iloc[indice]['Nombre']
        else:
            print('Número inválido.')
            time.sleep(2)
            return
    except ValueError:
        print('Debe ingresar un número.')
        time.sleep(2)
        return

    print(f"\nPaciente seleccionado: {nombre}")
    fecha = input('Fecha (DD-MM-AAAA): ').strip()
    if fecha.lower() == 'cancelar':
        return
    hora = input('Hora (HH:MM): ').strip()
    if hora.lower() == 'cancelar':
        return

    try:
        datetime.strptime(f"{fecha} {hora}", "%d-%m-%Y %H:%M")
        nueva_cita = {'Nombre': nombre, 'Fecha_cita': fecha, 'Hora_cita': hora}

        if any(c['Nombre'] == nombre and c['Fecha_cita'] == fecha and c['Hora_cita'] == hora for c in citas):
            print("Esta cita ya existe.")
        else:
            citas.append(nueva_cita)
            print('Cita registrada correctamente.')

        time.sleep(2)
    except ValueError:
        print('Formato incorrecto. Usa DD-MM-AAAA y HH:MM.')
        time.sleep(3)

# -------------------------------------------------------
# Eliminar cita
# -------------------------------------------------------
def eliminar_cita(citas):
    limpiar()
    print("=== Eliminar Cita ===")

    if not citas:
        print('No hay citas.')
        time.sleep(2)
        return

    df = pd.DataFrame(citas)
    df['FechaHora'] = pd.to_datetime(df['Fecha_cita'] + ' ' + df['Hora_cita'], dayfirst=True, errors='coerce')
    df = df.sort_values(by='FechaHora').reset_index(drop=True)

    for i, row in df.iterrows():
        print(f"{i+1}. {row['Nombre']} | {row['Fecha_cita']} {row['Hora_cita']}")

    seleccion = input('\nElija el número a eliminar (o R para regresar): ').strip()
    if seleccion.lower() == 'r':
        return

    try:
        num = int(seleccion) - 1
        if 0 <= num < len(df):
            cita = df.iloc[num].to_dict()
            for i, c in enumerate(citas):
                if (c['Nombre'] == cita['Nombre'] and 
                    c['Fecha_cita'] == cita['Fecha_cita'] and 
                    c['Hora_cita'] == cita['Hora_cita']):
                    citas.pop(i)
                    print('Cita eliminada correctamente.')
                    time.sleep(2)
                    return
        print('Número inválido.')
    except ValueError:
        print('Debe ingresar un número.')
        time.sleep(2)

# -------------------------------------------------------
# Mostrar citas
# -------------------------------------------------------
def mostrar_citas(citas):
    limpiar()
    print("=== Citas Registradas ===")

    if not citas:
        print('No hay citas registradas.')
    else:
        df = pd.DataFrame(citas)
        df['FechaHora'] = pd.to_datetime(df['Fecha_cita'] + ' ' + df['Hora_cita'], dayfirst=True, errors='coerce')
        df = df.sort_values(by='FechaHora')
        print(df[['Nombre', 'Fecha_cita', 'Hora_cita']].to_string(index=False))

    input("\nPresione Enter para continuar...")

# -------------------------------------------------------
# Menú principal
# -------------------------------------------------------
def Citas_medicas():
    pacientes, citas = cargar_datos_iniciales()
    if pacientes is None:
        return

    while True:
        limpiar()
        print("""
===============================
======= Módulo Citas ==========
===============================
1. Registrar cita📓
2. Eliminar cita❌
3. Mostrar citas👁️
4. Regresar🚪
===============================
""")

        opcion = input("\nElija una opción: ").strip()

        if opcion == '1':
            registrar_cita(pacientes, citas)
        elif opcion == '2':
            eliminar_cita(citas)
        elif opcion == '3':
            mostrar_citas(citas)
        elif opcion == '4':
            guardar_citas(citas)
            return
        else:
            print("Opción inválida.")
            time.sleep(2)
