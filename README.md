# 🍽️ Restaurante App — Componentes y Contenedores con Tkinter

🌟 **Estudiante:** Ramiro Alcoser A.

## 📚 Tema

**Semana 14:** Componentes y contenedores en la aplicación **restaurante_app**, construida con **Tkinter**.

## 🎯 Objetivo de aprendizaje

Evolucionar el proyecto **restaurante_app** desarrollado en la Semana 13 **sin cambiar su arquitectura principal**. La aplicación conserva el inicio de sesión, los modelos, los servicios y la persistencia en JSON, pero ahora organiza mejor la interfaz mediante `Frame`, `LabelFrame`, formularios, tablas (`Treeview`) e iconos.

## 🔄 Evolución del programa

**ANTES (Semana 13)**
```
Usuario -> GUI simple -> Servicios -> Modelos -> JSON
```

**AHORA (Semana 14)**
```
Usuario -> GUI con menú lateral, formularios y tablas -> Eventos -> Servicios -> Modelos -> JSON
```

Esta versión mantiene el trabajo con **Producto** y **Usuario**. Las demás entidades y operaciones desarrolladas en semanas anteriores (Bebida, Cliente, Venta, índices de búsqueda, menú de consola, etc.) se seguirán recuperando e incorporando progresivamente en las próximas semanas.

## 🗂️ Estructura del proyecto

```text
restaurante_app/
├── assets/
│   ├── icons/
│   │   ├── home.png
│   │   ├── users.png
│   │   ├── products.png
│   │   ├── logout.png
│   │   ├── add.png
│   │   ├── edit.png
│   │   ├── delete.png
│   │   ├── search.png
│   │   └── clean.png
│   └── logo/
│       ├── logo.png
│       └── icono.png
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## 🧱 Capas del proyecto

- 🧩 `modelos/`: clases `Producto` y `Usuario`, con validaciones básicas mediante `property` para evitar objetos con datos obligatorios vacíos o precios inválidos.
- ⚙️ `servicios/`: `ArchivoServicio` (lectura/escritura JSON) y `RestauranteServicio` (lógica de negocio, validación de acceso y CRUD completo de productos).
- 💾 `datos/`: archivos JSON con la información persistente de productos y usuarios.
- 🖼️ `ui/`: vistas gráficas creadas con Tkinter (`LoginView` y `MainView`).
- 🎨 `assets/icons/`: iconos PNG usados por los botones. Si falta un icono, la aplicación sigue funcionando con texto (no es obligatorio para ejecutar el sistema).
- 🏷️ `assets/logo/`: identidad visual del sistema. `logo.png` se muestra en el login y `icono.png` se usa como icono de la ventana.
- 🚪 `main.py`: punto de entrada que inicializa los servicios, configura el icono de la ventana, muestra la primera vista y ejecuta la aplicación.

## 🖥️ Pantallas principales

- 🔐 **LoginView:** pantalla de inicio de sesión. Usa el logo del sistema, campos `Entry` para usuario y contraseña, y un botón con `command=` que solicita la validación a `RestauranteServicio`.
- 🏠 **Inicio:** panel de resumen con tarjetas que muestran cuántos usuarios y productos existen en los archivos JSON.
- 👤 **Usuarios:** pantalla de consulta. Muestra los usuarios registrados en una tabla (`Treeview`), sin operaciones CRUD, para mantener esta sección sencilla.
- 🍔 **Productos:** pantalla de gestión completa. Incluye formulario (`LabelFrame` + `grid()`), botones de acción y tabla (`Treeview`) para registrar, cargar, actualizar y eliminar productos.

## 🧩 Componentes Tkinter utilizados

- 🪟 `Tk`: crea la ventana principal de la aplicación.
- 🏷️ `Label`: muestra textos y títulos dentro de la interfaz.
- ⌨️ `Entry`: permite ingresar datos como usuario, contraseña y los campos del formulario de productos.
- 🔘 `ttk.Button`: ejecuta una acción cuando el usuario hace clic (navegación y operaciones CRUD).
- 📊 `ttk.Treeview`: presenta usuarios y productos en formato de tabla.
- 🧭 `ttk.Scrollbar`: barra de desplazamiento vertical para las tablas.
- 💬 `messagebox`: muestra mensajes emergentes de confirmación o error.
- 🎨 `ttk.Style`: define estilos reutilizables para botones y encabezados de tabla.

## 📦 Contenedores utilizados

- 🪟 `Tk`: ventana principal de la aplicación.
- 🧱 `Frame`: separa el menú lateral, el área de contenido, las tarjetas de resumen y la barra de estado.
- 🗂️ `LabelFrame`: agrupa visualmente el formulario de productos y las tablas de información.

## 📐 Uso de gestores de geometría

- La ventana principal usa `pack()` para separar el menú lateral y el contenido.
- El formulario de productos usa `grid()` para alinear etiquetas y campos de entrada.
- No se mezcla `pack()` y `grid()` dentro del mismo contenedor.

## ⚡ Concepto de evento

```
Usuario hace clic -> Button genera una acción -> command ejecuta un método
-> el método consulta/solicita al servicio -> la interfaz refresca el resultado
```

En el login, el botón usa `command=self.iniciar_sesion`. Ese método obtiene los datos escritos, valida campos vacíos y solicita a `RestauranteServicio` la verificación de credenciales. En productos, cada botón (`Registrar`, `Cargar por código`, `Actualizar`, `Eliminar`, `Limpiar`) ejecuta un método que delega la operación a `RestauranteServicio` y luego refresca la tabla.

## ✅ Funcionalidades implementadas

```
Inicio -> Login -> Validación -> Interfaz principal (menú lateral)
   -> Usuarios (consulta) | Productos (CRUD) -> Cerrar sesión -> Login
```

- 🔐 **Inicio de sesión:** formulario con usuario y contraseña, botón "Iniciar sesión" y mensajes de error visibles ante campos vacíos o credenciales incorrectas. La validación se solicita a `RestauranteServicio`; la vista no valida las credenciales por su cuenta.
- 🧭 **Menú lateral:** navegación entre **Inicio**, **Usuarios** y **Productos**, además del botón **Cerrar sesión**, con resaltado visual de la sección activa.
- 👤 **Usuarios:** lista los usuarios cargados desde `datos/usuarios.json` (identificador, nombre y usuario) en una tabla, solicitando la información a `RestauranteServicio.listar_usuarios()`.
- 🍔 **Productos:**
  - ➕ **Registrar:** crea un producto nuevo si el código no está repetido.
  - 🔍 **Cargar por código:** busca un producto por su código y llena el formulario.
  - ✏️ **Actualizar:** modifica nombre, categoría y precio de un producto existente.
  - 🗑️ **Eliminar:** borra un producto existente por código.
  - 🧹 **Limpiar:** vacía el formulario.
  
  Cada operación usa los métodos de `RestauranteServicio`, guarda los cambios en `datos/productos.json` y refresca la tabla automáticamente.
- 📊 **Barra de estado:** muestra en todo momento la cantidad de productos y usuarios cargados.
- 🚪 **Cerrar sesión:** regresa a la pantalla de login dentro de la misma ventana, sin crear una nueva instancia de `Tk`.

## 💾 Persistencia JSON

Los productos y usuarios se cargan desde archivos JSON locales (`datos/productos.json` y `datos/usuarios.json`) al iniciar la aplicación, a través de `ArchivoServicio`. Los cambios en productos (registrar, actualizar, eliminar) se guardan de inmediato en `datos/productos.json`.

La GUI **no** reemplaza los servicios ni los modelos. La interfaz solicita operaciones a `RestauranteServicio`, y el servicio trabaja con los modelos y los datos persistidos. Ninguna vista lee o escribe los archivos JSON de forma directa.

## 🖼️ Organización de iconos y logo

Los iconos deben guardarse como PNG dentro de `restaurante_app/assets/icons/` con estos nombres:

```text
home.png
users.png
products.png
logout.png
add.png
edit.png
delete.png
search.png
clean.png
```

El logo principal va en `restaurante_app/assets/logo/logo.png` y el icono de ventana en `restaurante_app/assets/logo/icono.png`. Si algún archivo no existe, la aplicación **sigue funcionando con texto**, gracias a la función auxiliar `cargar_icono()` que devuelve `None` cuando no encuentra el archivo. Las rutas usadas son relativas al proyecto, por lo que la carpeta puede moverse sin romper la carga de imágenes.

## 🛠️ Requisitos

- 🐍 Python 3.x
- 🪟 Tkinter disponible en la instalación de Python

No se requieren dependencias externas.

## ▶️ Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

En Windows, si el comando `python` no está disponible en la terminal, puede usarse:

```bash
py main.py
```

## 🔑 Credenciales de demostración

Usuario: `admin`
Contraseña: `1234`

También puede usarse:

Usuario: `caja1`
Contraseña: `abcd`

## ⚠️ Nota educativa sobre autenticación

La autenticación de este proyecto es local y simulada. Las contraseñas se guardan en JSON solo para fines pedagógicos. En una aplicación real, almacenar contraseñas de esta forma no sería apropiado ni seguro.

## 🚫 No se solicita (fuera del alcance de esta semana)

- Manejo avanzado de eventos con `bind()`.
- Doble clic, eventos de teclado o mouse.
- Edición directa dentro del `Treeview`.
- Bases de datos o autenticación real.

Eso queda reservado para una siguiente semana sobre eventos.

## 🚀 Próxima evolución

En las siguientes prácticas se recuperarán e incorporarán progresivamente a la interfaz gráfica las funcionalidades desarrolladas en la versión de consola (Bebida, Cliente, Venta, búsquedas por índice, ventas y consulta de categorías), construyendo sobre esta misma base de modelos, servicios, ui y main.py.
