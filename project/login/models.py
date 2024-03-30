from django.db import models


class User(models.Model):
    email = models.EmailField(unique = True)
    name = models.CharField(max_length = 32)
    pwd = models.CharField(max_length = 32)
    birth = models.DateField(null=True, blank=True)
    _time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-_time']
        verbose_name = '用戶資料庫'
        verbose_name_plural = '用戶資料庫'