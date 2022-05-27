# Generated by Django 3.1.7 on 2021-03-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20210310_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='quantity',
            field=models.CharField(choices=[('less than 5', 'LESS THAN 5'), ('less than 10', 'LESS THAN 10'), ('less than 15', 'LESS THAN 15'), ('less than 20', 'LESS THAN 20'), ('less than 30', 'LESS THAN 30'), ('less than 50', 'LESS THAN 50'), ('more than 50', 'MORE THAN 50')], default='less than 15', max_length=15),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='meal',
            field=models.CharField(choices=[('breakfast', 'BREAKFAST'), ('dinner', 'DINNER'), ('lunch', 'LUNCH')], default='dinner', max_length=15),
        ),
    ]
