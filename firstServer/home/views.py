from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import urllib.request
import json
import datetime
import requests

def keyboard(request) :
    return JsonResponse(
        {
        "type" : "buttons",
        "buttons" : ["선택 1", "선택 2", "선택 3"],
        }
    )

@csrf_exempt
def message(request) :
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']

    if return_str == '선택 1':
        return JsonResponse(
            { #return 밑에는 공통어
                "message": {
                    "text": weather()
                }
            }
        )
    if return_str == '선택 2':
        return JsonResponse(
            { #return 밑에는 공통어
                "message": {
                    "text": "안녕하셈?"
                }
            }
        )
    if return_str == '선택 3':
        return JsonResponse(
            { #return 밑에는 공통어
                "message": {
                    "text": "안녕하삼?"
                }
            }
        )
    
def weather():
    params = {"version": "1", "city":"서울", "county":"광진구","village":"군자동"}
    headers = {"appKey": "37a76141-3e16-46d4-a7b7-af72fe211ee2"}
    response = requests.get("https://api2.sktelecom.com/weather/current/minutely", params=params, headers=headers)
    data = json.loads(response.text)
    weather = data["weather"]["minutely"]
    sky = weather[0]["sky"]["name"]
    wind = weather[0]["wind"]["wspd"]
    temp = weather[0]["temperature"]["tc"]
    time = weather[0]["timeObservation"]

    printweather = '하늘 : ' + sky + '\n' + '온도 : ' + temp + 'C\n' + '풍속 : ' + wind + 'm/s'
    return printweather
        
