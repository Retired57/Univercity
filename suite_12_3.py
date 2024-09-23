# Домашнее задание по теме "Систематизация и пропуск тестов".
# Задача "Заморозка кейсов"

import unittest
import tests_12_3

test_mod_12_3 = unittest.TestSuite()

test_mod_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_mod_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(test_mod_12_3)

