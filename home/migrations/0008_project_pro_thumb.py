# Generated by Django 4.1.4 on 2024-01-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_project_pro_git'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pro_thumb',
            field=models.URLField(default='/projects'),
            preserve_default=False,
        ),
    ]