from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.forms import ModelForm
from django import forms
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.template.loader import render_to_string

from django.contrib.messages.views import SuccessMessageMixin
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from ..models import Project

class ProjectForm(forms.ModelForm):
	completion_date = forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
	class Meta:
		model=Project
		fields = ('client','project_name','completion_date','freelance','comments')

class ProjectDetailForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
	class Meta:
		model=Project
		fields=('project_description','project_techs')

class ProjectListView(generic.ListView):
	template_name='reviewhub/project/project_list.html'
	context_object_name='projectlistinfo'

	def get_queryset(self):
		queryset=Project.objects.all()
		return queryset

class ProjectCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'reviewhub.add_project'
    model=Project
    form_class = ProjectForm
    template_name='reviewhub/project/project_form.html'
    success_url = reverse_lazy('reviewhub:projectList')
    #return HttpResponseRedirect(reverse('freelanerList'))


class ProjectDetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'reviewhub.view_projectdetails'
    model=Project
    template_name='reviewhub/project/project_detail.html'
	
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context
	
class ProjectDetailUpdateView(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Project
    template_name = 'reviewhub/project/projectDetail_update_form.html'
    form_class = ProjectDetailForm
    success_url = reverse_lazy('reviewhub:projectList')
    success_message = 'Success: project detail was updated.'

    #def updateDetail(self, request, *args, **kwargs):
        #messages.success(self.request, self.success_message)
        #return super(ProjectDetailUpdateView, self).updateDetail(request, *args, **kwargs)

#class ProjectDetailUpdateView(generic.UpdateView):
#	model=Project
#	form_class=ProjectDetailForm
#	template_name='reviewhub/project/projectDetail_update_form.html'

#	def dispatch(self,*args,**kwargs):
#		self.project_id=kwargs['pk']
#		return super(ProjectDetailUpdateView,self).dispatch(*args,**kwargs)
	
#	def form_valid(self,form):
#		form.save()
#		project=Project.objects.get(id=self.project_id)
#		return HttpResponse(render_to_string('reviewhub/project/projectDetail_update_form_success.html',{'project': project}))