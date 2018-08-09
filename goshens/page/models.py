from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    cat_content = models.TextField()
    cat_image = models.FileField()

    def get_absolute_url(self):
        return reverse('page:page_detail', args=[self.slug])

    def __str__(self):
        return self.name


class Page(models.Model):
    page_title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    page_content = models.TextField()
    page_image = models.FileField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.page_title

