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

i = 0
cantidadDeFacturas = len(FacturasObjetos)
if os.path.exists(ArchivoDeExcelATrabajar):
    
    ProgramaExcel = clienteW2.Dispatch("Excel.Application")
    ProgramaExcel.Visible = 1
    LibroDeTrabajo = ProgramaExcel.Workbooks.Open(Filename=ArchivoDeExcelATrabajar, ReadOnly = 0)
    LibroDeTrabajoM = ProgramaExcel.ActiveWorkbook
    HojaDeTrabajo = LibroDeTrabajoM.Sheets(1)
    
    for Factura in FacturasObjetos:
    
        HojaDeTrabajo.Cells(100, 2).Value = Factura.obtenerNombreEmisor()
        IdEmisor = Factura.obtenerTipoIDEmisor() + "#" + Factura.obtenerIDEmisor()
        HojaDeTrabajo.Cells(101, 2).Value = IdEmisor 
        
        HojaDeTrabajo.Cells(102, 2).Value = Factura.obtenerNombreReceptor()
        IdReceptor = Factura.obtenerTipoIDReceptor() + "#" + Factura.obtenerIDReceptor()
        HojaDeTrabajo.Cells(103, 2).Value =  IdReceptor
        
        HojaDeTrabajo.Cells(104, 2).Value = Factura.TotalImpuesto
        HojaDeTrabajo.Cells(105, 2).Value = Factura.TotalVentaNeta
        HojaDeTrabajo.Cells(106, 2).Value = Factura.TotalComprobante
        HojaDeTrabajo.Cells(107, 2).Value  =Factura.Fecha.split("T")[0]
        ProgramaExcel.Application.Run("IntroducirFactura")
        print("#Mensaje#FacturasPrograma->Excel#" + str(i) + "#"+ str(cantidadDeFacturas)) 
        i+=1
    try:
        
        
        LibroDeTrabajo.Save()
        LibroDeTrabajo.Close()
        ProgramaExcel.Quit()
        
    except:
    
    #else:    
        print("Error  de macros llenando las hojas")
            
            
        ProgramaExcel.Quit()



#================================================================================================================================================================================================================================================
print("MMM")
print("MMM")
