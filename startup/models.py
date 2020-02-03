from django.db import models


class StartupCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Startup(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(StartupCategory, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
