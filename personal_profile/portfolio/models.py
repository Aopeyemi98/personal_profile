from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # image = models.ImageField(upload_to='projects/') install pillow for imageField
    link = models.URLField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.email}, {self.message[:20]}"