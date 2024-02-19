from django.urls import path

from x_app import views

urlpatterns = [
    path("",views.home,name="home"),
    path("new",views.new,name="new"),
    path("Student_login",views.Student_login,name="Student_login"),
    path("Admin1_login",views.Admin1_login,name="Admin1_login"),
    path("stu_base",views.stu_base,name="stu_base"),
    path("adm_base",views.adm_base,name="adm_base"),
    path("Login_view",views.Login_view,name="Login_view"),
]