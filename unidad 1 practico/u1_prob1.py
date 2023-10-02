def calcular_impuesto_isr(cantidad):
    if cantidad <= 0:
        return "La cantidad debe ser mayor que cero."
    elif cantidad < 10000:
        impuesto = cantidad * 0.05
    elif cantidad < 20000:
        impuesto = cantidad * 0.15
    elif cantidad < 35000:
        impuesto = cantidad * 0.20
    elif cantidad < 60000:
        impuesto = cantidad * 0.30
    else:
        impuesto = cantidad * 0.45
    
    return impuesto


cantidad = float(input("Ingrese la cantidad para calcular el impuesto: "))
impuesto_calculado = calcular_impuesto_isr(cantidad)
print(f"El impuesto es: {impuesto_calculado}")
