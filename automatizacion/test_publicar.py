"""Pruebas de que post elige publicar.py. Sin red: python3 -m unittest test_publicar"""
import unittest
from datetime import datetime

from publicar import MADRID, elegir_pendiente

POSTS = [
    {"orden": 1, "id": "a", "fecha": "2026-10-07", "hora": "21:30"},
    {"orden": 2, "id": "b", "fecha": "2026-10-08", "hora": "21:30"},
    {"orden": 3, "id": "c", "fecha": "2026-10-09", "hora": "14:00"},
]


def a_las(texto):
    return datetime.strptime(texto, "%Y-%m-%d %H:%M").replace(tzinfo=MADRID)


class ElegirPendiente(unittest.TestCase):
    def test_antes_de_su_hora_no_publica(self):
        self.assertIsNone(elegir_pendiente(POSTS, {"a": {}}, a_las("2026-10-08 17:38")))

    def test_a_su_hora_publica_el_de_hoy(self):
        self.assertEqual(elegir_pendiente(POSTS, {"a": {}}, a_las("2026-10-08 21:30"))["id"], "b")

    def test_un_post_sin_ejecucion_en_su_franja_sale_al_dia_siguiente(self):
        # 8 oct: GitHub no corrio entre las 21:30 y medianoche; la siguiente ejecucion es el 9 a las 03:00
        self.assertEqual(elegir_pendiente(POSTS, {"a": {}}, a_las("2026-10-09 03:00"))["id"], "b")

    def test_varios_atrasados_salen_de_uno_en_uno_el_mas_antiguo_primero(self):
        self.assertEqual(elegir_pendiente(POSTS, {}, a_las("2026-10-09 15:00"))["id"], "a")

    def test_lo_ya_registrado_no_se_repite(self):
        self.assertIsNone(elegir_pendiente(POSTS, {"a": {}, "b": {}, "c": {}}, a_las("2026-10-10 12:00")))


if __name__ == "__main__":
    unittest.main()
