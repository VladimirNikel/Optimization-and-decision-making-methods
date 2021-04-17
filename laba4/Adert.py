import json
import keyword


class Advert:
    _price = 0

    def __setattr__(self, key, value):
        if keyword.iskeyword(key):
            key = key + "_key_"
        super.__setattr__(self, key, value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, var: int):
        if var < 0:
            raise ValueError("цена должна быть больше 0")
        self._price = var


def json_to_object(input_json: dict, unit_class: object) -> object:
    """Translation function from JSON to object.
    The input_json variable is required - str(JSON)
    unit_class variable - class description
    The return value is an object with the passed attributes in JSON"""
    new_object = unit_class()
    for left_value, right_value in input_json.items():
        if isinstance(right_value, (list, tuple)):
            new_object.__setattr__(left_value, [json_to_object(tmp, unit_class)
                                                if isinstance(tmp, dict)
                                                else tmp for tmp in right_value])
        else:
            new_object.__setattr__(left_value, json_to_object(right_value, unit_class)
                                   if isinstance(right_value, dict) else right_value)
    return new_object


if __name__ == "__main__":
    try:
        lesson_str = """{
            "title": "iPhone X", 
            "price": 100,
            "location": {
                "address": "город Самара, улица Мориса Тореза, 50",
                "metro_stations": ["Спортивная", "Гагаринская"]
            }
        }"""
        lesson = json.loads(lesson_str)
        print(lesson)
        temp_unit = json_to_object(lesson, Advert)
        print(temp_unit)
        print(temp_unit.title)
        print(temp_unit.location.address)
        print(temp_unit.location.metro_stations)
        print(temp_unit.price)
    except ValueError as err:
        print(f"Ошибочка вышла: {err}")
