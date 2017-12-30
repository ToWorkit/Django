from django.db import models

# Create your models here.

# 班级表
class Classes(models.Model):
  caption = models.CharField(max_length=32)
  
# 学生表
class Student(models.Model):
  name = models.CharField(max_length=32)
  # 绑定外键，建立一对多的关系，班级为 一 ，学生为 多
  cls = models.ForeignKey(
          'Classes', 
          on_delete=models.CASCADE,
        )

# 教师表
class Teacher(models.Model):
  name = models.CharField(max_length=32)
  # 建立多对多的关系(老师和班级)
  cls = models.ManyToManyField('Classes')

# 创建管理员登录表
class Administrator(models.Model):
  username = models.CharField(max_length=32)
  password = models.CharField(max_length=32)

