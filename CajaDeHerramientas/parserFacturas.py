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
        
        resultadoFactura = factura.Factura(pNombreEmisor ,pTipoIdentificacionEmisor ,pNumeroDeIdentificacionEmisor, pNombreReceptor,pTipoIdentificacionReceptor, pNumeroDeIdentificacionReceptor , pTotalImpuesto, pTotalVentaNeta, pTotalComprobante, pFecha)
        
        return resultadoFactura
        
    else:    
    #except:
        
        print("#Error# Datos incompletos en la factura" )
        return None
    
    
    
    