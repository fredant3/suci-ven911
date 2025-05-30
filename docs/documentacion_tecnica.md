# Documentación Técnica del Sistema SUCI (Sistema Unificado para el Control Interno del Ven911)

## 1. Introducción

El Sistema Unificado para el Control Interno del Ven911 (SUCI) es una aplicación web desarrollada para gestionar y controlar los procesos internos del servicio de emergencias Ven911. El sistema está diseñado con una arquitectura modular que permite la gestión de diferentes áreas operativas de la organización, incluyendo recursos humanos, administración, operaciones de emergencia, presupuesto, entre otros.

## 2. Arquitectura del Sistema

### 2.1 Tecnologías Utilizadas

- **Backend**: Django 5.1.1 (Framework de Python)
- **API REST**: Django REST Framework 3.15.2
- **Autenticación**: JWT (JSON Web Tokens) mediante djangorestframework_simplejwt 5.3.1
- **Base de Datos**: Compatible con SQLite y PostgreSQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Gestión de Formularios**: django-crispy-forms, django-formtools
- **Variables de Entorno**: python-dotenv
- **Exportación de Datos**: openpyxl (para Excel)
- **Datos de Prueba**: Faker

### 2.2 Estructura del Proyecto

El proyecto sigue una arquitectura modular basada en aplicaciones Django, donde cada módulo funcional está encapsulado en su propia aplicación:

```
suci-ven911/
├── apps/                   # Directorio principal de aplicaciones
│   ├── administracion/     # Gestión administrativa
│   ├── asesoria/           # Asesoría jurídica
│   ├── auditoria/          # Sistema de auditoría
│   ├── biblioteca/         # Biblioteca de manuales
│   ├── dashboard/          # Panel principal
│   ├── emergencia/         # Gestión de emergencias
│   ├── gestion_comunicacional/ # Gestión comunicacional
│   ├── helpers/            # Utilidades y clases base
│   ├── organizacion/       # Gestión organizacional
│   ├── planificacion/      # Planificación
│   ├── potencia/           # Módulo de potencia
│   ├── presupuesto/        # Gestión presupuestaria
│   ├── reporte_averia/     # Reportes de averías
│   ├── rrhh/               # Recursos humanos
│   ├── seguridad/          # Seguridad
│   ├── tecnologia/         # Tecnología e información
│   ├── uri/                # Unidad de Respuesta Inmediata
│   └── users/              # Gestión de usuarios
├── media/                  # Archivos subidos por usuarios
├── suci/                   # Configuración principal del proyecto
├── templates/              # Plantillas HTML
└── manage.py               # Script de gestión de Django
```

### 2.3 Patrón de Arquitectura

El sistema implementa una arquitectura basada en el patrón MVC (Modelo-Vista-Controlador), adaptado a la terminología de Django como MTV (Modelo-Plantilla-Vista):

- **Modelos**: Definen la estructura de datos y la lógica de negocio
- **Vistas**: Controlan la lógica de presentación y el flujo de la aplicación
- **Plantillas**: Definen la presentación visual de los datos

Adicionalmente, se implementa un patrón de repositorio para separar la lógica de acceso a datos de la lógica de negocio, y un patrón de servicio para encapsular la lógica de negocio.

## 3. Módulos del Sistema

### 3.1 Módulo de Usuarios (apps.users)

Gestiona la autenticación y autorización de usuarios en el sistema.

- **Características principales**:
  - Autenticación basada en JWT
  - Modelo de usuario personalizado con DNI como identificador
  - Gestión de permisos y roles

### 3.2 Módulo de Administración (apps.administracion)

Gestiona aspectos administrativos como:
- Sedes
- Departamentos
- Inventario
- Compras
- Averías
- Asignaciones

### 3.3 Módulo de Emergencia (apps.emergencia)

Gestiona las operaciones relacionadas con emergencias:
- Incidencias
- Operaciones
- Organismos

### 3.4 Módulo de Recursos Humanos (apps.rrhh)

Administra el personal de la organización:
- Cargos
- Contratos
- Empleados
- Familiares
- Sueldos
- Tipos de sueldos
- Dotaciones
- Educaciones

### 3.5 Módulo de Presupuesto (apps.presupuesto)

Gestiona los aspectos financieros:
- Acciones
- Asignaciones
- Cedentes
- Partidas
- Proyectos
- Receptores
- Traspasos

### 3.6 Módulo de Tecnología (apps.tecnologia)

Administra aspectos tecnológicos y de seguridad informática:
- Usuarios del sistema
- Grupos y permisos
- Auditoría de acciones

### 3.7 Otros Módulos

- **Asesoría Jurídica**: Gestión de denuncias y aspectos legales
- **Biblioteca**: Gestión de normativas y reglamentos
- **Organización**: Estructura organizacional
- **Planificación**: Actividades, infraestructuras, objetivos y transportes
- **Potencia**: Gestión de incidencias y URI (Unidad de Respuesta Inmediata)
- **Seguridad**: Control de entradas, salidas, gestiones y vehículos
- **Gestión Comunicacional**: Frente preventivo y comunicaciones

## 4. Estructura de Datos

### 4.1 Modelo Base

Todos los modelos del sistema heredan de `BaseModel`, que proporciona campos comunes:

```python
class BaseModel(models.Model):
    created_by = models.CharField(verbose_name="Creado por", max_length=6)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_by = models.CharField(verbose_name="Actualizado por", max_length=6)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")
    deleted_by = models.CharField(verbose_name="Eliminado por", max_length=6, null=True, blank=True)
    deleted_at = models.DateTimeField(verbose_name="Eliminado el", null=True, blank=True)
```

Este modelo implementa un borrado lógico (soft delete) en lugar de eliminar físicamente los registros.

### 4.2 Modelo de Usuario

El sistema utiliza un modelo de usuario personalizado:

```python
class User(AbstractBaseUser, PermissionsMixin):
    username = CharField(max_length=50, unique=True)
    dni = CharField(max_length=12, unique=True)
    is_staff = BooleanField(choices=BOOLEAN_CHOICES, default=BOOLEAN_CHOICES[1])
    is_active = BooleanField(choices=BOOLEAN_CHOICES, default=BOOLEAN_CHOICES[1])
    is_superuser = BooleanField(choices=BOOLEAN_CHOICES, default=BOOLEAN_CHOICES[1])
```

## 5. Patrones de Diseño

### 5.1 Patrón Repositorio

Cada módulo implementa un patrón repositorio para separar la lógica de acceso a datos:

```python
# Ejemplo de repositorio
class DepartamentoRepository:
    def get_all(self):
        return Departamento.objects.all()
    
    def get_by_id(self, id):
        return Departamento.objects.get(id=id)
```

### 5.2 Patrón Servicio

La lógica de negocio se encapsula en servicios:

```python
# Ejemplo de servicio
class DepartamentoService:
    def __init__(self):
        self.repository = DepartamentoRepository()
    
    def get_all(self):
        return self.repository.get_all()
    
    def create(self, data, user):
        # Lógica de negocio para crear un departamento
        pass
```

### 5.3 Mixins

El sistema utiliza varios mixins para reutilizar funcionalidad:

- `BaseModelMixin`: Proporciona funcionalidad común para modelos
- `CheckPermisosMixin`: Verifica permisos de usuario
- `ControllerMixin`: Funcionalidad común para controladores
- `CrudMixin`: Operaciones CRUD estándar
- `RepositoryMixin`: Funcionalidad común para repositorios
- `ServiceUtilMixin`: Utilidades para servicios

## 6. Seguridad

### 6.1 Autenticación

- Basada en JWT (JSON Web Tokens)
- Tokens de acceso con duración de 180 minutos
- Tokens de actualización con duración de 50 días
- Rotación de tokens de actualización

### 6.2 Autorización

- Sistema de permisos basado en grupos
- Verificación de permisos a nivel de vista
- Middleware para captura de IP y dispositivo

### 6.3 Auditoría

El sistema incluye un módulo de auditoría que registra:
- Acciones de usuarios
- Direcciones IP
- Información del dispositivo
- Timestamps de acciones

## 7. Interfaces

### 7.1 Interfaz Web

- Basada en el tema Sneat
- Diseño responsivo
- Componentes reutilizables

### 7.2 API REST

- Implementada con Django REST Framework
- Autenticación mediante JWT
- Paginación estándar (10 elementos por página)

## 8. Configuración y Despliegue

### 8.1 Requisitos del Sistema

- Python 3.x
- PostgreSQL (opcional, también soporta SQLite)
- Dependencias listadas en requirements.txt

### 8.2 Variables de Entorno

El sistema utiliza variables de entorno para configuración:

- `SECRET_KEY`: Clave secreta de Django
- `DEBUG`: Modo de depuración (True/False)
- `DB_BACKEND`: Motor de base de datos (postgresql/sqlite)
- `DB_DATABASE`: Nombre de la base de datos
- `DB_USERNAME`: Usuario de la base de datos
- `DB_PASSWORD`: Contraseña de la base de datos
- `DB_HOST`: Host de la base de datos
- `DB_PORT`: Puerto de la base de datos
- `LOG_LEVEL`: Nivel de registro (info, debug, etc.)

### 8.3 Proceso de Instalación

1. Clonar el repositorio
2. Crear y activar entorno virtual
3. Instalar dependencias
4. Configurar variables de entorno
5. Ejecutar migraciones
6. Crear superusuario
7. Iniciar servidor

## 9. Conclusiones

El Sistema Unificado para el Control Interno del Ven911 (SUCI) es una aplicación web robusta y modular diseñada para gestionar eficientemente los procesos internos del servicio de emergencias. Su arquitectura basada en Django proporciona una base sólida para el desarrollo y mantenimiento continuo, mientras que su diseño modular permite la extensión y adaptación a nuevas necesidades organizacionales.

La implementación de patrones de diseño como Repositorio y Servicio, junto con el uso de mixins para la reutilización de código, facilita el mantenimiento y la escalabilidad del sistema. Además, la seguridad se aborda de manera integral mediante autenticación JWT, control de permisos y auditoría de acciones.

## 10. Referencias

- [Documentación de Django](https://docs.djangoproject.com/)
- [Documentación de Django REST Framework](https://www.django-rest-framework.org/)
- [Documentación de Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)