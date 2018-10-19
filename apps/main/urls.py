from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
path('',views.index, name = 'index'),
path('register/',views.register,name='register'),
path('logout/',views.user_logout,name='logout'),
path('special/',views.special,name='special'),
path('user_login/',views.user_login,name='login'),
path('search/',views.gh_user_search,name='gh_user_search'),
path('search/<str:username>/<str:repo_name>/',views.gh_UserCommits,name='repo_detail'),
]
