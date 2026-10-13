from django.db import models

class labapi_model(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"API User Profile: {self.name} | {self.email}"


class asset_record_model(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField() 
    category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Asset: {self.title} [{self.category}]"