from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import Feedback
from core.helpers import get_avg


@receiver(signal=post_save, sender=Feedback)
def create_user_profile(sender, instance, created, **kwargs):
    product = instance.product
    product_feedbacks = product.feedbacks.filter(is_moderated=True).values_list('rate', flat=True)

    product.avg = get_avg(product_feedbacks)
    product.save()
