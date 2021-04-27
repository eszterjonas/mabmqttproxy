from django.http import HttpResponse
from django.shortcuts import render
import paho.mqtt.client as mqtt
import sys
from . import mqtt
import json


def add(request):
    message = request.GET.get('message', '')
    mqtt.publishMessage(message,"add")
    return HttpResponse('<h1> haliho </h1>')


def vote(request):
    message = request.GET.get('message', '')
    mqtt.publishMessage(message,"vote")
    return HttpResponse('<h1> haliho </h1>')

def chat(request):
    message = request.GET.get('message', '')
    mqtt.publishMessage(message,"chat")
    return HttpResponse('<h1> haliho </h1>')

def home(request):
    return HttpResponse('<h1> Haliho ez a Levi & Eszter MAB Mqtt Proxyja. :) </h1>')
