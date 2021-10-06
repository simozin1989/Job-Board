# Generated by Django 3.2.7 on 2021-10-02 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='desription',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')], max_length=15),
        ),
    ]