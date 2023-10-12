from django.db import models

all_posts = [    
]


class Tag(models.Model):
  caption = models.CharField(max_length=20)

  def __str__(self):
    return self.caption
  
  def get_tags(self, obj):
        return " / ".join([t.caption for t in obj.tag.all()])


class Author(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email = models.EmailField(max_length=100)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class Post(models.Model):
  title = models.CharField(max_length=50)
  excerpt = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  image_name = models.CharField(max_length=20)
  slug = models.SlugField(unique=True, db_index=True)
  date = models.DateField(auto_now=True)
  author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
  tag = models.ManyToManyField(Tag, null=True)


