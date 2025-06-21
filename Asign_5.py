import requests
import pandas as pd

params = {
    "key":"2e4bef5469974e628b1192000251406",
    "q":"176.111.185.41",
    "days":"7"
}

r = requests.get("http://api.weatherapi.com/v1/forecast.json", params=params)

totalforecast = r.json()["forecast"]['forecastday']

dic = {}

for i in totalforecast:
    dic[i["date"]] = pd.DataFrame(columns=["hour", "temp", "wind_speed"])
    for k in i["hour"]:
        dic[i["date"]] = pd.concat([dic[i["date"]], pd.DataFrame({"hour":[k["time"].split(" ")[1]], "temp":[k["temp_c"]], "wind_speed":[k["wind_kph"]]})])

df = pd.DataFrame(columns=["hour", "temp", "wind_speed"])

for i in range(3):
    df = pd.concat([df, dic[list(dic.keys())[i]]])

print("Min temperature -", df["temp"].min())
print("Max temperature -", df["temp"].max())
print("Average temperature -", df["temp"].mean())

for i in range(3, 7):
    df = pd.concat([df, dic[list(dic.keys())[i]]])

print(len(df[df["wind_speed"]>df["wind_speed"].mean()]), "hours have wind speed greater than the overall average wind speed")