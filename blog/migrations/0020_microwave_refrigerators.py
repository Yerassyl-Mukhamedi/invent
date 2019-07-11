# Generated by Django 2.1 on 2019-07-04 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20190703_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Microwave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker')),
            ],
        ),
        migrations.CreateModel(
            name='Refrigerators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker')),
            ],
        ),
    ]
