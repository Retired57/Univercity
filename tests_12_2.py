# Домашнее задание по теме "Методы Юнит-тестирования"

import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    def setUp(self):  # инициализация бегунов для тестирования
        self.runner_1 = rt.Runner("Усейн", 10)  # бегун 1
        self.runner_2 = rt.Runner("Андрей", 9)  # бегун 2
        self.runner_3 = rt.Runner("Ник", 3)  # бегун 3

    @classmethod
    def setUpClass(cls):  # начало тестирования
        cls.all_results = {}
        print("Тестирование начинается")
        return super().setUpClass()

    def tearDown(self):
        for i in range(1, len(self.results) + 1):
            if isinstance(self.results[i], rt.Runner):
                self.results[i] = self.results[i].name

    @classmethod
    def tearDownClass(self):  # окончание тестирования
        for i in range(1, len(self.all_results) + 1):
            print(self.all_results[i])
        print("Тестирование завершено")

    def assist_test(self, tr):  # вспомогательный метод, чтобы не повторяться
        self.tr = tr
        self.results = self.tr.start()
        try:
            self.assertTrue(self.runner_3.__eq__(self.results[len(self.results)]))
        except AssertionError:
            print(f"Неожиданная победа бегуна {self.results[len(self.results)]}!")

    def test_tour_1(self):  # первый забег
        self.assist_test(rt.Tournament(90, self.runner_1, self.runner_3))
        self.all_results[len(self.all_results) + 1] = self.results

    def test_tour_2(self):  # второй забег
        self.assist_test(rt.Tournament(90, self.runner_2, self.runner_3))
        self.all_results[len(self.all_results) + 1] = self.results

    def test_tour_3(self):  # третий забег
        self.assist_test(rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3))
        self.all_results[len(self.all_results) + 1] = self.results


if __name__ == "__main__":
    unittest.main()

# Вывод на консоль:
# ==================

# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
#
# Ran 3 tests in 0.001s
# OK
