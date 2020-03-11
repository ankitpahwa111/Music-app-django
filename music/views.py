from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Hi  BHosdike </h1>")

def details(request, album_id):
    return HttpResponse("<h2> The details for the page with id " + str(album_id) + " </h2>")
