# Generated by Django 3.2.12 on 2022-03-26 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='deposit',
            field=models.CharField(choices=[('5', 5), ('10', 10), ('20', 20), ('50', 50), ('100', 100)], default=0, max_length=10),
        ),
    ]
