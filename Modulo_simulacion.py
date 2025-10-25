def iniciar_simulacion():
      import time
      from Modulo_Limpiar_Pantalla import limpiar
      from Modulo_pacientes import pacientes
      from Modulo_citas import Citas_medicas
      from Modulo_reportes import reportes

# =====================================================================
# CODIGO SIMULACION DE CLINICA
# =====================================================================
      while True:
            limpiar()
            try:
                  print('=== Clínica Simulador ===')
                  print('1. Pacientes')
                  print('2. Citas médicas')
                  print('3. Reportes')
                  print('4. Regresar al menú principal')
                  print('=============================')  
                  opcion_menu = int(input("Seleccione una opción: "))
                  if opcion_menu == 1:
                              pacientes()
                  elif opcion_menu == 2:
                              Citas_medicas()
                  elif opcion_menu == 3:
                              reportes()
                  elif opcion_menu == 4:
                        print("Regresando...")
                        time.sleep(1)
                        return 
                  else:
                        print("Opción no válida. Por favor, intente de nuevo.")
            except ValueError:
                  print("Entrada no válida. Por favor, ingrese un número correspondiente a las opciones.")