from django.shortcuts import render
from django.http import HttpResponse

def chores(request):
    return HttpResponse("chores")
