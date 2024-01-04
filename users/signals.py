from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

from .models import Reader
from .models import Librarian


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance

        if user.is_superuser:
            pass

        else:
            if user.is_staff:
                if user.first_name and user.last_name:
                    librarian = Librarian.objects.create(
                        user=user,
                        first_name=user.first_name.title(),
                        last_name=user.last_name.title(),
                        username=user.username,
                        email=user.email,
                        is_librarian=True
                    )
                else:
                    librarian = Librarian.objects.create(
                        user=user,
                        username=user.username,
                        email=user.email,
                        is_librarian=True
                    )
            else:
                if user.first_name and user.last_name:
                    reader = Reader.objects.create(
                        user=user,
                        first_name=user.first_name.title(),
                        last_name=user.last_name.title(),
                        username=user.username,
                        email=user.email,
                    )
                else:
                    reader = Reader.objects.create(
                        user=user,
                        username=user.username,
                        email=user.email,
                    )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Reader)
post_delete.connect(deleteUser, sender=Librarian)
