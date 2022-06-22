from django.db import models

# Create your models here.

pipeline_options = (
    (0,'Engine 1'),
    (1,'Engine 2')
)

classification_model_options = (
    (0,'Engine 1'),
    (1,'Engine 2')
)

# Create your models here.
class NewProcess(models.Model):
    name = models.CharField(max_length=20)
    classication = models.CharField(choices=classification_model_options)
    pipeline = models.CharField(choices=pipeline_options)