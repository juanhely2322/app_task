from django.urls import URLPattern, path
from . import views
urlpatterns=[
    path("signup",views.signup,name="signup"),
    path("logout",views.logout_session,name="logout"),
    path("login",views.login_session,name="login"),
]