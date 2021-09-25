from django.shortcuts import render, render

from django.template import RequestContext


def index(request):
    return render(request, "index.html")


def page_not_found(request, exception=None):
    return render(request, "page_not_found.html")
