from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True, null=True)
    slug = models.SlugField(unique=True, null=True, db_index=True) #added db_index for faster querying
    content = models.TextField(validators=[MinLengthValidator(20)])
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, related_name="posts")
    
    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Comment(models.Model):
    user_name = models.CharField(max_length=25)
    title = models.CharField(max_length=150, null=True)
    text = models.TextField(max_length=500, null=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, null=True, related_name="comments")



