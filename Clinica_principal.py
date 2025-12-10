import time
from Modulo_Limpiar_Pantalla import limpiar 


from Modulo_pacientes import pacientes 
from Modulo_citas import Citas_medicas 
from Modulo_reportes import reportes 


def Sistema_Medico_Principal():
    """
    Función principal que actúa como el HUB de control del sistema,
    llamando a los módulos de gestión (Pacientes, Citas, Reportes).
    """
    while True:
        limpiar()
        print("""
========================================
🏥 Sistema de Gestión Profesional 
========================================
1. Módulo de Pacientes 
2. Módulo de Citas Médicas 
3. Módulo de Reportes (CSV / EXCEL) 
4. Salir del Sistema 
========================================
""")

        try:
            opcion_principal = input('Seleccione una opción: ').strip()
            opcion_principal = int(opcion_principal)
        except ValueError:
            print("\n⚠️ Por favor ingrese un número válido.")
            time.sleep(2)
            continue
            
        limpiar()

        if opcion_principal == 1:
            pacientes() 
        
        elif opcion_principal == 2:
            Citas_medicas() 
            
        elif opcion_principal == 3:
            reportes() 
            
        elif opcion_principal == 4:
            print("\nSesión terminada. ¡Gracias por usar el Sistema de Gestión Profesional!")
            time.sleep(2)
            break
            
        else:
            print("\nOpción no válida.")
            time.sleep(2)
            
if __name__ == "__main__":
    Sistema_Medico_Principal()