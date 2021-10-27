# Simple program to copy file from source location to destionation location.
import shutil



def cp_file(): # Function . Does not get called unless var y_n returns true with string "y" 

        print("Please enter file to copy from. Full path")
        frompath = r'' # Assigns first a storage box (variable) soo the input from console can get saved here.
        frompath = input() # Promts the user to input src file.

        print("please enter full destionation path")
        dest = r'' # Assigns first a storage box (variable) for the dst file to be saved.
        dest = input() # Promts the user to supply the full path

        shutil.copyfile(frompath, dest)



print("Do you want to copy files? select (Y/n)")

y_n = input() # Promts the user to input either y or n and store it in the y_n variable


if y_n == "y":  # If "y" returns true (bool) then execute function cp_file  
 cp_file()


print("cancelling...") 

