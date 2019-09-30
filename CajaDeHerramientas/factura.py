'''
Created on 28 sep. 2019

@author: Crucio
'''

from CajaDeHerramientas.PartesDeLaFactura import persona

class Factura:
    
    def __init__(self, pNumeroConsecutivo , pemisor ,ptipoIDEmisor ,pidEmisor, preceptor,pTidoIdReceptor, pidreceptor , pTotalImpuesto, pTotalVentaNeta, pTotalComprobante, pfecha, pTotalGravado = 0 , pTotalExento = 0, pTotalExonerado = 0, pTotalDescuento = 0):
        
        self.NumeroConsecutivo = pNumeroConsecutivo
        self.receptor = preceptor
        self.TotalImpuesto = pTotalImpuesto
        self.TotalVentaNeta= pTotalVentaNeta
        self.TotalComprobante = pTotalComprobante
        self.Fecha = pfecha
    
        self.emisor = persona.Persona(pNombre =pemisor, pTipoIdentificacion = ptipoIDEmisor ,pIdentificacion = pidEmisor )
        self.receptor = persona.Persona(pNombre = preceptor, pTipoIdentificacion = pTidoIdReceptor ,pIdentificacion = pidreceptor )
        self.TotalGravado = pTotalGravado
        self.TotalExento = pTotalExento
        self.TotalExonerado = pTotalExonerado
        
        self.TotalDescuento = pTotalDescuento
        
        self.detallesDeLosServicios = []
    
    
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
    
    
    