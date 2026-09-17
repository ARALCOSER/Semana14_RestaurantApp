from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios = []
        self.productos = []
        self.cargar_datos()

    def cargar_datos(self):
        # Carga los datos persistidos y los convierte en objetos.
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        productos_json = self.archivo_servicio.leer_json("productos.json")

        self.usuarios = [
            Usuario(
                datos.get("identificador", ""),
                datos.get("nombre", ""),
                datos.get("usuario", ""),
                datos.get("contraseña", datos.get("contrasena", "")),
            )
            for datos in usuarios_json
        ]

        self.productos = [
            Producto(
                datos.get("codigo", ""),
                datos.get("nombre", ""),
                datos.get("categoria", ""),
                datos.get("precio", 0),
            )
            for datos in productos_json
        ]

    def validar_acceso(self, usuario, contrasena):
        # Verifica si las credenciales coinciden con un usuario cargado.
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado
        return None

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)

    def listar_usuarios(self):
        # Entrega los usuarios cargados para mostrarlos en la interfaz.
        return self.usuarios

    def listar_productos(self):
        # Entrega los productos cargados para mostrarlos en la interfaz.
        return self.productos

    def guardar_productos(self):
        datos = [
            {
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "categoria": producto.categoria,
                "precio": producto.precio,
            }
            for producto in self.productos
        ]
        self.archivo_servicio.escribir_json("productos.json", datos)

    def buscar_producto_por_codigo(self, codigo):
        codigo = codigo.strip()
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_producto(self, codigo, nombre, categoria, precio):
        nuevo_producto = Producto(codigo, nombre, categoria, precio)
        if self.buscar_producto_por_codigo(nuevo_producto.codigo) is not None:
            raise ValueError("Ya existe un producto con ese codigo.")
        self.productos.append(nuevo_producto)
        self.guardar_productos()
        return nuevo_producto

    def actualizar_producto(self, codigo, nombre, categoria, precio):
        producto_actual = self.buscar_producto_por_codigo(codigo)
        if producto_actual is None:
            raise ValueError("No existe un producto con ese codigo.")
        datos_validados = Producto(codigo, nombre, categoria, precio)
        producto_actual.nombre = datos_validados.nombre
        producto_actual.categoria = datos_validados.categoria
        producto_actual.precio = datos_validados.precio
        self.guardar_productos()
        return producto_actual

    def eliminar_producto(self, codigo):
        producto_actual = self.buscar_producto_por_codigo(codigo)
        if producto_actual is None:
            raise ValueError("No existe un producto con ese codigo.")
        self.productos.remove(producto_actual)
        self.guardar_productos()
        return producto_actual


