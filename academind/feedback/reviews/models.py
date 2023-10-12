from django.db import models

class Review(models.Model):
  user_name = models.CharField(max_length=10, blank=False)
  name = models.CharField(max_length=30)
  email = models.EmailField()
  review_text = models.TextField()
  rating = models.IntegerField()
