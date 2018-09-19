from django.db import models
from datetime import datetime
# Create your models here.


class StudentInfo(models.Model):
    #charfile代表字段字段最大长度max_length
    #verbose_name别名
    name = models.CharField(max_length=20,verbose_name='学生姓名')
    #integerfield 整型field字段,默认值18
    age = models.IntegerField(default=18,verbose_name='学生年龄')
    #choices((),())选择就用choice
    gender = models.CharField(max_length=6,choices=(('girl','女'),('boy','男')),
                              default='girl',verbose_name='学生性别')
    stuid = models.CharField(max_length=20,verbose_name='学生学号')
    #TextField 代表文本不指定长度
    address = models.TextField(verbose_name='学生地址')
    #DecimelField 代表小数可以规定长度,max_digits 代表整数位数decimal_places代表小数的位数
    height = models.DecimalField(max_digits=5,decimal_places=2)
    #imageField 代表图片upload_to上传到后台文件夹user/年/月/天
    #本质还是字符串
    #image = models.ImageField(upload_to='user/%y/%m/$d',max_length=100,verbose_name='学生图片')
    #DateTimeField代表日期时间
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    #是否删除booleanfield 代表布尔值
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    def __str__(self):
        return self.name
    #元配置，对整张表进行配置
    class Meta():
        #对表进行重命名
        #db_table = ''
        #按照age正序排序
        #ordering = ['-age']
        #对表其别名
        verbose_name = '学生信息'
        #必须要写下面这行不然别名后面会复数显示自动加S
        #就是复数形式也用verbose_name这个名字
        verbose_name_plural = verbose_name