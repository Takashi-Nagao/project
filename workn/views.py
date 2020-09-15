from django.shortcuts import render

def index (request):
  return render (request, 'workn/index.html')

def add (request):
  return render (request, 'workn/add.html')