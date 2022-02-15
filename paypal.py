#calculo de las tasas y comisiones para pagos paypal
#tasa 5.4% 
#comision 0.30$
def calculo(monto):
    monto = float(monto)
    total= round((monto+0.30)/0.946,2)
    return total


def calculo_venta(buyer_price, quantity):
    buyer_price = float(buyer_price)
    quantity = float(quantity)
    whit_tax = calculo(quantity)
    total = round (whit_tax * buyer_price, 2)
    return total


    