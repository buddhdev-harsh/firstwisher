from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name ="home"),
    path("handlesignup",views.handlesignup,name="handlesignup"),
    path("handlelogin",views.handlelogin,name="handlelogin"),
    path("handlelogout",views.handlelogout,name="handlelogout"),
]