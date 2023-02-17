import requests
api_key="91b646691c059075c46a8d5dc88dba42"
user_input=input("Enter City: ")
print(user_input)
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json()['cod']=='404':
    print("No city Found")
else:
    weather= weather_data.json()['weather'][0]['main']
temp=round(weather_data.json()['main']['temp']) 
print(f"the weather in {user_input} is: {weather}")
print(f"the temperature in {user_input} is: {temp}")