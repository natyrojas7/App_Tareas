import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestIndexHTML(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Cambia a tu driver preferido
        self.driver.get("http://localhost:5000/")  # Cambia la URL a la de tu aplicación

    def tearDown(self):
        self.driver.quit()

    def test_tareas_pendientes(self):
        # Verifica que solo se muestren tareas pendientes en la lista de tareas pendientes
        tareas_pendientes = self.driver.find_elements_by_xpath("//ul[@id='tareas_pendientes']/li")
        for tarea in tareas_pendientes:
            self.assertEqual(tarea.find_element_by_xpath("strong[text()='Estado:']").text, "Estado: pendiente")

    def test_agregar_tarea(self):
        # Simula agregar una nueva tarea y verifica que aparezca en la lista de tareas pendientes
        tarea_input = self.driver.find_element_by_id("tarea")
        tarea_input.send_keys("Nueva tarea")
        estado_select = self.driver.find_element_by_id("estado")
        estado_select.send_keys(Keys.DOWN)  # Selecciona "pendiente"
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        nueva_tarea = self.driver.find_element_by_xpath("//ul[@id='tareas_pendientes']/li[last()]")
        self.assertEqual(nueva_tarea.find_element_by_xpath("strong[text()='Tarea:']").text, "Tarea: Nueva tarea")
        self.assertEqual(nueva_tarea.find_element_by_xpath("strong[text()='Estado:']").text, "Estado: pendiente")

if __name__ == '__main__':
    unittest.main()
