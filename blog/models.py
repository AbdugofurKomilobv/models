from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Category name',max_length=250)
    slug =models.SlugField(max_length=240,unique=True)

    def  __str__(self):
        return self.name
    


class Tag(models.Model):
    name = models.CharField(verbose_name='Tag name',max_length=250)
    slug = models.SlugField(max_length=250,unique=True)


    def __str__(self):
        return self.name


class Post(models.Model):
    ...

