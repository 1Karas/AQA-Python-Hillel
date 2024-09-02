import json

def valid_json(path_file):
    try:
        with open(path_file, 'r') as  file:
            json.load(file)
        return True
    except json.JSONDecodeError:
        return False

def check_result(path_file):
    result = {}
    for path_file in path_file:
        result[path_file] = valid_json(path_file)
    return result

path_file = ['localizations_en.json', 'localizations_ru.json', 'login.json', 'swagger.json']
result = check_result(path_file)

for file_path, is_valid in result.items():
    if is_valid:
        print(f"В файле {file_path} валидный JSON.")
    else:
        print(f" В файле {file_path} не валидный JSON.")