import unittest
from app import app

class TestApp(unittest.TestCase):
#####pruebas de las tareas para los metodos get y post de la app #######
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_post(self):
        # Prueba de envío de formulario POST a '/'
        response = self.app.post('/', data={'tarea': 'Hacer la compra', 'estado': 'pendiente'})
        self.assertEqual(response.status_code, 302) 

    def test_index_get(self):
        # Prueba de acceso a la página principal con método GET
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  

    def test_actualizar_estado(self):
        # Prueba de actualización de estado de una tarea
        registros = [{'tarea': 'Hacer la compra', 'estado': 'pendiente'}]
        app.registros = registros 
        response = self.app.post('/actualizar_estado/Hacer%20la%20compra', data={'estado': 'Completada'})
        self.assertEqual(response.status_code, 302)  

    def test_eliminar_tarea(self):
        # Prueba de eliminación de una tarea ##
        registros = [{'tarea': 'Hacer la compra', 'estado': 'pendiente'}]
        app.registros = registros 
        response = self.app.post('/eliminar_tarea/Hacer%20la%20compra')
        self.assertEqual(response.status_code, 302) 
if __name__ == '__main__':
    unittest.main()
