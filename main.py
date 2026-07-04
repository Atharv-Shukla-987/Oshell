import random
import sys ,subprocess ,os ,shlex,time
try:
    import readline
except ModuleNotFoundError:
    import pyreadline3 as readline
    
home = os.path.expanduser("~")
current_path = os.getcwd()
previous_path = os.getcwd()
valid_com = ['gd','gpd','history','exit','copy' ,'Is','home','pwd','declare','-d','-p']
variables = {}


def err(text):
   print(f"\033[91mError You are a dumb!!!\033[0m")
   print(f"\033[91mError {text}\033[0m")



def main():
    global current_path , previous_path 
    if sys.platform == 'win32':
       os.system('color')
    while True :
        com = input(f"{current_path}---==>").strip()
   
        if not com:
           continue
        words = com.split()
        main_com = words[0].lower()
        args = words[1:]
        
        try:
            words = shlex.split(com)
        except ValueError:
           continue
   
        
        if main_com == "exit":
           break
        
        elif main_com == "cls":
           os.system('cls' if os.name == 'nt' else 'clear')
        elif main_com == "gpd":
           if previous_path :
                current_path = previous_path
                os.chdir(current_path)
           else :
                err("Invaild path")
             
        elif main_com == "gd":
          print()
          if len(words) == 2 :
            target_path = words[1]
            if os.path.isdir(os.path.abspath(os.path.join(current_path,target_path))):
               previous_path = current_path
               current_path = os.path.abspath(os.path.join(current_path,target_path))
               os.chdir(current_path) 
            else:
               print(f"\033[91mError: Directory '{target_path}' not found \033[0m")
        elif main_com == 'home':
           current_path = home
           os.chdir(current_path)
        elif main_com == 'pwd' :
           print(os.getcwd())    
        elif main_com == 'cat' :
           if len(words) == 1:
              err("please enter filename")
           elif len(words) > 2 :
              err("filename can't have space")
           elif len(words) == 2:
              for filename in args :
                 try:
                    with open(filename , 'r' , encoding='utf-8') as file:
                       while chunk := file.read(4096):
                          print(chunk)
                 except FileNotFoundError:
                    err(f"{filename} : no such file or directory exists")
                 except IsADirectoryError:
                    err(f"{filename} : is a directory")
                 except PermissionError:
                    err(f"{filename} : permission denied")
                    
        elif main_com == 'declare':
           if len(words) == 1 :
              print("please enter name of variable then its value")
           if len(words) == 2 :
              print("please enter value of variable")
           if len(words) > 3:
              print("you can only write two words after declare , first is name of variable and second is value")  
           if len(words) == 3 :
              var = words[1]
              val = words[2] 
              if var in variables :
                 print("varible is alredy exits")
              else:
                 if var.isidentifier():
                    variables[var] = val
                    print("declared!!")
                 else:
                    print(f"\033[91mError: invaild identifier\033[0m")
        elif main_com == 'history':
           if len(words) == 1 :
              his_len = readline.get_current_history_length()
              for i in range(1,his_len+1):
                 cmd = readline.get_history_item(i)
                 if cmd:
                    print(f"{i:5} {cmd}")
           
           elif len(words) == 2 :
              try:
                 n = int(words[1])
                 his_len = readline.get_current_history_length()
                 if (n < his_len) :
                   for i in range(his_len-n + 1,his_len+1):
                     cmd = readline.get_history_item(i)
                     if cmd:
                        print(f"{i:5} {cmd}")
               
                     else:
                        err("number must be smaller than number of total commands")
                
              except ValueError:
                 err("plzz enter a number only after history")
                   
        elif main_com == '-p':
           if len(words) > 2 :
              print("The name of variable cant have space")
           elif len(words) == 1 :
              print("enter the name of variable")
           var = words[1]
           if var in variables :
                 val = variables[var]
                 print(var ," : ", val)
           else:
              print("no such variable exits")
      
        elif main_com == '-d':
           if len(words) > 2:
              print("the name of variable cant have space")
           elif len(words) == 1 :
              print("enter the name of variable")
           if var in variables :
              var = words[1]
              print(var , "is deleted!!!")
              del variables[var]
        elif com.startswith("copy "):
          print()
          print(com[5:])
        elif main_com == "help":
           print()
           print("gd : go to previous directory")
           print("gpd : go to previous directory")
           print("history : show command history")
           print("exit : exit the shell")
           print("copy : copy the text after copy command")
           print("Is : check if the command is a buildin command or not")
           print("home : go to home directory")
           print("pwd : show current working directory")
           print("declare : declare a variable with its value")
           print("-p : print the value of variable")
           print("-d : delete the variable")
           print("random : generate a random number between two numbers")
        elif main_com == 'random':
           n1 = int(words[1])
           n2 = int(words[2])
           res = random.randint(n1,n2)
           print(f'Result: {res}')
        elif com.startswith("Is "):
          user_input = com[3:]
          if user_input in valid_com :
             print()
             print(f'{user_input} is a buildin command' )
          else :
             print()
             paths = current_path.split(os.pathsep)
             found = False
             for i in paths:
                full_path = os.path.join(i,user_input)
                if os.path.isfile(full_path) and os.access(full_path,os.X_OK):
                   print(f'{user_input} is {full_path}')
                   found = True
                   break
            
             if not found :
                print(f'{user_input}: not found')
          print()
              
        else :
            print()
            try:
                subprocess.run(words)
            except FileNotFoundError:
                err(f"{main_com} :command not found")
            except Exception as e:
                err(f"executing command: {e}")
            print()

def auto_com(text , state):
    matches = [c for c in valid_com if c.startswith(text)]
    if not matches:
       err("")
       sys.stdout.flush()
       time.sleep(0.05)
       return None
    if state < len(matches):
       return matches[state]
    return None
   

readline.set_completer(auto_com)
readline.parse_and_bind("tab: complete")
        
if __name__ == "__main__":
    main()
