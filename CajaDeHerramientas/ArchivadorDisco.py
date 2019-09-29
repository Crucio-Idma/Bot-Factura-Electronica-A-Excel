
"""Se encarga de crear de forma ordenada las carpetas y los archivos que se utilizarán posteriormente"""
from pathlib import Path
import shutil

def crearCarpetas(_UrlDeLaSalida):
    
    try:
        CarpetaHoja = Path(_UrlDeLaSalida)
        CarpetaHoja.mkdir(parents = True)
        _UrlDeLaSalidaT = _UrlDeLaSalida
    except:
    
        flag = True
        i = 0
        while flag:
            
            i+=1
            _UrlDeLaSalidaT = _UrlDeLaSalida + str(i) 
            CarpetaHoja = Path(_UrlDeLaSalidaT)
             
            try:
                CarpetaHoja.mkdir(parents = True)
                print("El directorio existe. Se va a crear uno nuevo llamado:" + _UrlDeLaSalidaT)
                flag = False
            except:
                flag = True
            
    return _UrlDeLaSalidaT

def crearArchivoEnBaseAUnaPlantilla(pUrlPlantilla, pUrlDestino):

    try:
        
        shutil.copy(pUrlPlantilla, pUrlDestino)
        return True
        
    except:
        return False
    