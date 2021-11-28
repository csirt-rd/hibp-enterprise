import requests, json, csv, urllib3, datetime

urllib3.disable_warnings() 

def request_api(domain): 

    try: 

        headers = { 'Authorization': 'Bearer C63ogLvJNSN_kP9cv-TyiOrc6-eYN5HfplElWhKsf3qzP-7yg68o38yBbepMueh12iM5d6thTx9dAQEzNHkKxdQkXjIoBFQa5uTmCqJtWxw-usVa4w_71_SZyaABrZUdSS8qAEoMqmO2vyygttwt-jgl9A-zOgjdP_h-Kjw9DJINhuZGnKTRVE1Xjfv0mXoqE8KctwYQD2UXePN8K1QKRRN0OV691Q-Rxe9bvCX4XVv-GV-f3X4O2NZ-Jf6wMs0Fi9nhVNgYdzW0wMTr_zgWyGstPjWiQMsvV8PNLX0iB_guiF6P0EEdQP8Wwl6eOWeOAQ2l6v1KJYxHbi9FargW9iMcMJOLUMN4tHxbdk7SzqJvvYVqoaQ8FFopPMuePPeslOGetDjTSLLR5XFKAjPrbCJTu0JBwPtiZ4ftQ3H8dKI','Content-Type': 'application/x-www-form-urlencoded'}

        url = "https://haveibeenpwned.com/api/v2/enterprisesubscriber/domainsearch/{}".format(domain) 

        print('# Respuesta: ', str(domain).ljust(80), end='\r') 

        response = requests.request('GET', url, headers=headers, timeout=15, verify=False, allow_redirects=True) 

        keyval = json.loads(response.content.decode('utf8')) 

        dic = dict(keyval)

        if keyval:

            with open('Reporte.csv', 'a', encoding='UTF8', newline='') as output: 

                header = ['Domain', 'Account', 'Data-Breach', 'Count', 'Date'] 

                writer = csv.writer(output)

                writer.writerow(header)

                for i in keyval:

                    brechas = ','.join(dic[i]) 

                    detail = [domain, i, brechas, (brechas.count(',') + 1), datetime.date.today()]
                    
                    writer.writerow(detail)

                    print(detail) 

    except Exception as ex:

        print(ex)

        print('No se pudo obtener las brechas de datos')

filename = 'Dominios.txt'  

with open(filename, 'r') as file: 
    
    for i in file.readlines():

            request_api(i.strip()) 