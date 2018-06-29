from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def keyboard(request):
    return JsonResponse (
    {
    "type" : "buttons",
    "buttons" : ["선택 1", "선택 2", "선택 3"],
    }
    )