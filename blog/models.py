from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from pathlib import Path
from uuid import uuid4

# Create your models here.

class Articles(models.Model):

  def get_file_name(self, filename: str):
    ext = filename.strip().split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return str(Path('images/blog', filename))

  title = models.CharField('Title', max_length=80)
  excerpt = models.CharField('Excerpt', max_length=250)
  content = CKEditor5Field('Content', config_name='default', blank=True, null=True)
  date = models.DateTimeField('Date published', blank=False, null=False)
  cover = models.ImageField('Cover', upload_to=get_file_name, blank=True, null=True)

  def __str__(self):
    return f'{self.title}'

  class Meta:
    verbose_name = "Article"
    verbose_name_plural = "News"