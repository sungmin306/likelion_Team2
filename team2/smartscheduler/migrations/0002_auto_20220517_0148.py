# Generated by Django 3.1.2 on 2022-05-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartscheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecture_review',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='강의평'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='apply_count',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='지원인원수'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='area',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='개설영역'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='credit',
            field=models.CharField(blank=True, default='', max_length=4, null=True, verbose_name='학점'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_number',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='학수번호'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_room',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='강의실'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_time',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='강의시간'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='limit_count',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='제한인원수'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='note',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='비고'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='professor',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='담당교수'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='star_point',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='별점'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='time',
            field=models.CharField(blank=True, default='', max_length=4, null=True, verbose_name='시간'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='type',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='과목유형'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='year',
            field=models.CharField(blank=True, default='', max_length=4, null=True, verbose_name='학년'),
        ),
    ]