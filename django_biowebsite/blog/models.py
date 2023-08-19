from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

