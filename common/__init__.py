import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class YGBaseModel(models.Model):
    id = models.CharField(max_length=50, primary_key=True,
                          verbose_name='ID')

    class Meta:
        abstract = True


@receiver(pre_save)
def new_uuid_value(sender, **kwargs):
    if issubclass(sender, YGBaseModel):
        instance = kwargs.get('instance')
        if not instance.id:
<<<<<<< HEAD
            instance.id = uuid.uuid4().hex
=======
            instance.id = uuid.uuid4().hex
>>>>>>> a13abf785cb37e62d27c56b1627dd587b60a980e
