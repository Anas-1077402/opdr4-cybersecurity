# Generated by Django 4.2.9 on 2024-02-27 12:19

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0002_organisaties_typeonderzoek_delete_organisatie_and_more'),
        ('beheerder', '0001_initial'),
        ('ervaringsdeskundige', '0006_remove_ervaringsdeskundige_achternaam_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeperkingenErvaringsdeskundigen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beperking_id', models.IntegerField()),
                ('ervaringsdeskundigen_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Beperkingen_ervaringsdeskundigen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BeperkingenOnderzoeken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onderzoeks_id', models.IntegerField()),
                ('beperking_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Beperkingen_onderzoeken',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=10)),
                ('geslacht', models.CharField(choices=[('M', 'Man'), ('V', 'Vrouw'), ('0', 'Anders')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('telefoonnummer', models.CharField(max_length=100)),
                ('geboortedatum', models.DateField()),
                ('gebruikte_hulpmiddelen', models.TextField(max_length=200)),
                ('bijzonderheden', models.TextField(blank=True, default='', max_length=100)),
                ('bijzonderheden_beschikbaarheid', models.TextField(blank=True, max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('voorkeur_benadering', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
                ('datum_goedgekeurd', models.DateTimeField(blank=True, null=True)),
                ('goedegekeurd_door', models.ForeignKey(blank=True, db_column='goedegekeurd_door', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='beheerder.beheerders')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_groups', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('toezichthouder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_toezichthouders', to='main.toezichthouders')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_user_permissions', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
        migrations.DeleteModel(
            name='Ervaringsdeskundige',
        ),
    ]
