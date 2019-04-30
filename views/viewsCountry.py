from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django import forms
from django.contrib.auth.decorators import permission_required

from ..models import Country



#......... Country view has been created without class view .................

class CountryForm(ModelForm):
	class Meta:
		model=Country
		fields=['country_name']

#def view_a(request):
	#return render(request,'view_a.html')

def countryList(request):
	countries=Country.objects.all() #.order_by('id')[:5]
	context={'countries': countries}
	return render(request,'reviewhub/country/list.html',context)

@permission_required('reviewhub.add_country')
def countryCreate(request, template_name='reviewhub/country/create.html'):
	form=CountryForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('reviewhub:countryList')
	return render(request,template_name,{'form': form})

def countryUpdate(request,pk,template_name='reviewhub/country/create.html'):
	country=get_object_or_404(Country,pk=pk)
	form=CountryForm(request.POST or None,instance=country)
	if form.is_valid():
		form.save()
		return redirect('reviewhub:countryList')
	return render(request,template_name,{'form': form})

def countryDelete(request,pk,template_name='reviewhub/country/delete.html'):
	country=get_object_or_404(Country,pk=pk)
	if request.method=='POST':
		country.delete()
		return redirect('reviewhub:countryList')
	return render(request,template_name,{'object': country})