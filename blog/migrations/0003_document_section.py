# Generated by Django 2.0.13 on 2019-07-12 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190712_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='section',
            field=models.CharField(choices=[('s1', 'Справочник'), ('s2', 'Документы'), ('s3', 'Константа'), ('s4', 'План обмена'), ('s5', 'Журнал документов'), ('s6', 'Отчет'), ('s7', 'Обработка'), ('s8', 'План счетов'), ('s9', 'Регистр сведений'), ('s10', 'Регистр накоплений'), ('s11', 'Регистр бухгалтерий')], default='s1', max_length=3),
        ),
    ]
