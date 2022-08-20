# Generated by Django 4.0.6 on 2022-08-20 06:15

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='사용자 아이디')),
                ('password', models.CharField(max_length=64, null=True, verbose_name='사용자 비밀번호')),
                ('email', models.EmailField(max_length=128, null=True, verbose_name='사용자 이메일')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('link', models.TextField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('x', models.CharField(max_length=100, null=True)),
                ('y', models.CharField(max_length=100, null=True)),
                ('reserveLink', models.TextField(null=True)),
                ('favorite', models.BooleanField(default=False)),
                ('star', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('menuInfo', models.TextField(null=True)),
                ('hourInfo', models.TextField(null=True)),
                ('link', models.TextField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('x', models.CharField(max_length=100, null=True)),
                ('y', models.CharField(max_length=100, null=True)),
                ('favorite', models.BooleanField(default=False)),
                ('star', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
                ('doro', models.CharField(max_length=100, null=True)),
                ('hourInfo', models.TextField(null=True)),
                ('x', models.FloatField(null=True)),
                ('y', models.FloatField(null=True)),
                ('link', models.CharField(max_length=100, null=True)),
                ('distance', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('link', models.TextField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('x', models.CharField(max_length=100, null=True)),
                ('y', models.CharField(max_length=100, null=True)),
                ('favorite', models.BooleanField(default=False)),
                ('star', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postType', models.CharField(max_length=100, null=True)),
                ('postImage', models.ImageField(blank=True, default='NULL', upload_to='posts/%Y%m%d', verbose_name='사진')),
                ('postGood', models.TextField(null=True)),
                ('postBad', models.TextField(null=True)),
                ('ranking', models.IntegerField(null=True)),
                ('placeId', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('placeType', models.CharField(max_length=50)),
                ('placeId', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
