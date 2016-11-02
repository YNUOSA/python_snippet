#!/usr/bin/env python2
# coding=utf8

import urllib
import json

# reset encoding
import sys
reload(sys)
sys.setdefaultencoding('utf8')

SYSTEM_ENCODING_NAME = sys.stdin.encoding
UTF8_ENCODING_NAME = 'utf8'

def convertEncoding(str, sourceEncoding, targetEncoding):
    return str.decode(sourceEncoding).encode(targetEncoding)

def getWeatherInfo(city_name = 'kunming'):
    """
    use the weather api of thinkpage
    :param city_name: the name of the city to query, which can be hanzi, pinyin, city_code
    :return:
    """
    # see more details on https://www.thinkpage.cn/doc
    request_url = 'https://api.thinkpage.cn/v3/weather/now.json?key=mqcsqujxpsaabuf3&location={city_name}'.format(city_name= convertEncoding(city_name, SYSTEM_ENCODING_NAME, UTF8_ENCODING_NAME));
    print 'The query url is {url}'.format(url = convertEncoding(request_url, UTF8_ENCODING_NAME, SYSTEM_ENCODING_NAME))
    response = urllib.urlopen(request_url)
    response_text = response.read()
    return json.loads(response_text)

if __name__ == '__main__':
    # set default city name
    city_name = 'kunming'
    if len(sys.argv) >= 2:
        city_name = str(sys.argv[1])
    print 'Searching the weather of {city_name}'.format(city_name=city_name)
    weatherInfo = getWeatherInfo(city_name)
    # if result is in the json object, then it's a success query
    if 'results' in weatherInfo:
        temperature = convertEncoding(weatherInfo['results'][0]['now']['temperature'], UTF8_ENCODING_NAME, SYSTEM_ENCODING_NAME)
        weather = convertEncoding(weatherInfo['results'][0]['now']['text'], UTF8_ENCODING_NAME, SYSTEM_ENCODING_NAME)
        print 'The weather of {city_name} is {weather}, its temperature is {temperature}'.format(city_name=city_name, weather=weather, temperature=temperature)
    # if status is in the json object, then something is error, such as wrong spell of city name
    elif 'status' in weatherInfo:
        print '{status}'.format(status=weatherInfo['status'])
    # if go here, something unpredictable situation occurs, we just print 'Something is error'
    else:
        print 'Something is error'