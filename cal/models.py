from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
SEX_CHOICES = (
        ('F', 'Femenino',),
        ('M', 'Masculino',),
        ('O', 'Otro',),
    )
class Profession(models.Model):
    name = models.CharField(max_length=20, blank=True, verbose_name='Profesion')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profession'
        verbose_name_plural = 'Professiones'
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    number_code = models.CharField(verbose_name='ISO 3166-1 numerico', max_length=3)
    alfa_two = models.CharField(verbose_name='ISO 3166-1 alfa-2', max_length=2)
    alfa_three = models.CharField(verbose_name='ISO 3166-1 alfa-3', max_length=3)
    name = models.CharField(verbose_name='Nombre del país', max_length=254)
    phone_code = models.CharField(verbose_name='Código número telefónico', max_length=5)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(verbose_name='Nombre del departamento', max_length=254)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='País')
    numero_municipios = models.IntegerField(verbose_name='Numero de municipios',blank=True,null=True)
    potencial = models.IntegerField(verbose_name='Potencial', blank=True, null=True)
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return '{} | {}'.format(self.country.name, self.name)


class City(models.Model):
    name = models.CharField(verbose_name='Nombre municipio', max_length=254)
    state = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Departamento')
    potencial = models.IntegerField(verbose_name='Potencial',  blank=True, null=True)
    numero_comunas = models.IntegerField(verbose_name='Numero de COmunas', blank=True, null=True)
    numero_barrios = models.IntegerField(verbose_name='Numero de Barrios o veredas', blank=True, null=True)
    numero_puestos = models.IntegerField(verbose_name='Numero de Puestos de votacion', blank=True, null=True)
    numero_mesas = models.IntegerField(verbose_name='Numero de mesas',  blank=True, null=True)
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return '{} | {} | {}'.format(self.state.country.name, self.state.name, self.name)

    def save(self, *args, **kwargs):
        super(City, self).save(*args, **kwargs)


class Zone(models.Model):
    name = models.CharField(verbose_name='COmuna', max_length=254)
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Municipio')
    potencial = models.IntegerField(verbose_name='Potencial', blank=True, null=True)
    numero_barrios = models.IntegerField(verbose_name='Numero de Barrios o veredas', blank=True,
                                         null=True)
    numero_puestos = models.IntegerField(verbose_name='Numero de Puestos de votacion', blank=True,
                                         null=True)
    numero_mesas = models.IntegerField(verbose_name='Numero de mesas', blank=True, null=True)
    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def __str__(self):
        return '{} | {} | {} | {}'.format(self.city.state.country.name, self.city.state.name, self.city.name, self.name)


class Neighborhood(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=254)
    zone_type = models.ForeignKey(Zone, on_delete=models.PROTECT, verbose_name='Comuna')
    numero_puestos = models.IntegerField(verbose_name='Numero de puestos',  blank=True,
                                         null=True)
    numero_mesas = models.IntegerField(verbose_name='Numero de mesas',  blank=True, null=True)

    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'

    def __str__(self):
        return '{} | {} | {} | {} | {}'.format(self.zone_type.city.state.country.name, self.zone_type.city.state.name,
                                               self.zone_type.city.name, self.zone_type.name, self.name)


class VotingPost(models.Model):
    name = models.CharField(verbose_name='Puesto de votación', max_length=254)
    sector = models.ForeignKey(Neighborhood, on_delete=models.PROTECT, verbose_name='Sector')
    numero_barrios = models.IntegerField(verbose_name='Numero de Barrios o veredas',  blank=True,
                                         null=True)
    potencial = models.IntegerField(verbose_name='POtencial',  blank=True,
                                         null=True)
    numero_mesas = models.IntegerField(verbose_name='Numero de mesas',  blank=True, null=True)

    class Meta:
        verbose_name = 'Puesto de votación'
        verbose_name_plural = 'Puestos de votaciones'

    def __str__(self):
        return '{} | {} | {} | {} | {} | {}'.format(self.sector.zone_type.city.state.country.name, self.sector.zone_type.city.state.name,
                                               self.sector.zone_type.city.name, self.sector.zone_type.name, self.sector.name, self.name)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)
    first_name = models.CharField(max_length=200,verbose_name='Nombres', blank=True)
    fecha_nacimiento=models.DateTimeField(auto_now=False, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name='Sexo', null=True, blank=True)
    cedula = models.CharField(max_length=20,verbose_name='Cedula',blank=True,null=True)
    profesion  = models.ForeignKey(Profession,verbose_name='Profesion',on_delete=models.PROTECT,blank=True,null=True)

    phone_number = models.CharField(max_length=20, blank=True)
    '''
    country = models.ForeignKey(Country, verbose_name='País', on_delete=models.CASCADE)
    state = ChainedForeignKey(Region, verbose_name='Departamento',
                              chained_field='country', chained_model_field='country',
                              show_all=False, auto_choose=True)
    city = ChainedForeignKey(City, verbose_name='Municipio', chained_field='state', chained_model_field='state')
    zone = ChainedForeignKey(Zone, verbose_name='Tipo de zona', chained_field='city',
                             chained_model_field='city')
    sector = ChainedForeignKey(Neighborhood, verbose_name='Sector', chained_field='zone_type',
                               chained_model_field='zone_type')
    puesto_votacion = ChainedForeignKey(VotingPost, verbose_name='Puesto de votación', null=True, blank=True,
                                        on_delete=models.PROTECT)'''
    country = models.ForeignKey(Country, verbose_name='País', on_delete=models.CASCADE,blank=True,null=True)
    state = models.ForeignKey(Region, verbose_name='Departamento',on_delete=models.PROTECT,blank=True,null=True)
    city = models.ForeignKey(City, verbose_name='Municipio',on_delete=models.PROTECT,blank=True,null=True)
    zone = models.ForeignKey(Zone, verbose_name='COmuna',on_delete=models.PROTECT,blank=True,null=True)
    puesto_votacion = models.ForeignKey(VotingPost, verbose_name='Puesto votacion',on_delete=models.PROTECT,blank=True,null=True)
    mesa_votacion = models.CharField(max_length=200,verbose_name='mesa de votacion',blank=True,null=True)
    sector = models.ForeignKey(Neighborhood, verbose_name='Sector o barrio',on_delete=models.PROTECT,blank=True,null=True)
    direccion = models.CharField(max_length=200,verbose_name='Direccion',blank=True,null=True)
    email = models.EmailField(max_length=200,verbose_name='Correo electronico',blank=True,null=True)
    delegado = models.BooleanField(verbose_name='Delegado',blank=True,null=True)
    verificacion = models.BooleanField(verbose_name='Verificacion',blank=True,null=True)
    publicidad = models.BooleanField(verbose_name='Publicidad',blank=True,null=True)
    logistica = models.BooleanField(verbose_name='Logistica',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class MPTTMeta:
        order_insertion_by = ['id']

    class Meta:
        ordering = ['id']
        verbose_name = 'Registro Votante'
        verbose_name_plural = 'Registros Votantes'

    def __str__(self):
        return '{}'.format(self.cedula)
class TypeMeeting(models.Model):
    name = models.CharField(max_length=180, verbose_name='Tipo de actividad')

    class Meta:
        verbose_name = 'Tipo de actividad'
        verbose_name_plural = 'Tipos de actividades'

    def save(self, *args, **kwargs):
        super(TypeMeeting, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    country = models.ForeignKey(Country, verbose_name='País', on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(Region, verbose_name='Departamento', on_delete=models.PROTECT, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Municipio', on_delete=models.PROTECT, blank=True, null=True)
    zone = models.ForeignKey(Zone, verbose_name='COmuna', on_delete=models.PROTECT, blank=True, null=True)
    puesto_votacion = models.ForeignKey(VotingPost, verbose_name='Puesto votacion', on_delete=models.PROTECT,
                                        blank=True, null=True)
    type_activity = models.ForeignKey(TypeMeeting, verbose_name='Tipo de actividad', null=True, blank=True,
                                      on_delete=models.PROTECT)
    esteemed_assistants = models.PositiveIntegerField(verbose_name='Número de asistentes esperados', null=True,
                                                      blank=True)
    number_chairs = models.PositiveIntegerField(verbose_name='Número de sillas', null=True, blank=True)
    number_tables = models.PositiveIntegerField(verbose_name='Número de mesas', null=True, blank=True)
    number_snacks = models.PositiveIntegerField(verbose_name='Número de refrigerios', null=True, blank=True)
    number_gifts = models.PositiveIntegerField(verbose_name='Número de regalos', null=True, blank=True)
    observations = models.TextField(verbose_name='Observaciones', null=True, blank=True)
    encargado = models.ForeignKey(Profile, related_name='Encargadoreunion', on_delete=models.PROTECT, null=True,
                                  blank=True)
    delegado = models.ForeignKey(Profile, related_name='delegadoreunion', on_delete=models.PROTECT, null=True,
                                 blank=True)
    verificador = models.ForeignKey(Profile, related_name='verificadorreunion', on_delete=models.PROTECT, null=True,
                                    blank=True)
    publicidad = models.ForeignKey(Profile, related_name='publicidadpureunion', on_delete=models.PROTECT, null=True,
                                   blank=True)
    logistica = models.ForeignKey(Profile, related_name='logisticareunion', on_delete=models.PROTECT, null=True,
                                  blank=True)

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} {self.start_time}</a>'
