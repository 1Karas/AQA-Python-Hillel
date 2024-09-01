import xml.etree.ElementTree as ET
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def find_incoming_value(group_number, xml_file):
    try:
        # Загрузка и парсинг XML файла
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Поиск группы по номеру
        for group in root.findall('group'):
            number = group.find('number').text
            if number == str(group_number):
                # Поиск и возврат значения timingExbytes/incoming
                incoming_value = group.find('timingExbytes/incoming').text
                logging.info(f"Для группы с номером {group_number}, значение timingExbytes/incoming: {incoming_value}")
                return incoming_value

        logging.info(f"Группа с номером {group_number} не найдена.")
        return None

    except ET.ParseError as e:
        logging.error(f"Ошибка парсинга XML: {e}")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")


# Пример использования
xml_file_path = 'groups.xml'  # Укажите путь к вашему XML-файлу
group_number_to_search = 5  # Укажите номер группы для поиска
find_incoming_value(group_number_to_search, xml_file_path)
