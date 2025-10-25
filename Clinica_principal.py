import time
from Modulo_Limpiar_Pantalla import limpiar 

# 🚨 IMPORTACIONES
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
        print('========================================')
        print('🏥 Sistema de Gestión Profesional 📊')
        print('========================================')
        print('1. Módulo de Pacientes 🧑‍🤝‍🧑')
        print('2. Módulo de Citas Médicas 📅')
        print('3. Módulo de Reportes (CSV \ Excel) 📈')
        print('4. Salir del Sistema 🚪')
        print('----------------------------------------')

        try:
            opcion_principal = input('Seleccione una opción: ').strip()
            opcion_principal = int(opcion_principal)
        except ValueError:
            print("\n⚠️ Por favor ingrese un número válido.")
            time.sleep(2)
            continue
            
        limpiar() # Limpia la pantalla antes de entrar al módulo

        if opcion_principal == 1:
            pacientes() # Llama al módulo de gestión de pacientes
        
        elif opcion_principal == 2:
            Citas_medicas() # Llama al módulo de gestión de citas
            
        elif opcion_principal == 3:
            reportes() # Llama al módulo de generación de reportes
            
        elif opcion_principal == 4:
            print("\n✅ Sesión terminada. ¡Gracias por usar el Sistema de Gestión Profesional!")
            time.sleep(2)
            break
            
        else:
            print("\n⚠️ Opción no válida.")
            time.sleep(2)
            
if __name__ == "__main__":
    Sistema_Medico_Principal()