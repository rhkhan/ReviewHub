from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.forms import ModelForm
from django.urls import reverse,reverse_lazy
from django.views import generic

from ..models import Freelancer


class FreelancerForm(ModelForm):
    class Meta:
        model = Freelancer
        fields = ('freelancer_name','country')

class FreelancerCreateView(generic.CreateView):
    model=Freelancer
    form_class = FreelancerForm
    template_name='reviewhub/freelancer/freelancer_form.html'
    success_url = reverse_lazy('reviewhub:freelanerList')
    #return HttpResponseRedirect(reverse('freelanerList'))

class FreelancerUpdateView(generic.UpdateView):
	model=Freelancer
	form_class=FreelancerForm
	template_name='reviewhub/freelancer/freelancer_form.html'
	success_url=reverse_lazy('reviewhub:freelanerList')

class FreelancerListView(generic.ListView):
	template_name='reviewhub/freelancer/freelancer_list.html'
	context_object_name='freelancerlistinfo'

	def get_queryset(self):
		return Freelancer.objects.all()

class FreelancerDeleteView(generic.DeleteView):
	model=Freelancer
	template_name="reviewhub/freelancer/freelancer_delete.html"
	success_url=reverse_lazy('reviewhub:freelanerList')