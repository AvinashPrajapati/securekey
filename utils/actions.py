from tinydb import TinyDB, Query
db = TinyDB('db.json', indent=4)
qry = Query()

from .enc_dec import encrypt_data, decrypt_data, generate_key

# db.truncate()

def insert_data(data:dict)->None:
    if data:
        db.insert(
            data
        )
    else:
        print('something went wrong...')

def encrypted_str(key:str, string_data:str)->str:
    encoded_str = string_data.encode('utf-8')
    encoded_key = key.encode('utf-8')
    enc_str = encrypt_data(key=encoded_key, data=encoded_str)
    return enc_str.hex()
def decrypted_str(key:str, string_data:str)->str:
    bytes_string = bytes.fromhex(string_data)
    encoded_key = key.encode('utf-8')
    # print(bytes_string)
    encoded_str = decrypt_data(key=encoded_key, encrypted_data=bytes_string)
    dec_str = encoded_str.decode('utf-8')
    return dec_str

def return_single_data(url:str):
    result = db.search(qry.url==url)
    return result

def all_data():
    return db.all()

def update_item(data:dict, item_id:str)->None:
    # print(data, url)
    db.update(data, doc_ids = [int(item_id)])
    # print("updated:", data_updated)

def delete_single(url:str)->None:
    # print(url)
    db.remove(qry.url==url)
    # print(deleted_data)
