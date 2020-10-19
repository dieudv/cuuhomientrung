# Generated by Django 3.1.2 on 2020-10-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_auto_20201019_0950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuuho',
            options={'verbose_name': 'Các đội Cứu hộ', 'verbose_name_plural': 'Các đội Cứu hộ'},
        ),
        migrations.AlterModelOptions(
            name='hodan',
            options={'verbose_name': 'Hộ dân cần ứng cứu', 'verbose_name_plural': 'Hộ dân cần ứng cứu'},
        ),
        migrations.RemoveField(
            model_name='hodan',
            name='need',
        ),
        migrations.AlterField(
            model_name='hodan',
            name='status',
            field=models.IntegerField(choices=[(0, 'Chưa xác minh'), (1, 'Cần ứng cứu gấp'), (2, 'Không gọi được'), (3, 'Đã được cứu'), (4, 'Gặp nạn')], default=0, verbose_name='Tình trạng'),
        ),
    ]
