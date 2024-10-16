from django.http import HttpResponse
from django.template import loader

def error404(request):
  template = loader.get_template('indexxx.html')
  return HttpResponse(template.render())
