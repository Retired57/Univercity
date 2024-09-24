# Домашнее задание по теме "Логирование"
# Задача "Логирование бегунов"

# --- class Runner и class Tournament взяты из ДЗ (с GitHub)
# =======================================================================================
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# first = Runner('Вася', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())

# =======================================================================================
# --- ниже идет мой код

import unittest
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            first = Runner("Вася", -10)
            for i in range(10):
                first.walk()
            self.assertEqual(first.distance, 100)
            logging.info("'test_walk' выполнен успешно")
        except ValueError:
            logging.warning(msg="'test_walk'. Неверная скорость для Runner", exc_info=True)
        except TypeError:
            logging.warning(msg="'test_walk'. Неверный тип данных для объекта Runner", exc_info=True)
        except AssertionError:
            logging.warning(msg=f"'test_walk'. Ошибка! Вместо 100 получили {first.distance}!", exc_info=True)

    def test_run(self):
        try:
            second = Runner(123, 5)
            for i in range(10):
                second.run()
            self.assertEqual(second.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except ValueError:
            logging.warning(msg="'test_run'. Неверная скорость для Runner", exc_info=True)
        except TypeError:
            logging.warning(msg="'test_run'. Неверный тип данных для объекта Runner", exc_info=True)
        except AssertionError:
            logging.warning(msg=f"'test_run'. Ошибка! Вместо 100 получили {second.distance}!", exc_info=True)

    def test_challenge(self):
        try:
            first = Runner("Вася", 10)
            second = Runner("Илья", 5)
            for i in range(10):
                first.run()
                second.run()
            self.assertNotEqual(first.distance, second.distance)
            logging.info("'test_challenge' выполнен успешно")
        except ValueError:
            logging.warning(msg="'test_challenge'. Неверная скорость для Runner", exc_info=True)
        except TypeError:
            logging.warning(msg="'test_challenge'. Неверный тип данных для объекта Runner", exc_info=True)
        except AssertionError:
            logging.warning(msg=f"'test_challenge'. Ошибка! Дистанции равны!"
                                f" {first.distance} = {second.distance} !", exc_info=True)


if __name__ == "__main__":
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                    format="%(asctime)s * %(levelname)s * %(message)s")
