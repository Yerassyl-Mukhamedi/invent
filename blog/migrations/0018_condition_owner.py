# Generated by Django 2.0.13 on 2019-06-28 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190628_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
    ]