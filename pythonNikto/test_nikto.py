import subprocess
import unittest
import logging

logging.basicConfig(filename='test_nikto.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class TestNiktoOutput(unittest.TestCase):
    def test_nikto_output(self):
        try:
            result = subprocess.run(
                ['nikto', '-h', 'https://test-stand.gb.ru/', '-ssl', '-Tuning', '4'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )

            output = result.stdout + result.stderr
            logging.info("Вывод команды nikto:\n%s", output)
            assert "0 error(s)" in output, "Текст '0 error(s)' не найден в выводе команды nikto."
            logging.info("Тест пройден: текст '0 error(s)' найден в выводе команды nikto.")

        except FileNotFoundError:
            error_message = "Ошибка: программа nikto не найдена. Пожалуйста, установите её и добавьте в PATH."
            logging.error(error_message)
            assert False, error_message
        except subprocess.CalledProcessError as e:
            error_message = f"Команда nikto завершилась с ошибкой: {e}"
            logging.error(error_message)
            assert False, error_message
        except Exception as e:
            error_message = f"Произошла ошибка при выполнении команды nikto: {e}"
            logging.error(error_message)
            assert False, error_message


if __name__ == '__main__':
    unittest.main()
