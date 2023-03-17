# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Diccionario(models.Model):
    dic_key = models.AutoField(primary_key=True)
    dic_palabra = models.CharField(max_length=50, blank=True, null=True)
    dic_definicion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Diccionario'


class Lectura(models.Model):
    lec_key = models.FloatField()
    lec_fecha = models.CharField(max_length=255, blank=True, null=True)
    lec_am_libro = models.IntegerField(blank=True, null=True)
    lec_am_cap_start = models.IntegerField(blank=True, null=True)
    lec_am_cap_end = models.IntegerField(blank=True, null=True)
    lec_am_vers_start = models.IntegerField(blank=True, null=True)
    lec_am_vers_end = models.IntegerField(blank=True, null=True)
    lec_pm_libro = models.IntegerField(blank=True, null=True)
    lec_pm_cap_start = models.IntegerField(blank=True, null=True)
    lec_pm_cap_end = models.IntegerField(blank=True, null=True)
    lec_pm_vers_start = models.IntegerField(blank=True, null=True)
    lec_pm_vers_end = models.IntegerField(blank=True, null=True)
    lec_am_start = models.IntegerField(blank=True, null=True)
    lec_am_end = models.IntegerField(blank=True, null=True)
    lec_pm_start = models.IntegerField(blank=True, null=True)
    lec_pm_end = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Lectura'


class Usuarios(models.Model):
    user_key = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_password = models.TextField(blank=True, null=True)
    user_nombre = models.CharField(max_length=50, blank=True, null=True)
    user_apellido = models.CharField(max_length=50, blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    user_fk_cia_key = models.IntegerField(blank=True, null=True)
    user_role = models.IntegerField(blank=True, null=True)
    user_address = models.CharField(max_length=50, blank=True, null=True)
    user_llave = models.TextField(blank=True, null=True)
    user_celular = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuarios'


class Anuncios(models.Model):
    an_key = models.AutoField(primary_key=True)
    an_title = models.CharField(max_length=50, blank=True, null=True)
    an_date = models.CharField(max_length=50, blank=True, null=True)
    an_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anuncios'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Displayverso(models.Model):
    dv_key = models.AutoField(primary_key=True)
    dv_verso = models.IntegerField()
    dv_nro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'displayVerso'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class EstudioVersos(models.Model):
    ve_key = models.AutoField(primary_key=True)
    ve_fk_e_id_key = models.IntegerField(blank=True, null=True)
    ve_fk_v_idversiculo = models.IntegerField(db_column='ve_fk_V_IdVersiculo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estudio_versos'


class Eventos(models.Model):
    eve_key = models.AutoField(primary_key=True)
    eve_title = models.CharField(max_length=50, blank=True, null=True)
    eve_date = models.CharField(max_length=50, blank=True, null=True)
    eve_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventos'


class Lcapitulos(models.Model):
    c_idcapitulo = models.IntegerField(db_column='C_IdCapitulo', primary_key=True)  # Field name made lowercase.
    c_capitulo_desc = models.IntegerField(db_column='C_Capitulo_Desc', blank=True, null=True)  # Field name made lowercase.
    c_idlibro = models.ForeignKey('Llibros', models.DO_NOTHING, db_column='C_IdLibro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lCapitulos'


class Lestudios(models.Model):
    e_id_key = models.AutoField(primary_key=True)
    e_estudio = models.CharField(max_length=200, blank=True, null=True)
    e_http = models.CharField(max_length=200, blank=True, null=True)
    e_fk_id_cat = models.IntegerField(blank=True, null=True)
    e_remarks = models.CharField(max_length=200, blank=True, null=True)
    e_short_url = models.CharField(max_length=10, blank=True, null=True)
    e_flag_activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lEstudios'


class Llibros(models.Model):
    l_idlibro = models.IntegerField(db_column='L_IdLibro', primary_key=True)  # Field name made lowercase.
    l_libro_desc = models.CharField(db_column='L_Libro_Desc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    l_link = models.CharField(db_column='L_link', max_length=200, blank=True, null=True)  # Field name made lowercase.
    l_link2 = models.CharField(db_column='L_link2', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lLibros'


class LpaCara(models.Model):
    ca_key = models.AutoField(primary_key=True)
    ca_fk_pa_key = models.IntegerField(blank=True, null=True)
    ca_verso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lPa_cara'


class LpaSello(models.Model):
    se_key = models.AutoField(primary_key=True)
    se_fk_pa_key = models.IntegerField(blank=True, null=True)
    se_verso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lPa_sello'
