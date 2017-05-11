from django.http import HttpResponse
from django.template import loader

from .models import Signal, Rule, Trigger, Action

def index(request):
    rules_list = Rule.objects.all()
    template = loader.get_template('phoenix/index.html')
    context = {
        'rules_list': rules_list,
    }
    return HttpResponse(template.render(context, request))
