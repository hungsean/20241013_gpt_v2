# tests/test_main.py
import unittest
from unittest.mock import patch
from src.main import main


class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', return_value='exit')
    @patch('builtins.print')
    def test_main_exit(self, mock_print, mock_input):
        # 測試輸入 'exit' 時，main() 返回 1，且打印 'Exiting...'
        result = main()
        mock_input.assert_called_once_with("Enter a command: ")
        mock_print.assert_called_once_with("Exiting...")
        self.assertEqual(result, 1)

    @patch('builtins.input', return_value='hello')
    @patch('builtins.print')
    def test_main_command_received(self, mock_print, mock_input):
        # 測試非 'exit' 指令時，main() 返回 0，並打印對應指令
        result = main()
        mock_input.assert_called_once_with("Enter a command: ")
        mock_print.assert_called_once_with("Command received: hello")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
