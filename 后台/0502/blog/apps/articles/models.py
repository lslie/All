from django.db import models
from users.models import UserProFile
from datetime import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name='文章类别')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    def __str__(self):
        return self.name
    class Meta():
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

class ArticleInfo(models.Model):
    name = models.CharField(max_length=50,verbose_name='文章标题')
    author = models.ForeignKey(UserProFile,verbose_name='文章作者')
    desc = models.CharField(max_length=200,verbose_name='文章摘要')
    label = models.ForeignKey(Category,verbose_name='文章类别',null=True,blank=True)
    content = models.TextField(verbose_name='文章内容')
    click_num = models.IntegerField(default=0,verbose_name='浏览量')
    love_num = models.IntegerField(default=0,verbose_name='点赞数')
    image = models.ImageField(max_length=200,verbose_name='文章图片',upload_to='article/%y/%m/%d')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')

    def __str__(self):
        return self.name
    class Meta():
        verbose_name = '文章信息'
        verbose_name_plural = verbose_name
class TagInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='标签名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    article = models.ManyToManyField(ArticleInfo,verbose_name='文章标签')
    def __str__(self):
        return self.name
    class Meta():
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name