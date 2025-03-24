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
    title = models.CharField(verbose_name='Post titlr',max_length=550)
    body = models.TextField(verbose_name='Post title')
    author = models.CharField(verbose_name='Post author',default='Admin',max_length=100)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='posts')
    tag = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=4003)
    publesh_data = models.DateTimeField(verbose_name='Published time',auto_now_add=True)
    published = models.BooleanField(default=True)
    on_top = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    



class Comments(models.Model):
    author = models.CharField(verbose_name='Comment author',max_length=150,blank=False)
    comment = models.TextField(verbose_name='Comment')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')
    created_at =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author
    


class Rating(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='rating')
    value = models.PositiveSmallIntegerField(default=0,verbose_name='Post rating')


    def __str__(self):
        return self.value




    

