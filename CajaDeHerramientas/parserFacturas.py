'''
Created on 28 sep. 2019

Este es el parse que traduce las facturas

@author: Crucio
'''


from CajaDeHerramientas import factura
from  xml.dom import minidom



def cargarFacturaDesdeArchivo(pUrlDelaFactura):
    
    if True:
    #try:
    
        _FacturaXML = minidom.parse(pUrlDelaFactura)
        
        
        FacturaSinFirmas = _FacturaXML.getElementsByTagName("FacturaElectronica")[0]
        
        NumeroConsecutivo = FacturaSinFirmas.getElementsByTagName("NumeroConsecutivo")[0].firstChild.data
        
         
        Emisor = FacturaSinFirmas.getElementsByTagName("Emisor")[0]
        pNombreEmisor = Emisor.getElementsByTagName("Nombre")[0].firstChild.data
        
        pFecha = FacturaSinFirmas.getElementsByTagName("FechaEmision")[0].firstChild.data
        
        _FacturaXML = minidom.parse(pUrlDelaFactura)
        FacturaSinFirmas = _FacturaXML.getElementsByTagName("FacturaElectronica")[0] 
        Emisor = FacturaSinFirmas.getElementsByTagName("Emisor")[0]
        pNombreEmisor = Emisor.getElementsByTagName("Nombre")[0].firstChild.data
    
        IdentificacionXMLEmisor = Emisor.getElementsByTagName("Identificacion")[0]
        pTipoIdentificacionEmisor = IdentificacionXMLEmisor.getElementsByTagName("Tipo")[0].firstChild.data
        pNumeroDeIdentificacionEmisor = IdentificacionXMLEmisor.getElementsByTagName("Numero")[0].firstChild.data

#========================================================================================================================

        Receptor = FacturaSinFirmas.getElementsByTagName("Receptor")[0]
        pNombreReceptor = Receptor.getElementsByTagName("Nombre")[0].firstChild.data
    
        IdentificacionXMLReceptor =  Receptor.getElementsByTagName("Identificacion")[0]
        pTipoIdentificacionReceptor = IdentificacionXMLReceptor.getElementsByTagName("Tipo")[0].firstChild.data
        pNumeroDeIdentificacionReceptor = IdentificacionXMLReceptor.getElementsByTagName("Numero")[0].firstChild.data


        ResumenFacturaXML = FacturaSinFirmas.getElementsByTagName("ResumenFactura")[0]
        pTotalImpuesto = float( ResumenFacturaXML.getElementsByTagName("TotalImpuesto")[0].firstChild.data)
        pTotalVentaNeta = float( ResumenFacturaXML.getElementsByTagName("TotalVentaNeta")[0].firstChild.data)
        pTotalComprobante = float( ResumenFacturaXML.getElementsByTagName("TotalComprobante")[0].firstChild.data)
        
        
        try:
            
            pTotalExcentoP = ResumenFacturaXML.getElementsByTagName("TotalExento")[0].firstChild.data
        
        except:
            
            pTotalExcentoP = 0
        
        try:
            
            pTotalGravadoP = ResumenFacturaXML.getElementsByTagName("TotalGravado")[0].firstChild.data
        
        except:
            
            pTotalGravadoP = 0
        
        try:
            
            pTotalExoneradoP = ResumenFacturaXML.getElementsByTagName("TotalExonerado")[0].firstChild.data 
            
        except:
            
            pTotalExoneradoP = 0
         
        try:
            
            pTotalDescuentoP = ResumenFacturaXML.getElementsByTagName("TotalDescuentos")[0].firstChild.data 
            
        except:
            
            pTotalDescuentoP = 0
        
        
        resultadoFactura = factura.Factura(NumeroConsecutivo, pNombreEmisor ,pTipoIdentificacionEmisor ,pNumeroDeIdentificacionEmisor, pNombreReceptor,pTipoIdentificacionReceptor, pNumeroDeIdentificacionReceptor , pTotalImpuesto, pTotalVentaNeta, pTotalComprobante, pFecha, pTotalExento = pTotalExcentoP, pTotalGravado = pTotalGravadoP, pTotalExonerado = pTotalExoneradoP, pTotalDescuento = pTotalDescuentoP)
        
        
        
        
        LineasDeServicios = FacturaSinFirmas.getElementsByTagName("DetalleServicio")[0].getElementsByTagName("LineaDetalle")
        
        
        for servicio in LineasDeServicios:
            
            
            
            
            
            
            
            
            
            
            resultadoFactura.introducirLineaDeServicio(piUnidadMedida = 0, piCantidad = 0, piDetalle = 0, piPrecioUnitario = 0, piMontoTotal = 0 , piNaturalezaDescuento = 0, piMontoDescuento = 0, piSubTotal = 0 , piTarifaImpuesto = 0, piMontoImpuesto = 0, piImpuestoNeto = 0, piMontoTotalLinea = 0)
         
        
        
        return resultadoFactura
        
    else:    
        
        
        
    #except:
        
        print("#Error# Datos incompletos en la factura" )
        return None
    
    
    
    