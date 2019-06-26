# Generated by Django 2.1.7 on 2019-06-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190625_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='slug',
            field=models.SlugField(default='a', max_length=40),
        ),
        migrations.AlterField(
            model_name='camera',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2),
        ),
        migrations.AlterField(
            model_name='condition',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2),
        ),
        migrations.AlterField(
            model_name='dispenser',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2),
        ),
        migrations.AlterField(
            model_name='printer',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2),
        ),
        migrations.AlterField(
            model_name='shredder',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2),
        ),
        migrations.AlterField(
            model_name='television',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2),
        ),
        migrations.AlterField(
            model_name='worker',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2),
        ),
        migrations.AlterField(
            model_name='worker',
            name='job',
            field=models.CharField(choices=[('j1', 'Оператор'), ('j2', 'Менеджер по продажам'), ('j3', 'Фин отдел'), ('j4', 'Бухгалтер'), ('j5', 'Логисты'), ('j6', 'Продакт Менеджер'), ('j7', 'Оператор 1С'), ('j8', 'Специалист по кадрам'), ('j9', 'Экономист'), ('k1', 'Коммерческий директор'), ('k2', 'Руководитель отдела продаж'), ('k3', 'Оператор по закупкам'), ('k4', 'Региональный менеджер'), ('k5', 'Кассир'), ('k6', 'Руководитель'), ('k7', 'Руководитель департамента отдела поддержки')], default='pd', max_length=2),
        ),
    ]
