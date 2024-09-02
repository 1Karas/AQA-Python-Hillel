import pandas as pd

# Загрузка CSV файлов в DataFrame
test_df = pd.read_csv('r-m-c.csv')
next_df = pd.read_csv('rmc.csv')

# Конкатенация двух DataFrame для сравнения
combined_df = pd.concat([test_df, next_df])

# Удаление дубликатов и сохранение уникальных строк
unique_df = combined_df.drop_duplicates(keep=False)

# Сохранение уникальных строк в новый CSV файл
unique_df.to_csv('result_Karas.csv', index=False)

print("Уникальные строки сохранены в файл 'result_Karas.csv'.")