# Generated by Django 3.0.8 on 2020-08-23 02:17

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('story', '0002_auto_20200812_0745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='story',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='story',
            name='body',
            field=models.TextField(),
        ),
    ]
