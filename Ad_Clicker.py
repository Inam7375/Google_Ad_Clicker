#!/usr/bin/env python
# coding: utf-8

# In[1]:


from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from tkinter import *
from tkinter import messagebox


#Configuring main window
mainWin = Tk()
mainWin.title("Ad Clicker")
mainWin.geometry("850x180")

mainFrame = Frame(mainWin)
mainFrame.pack()

#topFrame = Frame(mainFrame)
#topFrame.pack()


#bottomFrame = Frame(mainFrame)
#bottomFrame.pack()


#defining command for ad clicking
def clicking():
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.google.com/')
        sleep(0.5)
        search_input = driver.find_element_by_name('q')

        # let google find any linkedin user with keyword "python developer" and "San Francisco"
        keyWord = str(textBox.get("1.0",END))
        print(type(keyWord))
        if textBox.compare("end-1c", "!=", "1.0"):
            search_input.send_keys(keyWord)

            # grab all linkedin profiles from first page at Google
            profiles = driver.find_elements_by_xpath('//*[@id="vn1s0p1c0"]')
            profiles = [profile.get_attribute('href') for profile in profiles]

            # visit each profile in linkedin and grab detail we want to get
            for profile in profiles:
                driver.get(profile)
        else:
            messagebox.showwarning(title='Note!', message='Empty Message  box')        
    except:
        messagebox.showinfo(title='Note!', message='No ads found')
        
def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return("break")


#Widgets For entry
label = Label(mainFrame, text='Please enter the keyword here', font=("bold", 12, "italic"))
label.grid(row=0, column=0, padx=2)
label.config(font=("Courier", 12))


textBox = Text(mainFrame, height=5, width=50, font=("courier", 12))
textBox.bind("<Tab>", focus_next_window)
textBox.grid(row=0, column=1, pady=10)
#textBox.place(x=10, y=20)


button = Button(mainFrame, text='Go!', height=2, width=50, command=clicking)
button.bind("<Tab>", focus_next_window)
button.grid(row=1,  column=1, pady=2, sticky='EW')

mainWin.mainloop()


# In[ ]:





# In[ ]:




