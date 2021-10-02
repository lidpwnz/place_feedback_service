from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey('app.Category', on_delete=models.RESTRICT, related_name='products')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=settings.AVATAR_FOLDER, null=True, blank=True,
                              default=settings.AVATAR_DEFAULT_VALUE)
    avg = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return f'{self.title} | {self.category} | {self.description} | {self.image.url}'


class Feedback(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default='AnonymousUser',
                               related_name='feedbacks')
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE, related_name='feedbacks')
    description = models.TextField()
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.product}, {self.rate} | {self.author}: {self.description}'
