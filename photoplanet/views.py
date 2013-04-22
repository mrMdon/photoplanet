
from django.http import HttpResponse
from django.views.generic import TemplateView


def hello(request):
 return HttpResponse('Hello,world')
