def read_ini_file(file_path='./needed_for_decryption.ini'):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split('=')
                if key.strip() == 'state':
                    return int(value.strip())
    except FileNotFoundError:
        print('New file will be created..')
        return None
    except Exception as e:
        print("Error occurred while reading the file:", e)

    return None

def write_ini_file(file_path='./needed_for_decryption.ini', count=None):
    try:
        with open(file_path, 'w') as file:
            file.write(f'state={count}\n')
    except Exception as e:
        print("Error occurred while writing to the file:", e)

def setState():
    file_path='./needed_for_decryption.ini'
    count = read_ini_file()
    if count is not None:
        if count == 1:
            print("Count is alredy 1. nothing done...")
        else:
            print(f"Count is {count}.")
            print("reseted count to 1 in state.ini")
            write_ini_file(file_path, 1)
            print("done.")
    else:
        print("setting count to 1 in state.ini...")
        write_ini_file(file_path, 1)
        print("done.")
