from django.shortcuts import render
from django.http import HttpResponse
from paladiy.func import paladiy

def index(request):
    return HttpResponse(f'Курс паладия за последние 10 дней: {paladiy()}')

# Create your views here.
