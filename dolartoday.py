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
        mensualidad = round(7 * precio, 2)
        
        mensaje = 'El precio del dolar en Venezuela segun DolarToday es de: {} y el monto de la mensualidad sera de {} '.format(precio, mensualidad)

        return mensaje
