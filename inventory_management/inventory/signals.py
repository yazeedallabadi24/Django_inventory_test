from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance, created, **kwards):
    if created:
        user=instance
        profile = Profile.objects.create(
            user=user,
            username=username,
            email=user.email,
            name=user.first_name
        )
        
        send_email(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            
        )