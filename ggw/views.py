from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from ggw.models import User, City, Trip

def index(request):
    return render(request, 'ggw/index.html', None)