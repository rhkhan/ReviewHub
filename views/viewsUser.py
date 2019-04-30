from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.forms import ModelForm
from django import forms
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rolepermissions.mixins import HasRoleMixin

from ..models import User,Project


#class FreelancerForm(ModelForm):
    #class Meta:
        #model = Freelancer
        #fields = ('freelancer_name','country')

class UserForm(forms.ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('full_name','country','user_name','user_password','user_type')

class UserCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'reviewhub.add_user'
    model=User
    form_class = UserForm
    template_name='reviewhub/user/user_form.html'
    success_url = reverse_lazy('reviewhub:userList')
    #return HttpResponseRedirect(reverse('freelanerList'))

class UserUpdateView(generic.UpdateView):
	model=User
	form_class=UserForm
	template_name='reviewhub/user/user_form.html'
	success_url=reverse_lazy('reviewhub:userList')

class UserListView(generic.ListView):
	template_name='reviewhub/user/user_list.html'
	context_object_name='userlistinfo'

	def get_queryset(self):
		queryset=User.objects.all()
		return queryset

class UserDetailView(generic.DeleteView):
	model=User
	template_name='reviewhub/user/user_detail.html'
	
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		return context
		
def userList(request): #We can show all users using this def instead of using above generic class. (reason to do is for learning python)
	val=request.GET.get('t')
	queryset=User.objects.all()
	if val is not None:
		queryset=queryset.filter(user_type__exact=val)
	context={'userlistinfo': queryset,'usertype': val}
	return render(request,'reviewhub/user/user_list.html',context)

def projectWorkList(request, id, usertype): #showing project work history by user id according to user type
	userinfo=get_object_or_404(User,id=id)
	if usertype == 'FRELANCERS':
		projectlist=Project.objects.filter(freelance_id=userinfo.id)
	else:
		projectlist=Project.objects.filter(client_id=userinfo.id)
	
	context={'projectlistinfo': projectlist,'dd': usertype}
	return render(request,'reviewhub/project/project_list.html',context)

class UserDeleteView(generic.DeleteView):
	model=User
	template_name="reviewhub/user/user_delete.html"
	success_url=reverse_lazy('reviewhub:userList')
	