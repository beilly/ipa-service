from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def plist(request):
    with open('static/dkw_ios_test.plist', 'r', encoding='UTF-8') as f:
        c = f.read()
    response = HttpResponse(c)

    file_name = "ios_test.plist"
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="{0}"'.format(file_name)
    
    return response
