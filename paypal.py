#calculo de las tasas y comisiones para pagos paypal
#tasa 5.4% 
#comision 0.30$
def calculo(command):
    monto = float(command)
    total= round((monto+0.30)/0.946,2)
    return total

