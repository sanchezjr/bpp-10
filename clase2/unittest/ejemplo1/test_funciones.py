import unittest
import funciones

'''
.assertEqual(a, b): Verifica la igualdad de ambos valores.
.assertTrue(x): Verifica que el valor es True.
.assertFalse(x): Verifica que el valor es False.
.assertIs(a, b): Verifica que ambas variables son la misma (ver operador is).
.assertIsNone(x): Verifica que el valor es None.
.assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in).
.assertIsInstance(a, b): Verifica que a es una instancia de b
.assertRaises(x): Verifica que se lanza una excepción.

'''


class TestFunciones(unittest.TestCase):
    
    
    def setUp(self):
        print('setUp')


    def tearDown(self):
        print('tearDown\n')
    
    def test_suma(self):
        print("Comenzando suma")
        self.assertEqual(funciones.add(10,20),30)
        self.assertEqual(funciones.add(10,10),30)
        self.assertEqual(funciones.add(10,2),12)
        self.assertEqual(funciones.add(10,22),32)


    def test_subtract(self):
        print("Comenzando resta")
        
        self.assertEqual(funciones.subtract(10, 5), 5)
        self.assertEqual(funciones.subtract(-1, 1), -2)
        self.assertEqual(funciones.subtract(-1, -1), 0)

    def test_multiply(self):
        print("Comenzando multi")

        self.assertEqual(funciones.multiply(10, 5), 55)
        self.assertEqual(funciones.multiply(-1, 1), -1)
        self.assertEqual(funciones.multiply(-1, -1), 1)

    def test_divide(self):
        print("Comenzando división")

        self.assertEqual(funciones.divide(10, 5), 2)
        self.assertEqual(funciones.divide(-1, 1), -1)
        self.assertEqual(funciones.divide(-1, -1), 1)
        self.assertEqual(funciones.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            funciones.divide(10, 0)