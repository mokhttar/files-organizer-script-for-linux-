# I created this script to sort files auto based on the extention of the files
# i know i can simplify it using all the functions of os library
# but  i did create it for me im using linux so i did use linux commands for it using subproces
#(bash script better >>>> idk why i did choose python for this)
#thanks for reading the shit 
import subprocess
import os 
import sys

#function to get the os 
def get_Platform():
     platform = sys.platform
     if platform == "linux" or  platform == "linux2":
         return "linux"
     else:
         return f"{platform},the script wont work on it it only working with linux sorry!!"


#function to run linux commands(latrr i will update it to windows too ) 
#args === > list[arg1,arg2,...]
def run_command(command,args=None):
     if args is None:
         return subprocess.run([command], shell=True, capture_output=True, text=True).stdout.splitlines()
     else:
        return subprocess.run(f"{command} {args}", shell=True, capture_output=True, text=True).stdout.splitlines()   
    
    

def main():
  print(f"The script is running on {get_Platform() }")  
  dir=input(f"Please provide the path to your directory. If not specified, the script's current directory will be used by default\n")
  if dir == "":
    dir=os.getcwd()
  os.chdir(dir)  
  print(f"{dir}")
  items = run_command("ls")
  files=[]
  dirs=[]
  for item in items:
      if os.path.isfile(item):
       files.append(item)
      else:
         dirs.append(item)  
  for file in files:        
   # Handle files with no extension
   if '.' not in file:
       continue
   #split the shit and get the extention after spliting we get name,ext ==[-1] give us the ext
   ext = file.split('.')[-1]
   if ext not in dirs:
       #create dirs based on extention of the files so we can categories the shit 
       run_command("mkdir",ext)
       dirs.append(ext)
       #mv the shity files into the correspending dir 
   run_command("mv", f"'{file}' '{ext}/'")
      
       
if  __name__  == "__main__":
 main()