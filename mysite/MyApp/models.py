from django.db import models
from django.utils import timezone


# 作者の表を作成
class Author(models.Model):
    author = models.CharField(max_length = 180, verbose_name = "作者")
    def __str__(self):
        return self.author

# 本の表を作成
class Book(models.Model):
    title = models.CharField(max_length = 500, verbose_name = "タイトル")
    start_date = models.DateField(verbose_name = "開始日")
    end_date = models.DateField(verbose_name = "終了日")
    author = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name = "作者", related_name = "book")
    def __str__(self):
        return self.title

# 記録の表を作成
class Memory(models.Model):
    text = models.TextField(verbose_name = "感想")
    title = models.ForeignKey(Book, on_delete = models.CASCADE, verbose_name = "タイトル", related_name = "memory")
    def __str__(self):
        return self.text