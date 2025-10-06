# Imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY src/ .

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar Flask
CMD ["python", "app.py"]
