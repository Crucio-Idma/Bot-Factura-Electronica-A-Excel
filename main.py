"""
Created on 28 sep. 2019

@author: Crucio
""" 
 
#===================================================================================

from  xml.dom import minidom
from os import scandir, getcwd, listdir, walk
from CajaDeHerramientas import bibliotecarioDeArchivos, factura, parserFacturas


#Variables de inicio================================================================

urlDelArchivoDeConfiguraciones = "configuraciones/manejoDeArchivos.xml"

FacturasURLS = []
FacturasObjetos = []

#===================================================================================

#Se carga el archivo XML============================================================
try:
    _ArchivoConfig = minidom.parse(urlDelArchivoDeConfiguraciones)
    
except Exception as error:
    print("No se pudo cargar el archivo de configuraciones\n")
    print("El error ocurrido a sido:\n" + str(error))



_UrlInputDeArchivos =  _ArchivoConfig.getElementsByTagName("urlCarpetaDeEntrada")[0].firstChild.data
#directorios, subdirectorios, archivos
FacturasURLS = bibliotecarioDeArchivos.buscarFacturasEnLasCarpetas(_UrlInputDeArchivos)

for urlFactura in FacturasURLS:
    
    temporalObjetoFactura = parserFacturas.cargarFacturaDesdeArchivo(urlFactura)
    
    if temporalObjetoFactura != None:
        
        FacturasObjetos.append(temporalObjetoFactura)
    

    
print("MMM")
print("MMM")
