from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Index")


class HelloView(View):

    msg = None

    def get(self, request):
        return HttpResponse("GET OK %s" % self.msg)


class HelloTemplate(TemplateView):
    pass