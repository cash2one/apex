from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template('homepage/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def policy(request):
    template = loader.get_template('homepage/policy.html')
    context = {}
    return HttpResponse(template.render(context, request))
