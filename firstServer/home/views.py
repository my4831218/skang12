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
    if return_str == 선택 1:
        return JsonResponse(
            { #return 밑에는 공통어
                "message": {
                    "text": "안녕하세요?"
            }
        }
        )
