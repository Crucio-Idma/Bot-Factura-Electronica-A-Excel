"""
Created on 28 sep. 2019

@author: Crucio
""" 
 
#===================================================================================

from  xml.dom import minidom
from os import scandir, getcwd, listdir, walk

import os
from CajaDeHerramientas import bibliotecarioDeArchivos, factura, parserFacturas, ArchivadorDisco

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

if os.path.exists(ArchivoDeExcelATrabajar):
    
    ProgramaExcel = clienteW2.Dispatch("Excel.Application")
    ProgramaExcel.Visible = 1
    LibroDeTrabajo = ProgramaExcel.Workbooks.Open(Filename=ArchivoDeExcelATrabajar, ReadOnly = 0)
    LibroDeTrabajoM = ProgramaExcel.ActiveWorkbook
    HojaDeTrabajo = LibroDeTrabajoM.Sheets(1)
    
    HojaDeTrabajo.Cells(100, 2).Value = FacturasObjetos[0].obtenerNombreEmisor()
    IdEmisor = FacturasObjetos[0].obtenerTipoIDEmisor() + "#" + FacturasObjetos[0].obtenerIDEmisor()
    HojaDeTrabajo.Cells(101, 2).Value = IdEmisor 
    
    HojaDeTrabajo.Cells(102, 2).Value = FacturasObjetos[0].obtenerNombreReceptor()
    IdReceptor = FacturasObjetos[0].obtenerTipoIDReceptor() + "#" + FacturasObjetos[0].obtenerIDReceptor()
    HojaDeTrabajo.Cells(103, 2).Value =  IdReceptor
    
    HojaDeTrabajo.Cells(104, 2).Value = FacturasObjetos[0].TotalImpuesto
    HojaDeTrabajo.Cells(105, 2).Value = FacturasObjetos[0].TotalVentaNeta
    HojaDeTrabajo.Cells(106, 2).Value = FacturasObjetos[0].TotalComprobante
    HojaDeTrabajo.Cells(107, 2).Value  =FacturasObjetos[0].Fecha.split("T")[0] 
    
    #ProgramaExcel =  clienteW2.Dispatch('Excel.Application')
    #LibroDeTrabajo = ProgramaExcel.Workbooks.Open(Filename = pUrlHojaDeExcel, ReadOnly = 0)
    try:
        ProgramaExcel.Application.Run("IntroducirFactura")
        LibroDeTrabajo.Save()
        LibroDeTrabajo.Close()
        ProgramaExcel.Quit()
            
        print("Se relleno el archivo: \n" + pUrlHojaDeExcel)
        #ProgramaExcel.Application.Run(pUrlHojaDeExcel + "!ModMacros.GenerarPrueba")
    except:
    
    #else:    
        print("Error  de macros llenando las hojas")
            
            
        ProgramaExcel.Quit()

    return True
                
    
else:
    return False
"""



#================================================================================================================================================================================================================================================
print("MMM")
print("MMM")
