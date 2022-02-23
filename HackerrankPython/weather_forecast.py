import requests

def getWeather1(city):
    r = requests.get(u"http://wthrcdn.etouch.cn/weather_mini?city=" + city)
    data = r.json()["data"]["forecast"][0]
    return "%s : %s, %s" % (city, data["low"], data["high"])

result = getWeather1(u"北京")
print(result)



def getWeather2(city):
    api_address = "http://wthrcdn.etouch.cn/weather_mini?city="
    city = input("city name: ")
    url = api_address + city
    json_data = requests.get(url).json()["data"]["forecast"][0]

    return "{}: {}, {}, {}".format(city, json_data["date"], json_data["low"], json_data["high"])

result = getWeather2(" ")
print(result)