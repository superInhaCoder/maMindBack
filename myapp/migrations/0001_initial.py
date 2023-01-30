# Generated by Django 4.1.5 on 2023-01-30 14:07

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('sub', models.CharField(db_index=True, max_length=64, verbose_name='SUB')),
                ('name', models.CharField(default='', max_length=64, verbose_name='이름')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='가입 날짜')),
                ('last_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='마지막 로그인')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'user',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(default='', max_length=64, verbose_name='이름')),
                ('content', models.TextField(default='', max_length=1000, verbose_name='내용')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='가입 날짜')),
                ('last_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='마지막 로그인')),
            ],
            options={
                'verbose_name': '의사',
                'verbose_name_plural': '의사',
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='GoalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(editable=False, max_length=100, verbose_name='주제')),
            ],
            options={
                'verbose_name': '목표 카테고리',
                'verbose_name_plural': '목표 카테고리',
                'db_table': 'goal_category',
            },
        ),
        migrations.CreateModel(
            name='GoalList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(editable=False, max_length=100, verbose_name='주제')),
                ('mission1', models.CharField(editable=False, max_length=100, verbose_name='미션 1')),
                ('mission2', models.CharField(editable=False, max_length=100, verbose_name='미션 2')),
                ('mission3', models.CharField(editable=False, max_length=100, verbose_name='미션 3')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.goalcategory', verbose_name='카테고리')),
            ],
            options={
                'verbose_name': '목표 목록',
                'verbose_name_plural': '목표 목록',
                'db_table': 'goal_list',
            },
        ),
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(editable=False, max_length=20, verbose_name='가입 경로')),
            ],
            options={
                'verbose_name': '가입 경로',
                'verbose_name_plural': '가입 경로',
                'db_table': 'social_platform',
            },
        ),
        migrations.CreateModel(
            name='TestList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(editable=False, max_length=100, verbose_name='검사 이름')),
                ('content', models.CharField(editable=False, max_length=100, verbose_name='검사 설명')),
                ('count', models.IntegerField(default=10, verbose_name='검사 항목 수')),
            ],
            options={
                'verbose_name': '검사 목록',
                'verbose_name_plural': '검사 목록',
                'db_table': 'test_list',
            },
        ),
        migrations.CreateModel(
            name='UserGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.BooleanField(default=0, verbose_name='달성 여부')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.goallist', verbose_name='카테고리')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '사용자 목표',
                'verbose_name_plural': '사용자 목표',
                'db_table': 'user_goal',
                'ordering': ['success'],
            },
        ),
        migrations.CreateModel(
            name='UserCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_date', models.DateField(default=django.utils.timezone.now, verbose_name='선택 날짜')),
                ('value', models.TextField(default='', max_length=200, verbose_name='값')),
                ('test_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.testlist', verbose_name='선택된 질문')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '사용자 체크리스트',
                'verbose_name_plural': '사용자 체크리스트',
                'db_table': 'user_check',
                'ordering': ['-selected_date'],
            },
        ),
        migrations.CreateModel(
            name='TestItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', max_length=200, verbose_name='내용')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.testlist', verbose_name='검사 종류')),
            ],
            options={
                'verbose_name': '검사 종류',
                'verbose_name_plural': '검사 종류',
                'db_table': 'test_item',
            },
        ),
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', max_length=200, verbose_name='내용')),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.doctor', verbose_name='의사')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '상담',
                'verbose_name_plural': '상담',
                'db_table': 'consult',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.socialplatform', verbose_name='가입 경로'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
