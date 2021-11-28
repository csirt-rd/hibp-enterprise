import requests #Importamos la biblioteca request para poder enviar solicitudes HTTP al servidor Have I Been Pwned.

filename = 'Dominios.txt' #Seleccionamos la ruta del archivo.

with open(filename) as obj: #Abrimos el archivo para luego leerlo.
    
    
    for i in obj: #el proposito de esta iteracion es que podamos leer el archivo linea por linea y enviar la peticion post al servidor para registrar el dominio.
        
        print(i.rstrip()) #imprimos los dominios enviados sin espacios y sin saltos de lineas.

        url = 'https://haveibeenpwned.com/api/v2/enterprisesubscriber/domain' #URL utilizada para añadir dominios esta info se encuentra en la documentacion.

        headers = { 'Authorization': 'Bearer <TOKEN>','Content-Type': 'application/x-www-form-urlencoded'}

        payload = {'domain': i.strip()} #Como key la pasamos el dominio y luego le pasamos el dominio leido por el script.

        response = requests.request('POST', url, headers=headers, data=payload) #le pasamos como solicitud el POST con los datos cargados.

        print(response.text) #Devolvemos la respuesta que nos suministra el servidor.

        
