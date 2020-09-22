from django.db import models

class Application(models.Model):
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    mail=models.EmailField(max_length=256)
    mobile=models.CharField(max_length=256)
    information=models.CharField(max_length=256)
    resume_file=models.FileField(upload_to='files/')
    def __str__(self):
        return self.first_name