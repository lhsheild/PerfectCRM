# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-02 22:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_customer_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='classlist',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='classlist',
            name='course',
        ),
        migrations.RemoveField(
            model_name='classlist',
            name='teachers',
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='courserecord',
            name='from_class',
        ),
        migrations.RemoveField(
            model_name='courserecord',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='consult_course',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='customerfollowup',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='customerfollowup',
            name='customer',
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='enrolled_class',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='role',
            name='menus',
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='studyrecord',
            name='course_record',
        ),
        migrations.RemoveField(
            model_name='studyrecord',
            name='student',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='ClassList',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='CourseRecord',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='CustomerFollowUp',
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='StudyRecord',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]