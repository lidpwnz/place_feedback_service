from django.contrib import admin
import app.models as models


admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Feedback)
