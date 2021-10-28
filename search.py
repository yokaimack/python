from tkinter import *
import webbrowser
import time
root = Tk()

#WINDOW
root.resizable(FALSE, FALSE)
root.geometry("400x300")


#SET RADIOBUTTON // VARIABLE

r = IntVar()
r.set('1')



#FUNCTION

def search():
    #Function Delay
      time.sleep(1)  
      webbrowser.open('https://www.google.com/')
      print("wait")
  

def search1():
      time.sleep(1)  
      webbrowser.open('https://www.youtube.com/')

def search2():
      time.sleep(1)  
      webbrowser.open('https://gmail.com/')
      
def search3():
      time.sleep(1)  
      webbrowser.open('https://jovempan.com.br/')

#RADIOBUTTON

Radiobutton(root, text="Google",value=1, variable=r, command=search).pack()
Radiobutton(root, text="Youtube",value=2, variable=r,command=search1).pack()
Radiobutton(root, text="Gmail",value=3, variable=r,command=search2).pack()
Radiobutton(root, text="News",value=4, variable=r,command=search3).pack()

root.mainloop()