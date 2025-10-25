def limpiar(): #Limpiar pantalla
    import os
    import platform
    sistema = platform.system()
    
    if sistema == ('Windows'):
        comando ='cls'
    else:
        comando = 'clear'

    os.system(comando)