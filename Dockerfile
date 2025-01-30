# Usar una imagen base de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver"]