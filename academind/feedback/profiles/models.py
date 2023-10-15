from django.db import models

class Profile(models.Model):
  image = models.ImageField(upload_to="images")
  text = models.FileField(upload_to="files", null=True)

