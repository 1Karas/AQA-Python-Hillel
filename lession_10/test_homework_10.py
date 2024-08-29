import unittest
from unittest.mock import patch
import sys
import os
sys.path.append('/home/bardin/PycharmProjects/My project/AQA-Python-Hillel/lession_10')

from homework_10 import log_event


class TestLogEvent(unittest.TestCase):

    @patch('homework_10.logging.getLogger')  # Патчим getLogger
    def test_log_event_success(self, mock_get_logger):
        # Создаем mock для логгера
        mock_logger = mock_get_logger.return_value

        # Вызываем функцию с статусом 'success'
        log_event('test_user', 'success')

        # Проверяем, что info был вызван с правильным сообщением
        mock_logger.info.assert_called_once_with('Login event - Username: test_user, Status: success')

    @patch('homework_10.logging.getLogger')  # Патчим getLogger
    def test_log_event_expired(self, mock_get_logger):
        # Создаем mock для логгера
        mock_logger = mock_get_logger.return_value

        # Вызываем функцию с статусом 'expired'
        log_event('test_user', 'expired')

        # Проверяем, что warning был вызван с правильным сообщением
        mock_logger.warning.assert_called_once_with('Login event - Username: test_user, Status: expired')

    @patch('homework_10.logging.getLogger')  # Патчим getLogger
    def test_log_event_failed(self, mock_get_logger):
        # Создаем mock для логгера
        mock_logger = mock_get_logger.return_value

        # Вызываем функцию с любым другим статусом, например, 'failed'
        log_event('test_user', 'failed')

        # Проверяем, что error был вызван с правильным сообщением
        mock_logger.error.assert_called_once_with('Login event - Username: test_user, Status: failed')

if __name__ == "__main__":
    unittest.main()
