from django.shortcuts import render
import logging
from django.http import HttpResponse
from datetime import *
import random

logger= logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='fersapp.log',filemode='a',format='%(levelname)s %(message)s')

def index(request):
    context = {
        'text': 'Добро пожаловать на мою первую страницу \ это только начало'
    }
    return render (request, 'fersapp/index.html',context=context)

def about(request):
    html = "<h1>Это страница обо мне</h1>" \
           "<p>Меня зовут Илья. Я уже год учусть в GB </p>"
    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)

def coin(request):
    
    return HttpResponse(random.choice(["Орёл","Решка"]))

def cube(request):
    logger.info('hhfhfhf')
    return HttpResponse(random.choice(["Один","Два","Три","Четыре","Пять","Шесть"]))