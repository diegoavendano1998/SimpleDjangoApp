from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
import stripe

# Create your models here.

# To store user data
class profile(models.Model):
    name        = models.CharField(max_length=120)
    # Si se agrega un campo despues de haber creado la tabla, este debe aceptar valores nulos o tener un default para que se pueda ahcer el migrate
    description = models.TextField(default='default description') #null=True
    # location    = models.CharField(max_length=120, default='default location', blank=True, null=True)
    # job         = models.CharField(max_length=120, default=True)
    # OneToOneField hace referencia a una FK
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING,)

    # def __unicode__(self):
    def __str__(self): # For python3
        return self.name
        
    def __unicode__(self):
        return self.name

# Para Stripe
class userStripe(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,)
    stripe_id   = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self): # For python3
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username

# def my_callback(sender, request, user, **kwargs):
#     print("Request finished!")
#     print (request)
#     print (user)
#     idStripe, created = userStripe.objects.get_or_create(user=user)
#     if created:
#         print ("Stripe user %s sucsesfully created!"%(user.username))
#     userProfile, is_created = profile.objects.get_or_create(user=user)
#     if is_created:
#         userProfile.name = user.username
#         userProfile.save()


# Separar my_callback en ds metodos para hacerlo mas mantenible o para difentes casos de uso
def stripeCallback(sender, request, user, **kwargs):
    user_stripe_account, created = userStripe.objects.get_or_create(user=user)
    if created:
        print ("created for %s"%(user.username))
    if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == "":
        # Crea un cliente (email) dentro de stripe (se puede ver en el dashboard de stripe)
        new_stripe_id = stripe.Customer.create(email=user.email) # Regresa un diccionario
        user_stripe_account.stripe_id = new_stripe_id['id']
        user_stripe_account.save()


def profileCallback(sender, request, user, **kwargs):
    userProfile, is_created = profile.objects.get_or_create(user=user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()

# user_logged_in.connect(my_callback)
user_logged_in.connect(stripeCallback)
user_signed_up.connect(stripeCallback)
user_signed_up.connect(profileCallback)
        

