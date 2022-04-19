
from django.urls import include, re_path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^profile/$',views.profile,name='profile'),
    re_path(r'^request/$',views.requestItem,name='request_item'),
    re_path(r'^profile/edit$', views.editprofile, name='edit_profile'),
    re_path(r'^password/$', views.change_password, name='change_password'),
    re_path(r'^claim/(?P<id>\d+)/$', views.claim, name='claim'),
]