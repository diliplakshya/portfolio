# Generated by Django 3.0.8 on 2020-07-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_company_professionalproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalproject',
            name='remarks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
