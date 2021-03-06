# Generated by Django 3.0.7 on 2020-06-13 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LikeVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('video_id', models.TextField(verbose_name='айди')),
                ('duration', models.TextField(verbose_name='время')),
                ('thumbnail', models.TextField(verbose_name='картинка')),
            ],
            options={
                'verbose_name': 'Понравившееся видео',
                'verbose_name_plural': 'Понравившееся видео',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.TextField(verbose_name='код видео')),
                ('video_title', models.TextField(verbose_name='Название видео')),
                ('video_text', models.TextField(verbose_name='описание видео')),
                ('video_channel_title', models.TextField(verbose_name='название канала')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_name', models.TextField(verbose_name='имя автора')),
                ('comment_text', models.TextField(verbose_name='текст комментария')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
