# Generated by Django 2.1 on 2019-07-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='fileName',
        ),
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='name', max_length=200),
        ),
        migrations.DeleteModel(
            name='FileName',
        ),
    ]
