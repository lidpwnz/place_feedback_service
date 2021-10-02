from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    title = models.CharField(max_length=150)


class Product(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey('app.Category', on_delete=models.RESTRICT, related_name='products')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=settings.AVATAR_FOLDER, null=True, blank=True)


class Feedback(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default='AnonymousUser', related_name='feedbacks')
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE, related_name='feedbacks')
    description = models.TextField()
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

