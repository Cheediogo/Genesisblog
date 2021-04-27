from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import GenesisListView, GenesisDetailView, GenesisCreateView, GenesisUpdateView, GenesisDeleteView, \
    SignUpView, login_request, PasswordsChangeView

urlpatterns = [
    path('', GenesisListView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('change_password/', PasswordsChangeView.as_view(template_name='password_change.html',), name='change_password'),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/login.html'), name='change_password_done'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('post/<int:pk>/delete/', GenesisDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', GenesisUpdateView.as_view(), name='post_edit'),
    path('post/new/', GenesisCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', GenesisDetailView.as_view(), name='post_detail'),
]
