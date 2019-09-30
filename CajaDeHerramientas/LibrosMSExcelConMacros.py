'''
Created on 28 sep. 2019

@author: Crucio



'''


import win32com.client as clienteW2
import os
from  CajaDeHerramientas.PartesDeLaFactura import lineaDeServicio

def cargarFacturasEnLibroDeExcel(pUrlDelLibroDeExcel, pListaConLasFacturas):
    
    i = 0
    cantidadDeFacturas = len(pListaConLasFacturas)
    if os.path.exists(pUrlDelLibroDeExcel):
        
        ProgramaExcel = clienteW2.Dispatch("Excel.Application")
        ProgramaExcel.Visible = 1
        LibroDeTrabajo = ProgramaExcel.Workbooks.Open(Filename=pUrlDelLibroDeExcel, ReadOnly = 0)
        LibroDeTrabajoM = ProgramaExcel.ActiveWorkbook
        HojaDeTrabajo = LibroDeTrabajoM.Sheets(1)
        
        for Factura in pListaConLasFacturas:
            
            
            HojaDeTrabajo.Cells(100, 2).Value = Factura.NumeroConsecutivo
            HojaDeTrabajo.Cells(101, 2).Value = Factura.obtenerNombreEmisor()
            IdEmisor = Factura.obtenerTipoIDEmisor() + "#" + Factura.obtenerIDEmisor()
            HojaDeTrabajo.Cells(102, 2).Value = IdEmisor 
            
            HojaDeTrabajo.Cells(103, 2).Value = Factura.obtenerNombreReceptor()
            IdReceptor = Factura.obtenerTipoIDReceptor() + "#" + Factura.obtenerIDReceptor()
            HojaDeTrabajo.Cells(104, 2).Value =  IdReceptor
            
            HojaDeTrabajo.Cells(105, 2).Value = Factura.TotalImpuesto
            HojaDeTrabajo.Cells(106, 2).Value = Factura.TotalVentaNeta
            
            
            HojaDeTrabajo.Cells(107, 2).Value  = Factura.TotalGravado
            HojaDeTrabajo.Cells(108, 2).Value  = Factura.TotalExento
            HojaDeTrabajo.Cells(109, 2).Value = Factura.TotalExonerado
            
            HojaDeTrabajo.Cells(110, 2).Value = Factura.TotalDescuento
            
            HojaDeTrabajo.Cells(111, 2).Value = Factura.TotalComprobante
            HojaDeTrabajo.Cells(112, 2).Value  =Factura.Fecha.split("T")[0]
            
            
            ProgramaExcel.Application.Run("IntroducirFactura")
            
            for producto in Factura.detallesDeLosServicios:
                
                HojaDeTrabajo.Cells(100, 5).Value = producto.UnidadMedida
                HojaDeTrabajo.Cells(101, 5).Value = producto.Detalle
                HojaDeTrabajo.Cells(102, 5).Value = producto.Cantidad
                HojaDeTrabajo.Cells(103, 5).Value = producto.PrecioUnitario
                HojaDeTrabajo.Cells(104, 5).Value = producto.MontoTotal
                HojaDeTrabajo.Cells(105, 5).Value = producto.NaturalezaDescuento
                HojaDeTrabajo.Cells(106, 5).Value = producto.MontoDescuento
                HojaDeTrabajo.Cells(107, 5).Value = producto.SubTotal
                HojaDeTrabajo.Cells(108, 5).Value = producto.TarifaImpuesto
                HojaDeTrabajo.Cells(109, 5).Value = producto.MontoImpuesto
                HojaDeTrabajo.Cells(110, 5).Value = producto.ImpuestoNeto
                HojaDeTrabajo.Cells(111, 5).Value = producto.MontoTotalLinea
                
                
                
                print("hola hola hola hola")
            
            
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
    
        