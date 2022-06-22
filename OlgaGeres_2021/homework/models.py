from django.db import models

class Project(models.Model):
    title = models.CharField (max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='img/')

class Tuesday(models.Model):
    First_field = models.CharField ('Первое поле', max_length=150)
    Second_field = models.TextField('Второе поле')
    Third_field = models.CharField('Третье поле', max_length=80)



