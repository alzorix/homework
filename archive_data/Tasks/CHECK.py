import os
import subprocess



def run_script(script_path):
    # Запуск скрипта и получение его вывода
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    return result.stdout, result.stderr



def get_files(directory_path):
    scripts = os.listdir(directory_path)
    return scripts


def transform_to_need_form(scripts_list:list,directory_path):
    scripts_list_good = list()
    for i in scripts_list:
        if i[-3::] == ".py":
            i = directory_path +"/" + i
            scripts_list_good.append(i)

    return scripts_list_good


if __name__ == "__main__":
    directory_path = input("Введите адрес папки с файлами:")

    scripts = transform_to_need_form(get_files(directory_path),directory_path)




    # # Список файлов скриптов, которые нужно запустить
    # scripts = ['4751.py', '5229.py']
    # #

    for script in scripts:
        stdout, stderr = run_script(script)
        print(f"{os.path.basename(script)}:{stdout}")

        if stderr:
            print(f"Errors of {script}:\n{stderr}")