import requests
import smtplib
import os


owpe= "https://api.openweathermap.org/data/2.5/forecast"
LAT = 30.319781200140344
LONG = -97.85182214531893
cnt = 4
api_key = os.environ.get("OWM_API_KEY")
my_email = os.environ.get("EMAIL_US")
password = os.environ.get("PASSWORD")

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": cnt

}
response = requests.get(url=owpe, params= parameters)
response.raise_for_status()
weather_data = response.json()
print (weather_data)
for i in range(cnt):
    if weather_data["list"][i]["weather"][0]["id"] < 700:
        will_rain = True
    else:
        will_rain = False
print (will_rain)
if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="kiran.gonsalves@gmail.com",
                        msg=f"Subject:weather condition\n\nDear Valued Citizen,\n\n"
                            f"Please bring an umbrella today\n\n"
                            f"Love,\n"
                            f"Sanchia")
    connection.close()
