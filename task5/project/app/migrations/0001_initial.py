# Generated by Django 4.0.4 on 2022-06-24 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigureNewProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(max_length=20)),
                ('classification_model', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=20)),
                ('pipeline', models.CharField(choices=[(0, 'Engine 1'), (1, 'Engine 2'), (2, 'Engine 3')], max_length=20)),
                ('process_sla', models.CharField(choices=[(0, '1 hour'), (1, '2 hours'), (2, '3 hours'), (3, '4 hours'), (4, '5 hours'), (5, '6 hours'), (6, '7 hours'), (7, '8 hours'), (8, '9 hours'), (9, '10 hours'), (10, '11 hours'), (11, '12 hours'), (12, '13 hours'), (13, '14 hours'), (14, '15 hours'), (15, '16 hours'), (16, '17 hours'), (17, '18 hours'), (18, '19 hours'), (19, '20 hours'), (20, '21 hours'), (21, '22 hours'), (22, '23 hours'), (23, '24 hours')], max_length=10)),
                ('timezon', models.CharField(choices=[(0, 'UTC +0000-2020-03-31 16:51:13 IST +05.30'), (0, 'UTC +0000-2020-03-31 16:51:13 IST +05.30'), (0, 'UTC +0000-2020-03-31 16:51:13 IST +05.30')], max_length=10)),
                ('preprocessing', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=20)),
                ('input_doc', models.CharField(choices=[(0, 'JPG'), (1, 'PDF'), (2, 'JPEG'), (3, 'TIF'), (4, 'PNG')], max_length=20)),
            ],
        ),
    ]
