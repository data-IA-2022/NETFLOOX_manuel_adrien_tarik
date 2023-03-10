# Generated by Django 4.1.6 on 2023-02-22 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NameBasics',
            fields=[
                ('nconst', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('primaryname', models.CharField(blank=True, db_column='primaryName', max_length=300, null=True)),
                ('birthyear', models.SmallIntegerField(blank=True, db_column='birthYear', null=True)),
                ('deathyear', models.SmallIntegerField(blank=True, db_column='deathYear', null=True)),
                ('primaryprofession', models.CharField(blank=True, db_column='primaryProfession', max_length=300, null=True)),
            ],
            options={
                'db_table': 'name_basics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TableDecenieVotesRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(blank=True, max_length=8, null=True)),
                ('avg_num_votes', models.DecimalField(blank=True, decimal_places=0, max_digits=11, null=True)),
                ('avg_rating', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'table_decenie_votes_rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TableDistribNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occurance', models.BigIntegerField()),
                ('averagerating', models.FloatField(blank=True, db_column='averageRating', null=True)),
                ('prc', models.DecimalField(blank=True, decimal_places=2, max_digits=26, null=True)),
            ],
            options={
                'db_table': 'table_distrib_notes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TableDistribTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occurance', models.BigIntegerField()),
                ('titletype', models.CharField(blank=True, db_column='titleType', max_length=15, null=True)),
                ('prc', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'table_distrib_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TableFilms2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=10)),
                ('nconst', models.CharField(max_length=10)),
                ('titletype', models.CharField(blank=True, db_column='titleType', max_length=15, null=True)),
                ('originaltitle', models.CharField(blank=True, db_column='originalTitle', max_length=500, null=True)),
                ('runtimeminutes', models.IntegerField(blank=True, db_column='runtimeMinutes', null=True)),
                ('isadult', models.IntegerField(blank=True, db_column='isAdult', null=True)),
                ('startyear', models.SmallIntegerField(blank=True, db_column='startYear', null=True)),
                ('genres', models.CharField(blank=True, max_length=100, null=True)),
                ('nconst_director', models.CharField(max_length=10)),
                ('name_director', models.CharField(blank=True, max_length=300, null=True)),
                ('birthyear_director', models.SmallIntegerField(blank=True, db_column='birthYear_director', null=True)),
                ('deathyear_director', models.SmallIntegerField(blank=True, db_column='deathYear_director', null=True)),
                ('profession_director', models.CharField(blank=True, max_length=300, null=True)),
                ('nconst_writer', models.CharField(blank=True, max_length=10, null=True)),
                ('name_writer', models.CharField(blank=True, max_length=300, null=True)),
                ('birthyear_writer', models.SmallIntegerField(blank=True, db_column='birthYear_writer', null=True)),
                ('deathyear_writer', models.SmallIntegerField(blank=True, db_column='deathYear_writer', null=True)),
                ('profession_writer', models.CharField(blank=True, max_length=300, null=True)),
                ('averagerating', models.FloatField(blank=True, db_column='averageRating', null=True)),
                ('numvotes', models.IntegerField(blank=True, db_column='numVotes', null=True)),
                ('nconst_staf', models.CharField(blank=True, max_length=10, null=True)),
                ('primaryname', models.CharField(blank=True, db_column='primaryName', max_length=300, null=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('job', models.CharField(blank=True, max_length=300, null=True)),
                ('characters', models.CharField(blank=True, max_length=1400, null=True)),
            ],
            options={
                'db_table': 'table_films_2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TableListFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=10)),
                ('originaltitle', models.CharField(blank=True, db_column='originalTitle', max_length=500, null=True)),
            ],
            options={
                'db_table': 'table_list_films',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TableListFilmsEx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=10)),
                ('originaltitle', models.CharField(blank=True, db_column='originalTitle', max_length=500, null=True)),
                ('averagerating', models.FloatField(blank=True, db_column='averageRating', null=True)),
                ('numvotes', models.IntegerField(blank=True, db_column='numVotes', null=True)),
                ('startyear', models.SmallIntegerField(blank=True, db_column='startYear', null=True)),
            ],
            options={
                'db_table': 'table_list_films_ex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TablePropNotesNull',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=8)),
                ('cpt', models.BigIntegerField()),
                ('prc', models.DecimalField(blank=True, decimal_places=2, max_digits=26, null=True)),
            ],
            options={
                'db_table': 'table_prop_notes_null',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TableRegionDiffusionAvgRatingVotesFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_rating', models.FloatField(blank=True, null=True)),
                ('st_rating', models.FloatField(blank=True, null=True)),
                ('min_rating', models.FloatField(blank=True, null=True)),
                ('max_rating', models.FloatField(blank=True, null=True)),
                ('avg_num_votes', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True)),
                ('st_num_votes', models.FloatField(blank=True, null=True)),
                ('min_num_votes', models.IntegerField(blank=True, null=True)),
                ('max_num_votes', models.IntegerField(blank=True, null=True)),
                ('region', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'table_region_diffusion_avg_rating_votes_films',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TableRegionDiffusionFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occurence', models.BigIntegerField()),
                ('region', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'table_region_diffusion_films',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NameBasicsKnowfortitles',
            fields=[
                ('nconst', models.OneToOneField(db_column='nconst', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='netfloox_app.namebasics')),
                ('tconst', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'name_basics_knowfortitles',
                'managed': False,
            },
        ),
    ]
