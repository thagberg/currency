from django.http import HttpResponse

def readfile(filename):
    fh = open(filename, 'rb')
    r = fh.read()
    fh.close()
    return r

ext_to_ct = {'js': 'application/javascipt', 'css': 'text/css', 'html': 'text/html'}    
    
def guess_content_type(filename):
    return ext_to_ct.get(filename.split('.')[1], 'text/plain')
    
def index(request):
	return HttpResponse(readfile("www/index.html"))

def app(request):
	return HttpResponse(readfile("www/app.html"))

def serve_file(request, filename):
    return HttpResponse(readfile("www/"+filename), mimetype=guess_content_type(filename))
