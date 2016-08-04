from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs_sql = FileSystemStorage(location='source_report')
fs_res = FileSystemStorage(location='result_report')

class Report(models.Model):
    type = models.IntegerField(default=0)
    name = models.CharField(max_length=64)
    text = models.FileField(storage=fs_sql)

class Choice(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    choice_name = models.CharField(max_length=64)
    publish = models.IntegerField(default=0)

class History(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
#    report_result = models.ForeignKey(Result, related_name='name', on_delete=models.CASCADE)
    user   = models.CharField(max_length=64)
    run_date = models.DateTimeField('report date') 

class Result(models.Model):
    name = models.ForeignKey(Report, related_name='result_name', on_delete=models.CASCADE)
    text = models.ForeignKey(Report, related_name='result_text', on_delete=models.CASCADE)
    rdate = models.ForeignKey(History, on_delete=models.CASCADE)
    result = models.FileField(storage=fs_res)
    user  = models.CharField(max_length=64)

class Database(models.Model):
    profile = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)
    port = models.CharField(max_length=64,default="1251")
    sid = models.CharField(max_length=16)
    userdb = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
