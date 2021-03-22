from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from . import signals

class ApplicationView(TemplateView):
	template_name = "application.html"

def favicon_view(request):
	return HttpResponseRedirect('/static/favicon.ico')