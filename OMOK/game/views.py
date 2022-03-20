from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import templates
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .api.omok import Omok

import json

@csrf_exempt
def index(request):
    context = {}
    return render(request, 'index.html', context)