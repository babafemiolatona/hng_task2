from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import json
import os
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        operation_type = body['operation_type']
        x = int(body['x'])
        y = int(body['y'])

        if operation_type == 'addition':
            result = x + y
        elif operation_type == 'subtraction':
            result = x - y
        elif operation_type == 'multiplication':
            result = x * y
        else:
            return HttpResponse(status=400)

        response_data = {'slackUsername': 'outsider', 'result': result, 'operation_type': operation_type}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(status=405)

