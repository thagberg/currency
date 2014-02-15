from django.http import HttpResponse

def readfile(filename):
    fh = open(filename, 'rb')
    r = fh.read()
    fh.close()
    return r

def index(request):
	return HttpResponse(readfile("www/index.html"))

def app(request):
	return HttpResponse(readfile("www/app.html"))

def serve_file(request, filename):
    return HttpResponse(readfile("www/"+filename))
