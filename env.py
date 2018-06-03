import requests

area=input('Region_name = ')

url='http://api.openweathermap.org/data/2.5/weather?q='+area+'&appid=40ec861494fcce665c5a32bf3ee37e41'

json_data=requests.get(url).json()
try:
	temp= str(round(json_data['main']['temp'] - 273.15,2))
	weather=json_data['weather'][0]['description']
	speed=str(json_data['wind']['speed'])
	print('temp : '+temp+' degree C ')
	print('weather : '+ weather)
	print('wind : '+speed+' m/s')
	print('if you like this please upvote!!!')

except KeyError:
	print("Sorry for inconvenience\nRegion not found please try other ")


