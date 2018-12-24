import requests
from pprint import pprint

#city = input('Enter your city : ')
latitude = input('Enter your latitude : ')
longitude = input('Enter your longitude : ')

url = 'https://api.darksky.net/forecast/81ce12e723d0682b9ec41556ccf59270/{},{}'.format(latitude,longitude )

res = requests.get(url)

data = res.json()

temp = data['currently']['temperature']
wind_speed = data['currently']['windSpeed']

latitude = data['latitude']
longitude = data['longitude']
timezone = data ['timezone']

description = data['hourly']['summary']

print('Temperature : {} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Time Zone : {}'.format(timezone))
print('Description : {}'.format(description))