from django.db import models
from paneluser.models import Usuarios

# Create your models here.

class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "nacionalidad"
        verbose_name_plural = "nacionalidades"
        
    def __str__(self):
        return self.nacionalidad
    
    
class Sexo(models.Model):
    sexo = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "sexo"
        verbose_name_plural = "sexos"
        
    def __str__(self):
        return self.sexo
    
    
class EstadoCivil(models.Model):
    estado_civil = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "estado_civil"
        verbose_name_plural = "estados_civiles"
        
    def __str__(self):
        return self.estado_civil
    
    
class Sangre(models.Model):
    tipo_sangre = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "tipo_sangre"
        verbose_name_plural = "tipos_sangre"
        
    def __str__(self):
        return self.tipo_sangre
    

class TallasCamisa(models.Model):
    talla_camisa = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "talla_camisa"
        verbose_name_plural = "tallas_camisas"
        
    def __str__(self):
        return self.talla_camisa
    
    
class TallasPantalon(models.Model):
    talla_pantalon = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "talla_pantalon"
        verbose_name_plural = "tallas_pantalones"
        
    def __str__(self):
        return self.talla_pantalon
    
    
class TallasZapatos(models.Model):
    talla_zapato = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "talla_zapato"
        verbose_name_plural = "tallas_zapatos"
        
    def __str__(self):
        return self.talla_zapato
    

class Grado(models.Model):
    grado_instruccion = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "grado_instruccion"
        verbose_name_plural = "grados_instruccion"
        
    def __str__(self):
        return self.grado_instruccion
    
    
class TipoPersonal(models.Model):
    tipo_personal = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "tipo_personal"
        verbose_name_plural = "tipos_personales"
        
    def __str__(self):
        return self.tipo_personal
    

class Cargo(models.Model):
    cargo = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "cargo"
        verbose_name_plural = "cargos"
        
    def __str__(self):
        return self.cargo
    

class Departamento(models.Model):
    departamento = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"
        
    def __str__(self):
        return self.departamento
    
    
class Sedes(models.Model):
    sede = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "sede"
        verbose_name_plural = "sedes"
        
    def __str__(self):
        return self.sede


class Personal(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    cedula = models.IntegerField()
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    fecha_nac = models.DateField()
    edad = models.IntegerField()
    telefono = models.CharField(max_length=11)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    conyugue = models.CharField(max_length=50, blank=True, null=True)
    cedula_conyugue = models.IntegerField(blank=True, null=True)
    tipo_sangre = models.ForeignKey(Sangre, on_delete=models.CASCADE)    
    discapacitado = models.BooleanField()
    talla_camisa = models.ForeignKey(TallasCamisa, on_delete=models.CASCADE) 
    talla_pantalon = models.ForeignKey(TallasPantalon, on_delete=models.CASCADE) 
    talla_zapato = models.ForeignKey(TallasZapatos, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=150)
    nro_cuenta = models.CharField(max_length=25)
    email = models.EmailField(blank=True, null=True)
    grado_instruccion = models.ForeignKey(Grado, on_delete=models.CASCADE) 
    estudias = models.BooleanField()
    comision_servicio = models.BooleanField()
    pnb = models.BooleanField()
    tipo_personal = models.ForeignKey(TipoPersonal, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    fecha_ingreso_911 = models.DateField()
    fecha_ingreso_apn = models.DateField()
    contratos = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    niño_menor_12 = models.IntegerField(blank=True, null=True)
    edades1 = models.IntegerField(blank=True, null=True)
    hijos_13_18 = models.IntegerField(blank=True, null=True)
    edades2 = models.IntegerField(blank=True, null=True)
    niña_menor_12 = models.IntegerField(blank=True, null=True)
    edades3 = models.IntegerField(blank=True, null=True)
    hijos_discapacidad = models.IntegerField(blank=True, null=True)
    edades4 = models.IntegerField(blank=True, null=True)
    motivo = models.CharField(max_length=50, blank=True, null=True)
    sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)
    fasmij = models.BooleanField()
    parentezco1 = models.CharField(max_length=10, blank=True, null=True)
    beneficiario1 = models.CharField(max_length=50, blank=True, null=True)
    cedula1 = models.CharField(max_length=50, blank=True, null=True)
    direccion1 = models.CharField(max_length=150, blank=True, null=True)
    parentezco2 = models.CharField(max_length=10, blank=True, null=True)
    beneficiario2 = models.CharField(max_length=50, blank=True, null=True)
    cedula2 = models.CharField(max_length=50, blank=True, null=True)
    direccion2 = models.CharField(max_length=150, blank=True, null=True)
    parentezco3 = models.CharField(max_length=10, blank=True, null=True)
    beneficiario3 = models.CharField(max_length=50, blank=True, null=True)
    cedula3 = models.CharField(max_length=50, blank=True, null=True)
    direccion3 = models.CharField(max_length=150, blank=True, null=True)
    creador = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "personal"
        verbose_name_plural = "personales"
        
    def __str__(self):
        return self.nombres