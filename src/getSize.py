from os import walk
from os.path import getsize , join

def get_size( user ) -> float :
    info = user.get_storage_space(giga=True)
    return float( info["total"] )  -  float ( info["used"] )

def get_size_folder( folder_path:str ) -> float :
    total_size:float = 0
    for path , dirs , files in walk(folder_path) :
        for file_name in files :
            file_path = join(path,file_name) 
            total_size += getsize(file_path)
    else :
        return total_size / (1024 ** 3)