from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from ranking.models import UserScore  # UserScore 모델을 import

@receiver(post_save, sender=get_user_model())
def create_user_score(sender, instance, created, **kwargs):
    if created:
        UserScore.objects.create(user=instance)
