# Generated by Django 4.2.4 on 2023-08-12 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0002_alter_event_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Nombre municipio')),
                ('potencial', models.IntegerField(blank=True, null=True, verbose_name='Potencial')),
                ('numero_comunas', models.IntegerField(blank=True, null=True, verbose_name='Numero de COmunas')),
                ('numero_barrios', models.IntegerField(blank=True, null=True, verbose_name='Numero de Barrios o veredas')),
                ('numero_puestos', models.IntegerField(blank=True, null=True, verbose_name='Numero de Puestos de votacion')),
                ('numero_mesas', models.IntegerField(blank=True, null=True, verbose_name='Numero de mesas')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number_code', models.CharField(max_length=3, verbose_name='ISO 3166-1 numerico')),
                ('alfa_two', models.CharField(max_length=2, verbose_name='ISO 3166-1 alfa-2')),
                ('alfa_three', models.CharField(max_length=3, verbose_name='ISO 3166-1 alfa-3')),
                ('name', models.CharField(max_length=254, verbose_name='Nombre del país')),
                ('phone_code', models.CharField(max_length=5, verbose_name='Código número telefónico')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Nombre')),
                ('numero_puestos', models.IntegerField(blank=True, null=True, verbose_name='Numero de puestos')),
                ('numero_mesas', models.IntegerField(blank=True, null=True, verbose_name='Numero de mesas')),
            ],
            options={
                'verbose_name': 'Barrio',
                'verbose_name_plural': 'Barrios',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='Profesion')),
            ],
            options={
                'verbose_name': 'Profession',
                'verbose_name_plural': 'Professiones',
            },
        ),
        migrations.CreateModel(
            name='TypeMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Tipo de actividad')),
            ],
            options={
                'verbose_name': 'Tipo de actividad',
                'verbose_name_plural': 'Tipos de actividades',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='esteemed_assistants',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de asistentes esperados'),
        ),
        migrations.AddField(
            model_name='event',
            name='number_chairs',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de sillas'),
        ),
        migrations.AddField(
            model_name='event',
            name='number_gifts',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de regalos'),
        ),
        migrations.AddField(
            model_name='event',
            name='number_snacks',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de refrigerios'),
        ),
        migrations.AddField(
            model_name='event',
            name='number_tables',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de mesas'),
        ),
        migrations.AddField(
            model_name='event',
            name='observations',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='COmuna')),
                ('potencial', models.IntegerField(blank=True, null=True, verbose_name='Potencial')),
                ('numero_barrios', models.IntegerField(blank=True, null=True, verbose_name='Numero de Barrios o veredas')),
                ('numero_puestos', models.IntegerField(blank=True, null=True, verbose_name='Numero de Puestos de votacion')),
                ('numero_mesas', models.IntegerField(blank=True, null=True, verbose_name='Numero de mesas')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cal.city', verbose_name='Municipio')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
            },
        ),
        migrations.CreateModel(
            name='VotingPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Puesto de votación')),
                ('numero_barrios', models.IntegerField(blank=True, null=True, verbose_name='Numero de Barrios o veredas')),
                ('potencial', models.IntegerField(blank=True, null=True, verbose_name='POtencial')),
                ('numero_mesas', models.IntegerField(blank=True, null=True, verbose_name='Numero de mesas')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cal.neighborhood', verbose_name='Sector')),
            ],
            options={
                'verbose_name': 'Puesto de votación',
                'verbose_name_plural': 'Puestos de votaciones',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Nombre del departamento')),
                ('numero_municipios', models.IntegerField(blank=True, null=True, verbose_name='Numero de municipios')),
                ('potencial', models.IntegerField(blank=True, null=True, verbose_name='Potencial')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cal.country', verbose_name='País')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='Nombres')),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], max_length=1, null=True, verbose_name='Sexo')),
                ('cedula', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cedula')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('mesa_votacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='mesa de votacion')),
                ('direccion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo electronico')),
                ('delegado', models.BooleanField(blank=True, null=True, verbose_name='Delegado')),
                ('verificacion', models.BooleanField(blank=True, null=True, verbose_name='Verificacion')),
                ('publicidad', models.BooleanField(blank=True, null=True, verbose_name='Publicidad')),
                ('logistica', models.BooleanField(blank=True, null=True, verbose_name='Logistica')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.city', verbose_name='Municipio')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cal.country', verbose_name='País')),
                ('profesion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.profession', verbose_name='Profesion')),
                ('puesto_votacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.votingpost', verbose_name='Puesto votacion')),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.neighborhood', verbose_name='Sector o barrio')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.region', verbose_name='Departamento')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.zone', verbose_name='COmuna')),
            ],
            options={
                'verbose_name': 'Registro Votante',
                'verbose_name_plural': 'Registros Votantes',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='zone_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cal.zone', verbose_name='Comuna'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cal.region', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.city', verbose_name='Municipio'),
        ),
        migrations.AddField(
            model_name='event',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cal.country', verbose_name='País'),
        ),
        migrations.AddField(
            model_name='event',
            name='delegado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='delegadoreunion', to='cal.profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='encargado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Encargadoreunion', to='cal.profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='logistica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='logisticareunion', to='cal.profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='publicidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='publicidadpureunion', to='cal.profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='puesto_votacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.votingpost', verbose_name='Puesto votacion'),
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.region', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='event',
            name='type_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.typemeeting', verbose_name='Tipo de actividad'),
        ),
        migrations.AddField(
            model_name='event',
            name='verificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='verificadorreunion', to='cal.profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cal.zone', verbose_name='COmuna'),
        ),
    ]
