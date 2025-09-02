# Guía de Despliegue para Obtener un Link Público

Esta guía te ayudará a desplegar tu aplicación de Diseño de Estructuras de Concreto en Streamlit Cloud para obtener un link público que puedas compartir con cualquier persona.

## Pasos para Desplegar en Streamlit Cloud

### 1. Crear una cuenta en GitHub

Si aún no tienes una cuenta en GitHub:
1. Ve a [GitHub](https://github.com/)
2. Haz clic en "Sign up" y sigue las instrucciones para crear una cuenta

### 2. Crear un nuevo repositorio en GitHub

1. Inicia sesión en tu cuenta de GitHub
2. Haz clic en el botón "+" en la esquina superior derecha y selecciona "New repository"
3. Nombra tu repositorio (por ejemplo, "ParcialCivil")
4. Deja el repositorio como público
5. Haz clic en "Create repository"

### 3. Subir tu código al repositorio

Desde tu computadora, abre una terminal o línea de comandos y ejecuta:

```bash
# Navega a la carpeta de tu proyecto
cd c:\Users\57314\Desktop\Downloads\parcialParcial\ParcialCivil

# Inicializa un repositorio Git local
git init

# Añade todos los archivos al repositorio
git add .

# Crea un commit con tus cambios
git commit -m "Versión inicial de la aplicación"

# Conecta tu repositorio local con el repositorio remoto en GitHub
# Reemplaza YOUR_USERNAME con tu nombre de usuario de GitHub
git remote add origin https://github.com/YOUR_USERNAME/ParcialCivil.git

# Sube tus cambios a GitHub
git push -u origin main
```

### 4. Crear una cuenta en Streamlit Cloud

1. Ve a [Streamlit Cloud](https://streamlit.io/cloud)
2. Haz clic en "Sign up" o "Get started"
3. Puedes registrarte usando tu cuenta de GitHub

### 5. Desplegar la aplicación

1. Una vez que hayas iniciado sesión en Streamlit Cloud, haz clic en "New app"
2. Selecciona tu repositorio de GitHub (ParcialCivil)
3. En "Main file path", escribe "app.py"
4. Haz clic en "Deploy"

### 6. Obtener y compartir el link público

Una vez que la aplicación se haya desplegado correctamente:

1. Streamlit Cloud te proporcionará una URL pública (algo como https://parcialcivil.streamlit.app/)
2. Este es tu link público que puedes compartir con cualquier persona
3. Cualquier persona con este link podrá acceder a tu aplicación sin necesidad de instalar nada

### Notas importantes

- Cada vez que hagas cambios en tu código y los subas a GitHub, Streamlit Cloud actualizará automáticamente tu aplicación
- La URL de tu aplicación permanecerá igual, por lo que no necesitas compartir un nuevo link después de actualizar
- Streamlit Cloud ofrece un plan gratuito con ciertas limitaciones, pero es suficiente para la mayoría de los proyectos personales o académicos