from django.db import models

# Create your models here.

class Tag(models.Model):
    capiton = models.CharField(max_length=15)

    def __str__(self):
        return self.capiton

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    date = models.DateField(null=True)
    slug = models.SlugField(null=True)
    content = models.CharField(max_length=10000)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, related_name="posts")
    

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



