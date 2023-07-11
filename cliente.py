class Cliente:
    def __init__(self, rut, nombre, direccion, telefono, email, visible):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.visible = visible
    
    def toDBCollection(self):
        return {
            'rut': self.rut,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'email': self.email,
            'visible': self.visible
        }