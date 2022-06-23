from django.db import models

# Create your models here.

pipeline_options = (
    (0,'Engine 1'),
    (1,'Engine 2'),
    (2,'Engine 3')
)

classification_options = (
    (0,'No'),
    (1,'Yes')
)
preprocessing_options = (
    (0,'No'),
    (1,'Yes')
)

input_doc_options = (
    (0, 'JPG'),
    (1, 'PDF'),
    (2, 'JPEG'),
    (3, 'TIF'),
    (4, 'PNG')
)

timeline = (
    (0,'1 hour'),
    (1,'2 hours'),
    (2,'3 hours'),
    (3,'4 hours'),
    (4,'5 hours'),
    (5,'6 hours'),
    (6,'7 hours'),
    (7,'8 hours'),
    (8,'9 hours'),
    (9,'10 hours'),
    (10,'11 hours'),
    (11,'12 hours'),
    (12,'13 hours'),
    (13,'14 hours'),
    (14,'15 hours'),
    (15,'16 hours'),
    (16,'17 hours'),
    (17,'18 hours'),
    (18,'19 hours'),
    (19,'20 hours'),
    (20,'21 hours'),
    (21,'22 hours'),
    (22,'23 hours'),
    (23,'24 hours'),
)

tz = (
    (0,'UTC +0000-2020-03-31 16:51:13 IST +05.30'),
    (0,'UTC +0000-2020-03-31 16:51:13 IST +05.30'),
    (0,'UTC +0000-2020-03-31 16:51:13 IST +05.30'),
)
# Create your models here.
class ConfigureNewProcess(models.Model):
    process_name = models.CharField(max_length=20)
    classication_model = models.CharField(max_length=20, choices=classification_options)
    pipeline = models.CharField(max_length=20, choices=pipeline_options)
    process_sla = models.CharField(max_length=10, choices=timeline )
    timezon = models.CharField(max_length=10, choices=tz )
    classication_model = models.CharField(max_length=20, choices=preprocessing_options)
    input_doc = models.CharField(max_length=20, choices=input_doc_options)

