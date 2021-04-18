import unittest
from advert import *


class MyTestCase(unittest.TestCase):
    full_description_json = """{
        "title": "Acer Aspire 7", 
        "price": 98560,
        "class": "laptop",
        "available": {
            "location": "DNS Москва 'ТЦ У Речного'",
            "address": "ул. Фестивальная, дом 13 корпус 1",
            "metro_stations": [["Речной вокзал", "70m"], ["Беломорская", "800m"]],
            "count": 15
        }
    }"""

    small_description_json = """{
        "title": "P250mkLfшkrbshtRlapAraTRRRRRRAAAA TA TA TAA",
        "author": "Marmok",
        "source": "https://www.youtube.com/c/MrMarmok",
        "video": "https://youtu.be/_FsYg53CbLA?t=126"
    }"""

    def test_title_in_full_description(self):
        answer_test = json_to_object(json.loads(self.full_description_json), Advert)
        self.assertEqual("Acer Aspire 7", answer_test.title)

    def test_repr_in_full_description(self):
        answer_test = json_to_object(json.loads(self.full_description_json), Advert)
        self.assertEqual("\033[1;33;40mAcer Aspire 7 | 98560 ₽\033[0;1;1m", str(answer_test))
        self.assertIn("Acer Aspire 7 | 98560 ₽", str(answer_test))

    def test_class_in_full_description(self):
        answer_test = json_to_object(json.loads(self.full_description_json), Advert)
        self.assertEqual("laptop", answer_test.class_)

    def test_param_available_in_full_description(self):
        answer_test = json_to_object(json.loads(self.full_description_json), Advert)
        self.assertEqual("DNS Москва 'ТЦ У Речного'", answer_test.available.location)
        self.assertIn("дом 13", answer_test.available.address)
        self.assertEqual(15, answer_test.available.count)

    def test_price_in_small_description(self):
        answer_test = json_to_object(json.loads(self.small_description_json), Advert)
        self.assertEqual(0, answer_test.price)

    def test_negative_price(self):
        input_json = """{
            "title": "test_product",
            "price": -106
        }"""
        with self.assertRaises(ValueError):
            json_to_object(json.loads(input_json), Advert)


if __name__ == '__main__':
    unittest.main()
