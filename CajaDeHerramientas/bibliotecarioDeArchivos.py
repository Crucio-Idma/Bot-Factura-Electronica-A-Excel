'''
Created on 28 sep. 2019

@author: Crucio



'''

"""
    Se Genera una lista con las direcciones de los archivos
    @param pUrlDeLaCarpetaDeEntrada: String con la dirección de la carpeta raíz 
    @return Retorna una lista con todos las facturas virtuales

"""
from os import walk
import re

def buscarFacturasEnLasCarpetas(_UrlInputDeArchivos, archivosResultado = []):
    
    directorio, subdirectorios, archivos = next(walk(_UrlInputDeArchivos))
    archivosR = comprobarSiEsFactura(archivos)
    
    i=0
    for archivo in archivosR:
        
        archivosR[i] = directorio + archivo
        i+=1
        
    if len ( archivosR ) > 0:
        
        archivosResultado += archivosR
        
    i=0
    for subdirectorio in subdirectorios:
        
        subdirectorio =  directorio + subdirectorio + "/"
        archivosResultado += buscarFacturasEnLasCarpetas(subdirectorio)

        
    return archivosResultado


"""
Comprueba si el archivo es una factura
@param pListaDeArchivos: lista de strings con los url de los archivos de las facturas
"""
def comprobarSiEsFactura(pListaDeArchivos):
    """
    Comprueba si el archivo es una factura
    @param pListaDeArchivos: lista de strings con los url de los archivos de las facturas
    """
        

    mascaraExtensionXml = re.compile(r'\.xml$')
    Resultado=[]
    
    for archivo in pListaDeArchivos:
        tst = mascaraExtensionXml.search(archivo)
        if mascaraExtensionXml.search(archivo) != None:
            Resultado.append(archivo)
            print("#Mensaje# Se ha encontrado una factura: " + archivo)
        
    return Resultado


def esUrlAbsoluta(pUrl):
    """
    Se revisa si la url es relativa o absoluta
    @param pUrl: String con la url
    @return: Retorna True si la url es absoluta, False en caso de que sea relativa
    """
    
        
    return True
    
def EncontrarArchivoDeExcelConMacros(pUrl):
    
    directorio, subdirectorios, archivos = next(walk(pUrl))
    mascaraExtensionXml = re.compile(r'\.xlsm$')
    
    
    for archivo in archivos:
        tst = mascaraExtensionXml.search(archivo)
        if mascaraExtensionXml.search(archivo) != None:
            resultado = directorio +  archivo
            return resultado


    return None
