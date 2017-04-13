from django.conf.urls import url, include
from django.contrib.auth.views import logout
from . import views

urlpatterns = [
    
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', logout, {'next_page':'/'}, name='logout'),

    # Users
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^user/new/$', views.user_new, name='user_new'),

    # Employees
    url(r'^employees/$', views.employee_list, name='employee_list'),
    url(r'^employee/new/$', views.employee_new, name='employee_new'),
    url(r'^employee/(?P<pk>[0-9]+)/edit/$', views.employee_edit,
        name='employee_edit'),

    # Clients

]