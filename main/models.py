from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class SliderItem(models.Model):
    title = models.CharField(max_length=255)
    image = ResizedImageField(size=[1024, 512], crop=['middle', 'center'], upload_to='slider/', blank=True)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class About(models.Model):
    name = models.CharField(max_length=255)
    designation = RichTextField(blank=True)
    link = models.URLField(blank=True)
    title = models.CharField(max_length=255)
    sub_Title = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    image = ResizedImageField(size=[1024, 768], crop=['middle', 'center'], upload_to='about/', blank=True)

    def __str__(self):
        return self.title
    
class Academic(models.Model):
    degree = models.CharField(max_length=255)
    start_Date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    end_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    institution = models.CharField(max_length=255)

    def __str__(self):
        return self.degree
    class Meta:
        ordering = ['-id']

class Experience(models.Model):
    designation = models.CharField(max_length=255)
    start_Date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    end_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    institution = models.CharField(max_length=255)

    def __str__(self):
        return self.designation
    class Meta:
        ordering = ['-id']
    
class Visitor(models.Model):
    visitor = models.CharField(max_length=100)

    def __str__(self):
        return self.visitor
    
class Affiliation(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    image = ResizedImageField(size=[400, 400], crop=['middle', 'center'], upload_to='about/', blank=True)

    def __str__(self):
        return self.name
