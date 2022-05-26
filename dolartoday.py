import requests
import json
import time




class Dolartoday():
   
    def __init__(self, url):
        self.url = url

    
    def get_data(self):
        response = requests.get(self.url)
        
        with open ('data.json', 'w') as file:
            json.dump(response.json(), file)

        with open ('data.json', 'r') as file:
            data = json.load(file)

        precio = data['USD']['dolartoday']
        precioComision = round(precio * 0.05 + precio , 2)
        mensualidad = round(7 * precioComision, 2)
        
       


        mensaje = 'El precio promedio del dolar en Venezuela es de: {} bs y el monto de la mensualidad sera de {} bs '.format(precioComision, mensualidad) 

        return mensaje


