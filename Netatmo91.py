import requests
import json
def get_access_token():
    payload = {'grant_type': 'password',
           'username': "mc_cube@list.ru",
           'password': "",
           'client_id':"",
           'client_secret': ""
           #'scope': 'read_camera'
           }
    response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
    response.raise_for_status()
    access_token=response.json()["access_token"]
    print("Access token: ", access_token)
    return access_token

def getpublicdata(token, lat_ne, lon_ne, lat_sw, lon_sw):
    host="https://api.netatmo.com/api/getpublicdata?access_token="
    s=(f"{host}{token}&lat_ne={lat_ne}&lon_ne={lon_ne}&lat_sw={lat_sw}&lon_sw={lon_sw}&filter=true&required_data=temperature")
    response = requests.get(s)
    return response.json()


if __name__=='__main__':
    token=get_access_token()
    r=getpublicdata(token, 56, 93, 55, 92)
    if r['status']=='ok':
        for i in r['body']:
            for j in i['modules']:
                try:
                    measures=i['measures'][j]
                except:
                    pass
                print(measures)
    else:
        print(r)

#https://dev.netatmo.com/en-US/resources/technical/samplessdks/tutorials
