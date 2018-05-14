from django.apps import path
from . import views


from .import views

app_name='haircut'

urlpatterns=[
   path("",views.home_page,name='home_page')
   ]
