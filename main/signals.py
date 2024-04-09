from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Word, Room


@receiver(post_save, sender=Word)
def create_room(sender, instance, created, **kwargs):
    if created:
        room = Room.objects.create(
            word=instance,
            creator=instance.creator,
        )
        room.save()