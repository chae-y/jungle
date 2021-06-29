import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

#print(rjson)
#print(rjson['RealtimeCityAir']['row'][0]['NO2'])


gue=rjson['RealtimeCityAir']['row']
for gu in gue:
    print(gu['MSRSTE_NM'],gu['IDEX_MVL'])