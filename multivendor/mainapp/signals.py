from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Retailer 
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def create_retailer(sender,instance,created,**kwargs):
    if created:
        Retailer.objects.create(user=instance)
@receiver(post_save,sender=User)
def save_retailer(sender,instance,**kwargs):
    instance.retailer.save()
