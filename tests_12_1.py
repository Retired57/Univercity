# Домашнее задание по теме "Простые Юнит-Тесты"
# Задача "Проверка на выносливость"

import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.person_1 = runner.Runner("Panda")
        for i in range(10):
            self.person_1.walk()
        try:
            self.assertEqual(self.person_1.distance, 50)
        except AssertionError:
            print(f"Ошибка! Вместо 50 получили {self.person_1.distance}!")

    def test_run(self):
        self.person_2 = runner.Runner("Rabbit")
        for i in range(10):
            self.person_2.run()
        try:
            self.assertEqual(self.person_2.distance, 100)
        except AssertionError:
            print(f"Ошибка! Вместо 100 получили {self.person_2.distance}!")

    def test_challenge(self):
        self.person_1 = runner.Runner("Panda")
        self.person_2 = runner.Runner("Rabbit")
        for i in range(10):
            self.person_1.walk()
            self.person_2.run()
        try:
            self.assertNotEqual(self.person_1.distance, self.person_2.distance)
        except AssertionError:
            print(f"Ошибка! Дистанции равны! {self.person_1.distance} = {self.person_2.distance} !")


if __name__ == "__main__":
    unittest.main()
