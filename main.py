# importing kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#others
import random

#Label
lbl = Label(text="start now")

#random choice

def newnum(event):
    global ran
    ran = random.randint(int(1),int(10))
    print(ran)




#textarea
text = TextInput()

#button function
# check if the user has typed the correct number
def function(event):
    if ran == int(text.text):
        lbl.text = "Correct"
        print("yes")

    else:
        lbl.text = "Wrong"
        print("nah")



#buttons

btn = Button(text="submit")
btn2 = Button(text="make a new number")

#binding the buttons to a functions
btn.bind(on_press = function)
btn2.bind(on_press = newnum)



class Numguess(App):
    def build(self):
        #add the sccreen
        screen =  Screen()
        box = BoxLayout(orientation="vertical")
        # add the box layout
        screen.add_widget(box)
        # add textarea to box layout 
        box.add_widget(text)
        # add button1 to box layout
        box.add_widget(btn)
        # button2 to boxlayout
        box.add_widget(btn2)
        #add label to boxlayout
        box.add_widget(lbl)
        return screen


#run the app
Numguess().run()
