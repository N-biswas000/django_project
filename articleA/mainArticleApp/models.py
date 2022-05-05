from django.db import models
from django.contrib.auth.models import User

class postArticle(models.Model):
    article_id = models.AutoField
    article_heading = models.CharField(max_length=20)
    article_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username")



