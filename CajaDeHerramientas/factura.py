'''
Created on 28 sep. 2019

@author: Crucio
'''
from PartesDeLaFactura import * 
from CajaDeHerramientas.PartesDeLaFactura.persona import persona

class Factura:
    
    def __init__(self , pemisor ,ptipoIDEmisor ,pidEmisor, preceptor,pTidoIdReceptor, pidreceptor , pTotalImpuesto, pTotalVentaNeta, pTotalComprobante):
        
        self.receptor = preceptor
        self.TotalImpuesto = pTotalImpuesto
        self.TotalVentaNeta= pTotalVentaNeta
        self.TotalComprobante = pTotalComprobante
    
        self.emisor = persona( pNombre =pemisor, pTipoIdentificacion = ptipoIDEmisor ,pIdentificacion = pidEmisor )
        self.receptor = persona( pNombre = preceptor, pTipoIdentificacion = pTidoIdReceptor ,pIdentificacion = pidreceptor )
        
    
    def obtenerNombreEmisor(self):       
        
        return self.emisor.Nombre
    
    def obtenerTipoIDEmisor(self):
        
        return self.emisor.TipoIdentificacion
    
    def obtenerIDEmisor(self):
        
        return self.emisor.Identificacion
    
    def obtenerNombreReceptor(self):       
        
        return self.receptor.Nombre
    
    def obtenerTipoIDReceptor(self):
        
        return self.receptor.TipoIdentificacion
    
    def obtenerIDReceptor(self):
        
        return self.receptor.Identificacion
    
    
    