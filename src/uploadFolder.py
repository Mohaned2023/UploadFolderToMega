from os import listdir 
from os.path import isfile

def upload( user , folder:str , folders_code:dict , counter:int , main_path:str , sp:str) :
    folder_spil:list = folder.split(f"{sp}")
    paths_list:list = listdir(folder)
    list_dir:list = []
    name = main_path.split(f"{sp}")
    name.remove(name[-1])
    name = folder.replace( f"{sp}".join(name) , "")
    print (f'mkdir \033[1;34m{name}\033[0m -> Mega.')

    if counter == 0 :
        folders_code = { folder : user.create_folder(folder_spil[-1])[folder_spil[-1]] }
        search_name = folder
    else :
        folder_name:str = folder_spil[-1]
        folder_spil.remove(folder_name)
        search_name:str = f"{sp}".join(folder_spil)
        code:str = folders_code[search_name]
        folders_code.update( { folder : user.create_folder( folder_name , code )[folder_name] } )

    for path in paths_list :
        path_name:str = f"{folder}{sp}{path}"
        if isfile(path_name) :
            print (f"Upload \033[0;32m{name}{sp}{path}\033[0m -> Mega.")
            user.upload(path_name,folders_code[folder])
        else :
            list_dir.append(path_name)
    else :
        return list_dir , folders_code


def main_upload(user , main_path:str , sp:str ) :
    counter:int = 0
    foleders_code:dict = {}
    foleders_list:list[str] = []
    folders_code_continer:dict = {}
    database_folders:list[str] = [ main_path ]

    while(True) :
        for folder in database_folders :
            if isfile(folder) :
                print ("Loding upload the file... ")
                user.upload(folder)
                database_folders.remove(folder)
            else :
                folders_list , folders_code_continer = upload(user , folder , foleders_code , counter , main_path , sp) 
                database_folders.remove(folder)
                # to add the new folders to the database_folders
                for item in folders_list :
                    database_folders.append(item) 
                # to update the folders_code
                foleders_code.update(folders_code_continer)
                counter += 1
        else :
            if len(database_folders) == 0 :
                print ("The upload is doen :)")
                break