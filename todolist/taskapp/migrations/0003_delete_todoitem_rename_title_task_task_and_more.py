# Generated by Django 5.1.1 on 2024-09-19 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TodoItem',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='task',
        ),
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='not_started', max_length=12),
        ),
    ]
