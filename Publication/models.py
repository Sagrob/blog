from django.db import models
from Author.models import Author

class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_publication = models.DateTimeField()
    pub_text = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    class Meta:
        db_table = "publications"