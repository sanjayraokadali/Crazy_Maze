from django.conf.urls import url
from mazeApp import views

app_name = 'mazeApp'

urlpatterns = [

    url('^$',views.HomePage,name='homepage'),
    url('^UserRegistrationPage/$',views.UserRegistrationPage,name='userregistrationpage'),

]
