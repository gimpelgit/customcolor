import unittest

from customcolor.runner import ColorTestRunner


class MyTest(unittest.TestCase):
	def test_fail(self):
		"""Описание теста, что он делает"""
		self.assertEqual(1, 2)


	def test_ok(self):
		self.assertEqual(2, 2)


	def test_error(self):
		raise ValueError("Неизвестная ошибка")


	@unittest.skip("Пропускаем этот тест, так как он еще не готов")
	def test_skip(self):
		self.assertEqual(1, 1)


	@unittest.expectedFailure
	def test_expected_failure(self):
		self.assertEqual(1, 0)


	@unittest.expectedFailure
	def test_unexpected_success1(self):
		self.assertEqual(1, 1)


	@unittest.expectedFailure
	def test_unexpected_success2(self):
		self.assertEqual(2, 2)


if __name__ == "__main__":
	unittest.main(testRunner=ColorTestRunner(verbosity=2))