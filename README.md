# Oshell 

<img width="1366" height="727" alt="image" src="https://github.com/user-attachments/assets/65f9d6ba-24c3-4311-ad33-018608d2e6cd" />


It is a custom shell made using python. I build it from scratch because i wanna learn how th shell actually works.It has variable management and tab-auto-completion and many custom commands. Its important to understand that its not for replacing powershell or cmd , It's just a fun learning project that 
actually works . Anyone can use it without any need of installing python , the user is just need to double click on .exe .


## THEME
No Internet because its a terminal project and can run without any internet>>>>>>>>>>>>>






## Features
1. exit : It is used to exit from the shell. 
2. cls : It is used to clear the shell
3. gpd : Full form of gpd is "go to previous directory". As its name suggests , it is used to go on previos directory at which user was
4. gd : Full form of gd is "go to directory". As its name suggests, it is used to go to  directory which user types just after it. 
5. pwd : Full form of pwd is "print working directory", its function is same as its name.
6. cat : It is used to view the content of a file. To view content of any file just type cat followed by the name of file.
7. declare : It is used to declare shell variables. To declare any variable just type declare followed by variable name and then by its value. Example :
```
    oshell> declare name Atharv
    declared!!
```
8. home : If you type home in oshell , it will redirect you to your home directory. 
9. history : As the command itself suggests , it is used to view the history of shell and to get any number of last commands of and jujus isutotory followed by that number.For Example if you have used two commands and then use history , its output will be :
```
oshell> history
      1  previous_command_1
      2  previous_command_2
      3  history
```
10. -p : It is used to print shell variables. to do it type -p followed by name of variable that you want to print type :
  ```
   oshell> declare name Atharv 
   oshell> -p name 
   name : Atharv
```
10. -d : It is used to delete shell variables. to do it type -p followed by name of variable that you want to delete Example :
```
   oshell> declare name Atharv
   declared!! oshell
   -d name
   name is deleted
 ```
  
    
12. copy : It is used to copy (print) whawhatevere user type next to it  Example:
   ```
oshell> copy Atharv
Atharv
```
13. Is : It is used to find that something is or is not present in the directory. It will find whatever typed next to it. It can find buitin commands and any file. If it finds that file , it will prints its path. Example:
 ```
 oshell> Is Is
 Is is a builtin command
```
14. Auto-completion : If you press tab it will auto complete uiltin commands that are you typing
 ```
oshell>ex<TAB>
oshell>exit 
```


15. help : it is used to show all available commands 

16. random : it is used to generate a random number between any 2 given numbers

17. save : it is used to save a directory for future, so  everytime you don't need to search for fravraite directory

18. add : it is used to add 2 or more numbers for example this is used to add 1+2+3+4

 ```
add 1 2 3  4 
```

19. mul : it is used to multiply as much number as you want for example if you need to multiply 45*98*85

 ```
mul 45 98 85 
```
20. min : it used to give the lowest value between given numbers
21. max : it is used to give highest value between given numbers
22. variables :  it is used to print/show all assigened variables in shell 

## How to run 
Just download a main.exe from here and double click to run and its ready to use. If you want to run it from source code , then run these commands in your terminal (make sure you have Python 3.x is installed in your device)

1. git clone https://github.com/Atharv-Shukla-987/Oshell.git
2. cd Oshell
3. python main.py
   Now enjoy using Oshell commands !!!!!

## Future Plans

1. adding relative paths
2. auto Filename Completion
3. adding Background Jobs
4. adding some logic between the braces.
   
## Contributing

Contributions are welcome! Feel free to contribute  love helps but never get any lol. Use the following steps

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Push and open a Pull Request


## License
this is free to be used by anyone
