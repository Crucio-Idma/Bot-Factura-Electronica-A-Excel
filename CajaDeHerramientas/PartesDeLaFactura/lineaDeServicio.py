'''
Created on 28 sep. 2019

@author: Crucio



'''

class LineaDeServicio:
    
    def __init__(self, pUnidadMedida = 0, pCantidad = 0, pDetalle = 0, pPrecioUnitario = 0, pMontoTotal = 0 , pNaturalezaDescuento = 0, pMontoDescuento = 0, pSubTotal = 0 , pTarifaImpuesto = 0, pMontoImpuesto = 0, pImpuestoNeto = 0, pMontoTotalLinea = 0):
        
        self.UnidadMedida = pUnidadMedida
        self.Cantidad = pCantidad

        self.Detalle = pDetalle
        self.PrecioUnitario = pPrecioUnitario
        self.MontoTotal = pMontoTotal
        
        self.NaturalezaDescuento = pNaturalezaDescuento
        self.MontoDescuento = pMontoDescuento
        
        self.SubTotal = pSubTotal
        
        self.TarifaImpuesto = pTarifaImpuesto
        self.MontoImpuesto = pMontoImpuesto
        
        self.ImpuestoNeto = pImpuestoNeto
        self.MontoTotalLinea = pMontoTotalLinea
        
        