from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
# from rest_framework.decorators import api_view

# @api_view(['GET'])
# def hello_world(request):
#     return Response({"message": "Welcome to ALX Travel App!"})


from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to ALX Travel Listings API"})
