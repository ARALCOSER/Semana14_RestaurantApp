class Producto:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    @staticmethod
    def validar_texto(valor, campo):
        # Reutiliza una validacion basica para datos obligatorios.
        if not valor or not str(valor).strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")
        return str(valor).strip()

    @staticmethod
    def validar_precio(valor):
        # Valida que el precio sea un numero valido y no sea negativo.
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un numero valido.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        return precio

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = self.validar_texto(valor, "codigo")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        self._categoria = self.validar_texto(valor, "categoria")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = self.validar_precio(valor)


