from django.db import models

# Create your models here.
class Women(models.Model):
    title =models.CharField(max_length=255)
    content = models.TextField(blank = True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='вид деятельности')

    def __str__(self):
        return self.name