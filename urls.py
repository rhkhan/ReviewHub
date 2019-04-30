from django.urls import path

from . import viewsmain
from .views import viewsCountry,viewsFreelancer
from .views import viewsUser,viewsProject

app_name = 'reviewhub'
urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
	
	path('', viewsmain.index, name='index'),
	path('countries',viewsCountry.countryList,name='countryList'),
	path('countries/create',viewsCountry.countryCreate,name='countryCreate'),
	path('countries/update/<int:pk>',viewsCountry.countryUpdate,name='countryUpdate'),
	path('countries/delete/<int:pk>',viewsCountry.countryDelete,name='countryDelete'),
	path('user/create', viewsUser.UserCreateView.as_view(),name='userCreate'),
	path('user/update/<int:pk>',viewsUser.UserUpdateView.as_view(),name='userUpdate'),
	path('user/delete/<int:pk>',viewsUser.UserDeleteView.as_view(),name='userDelete'),
	path('user/list',viewsUser.UserListView.as_view(), name='userList'), # we can use the below users/ path for showing all users, currently we are using class view to display all users
	path('users/',viewsUser.userList),
	path('user/detail/<int:pk>', viewsUser.UserDetailView.as_view(), name='userDetailView'),
	path('projects',viewsProject.ProjectListView.as_view(),name='projectList'),
	path('projects/create',viewsProject.ProjectCreateView.as_view(), name='projectCreate'),
	path('projectDetails/update/<int:pk>',viewsProject.ProjectDetailUpdateView.as_view(),name='projectDetailUpdate'),
	path('projectDetails/detail/<int:pk>',viewsProject.ProjectDetailView.as_view(),name='projectDetailView'),
	path('users/project/<int:id>/<str:usertype>', viewsUser.projectWorkList,name='projectWorkList'),
	path('signup/', viewsmain.SignUp.as_view(), name='signup'),
]

#accounts/ login/ [name='login']
#accounts/ logout/ [name='logout']
#accounts/ password_change/ [name='password_change']
#accounts/ password_change/done/ [name='password_change_done']
#accounts/ password_reset/ [name='password_reset']
#accounts/ password_reset/done/ [name='password_reset_done']
#accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/ reset/done/ [name='password_reset_complete']