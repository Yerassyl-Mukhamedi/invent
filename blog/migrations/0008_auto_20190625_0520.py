# Generated by Django 2.1.7 on 2019-06-25 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190625_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='camera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Camera'),
        ),
        migrations.AddField(
            model_name='worker',
            name='condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Condition'),
        ),
        migrations.AddField(
            model_name='worker',
            name='dispenser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Dispenser'),
        ),
        migrations.AddField(
            model_name='worker',
            name='shredder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Shredder'),
        ),
        migrations.AddField(
            model_name='worker',
            name='telephone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Telephone'),
        ),
        migrations.AddField(
            model_name='worker',
            name='television',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Television'),
        ),
    ]