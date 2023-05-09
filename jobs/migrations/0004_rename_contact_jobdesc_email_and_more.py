# Generated by Django 4.0.4 on 2023-05-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_jobseeker_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobdesc',
            old_name='contact',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='jobprovider',
            name='mobileNum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='mobileNum',
            field=models.IntegerField(),
        ),
    ]