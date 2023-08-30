from django.db import models
import wifi_qrcode_generator


# Create your models here.


class QrCode(models.Model):
    wifi_name = models.CharField(max_length=50)
    encryption = models.CharField(max_length=100)
    password = models.BigIntegerField()

    def __str__(self):
        return self.wifi_name

    class Meta:
        db_table = 'qrcode'



