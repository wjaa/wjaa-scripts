# !/usr/bin/env	python

from django.http import HttpResponse
from django.template import Context, loader

def index (request):
	template = loader.get_template('pages/index.html')
	context = Context({'param':"param",})
	return HttpResponse(template.render(context))
