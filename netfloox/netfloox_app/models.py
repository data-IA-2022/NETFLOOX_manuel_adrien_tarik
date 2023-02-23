# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class NameBasics(models.Model):
    nconst = models.CharField(primary_key=True, max_length=10)
    primaryname = models.CharField(db_column='primaryName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    birthyear = models.SmallIntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    deathyear = models.SmallIntegerField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.
    primaryprofession = models.CharField(db_column='primaryProfession', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'name_basics'


class NameBasicsKnowfortitles(models.Model):
    nconst = models.OneToOneField(NameBasics, models.DO_NOTHING, db_column='nconst', primary_key=True)
    tconst = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'name_basics_knowfortitles'
        unique_together = (('nconst', 'tconst'),)


class TableDecenieVotesRating(models.Model):
    annee = models.CharField(max_length=8, blank=True, null=True)
    avg_num_votes = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    avg_rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_decenie_votes_rating'


class TableDistribNotes(models.Model):
    occurance = models.BigIntegerField()
    averagerating = models.FloatField(db_column='averageRating', blank=True, null=True)  # Field name made lowercase.
    prc = models.DecimalField(max_digits=26, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_distrib_notes'


class TableDistribTypes(models.Model):
    occurance = models.BigIntegerField()
    titletype = models.CharField(db_column='titleType', max_length=15, blank=True, null=True)  # Field name made lowercase.
    prc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_distrib_types'


class TableFilms2(models.Model):
    tconst = models.CharField(max_length=10)
    nconst = models.CharField(max_length=10)
    titletype = models.CharField(db_column='titleType', max_length=15, blank=True, null=True)  # Field name made lowercase.
    originaltitle = models.CharField(db_column='originalTitle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    runtimeminutes = models.IntegerField(db_column='runtimeMinutes', blank=True, null=True)  # Field name made lowercase.
    isadult = models.IntegerField(db_column='isAdult', blank=True, null=True)  # Field name made lowercase.
    startyear = models.SmallIntegerField(db_column='startYear', blank=True, null=True)  # Field name made lowercase.
    genres = models.CharField(max_length=100, blank=True, null=True)
    nconst_director = models.CharField(max_length=10)
    name_director = models.CharField(max_length=300, blank=True, null=True)
    birthyear_director = models.SmallIntegerField(db_column='birthYear_director', blank=True, null=True)  # Field name made lowercase.
    deathyear_director = models.SmallIntegerField(db_column='deathYear_director', blank=True, null=True)  # Field name made lowercase.
    profession_director = models.CharField(max_length=300, blank=True, null=True)
    nconst_writer = models.CharField(max_length=10, blank=True, null=True)
    name_writer = models.CharField(max_length=300, blank=True, null=True)
    birthyear_writer = models.SmallIntegerField(db_column='birthYear_writer', blank=True, null=True)  # Field name made lowercase.
    deathyear_writer = models.SmallIntegerField(db_column='deathYear_writer', blank=True, null=True)  # Field name made lowercase.
    profession_writer = models.CharField(max_length=300, blank=True, null=True)
    averagerating = models.FloatField(db_column='averageRating', blank=True, null=True)  # Field name made lowercase.
    numvotes = models.IntegerField(db_column='numVotes', blank=True, null=True)  # Field name made lowercase.
    nconst_staf = models.CharField(max_length=10, blank=True, null=True)
    primaryname = models.CharField(db_column='primaryName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=20, blank=True, null=True)
    job = models.CharField(max_length=300, blank=True, null=True)
    characters = models.CharField(max_length=1400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_films_2'


class TableListFilms(models.Model):
    tconst = models.CharField(max_length=10)
    originaltitle = models.CharField(db_column='originalTitle', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table_list_films'


class TableListFilmsEx(models.Model):
    tconst = models.CharField(max_length=10)
    originaltitle = models.CharField(db_column='originalTitle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    averagerating = models.FloatField(db_column='averageRating', blank=True, null=True)  # Field name made lowercase.
    numvotes = models.IntegerField(db_column='numVotes', blank=True, null=True)  # Field name made lowercase.
    startyear = models.SmallIntegerField(db_column='startYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table_list_films_ex'


class TablePropNotesNull(models.Model):
    label = models.CharField(max_length=8)
    cpt = models.BigIntegerField()
    prc = models.DecimalField(max_digits=26, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_prop_notes_null'


class TableRegionDiffusionAvgRatingVotesFilms(models.Model):
    avg_rating = models.FloatField(blank=True, null=True)
    st_rating = models.FloatField(blank=True, null=True)
    min_rating = models.FloatField(blank=True, null=True)
    max_rating = models.FloatField(blank=True, null=True)
    avg_num_votes = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    st_num_votes = models.FloatField(blank=True, null=True)
    min_num_votes = models.IntegerField(blank=True, null=True)
    max_num_votes = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_region_diffusion_avg_rating_votes_films'


class TableRegionDiffusionFilms(models.Model):
    occurence = models.BigIntegerField()
    region = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_region_diffusion_films'
