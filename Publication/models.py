from django.db import models
from Author.models import Author

class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_publication = models.DateTimeField(auto_now_add=True)
    pub_text = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    class Meta:
        db_table = "publications"

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
class PostFormSubmission(models.Model):
    title = models.CharField(max_length=75)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20,  default='author')

    def __str__(self):
        return f"{self.title} - {self.created_at}"

