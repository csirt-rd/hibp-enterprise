import requests, json, csv, urllib3, datetime, uuid
# Importamos las librerías de Azure
from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient

urllib3.disable_warnings() 

header_written = False

def request_api(domain):
    global header_written

    try: 

        headers = { 'Authorization': 'Bearer <TOKEN>','Content-Type': 'application/x-www-form-urlencoded','Content-Type': 'application/x-www-form-urlencoded'}
        url = "https://haveibeenpwned.com/api/v2/enterprisesubscriber/domainsearch/{}".format(domain) 
        print('# Respuesta: ', str(domain).ljust(80), end='\r') 
        response = requests.request('GET', url, headers=headers, timeout=15, verify=False, allow_redirects=True) 
        keyval = json.loads(response.content.decode('utf8')) 
        dic = dict(keyval)

        if keyval:
            with open('leaks.csv', 'a', encoding='UTF8', newline='') as output: 
                header = ['Domain', 'Account', 'Email' , 'Data-Breach', 'Count', 'Date'] 
                writer = csv.writer(output)
                if not header_written:
                    writer.writerow(header)
                    header_written = True
                for i in keyval:
                    brechas = ','.join(dic[i]) 
                    detail = [domain, i, i+'@'+domain ,brechas, (brechas.count(',') + 1), datetime.date.today()]
                    writer.writerow(detail)
                    print(detail) 

    except Exception as ex:
        print(ex)
        print('No se pudo obtener las brechas de datos')
filename = 'Dominios.txt'  

with open(filename, 'r') as file: 
    for i in file.readlines():
            request_api(i.strip()) 

# Nombre del contenedor donde se guardará el archivo
container_name = "ihbpwned"

  # Dirección URL de la cuenta de almacenamiento de Azure
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix=core.windows.net"

  # Usamos la cadena de conexión para crear un cliente de servicio de blob
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

  # Verificamos si el contenedor existe
if container_name not in [c.name for c in blob_service_client.list_containers()]:
      # Si el contenedor no existe, lo creamos
    container_client = blob_service_client.create_container(container_name)
else:
    container_client = blob_service_client.get_container_client(container_name)
    unique_file_name = str(uuid.uuid1()) + "_" + 'leaks.csv'
    blob_client = container_client.get_blob_client(unique_file_name)

  # Abrimos el archivo en modo lectura binaria
with open('leaks.csv', "rb") as data:
    blob_client.upload_blob(data)

