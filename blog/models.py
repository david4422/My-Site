from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def fullName(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullName()

class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.TextField()
    image = models.ImageField(upload_to="posts")
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)
    date = models.DateField(auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    
    def __str__(self):
        return f"{user_name}"