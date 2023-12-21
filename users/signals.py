from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

from .models import Reader


def createReader(sender, instance, created, **kwargs):
    if created:
        user = instance
        reader = Reader.objects.create(
            user=user,
            username=user.username,
            email=user.email
        )
        print(reader)
    print("Updated")


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createReader, sender=User)
post_delete.connect(deleteUser, sender=Reader)
