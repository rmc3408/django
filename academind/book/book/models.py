from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


rate_validator_condition = [MinValueValidator(1), MaxValueValidator(10)]

class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField(validators=rate_validator_condition)
  author = models.CharField(null=True, max_length=30)
  is_bestselling = models.BooleanField(default=False)
  pub_date = models.DateTimeField("date published")
  slug = models.SlugField(default="", null=False, db_index=True)

  def __str__(self):
    return f"{self.title} by author {self.author}"
  
  def get_absolute_url(self):
    return reverse("book-details", args=[self.slug])
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title) # transform "Harry Pot" -> harry-pot
    super().save(*args, **kwargs)


class Category(models.Model):
  book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
  type = models.CharField(max_length=30)
  votes = models.IntegerField(default=0)