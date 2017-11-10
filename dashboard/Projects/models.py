# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from decimal import getcontext


# Create your models here.
class Contractor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title= models.CharField(max_length=30)
    subject_major= models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    hr_rate = models.DecimalField(max_digits=16, decimal_places=2,blank=True ,null=True)

    dateofjoin =models.DateField()
    maxhrs_week=models.DecimalField(max_digits=16, decimal_places=2,blank=True ,null=True)


    def __str__(self):
     return u'%s %s' % (self.first_name, self.last_name)


class Client(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='FIRST NAME')
    last_name = models.CharField(max_length=50,verbose_name='LAST NAME')
    company = models.CharField(max_length=50, verbose_name='COMPANY')
    phone_number = models.CharField(max_length=50,verbose_name='PHONE NUMBER')
    address = models.CharField(max_length=50,verbose_name='ADDRESS')
    city = models.CharField(max_length=60, verbose_name='CITY')
    state_province = models.CharField(max_length=30, verbose_name='STATE')
    email = models.EmailField()

    def __str__(self):
     return u'%s %s' % (self.first_name, self.last_name)

class Project(models.Model):
    projectname = models.CharField(max_length=100,verbose_name='PROJECT NAME')
    contractor = models.ManyToManyField(Contractor,verbose_name='CONTRACTOR')
    client = models.ForeignKey(Client,verbose_name='CLIENT')
    start_date =models.DateField(verbose_name='START DATE')
    devlivary_date = models.DateField(verbose_name='END DATE')
    client_cost=models.DecimalField(max_digits=16, decimal_places=2,verbose_name='RATE PER HOUR')
    budget = models.DecimalField(max_digits=38, decimal_places=2,verbose_name='BUDGET PER MONTH',null='True',blank='True')

    def __str__(self):
     return u'%s %s' % (self.projectname, self.client)

class Task(models.Model):
    contractor = models.ManyToManyField(Contractor,verbose_name='CONTRACTOR')
    projectname =models.ForeignKey(Project,verbose_name='PROJECTNAME')
    week =models.DateField(verbose_name='START DATE OF WEEK')
    Task =models.CharField(max_length=100,verbose_name='TASK NAME')

    def __str__(self):
        return u'%s %s %s' % (self.projectname, self.week,self.Task)
