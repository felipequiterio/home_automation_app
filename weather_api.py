import argparse
import requests
from bs4 import BeautifulSoup as bs

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 " \
             "Safari/537.36 "
# US english
LANGUAGE = "en-US,en;q=0.5"

URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"

parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                    Default is your current location determined by your IP Address""", default="")
# parse arguments
args = parser.parse_args()
region = args.region
URL += region


class WeatherData:

    def get_weather_data(url):
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE
        html = session.get(url)
        # create a new soup
        soup = bs(html.text, "html.parser")

        # store all results on this dictionary
        result = {'region': soup.find("div", attrs={"id": "wob_loc"}).text,
                  'temp_now': soup.find("span", attrs={"id": "wob_tm"}).text,
                  'dayhour': soup.find("div", attrs={"id": "wob_dts"}).text,
                  'weather_now': soup.find("span", attrs={"id": "wob_dc"}).text,
                  'precipitation': soup.find("span", attrs={"id": "wob_pp"}).text,
                  'humidity': soup.find("span", attrs={"id": "wob_hm"}).text,
                  'wind': soup.find("span", attrs={"id": "wob_ws"}).text}

        # get next few days' weather
        next_days = []
        days = soup.find("div", attrs={"id": "wob_dp"})
        for day in days.findAll("div", attrs={"class": "wob_df"}):

            # extract the name of the day
            day_name = day.findAll("div")[0].attrs['aria-label']

            # get weather status for that day
            weather = day.find("img").attrs["alt"]
            temp = day.findAll("span", {"class": "wob_t"})

            # maximum temperature in Celsius, use temp[1].text if you want fahrenheit
            max_temp = temp[1].text

            # minimum temperature in Celsius, use temp[3].text if you want fahrenheit
            min_temp = temp[3].text
            next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
        # append to result
        result['next_days'] = next_days
        return result

    data = get_weather_data(URL)
    print(data)

    location = data['region']
    temp_now = data['temp_now']
    weather_now = data['weather_now']
    precipitation = data['precipitation']
    humidity = data['humidity']
    wind = data['wind']
    nxt_day = data['next_days']

    print(location)
    print(temp_now)
    print(weather_now)
    print(precipitation)
    print(humidity)
    print(wind)
    print(nxt_day)

    temp = (int(temp_now) - 32) * 5 / 9
    temp = int(temp)
    temp = str(temp)

    print(temp)
