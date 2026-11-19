# Portal Web de Noticias - CANACO

**Autor:** José Alberto Rodríguez Gerónimo  
**Materia:** Tópicos de Desarrollo de Aplicaciones  
**Maestro:** Lic. José Manuel Gómez Zea  

---

## Descripción del Proyecto
Aplicación web completa desarrollada en **Django 4.2** para la gestión y publicación de noticias y contenido informativo. El sistema cuenta con una interfaz pública dinámica, un sistema de autenticación con roles, moderación de comentarios y un panel administrativo (CRUD) completo.

La interfaz fue rediseñada con un estilo moderno en tonos **azul cielo (`#38bdf8`)**, tarjetas con sombras suaves y bordes redondeados, preparada para su despliegue en producción mediante **Microsoft Azure App Service**.

---

## Tecnologías Utilizadas
* **Backend:** Python 3.12, Django 4.2
* **Frontend:** HTML5, CSS3 (estilos personalizados), Bootstrap 5, Bootstrap Icons, Quill.js (editor de texto enriquecido para publicaciones)
* **Base de Datos:** SQLite (`db.sqlite3`) para despliegue rápido en la nube (con soporte configurable para MySQL / WampServer64)
* **Producción y Despliegue:** Gunicorn, WhiteNoise (gestión de archivos estáticos), GitHub Actions y Microsoft Azure App Service (Linux)

---

## Funcionalidades Principales

### 1. Zona Pública
* **Inicio Dinámico (`/`):** Carrusel superior (*slider*) y sección de noticias recientes cargadas automáticamente desde la base de datos (solo publicaciones en estado *Publicado*).
* **Filtro por Categorías (`/categoria/`):** Listado general de noticias con selector desplegable para filtrar por categoría específica.
* **Detalle de Noticia (`/noticia/<id>/`):** Muestra portada, resumen, contenido enriquecido, galería de imágenes, contador automático de visitas, barra lateral con otras noticias y sección de comentarios aprobados.
* **Contexto Global:** Uso de *Context Processors* (`context_processors.py`) para mostrar las categorías y las 3 entradas más recientes en el pie de página (*footer*) de todo el sitio.

### 2. Autenticación y Perfil de Usuario
* Registro de nuevos usuarios (`sign_up`), inicio de sesión (`login`) y cierre de sesión (`logout`).
* Creación automática de perfiles extendidos (apellidos y foto de perfil).
* Gestión de perfil propio (`/perfil/` y `/crud_perfil/`) con subida y reemplazo de foto de perfil, y cambio de contraseña (`/crud_cambiar_contrasena/`).

### 3. Panel de Administración / Operador
Rutas protegidas mediante decoradores personalizados (`@login_required` y `@operador_required` para usuarios con permisos de *staff* activos):
* **CRUD de Noticias:** Crear, editar, eliminar y alternar estado (*Borrador* / *Publicado*), con soporte para imagen de portada, galería múltiple y editor Quill.
* **CRUD de Categorías:** Alta, edición y eliminación de categorías.
* **Moderación de Comentarios:** Panel para aprobar, bloquear o eliminar los comentarios enviados por los usuarios antes de que sean visibles públicamente.
* **Gestión de Usuarios:** Creación, edición, asignación de roles (*Colaborador*, *Editor*, *Administrador*), bloqueo/desbloqueo y eliminación de cuentas.

---

## Estructura del Proyecto
```text
canaco/
├── canaco/                  # Configuración principal del proyecto
│   ├── settings.py          # Configuración de BD, WhiteNoise, CSRF y Context Processors
│   └── urls.py              # Enrutamiento raíz
├── home/                    # Aplicación principal
│   ├── context_processors.py # Variables globales (categorías y noticias recientes)
│   ├── models.py            # Modelos: Perfil, Archivo, Categoria, Publicacion, GaleriaPublicacion, Comentario
│   ├── urls.py              # Rutas públicas y de los módulos CRUD
│   ├── views.py             # Lógica de negocio y vistas protegidas
│   └── templates/           # Plantillas HTML (partials y vistas de home)
├── static/                  # Archivos estáticos (CSS, JS, fuentes, imágenes base)
├── media/                   # Archivos subidos por los usuarios (portadas, galerías, fotos de perfil)
├── db.sqlite3               # Base de datos SQLite
├── manage.py                # Utilidad de administración de Django
└── requirements.txt         # Dependencias del proyecto
