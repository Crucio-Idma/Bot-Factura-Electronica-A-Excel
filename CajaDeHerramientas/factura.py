'''
Created on 28 sep. 2019

@author: Crucio
'''
from PartesDeLaFactura import import persona 

class Factura:
    
    def __init__(self , pemisor, pidEmisor, preceptor, pidreceptor , pTotalImpuesto, pTotalVentaNeta, pTotalComprobante):
        
        self.emisor = pemisor
        self.receptor = preceptor
        self.TotalImpuesto = pTotalImpuesto
        self.TotalVentaNeta= pTotalVentaNeta
        self.TotalComprobante = pTotalComprobante
    
        