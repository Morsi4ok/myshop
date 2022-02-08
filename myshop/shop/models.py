# notes/models.py
from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
