# Generated by Django 3.2.16 on 2023-06-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_pertanyaan_bobot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pertanyaan',
            name='bobot',
            field=models.IntegerField(blank=True, default=1, max_length=1, null=True),
        ),
    ]
