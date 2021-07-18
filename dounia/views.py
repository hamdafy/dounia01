from django.shortcuts import render,redirect
def pageoffii(request):

    return render(request,"dounia/base.html")


def service(request):
    return render(request, "dounia/service.html")

def start(request):
    return render(request, "dounia/start.html")

def location(request):
    return render(request, "dounia/location.html")

def rendezvous(request):
    return render(request, "dounia/rendezvous.html")
