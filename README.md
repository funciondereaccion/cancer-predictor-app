# Breast Cancer Predictor App

Esta es una aplicación de **predicción de cáncer de mama** que utiliza un modelo de Machine Learning (`Random Forest`) entrenado. Permite la predicción a través de una API REST, facilitando su ejecución local con **Docker** y su despliegue en entornos de nube.

---

## 1. Descripción del Proyecto

| Característica | Detalle |
| :--- | :--- |
| **Modelo** | Random Forest Classifier |
| **Dataset** | Wisconsin Breast Cancer (30 features) |
| **Entrada** | 30 características numéricas de tumores |
| **Salida** | Predicción: `0` (Maligno) o `1` (Benigno) |
| **API** | Construida con **Flask** (API REST) |

---

## 2. Instalación y Ejecución Local

Para ejecutar la aplicación localmente, se utiliza **Docker**, lo que garantiza que el entorno sea idéntico al de producción.

### Requisitos

Necesitas tener **Git** y **Docker** instalados en tu sistema.

### Pasos

1.  **Clona el repositorio** y navega al directorio:

    ```bash
    git clone [https://github.com/funciondereaccion/cancer-predictor-app.git](https://github.com/funciondereaccion/cancer-predictor-app.git)
    cd cancer-predictor-app
    ```

2.  **Construye la imagen de Docker**:

    ```bash
    docker build -t mlops-breastcancer .
    ```

3.  **Ejecuta el contenedor** y expón el puerto `5000`:

    ```bash
    docker run -p 5000:5000 mlops-breastcancer
    ```

4.  **Verifica que la API esté activa** (ejecuta esto en una nueva terminal):

    ```powershell
    Invoke-RestMethod -Uri "[http://127.0.0.1:5000/](http://127.0.0.1:5000/)"
    ```

    Deberías ver la siguiente respuesta:

    ```bash
    message
    -------
    API de predicción Breast Cancer activa 🚀
    ```

---

 ## 3. Ejemplo de Uso (API)

 Para obtener una predicción, envía una solicitud **POST** al *endpoint* `/predict` con un cuerpo JSON que contenga los 30 valores de las *features*.

 **Ejemplo de solicitud:**

 ```powershell
 Invoke-RestMethod -Uri "[http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict)" `
   -Method POST `
   -Headers @{ "Content-Type" = "application/json" } `
   -Body '{"features": [17.99,10.38,122.8,1001.0,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019.0,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]}'
 ---
```

 **Respuesta Esperada**

```json
{
  "prediction": 0,
  "resultado": "Maligno"
}
# Nota: Asegúrate de enviar 30 features, como espera el modelo #
```
## 4. Capturas de Pantalla
Se adjuntan 3 capturas de pantalla para orientar el curso de accion. La app corriendo, la dockerización y la prueba con get y post
