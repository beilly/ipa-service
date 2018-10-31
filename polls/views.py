import logging

import requests
from django.http import HttpResponse

# Create your views here.
logger = logging.getLogger("django")


# 默认显示
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    return HttpResponse('<pre>' + r.text + '</pre>')


# 获取plist
def plist(request, pid, ipa_id):
    with open('static/' + pid + '.plist', 'r', encoding='UTF-8') as f:
        c = f.readlines()

    logger.info(ipa_id)

    result = []
    for line in c:
        if '{{id}}' in line:
            line = line.replace('{{id}}', ipa_id)
        result.append(line)

    response = HttpResponse(result)

    file_name = "ios_test.plist"
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)

    return response
