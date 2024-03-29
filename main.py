"""
Created on 28 sep. 2019

@author: Crucio
""" 
 
#===================================================================================

from  xml.dom import minidom
from os import scandir, getcwd, listdir, walk

import os
from CajaDeHerramientas import bibliotecarioDeArchivos, factura, parserFacturas, ArchivadorDisco, LibrosMSExcelConMacros


#==================Temporal=======================================================================================
import win32com.client as clienteW2
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
_UrlOutputDeArchivos =  _ArchivoConfig.getElementsByTagName("urlCarpetaDeSalida")[0].firstChild.data
_UrlInputDePlantillaExcel =  _ArchivoConfig.getElementsByTagName("urlPlantillaExcel")[0].firstChild.data

#directorios, subdirectorios, archivos
FacturasURLS = bibliotecarioDeArchivos.buscarFacturasEnLasCarpetas(_UrlInputDeArchivos)
_UrlOutputDeArchivos = ArchivadorDisco.crearCarpetas(_UrlOutputDeArchivos)
ArchivadorDisco.crearCarpetas(_UrlOutputDeArchivos + "/LibrosDeExcel")
ArchivadorDisco.crearArchivoEnBaseAUnaPlantilla(_UrlInputDePlantillaExcel, _UrlOutputDeArchivos + "/LibrosDeExcel")

#====================================================================================================================================================================================

i = 0
largo = str(len(FacturasURLS))


for urlFactura in FacturasURLS:
    
    temporalObjetoFactura = parserFacturas.cargarFacturaDesdeArchivo(urlFactura)
    
    if temporalObjetoFactura != None:
        
        FacturasObjetos.append(temporalObjetoFactura)
        
    print("#FacturasAMemoria#" + str(i) +"de " + largo)
    
    i+=1

#================================================================================================================================================================================================================================================




ArchivoDeExcelATrabajar = bibliotecarioDeArchivos.EncontrarArchivoDeExcelConMacros(_UrlOutputDeArchivos + "/LibrosDeExcel")
ArchivoDeExcelATrabajar = ArchivoDeExcelATrabajar.replace("/", "\\")

LibrosMSExcelConMacros.cargarFacturasEnLibroDeExcel(ArchivoDeExcelATrabajar, FacturasObjetos)


#================================================================================================================================================================================================================================================
print("MMM")
print("MMM")
