from tkinter import *
root = Tk()

#control
def controller():
    print("Welcome to TU land")
    picklist = []
    detail = ["choose your Leader : ","choose your EducationArea : "
              ,"choose your Place : ","choose your Facility : ","choose your App1 : "
              ,"choose your App1 : "]
    maxorder = 6
    while len(picklist) < maxorder:
        for i in range(maxorder):
            item = input(detail[i]);
            picklist.append(item)
            
        
    print("That's your TU land")
    print(picklist)


#interface
def interface():
    root.title("TU land")
    root.geometry("200x100")
    app = Frame(root)
    app.grid()
    #ปุ่มกด
    button1 = Button(app, text = "เลือกผู้นำ")
    button1.grid()
    button2 = Button(app)
    button2.grid()
    button2.configure(text = "เลือกสถานที่")
    button3 = Button(app)
    button3.grid()
    button3["text"] = "เลือก Place"
    root.mainloop()

interface()

        
        
