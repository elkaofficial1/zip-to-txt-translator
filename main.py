import zipfile
import os

def extract_text_from_zip(zip_file_path, output_txt_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        
        with open(output_txt_path, 'w', encoding='utf-8') as output_file:
            if not file_list:
                print("ZIP-файл пуст.")
                return
            
            for file_name in file_list:
                print(f"Обрабатываем файл: {file_name}")  # Отладочная информация
                try:
                    with zip_ref.open(file_name) as file:
                        content = file.read().decode('utf-8', errors='replace')  # Обрабатываем ошибки кодировки
                        output_file.write(f"Содержимое файла '{file_name}':\n{content}\n\n")
                        print(f"Содержимое файла '{file_name}' добавлено в выходной файл.")  # Отладочная информация
                except Exception as e:
                    print(f"Ошибка при чтении файла '{file_name}': {e}")  # Сообщение об ошибке

if __name__ == "__main__":
    zip_file_path = input("Введите путь к zip-файлу: ")
    output_txt_path = input("Введите путь для сохранения выходного txt-файла: ")
    
    extract_text_from_zip(zip_file_path, output_txt_path)
    print(f"Процесс завершен. Проверьте файл: {output_txt_path}")
