import requests
from django.http import HttpResponse
import logging

# Create your views here.
logger = logging.getLogger("django")


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    logger.info(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def plist(request, ipa_id):
    with open('static/dkw_ios_test.plist', 'r', encoding='UTF-8') as f:
        c = f.readlines()

    logger.info(ipa_id)

    result=[]
    for line in c:
        if '{{id}}' in line:
            line = line.replace('{{id}}', ipa_id)
        result.append(line)

    response = HttpResponse(result)

    file_name = "ios_test.plist"
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)

    return response
