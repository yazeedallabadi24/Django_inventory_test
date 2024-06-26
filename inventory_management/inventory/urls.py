from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, LoginForm, blogpost, post_detail, upload_form, view_pic
from django.contrib.auth import views as auth_views

from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html', redirect_authenticated_user=True, authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="inventory/reset_password.html"), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="inventory/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="inventory/reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="inventory/reset_password_complete.html"), name="password_reset_complete"),
    path('blog/', blogpost, name="blogpost"),
    path('uploads/', upload_form, name='uploads'),
    path("list/", view_pic, name='list-view'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

