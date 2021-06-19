from django.db import models
from django.urls import reverse


# 模型的元数据，指的是“除了字段外的所有内容”，例如排序方式、数据库表名、
# 人类可读的单数或者复数名等等。所有的这些都是非必须的，甚至元数据本身对模型也是非必须的。
# 可以添加约束，constraints等等
class FinCategory(models.Model):
    # 应该设置unique的
    name = models.CharField(max_length=200,default='食品',db_index=True)
    # # slug由数字字母下划线组成，用在url中 
    # slug = models.SlugField(max_length=200, db_index=True, unique=True)
    # Django 模型类的Meta是一个内部类，它用于定义一些Django模型类的行为特性
    
    # ordering排序方式， verbose name可读性高的名字
    class Meta:
        ordering = ('-name',)
        verbose_name = 'fin_category'
        # 默认的是直接加s
        verbose_name_plural = 'fin_categories'
        db_table = 'FinCategory'

    def __str__(self):
        return self.name


class Finance(models.Model):
    category = models.ForeignKey(FinCategory,
        related_name='products',on_delete=models.CASCADE,default='食品')
    name = models.CharField(max_length=200, db_index=True)
    buyer = models.TextField(blank=True, default='', null=True)
    price = models.FloatField()
    
    facture = models.CharField(max_length=100, default='', null=True)  # a link to the file
    description = models.TextField(blank=True, default='', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id'),)
        db_table = 'Finance'

    def __str__(self):
        return self.name

    # @property
    # def save(self, *args, **kwargs):
    #     self.ttl_price = self.price * self.quantity
    #     super(Product, self).save(*args, **kwargs)
