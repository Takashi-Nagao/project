from django.db import models
from django.utils import timezone

class Category(models.Model):
  name = models.CharField('カテゴリー名', max_length=255)
  created_at = models.DateTimeField('作成日', default=timezone.now)