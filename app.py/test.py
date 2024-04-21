import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_post(self):
        # Prueba de envío de formulario POST a '/'
        response = self.app.post('/', data={'tarea': 'Hacer la compra', 'estado': 'pendiente'})
        self.assertEqual(response.status_code, 302)  # Se espera redireccionamiento después de guardar
        # Aquí puedes agregar más aserciones para verificar que la tarea se agregó correctamente

    def test_index_get(self):
        # Prueba de acceso a la página principal con método GET
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Se espera que la página se cargue correctamente
        # Aquí puedes agregar más aserciones para verificar que la página contiene los registros correctamente

    def test_actualizar_estado(self):
        # Prueba de actualización de estado de una tarea
        registros = [{'tarea': 'Hacer la compra', 'estado': 'pendiente'}]
        app.registros = registros  # Configura registros directamente en la aplicación
        response = self.app.post('/actualizar_estado/Hacer%20la%20compra', data={'estado': 'Completada'})
        self.assertEqual(response.status_code, 302)  # Se espera redireccionamiento después de actualizar
        # Aquí puedes agregar más aserciones para verificar que el estado se actualizó correctamente

    def test_eliminar_tarea(self):
        # Prueba de eliminación de una tarea
        registros = [{'tarea': 'Hacer la compra', 'estado': 'pendiente'}]
        app.registros = registros  # Configura registros directamente en la aplicación
        response = self.app.post('/eliminar_tarea/Hacer%20la%20compra')
        self.assertEqual(response.status_code, 302)  # Se espera redireccionamiento después de eliminar
        # Aquí puedes agregar más aserciones para verificar que la tarea se eliminó correctamente

if __name__ == '__main__':
    unittest.main()
