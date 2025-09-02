# Cómo Obtener un Link Público para tu Aplicación

Esta guía te explicará paso a paso cómo obtener un link público para compartir tu aplicación de Diseño de Estructuras de Concreto con cualquier persona.

## Método 1: Despliegue en Streamlit Cloud (Recomendado)

Streamlit Cloud es la forma más sencilla de obtener un link público para tu aplicación Streamlit.

### Paso 1: Crear una cuenta en GitHub

1. Ve a [GitHub](https://github.com/)
2. Haz clic en "Sign up" y sigue las instrucciones para crear una cuenta
3. Verifica tu dirección de correo electrónico

### Paso 2: Crear un repositorio en GitHub

1. Inicia sesión en tu cuenta de GitHub
2. Haz clic en el botón "+" en la esquina superior derecha y selecciona "New repository"
3. Nombra tu repositorio (por ejemplo, "ParcialCivil")
4. Deja el repositorio como público
5. Haz clic en "Create repository"

### Paso 3: Subir tu código al repositorio

Desde tu computadora, abre PowerShell o CMD y ejecuta:

```powershell
# Navega a la carpeta de tu proyecto
cd "c:\Users\57314\Desktop\Downloads\parcialParcial\ParcialCivil"

# Inicializa un repositorio Git local
git init

# Añade todos los archivos al repositorio
git add .

# Crea un commit con tus cambios
git commit -m "Versión inicial de la aplicación"

# Configura la rama principal como 'main'
git branch -M main

# Conecta tu repositorio local con el repositorio remoto en GitHub
# Reemplaza TU_USUARIO con tu nombre de usuario de GitHub
git remote add origin https://github.com/TU_USUARIO/ParcialCivil.git

# Sube tus cambios a GitHub
git push -u origin main
```

### Paso 4: Crear una cuenta en Streamlit Cloud

1. Ve a [Streamlit Cloud](https://streamlit.io/cloud)
2. Haz clic en "Sign up" o "Get started"
3. Regístrate usando tu cuenta de GitHub (recomendado)

### Paso 5: Desplegar la aplicación

1. Una vez que hayas iniciado sesión en Streamlit Cloud, haz clic en "New app"
2. Selecciona tu repositorio de GitHub (ParcialCivil)
3. En "Main file path", escribe "app.py"
4. Haz clic en "Deploy"

### Paso 6: Compartir el link público

Una vez que la aplicación se haya desplegado correctamente:

1. Streamlit Cloud te proporcionará una URL pública (algo como https://parcialcivil.streamlit.app/)
2. Este es tu link público que puedes compartir con cualquier persona
3. Cualquier persona con este link podrá acceder a tu aplicación sin necesidad de instalar nada

## Ventajas de usar Streamlit Cloud

- **Gratuito** para proyectos personales y académicos
- **Actualización automática** cada vez que subes cambios a GitHub
- **URL permanente** que no cambia con las actualizaciones
- **No requiere conocimientos de servidores** o infraestructura
- **Fácil de mantener** y actualizar

## Solución de problemas comunes

### Si tienes problemas con Git

1. Asegúrate de tener Git instalado en tu computadora. Puedes descargarlo desde [git-scm.com](https://git-scm.com/)
2. Si no estás familiarizado con Git, considera usar GitHub Desktop, una interfaz gráfica más amigable: [desktop.github.com](https://desktop.github.com/)

### Si la aplicación no se despliega correctamente

1. Verifica que todos los archivos necesarios estén en tu repositorio (app.py, requirements.txt)
2. Asegúrate de que requirements.txt contenga todas las dependencias necesarias
3. Revisa los logs de despliegue en Streamlit Cloud para identificar errores específicos

### Si necesitas ayuda adicional

1. Consulta la [documentación oficial de Streamlit](https://docs.streamlit.io/)
2. Visita el [foro de la comunidad de Streamlit](https://discuss.streamlit.io/)

---

¡Listo! Siguiendo estos pasos, tendrás un link público para compartir tu aplicación con cualquier persona en el mundo.