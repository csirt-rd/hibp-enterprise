############################################################################################################################################################
#Con este script importamos los dominios x.gob.do que se encuentren en un archivo proporcionado que contiene los dominios validos mencionados anteriolmente.
############################################################################################################################################################

import requests #Importamos la biblioteca request para poder enviar solicitudes HTTP al servidor Have I Been Pwned.

filename = 'Dominios.txt' #Seleccionamos la ruta del archivo.

with open(filename) as obj: #Abrimos el archivo para luego leerlo.
    
    
    for i in obj: #el proposito de esta iteracion es que podamos leer el archivo linea por linea y enviar la peticion post al servidor para registrar el dominio.
        
        print(i.rstrip()) #imprimos los dominios enviados sin espacios y sin saltos de lineas.

        url = 'https://haveibeenpwned.com/api/v2/enterprisesubscriber/domain' #URL utilizada para añadir dominios esta info se encuentra en la documentacion.

        headers = { 'Authorization': 'Bearer C63ogLvJNSN_kP9cv-TyiOrc6-eYN5HfplElWhKsf3qzP-7yg68o38yBbepMueh12iM5d6thTx9dAQEzNHkKxdQkXjIoBFQa5uTmCqJtWxw-usVa4w_71_SZyaABrZUdSS8qAEoMqmO2vyygttwt-jgl9A-zOgjdP_h-Kjw9DJINhuZGnKTRVE1Xjfv0mXoqE8KctwYQD2UXePN8K1QKRRN0OV691Q-Rxe9bvCX4XVv-GV-f3X4O2NZ-Jf6wMs0Fi9nhVNgYdzW0wMTr_zgWyGstPjWiQMsvV8PNLX0iB_guiF6P0EEdQP8Wwl6eOWeOAQ2l6v1KJYxHbi9FargW9iMcMJOLUMN4tHxbdk7SzqJvvYVqoaQ8FFopPMuePPeslOGetDjTSLLR5XFKAjPrbCJTu0JBwPtiZ4ftQ3H8dKI','Content-Type': 'application/x-www-form-urlencoded'}

        payload = {'domain': i.strip()} #Como key la pasamos el dominio y luego le pasamos el dominio leido por el script.

        response = requests.request('POST', url, headers=headers, data=payload) #le pasamos como solicitud el POST con los datos cargados.

        print(response.text) #Devolvemos la respuesta que nos suministra el servidor.

        
