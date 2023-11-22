def get_keys():
    with open("validkeys.txt",'r') as file:
        return file.read().split(";")
def check_key(key:str):
    if key in get_keys():
        return True
    else:
        return False
