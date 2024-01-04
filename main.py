# Writen by Mohaned Sherhan.

from src.getSize import get_size , get_size_folder
from src.uploadFolder import main_upload
from argparse import ArgumentParser
from os.path import isfile,getsize
from src.usage import usage
from os import name,system
from mega import Mega


def main( email:str , password:str , folder_path:str ) :
    try :
        sp:str = "" 
        if name == "nt" :
            sp = "\\"
        else : 
            sp = "/"
        user = Mega().login( email , password )
        account_size:float = get_size(user)
        folder_size:float 
        if not isfile(folder_path) :
            folder_size = get_size_folder(folder_path)
        else :
            folder_size = getsize(folder_path)/(1024 ** 3)
        print ( f"You'r empty space in the account : {account_size}GB" )
        print ( f"Your folder or file have the size : {folder_size}GB" )
        if account_size <= folder_size :
            print ("ERROR : A large size..! ")
        else :
            main_upload( user, folder_path , sp )
    except Exception as error :
        print( f"ERROR : {error}" )

if __name__ == "__main__" :
    preser = ArgumentParser()
    preser.usage = usage()
    preser.add_argument('-E','--email',help="Set the email for mega **require!",type=str)
    preser.add_argument('-P','--password',help="Set the password for the account **require!" ,type=str)
    preser.add_argument('-p','--folder-path',help="Set the folder path **require!",type=str)
    arge = preser.parse_args()
    if arge.email and arge.password and arge.folder_path :
        main(arge.email , arge.password , arge.folder_path )
    else :
        system("python main.py --help")