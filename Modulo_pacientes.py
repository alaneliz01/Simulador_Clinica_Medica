import pandas as pd
import os
import time
from datetime import datetime
import numpy as np
from Modulo_Limpiar_Pantalla import limpiar

ARCHIVO = "pacientes.csv"
COLUMNAS = ["Nombre", "Sexo", "Edad", "Teléfono", "Estatura", "Peso", "Fecha de Cumpleaños", "Grupo Sanguíneo"]

# =====================================================================
# FUNCIONES AUXILIARES
# =====================================================================

def cargar_pacientes():
    limpiar()
    if not os.path.exists(ARCHIVO):
        print("Archivo pacientes.csv no encontrado.")
        return pd.DataFrame(columns=COLUMNAS)

    try:
        df = pd.read_csv(ARCHIVO)
        # Asegurar columnas correctas
        for col in COLUMNAS:
            if col not in df.columns:
                df[col] = np.nan
        return df[COLUMNAS]
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return pd.DataFrame(columns=COLUMNAS)

def guardar_pacientes(df):
    try:
        df.to_csv(ARCHIVO, index=False)
        return True
    except Exception as e:
        print(f"Error al guardar: {e}")
        time.sleep(2)
        return False

def _input_validado(mensaje, tipo, condicion=None, error="Valor inválido."):
    while True:
        try:
            valor = tipo(input(mensaje).strip())
            if condicion and not condicion(valor):
                print(error)
                continue
            return valor
        except ValueError:
            print(error)

def _obtener_datos_paciente(df):
    datos = {}

    # Nombre único
    while True:
        nombre = input("Nombre completo: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
        elif nombre.lower() in df["Nombre"].astype(str).str.lower().values:
            print("Ese paciente ya existe.")
        else:
            datos["Nombre"] = nombre
            break

    datos["Sexo"] = _input_validado("Sexo (M/F): ", str, lambda x: x.upper() in ["M", "F"], "Debe ser M o F").upper()
    datos["Edad"] = _input_validado("Edad: ", float, lambda x: 0 < x < 130, "Edad no válida.")
    datos["Teléfono"] = _input_validado("Teléfono: ", str, lambda x: x.isdigit() and len(x) >= 7, "Teléfono no válido.")
    datos["Teléfono"] = int(datos["Teléfono"])
    datos["Estatura"] = _input_validado("Estatura (cm): ", float, lambda x: 30 < x < 300, "Estatura fuera de rango.")
    datos["Peso"] = _input_validado("Peso (kg): ", float, lambda x: 1 < x < 600, "Peso fuera de rango.")

    while True:
        try:
            fecha = datetime.strptime(input("Fecha de cumpleaños (DD-MM-YYYY): "), "%d-%m-%Y")
            datos["Fecha de Cumpleaños"] = fecha.date().isoformat()
            break
        except ValueError:
            print("Formato inválido. Use DD-MM-YYYY.")

    grupos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    datos["Grupo Sanguíneo"] = _input_validado(
        f"Grupo sanguíneo ({'/'.join(grupos)}): ",
        str,
        lambda x: x.upper() in grupos,
        "Grupo no válido."
    ).upper()

    return datos

# =====================================================================
# FUNCIÓN PRINCIPAL
# =====================================================================

def pacientes():
    df = cargar_pacientes()

    while True:
        limpiar()
        print("""
===============================
======= Módulo Pacientes ======
===============================
1. Agregar paciente
2. Ver pacientes👁️
3. Buscar paciente🔎
4. Eliminar paciente❌
5. Regresar🚪
===============================
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            limpiar()
            datos = _obtener_datos_paciente(df)
            df = pd.concat([df, pd.DataFrame([datos])], ignore_index=True)
            if guardar_pacientes(df):
                print(f"\n✅ Paciente {datos['Nombre']} guardado exitosamente.")
            time.sleep(2)

        elif opcion == "2":
            limpiar()
            print("=== Lista de Pacientes ===")
            print(df.to_string(index=False) if not df.empty else "No hay pacientes registrados.")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            limpiar()
            if df.empty:
                print("No hay pacientes registrados.")
            else:
                buscar = input("Buscar por nombre: ").strip()
                resultados = df[df["Nombre"].astype(str).str.contains(buscar, case=False, na=False)]
                print(resultados.to_string(index=False) if not resultados.empty else "No se encontraron coincidencias.")
            input("\nPresione Enter para continuar...")

        elif opcion == "4":
            limpiar()
            if df.empty:
                print("No hay pacientes para eliminar.")
                time.sleep(2)
            else:
                df_mostrar = df[["Nombre", "Teléfono"]].reset_index()
                df_mostrar.columns = ["ID", "Nombre", "Teléfono"]
                print(df_mostrar.to_string(index=False))
                valor = input("Ingrese NOMBRE o ID a eliminar: ").strip()

                if valor.isdigit():
                    idx = int(valor)
                    if 0 <= idx < len(df):
                        nombre = df.loc[idx, "Nombre"]
                        df = df.drop(index=idx).reset_index(drop=True)
                        guardar_pacientes(df)
                        print(f"✅ Paciente '{nombre}' eliminado.")
                    else:
                        print("ID inválido.")
                elif valor in df["Nombre"].values:
                    df = df[df["Nombre"] != valor].reset_index(drop=True)
                    guardar_pacientes(df)
                    print(f"✅ Paciente '{valor}' eliminado.")
                else:
                    print("No se encontró ese paciente.")
                time.sleep(2)

        elif opcion == "5":
            print("Regresando...")
            time.sleep(1)
            return
        else:
            print("Opción inválida.")
            time.sleep(1)
