from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_unique_slug
from questions.models import Question

@receiver(pre_save, sender=Question)
def set_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        instance.slug = generate_unique_slug(slug)