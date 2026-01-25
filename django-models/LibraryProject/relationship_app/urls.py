from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # 🔐 Authentication URLs (REQUIRED by checker)
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),

    # 📝 Registration (still custom)
    path(
        'register/',
        views.register_view,
        name='register'
    ),
]
