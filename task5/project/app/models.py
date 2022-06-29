from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.


#First model 
pipeline_options = (
    ('0','Engine 1'),
    ('1','Engine 2'),
    ('2','Engine 3')
)

classification_options = (
    ('0','No'),
    ('1','Yes')
)
preprocessing_options = (
    ('0','No'),
    ('1','Yes')
)

input_doc_options = (
    ('0', 'JPG'),
    ('1', 'PDF'),
    ('2', 'JPEG'),
    ('3', 'TIF'),
    ('4', 'PNG')
)

timeline = (
    ('0','1 hour'),
    ('1','2 hours'),
    ('2','3 hours'),
    ('3','4 hours'),
    ('4','5 hours'),
    ('5','6 hours'),
    ('6','7 hours'),
    ('7','8 hours'),
    ('8','9 hours'),
    ('9','10 hours'),
    ('10','11 hours'),
    ('11','12 hours'),
    ('12','13 hours'),
    ('13','14 hours'),
    ('14','15 hours'),
    ('15','16 hours'),
    ('16','17 hours'),
    ('17','18 hours'),
    ('18','19 hours'),
    ('19','20 hours'),
    ('20','21 hours'),
    ('21','22 hours'),
    ('22','23 hours'),
    ('23','24 hours'),
)

tz = (
    ('0','UTC +0000-2020-03-31 16:51:13 IST +05.30'),
    ('1','UTC +0000-2020-03-31 16:51:13 IST +05.30'),
    ('2','UTC +0000-2020-03-31 16:51:13 IST +05.30'),
)
# Create your models here.
class ConfigureNewProcess(models.Model):
    process_name = models.CharField(max_length=20)
    classification_model = models.CharField(max_length=20, choices=classification_options)
    pipeline = models.CharField(max_length=20, choices=pipeline_options)
    process_sla = models.CharField(max_length=10, choices=timeline )
    time_zon = models.CharField(max_length=10, choices=tz )
    preprocessing = models.CharField(max_length=20, choices=preprocessing_options)
    input_doc = MultiSelectField(max_length=20, choices=input_doc_options)





# Second Model
type_options = (
    ('0', 'Regular Model'),
    ('1', 'Vg16 Model'),
)


epochs_options = (
    ('0', '20'),
    ('1', '30'),
    ('2', '40'),
    ('3', '50'),
    ('4', '60'),
    ('5', '70'),
    ('6', '80'),
    ('7', '90'),
    ('8', '100'),
)


batch_options = (
    ('0', '16'),
    ('1', '32'),
    ('2', '64'),
)


kernel_options = (
    ('0', 'HE_Normal'),
    ('1', 'HE_UI_Form'),
)


optimizer_options = (
    ('0', 'adam'),
    ('1', 'sgd'),
    ('2', 'rmsprop'),
)



text_options = (
    ('0', '0.3'),
    ('1', '0.15'),
    ('2', '0.18'),
    ('3', '0.21'),
    ('4', '0.24'),
    ('5', '0.27'),
)


activation_options = (
    ('0', 'relu'),
    ('1', 'Leaky_relu'),
)


class ProcessManagement(models.Model):
    type = models.CharField(max_length=10, choices=type_options)
    name = models.CharField(max_length=20)
    threshold = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/', validators=[FileExtensionValidator(['zip', ])])
    epochs = models.CharField(max_length=10, choices=epochs_options)
    batch = models.CharField(max_length=10, choices=batch_options)
    kernel = models.CharField(max_length=10, choices=kernel_options)
    optimizer = models.CharField(max_length=10, choices=optimizer_options)
    text = models.CharField(max_length=10, choices=text_options)
    activation = models.CharField(max_length=10, choices=activation_options)





#third model
# attribute_type_options = (
#     ('0', 'key_item')
# )


# derived_options = (
#     ('0', 'Yes'),
#     ('1', 'No'),
# )




# class ManageAttribute(models.Model):
#     attribute_name = models.CharField(max_length=20)
#     attribute_type = models.CharField(max_length=10, choices=attribute_type_options)
#     attribute_cs = models.CharField(max_length=20)



    
