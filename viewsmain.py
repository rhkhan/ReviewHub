from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse,reverse_lazy
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from django.views import generic

#from .models import Country
# Create your views here.

def index(request):
	context={
		'header_line':"Welcome to the central hub of freelancers"
	}
	return render(request,'reviewhub/index.html',context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'reviewhub/signup.html'

#def countryList(request):
	#countries=Country.objects.all() #.order_by('id')[:5]
	#context={'countries': countries}
	#return render(request,'reviewhub/country/list.html',context)