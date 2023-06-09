# Generated by Django 4.0.4 on 2022-05-04 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Portal_Account', '0004_remove_students_profile_pic_courses_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance_Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attendance_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Portal_Account.students')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Portal_Account.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attendance_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Portal_Account.subjects')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Portal_Account.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Compliant_Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Student_name', models.CharField(default='', max_length=255)),
                ('Student_class', models.CharField(default='', max_length=255)),
                ('Student_course', models.CharField(default='', max_length=255)),
                ('complaint', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Portal_Account.teacher')),
            ],
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='attendance_id',
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='compliant_student',
            name='complaint_reply',
        ),
        migrations.RemoveField(
            model_name='compliant_student',
            name='teacher_id',
        ),
        migrations.RemoveField(
            model_name='note_student',
            name='student_id',
        ),
        migrations.AddField(
            model_name='compliant_student',
            name='Subject_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='compliant_student',
            name='teacher_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='note_student',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Portal_Account.courses'),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceReport',
        ),
    ]
