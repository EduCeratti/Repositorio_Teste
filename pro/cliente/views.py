# -*- coding: utf-8 -*-
from django.http import HttpResponse
import redis


def index(request):

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    return HttpResponse('<html><br><br><center>Bem vindo.<br> Data atual é: ' + str(r.get('date_key')) + '</center></html>' )
