# Домашнее задание по теме "Систематизация и пропуск тестов".
# Задача "Заморозка кейсов"

import runner
import unittest
import runner_and_tournament as rt


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "!!!")
    def test_walk(self):
        self.person_1 = runner.Runner("Panda")
        for i in range(10):
            self.person_1.walk()
        try:
            self.assertEqual(self.person_1.distance, 50)
        except AssertionError:
            print(f"Ошибка! Вместо 50 получили {self.person_1.distance}!")

    @unittest.skipIf(is_frozen, "!!!")
    def test_run(self):
        self.person_2 = runner.Runner("Rabbit")
        for i in range(10):
            self.person_2.run()
        try:
            self.assertEqual(self.person_2.distance, 100)
        except AssertionError:
            print(f"Ошибка! Вместо 100 получили {self.person_2.distance}!")

    @unittest.skipIf(is_frozen, "!!!")
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


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):  # инициализация бегунов для тестирования
        self.runner_1 = rt.Runner("Усейн", 10)  # бегун 1
        self.runner_2 = rt.Runner("Андрей", 9)  # бегун 2
        self.runner_3 = rt.Runner("Ник", 3)  # бегун 3

    @classmethod
    def setUpClass(cls):  # начало тестирования
        cls.all_results = {}
        return super().setUpClass()

    def tearDown(self):
        for i in range(1, len(self.results) + 1):
            if isinstance(self.results[i], rt.Runner):
                self.results[i] = self.results[i].name

    @classmethod
    def tearDownClass(self):  # окончание тестирования
        for i in range(1, len(self.all_results) + 1):
            print(self.all_results[i])

    def assist_test(self, tr):  # вспомогательный метод, чтобы не повторяться
        self.tr = tr
        self.results = self.tr.start()
        try:
            self.assertTrue(self.runner_3.__eq__(self.results[len(self.results)]))
        except AssertionError:
            print(f"Неожиданная победа бегуна {self.results[len(self.results)]}!")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tour_1(self):  # первый забег
        self.assist_test(rt.Tournament(90, self.runner_1, self.runner_3))
        self.all_results[len(self.all_results) + 1] = self.results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tour_2(self):  # второй забег
        self.assist_test(rt.Tournament(90, self.runner_2, self.runner_3))
        self.all_results[len(self.all_results) + 1] = self.results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tour_3(self):  # третий забег
        self.assist_test(rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3))
        self.all_results[len(self.all_results) + 1] = self.results


if __name__ == "__main__":
    unittest.main()
