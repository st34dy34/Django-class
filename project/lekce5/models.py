from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        permissions = [
			("can_publish", "Can publish articles"),
			("can_archive", "Can archive articles"),
		]