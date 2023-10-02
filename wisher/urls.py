from django.urls import path
from . import views

urlpatterns = [
    # path("",views.beforelogin,name ="beforelogin"),
    # path("afterlogin",views.afterlogin,name="afterlogin"),
    # path("handlesignup",views.handlesignup,name="handlesignup"),
    # path("handlelogin",views.handlelogin,name="handlelogin"),
    # path("handlelogout",views.handlelogout,name="handlelogout"),
    # path("addbirthday",views.addbirthday,name = "addbirthday"),
    # path("addtodb",views.addtodb,name = "addtodb"),
    # path("remove",views.remove,name="remove"),
    # path("update",views.update,name="update"),
    # path("updatenow",views.updatenow,name="updatenow"),
    # path("sendemail",views.sendemail,name="sendemail"),
    path("", views.afterlogin, name="afterlogin"),
    path("addbirthday",views.addbirthday,name = "addbirthday"),
    path("remove",views.remove,name="remove"),
    path("updatenow",views.updatenow,name="updatenow"),
    path("update",views.update,name="update"),
    path("addtodb",views.addtodb,name = "addtodb"),
    path("index.html", views.afterlogin, name="afterlogin"),
]