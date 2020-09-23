from tkinter import *
from subprocess import call
import csv
import os
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from maincode import MyMain




class MyGUI():

    def __init__(self,root):

        
        root.title("Janes Web Scraper")
        #root.geometry("1680x1380")
        root.state('zoomed')
        root.config(bg="lightblue")
        root.resizable(1,1)
        

        top_frame = Frame(root, width=1200, height=200, bg='lightblue')
        top_frame.place(x=0, y=0)

        bottom_frame = Frame(root, width=150, height=400,bg='lightblue')
        bottom_frame.place(x=350, y=150)

        #bottom_frame2 = Frame(root, width=100, height=400,bg="lightblue")
        #bottom_frame2.place(x=0, y=150)

        bottom_frame3 = Frame(root, width=150, height=400,bg="lightblue")
        bottom_frame3.place(x=550, y=150)

        self.frame_data = Frame(root, width=1180, height=500,bg="white")
        self.frame_data.place(x=50, y=400)

        bottom_frame5 = Frame(root, width=100, height=250,bg='lightblue')
        bottom_frame5.place(x=800, y=150)
        
        self.keyword_input = StringVar() 
        self.keyword_entry = Entry(top_frame, textvariable=self.keyword_input,width=30)
        self.keywordEntryText = StringVar()
        self.keywordEntryText.set("JANES SEARCH ENGINE")
        self.keyLabelEntry = Label(top_frame, textvariable=self.keywordEntryText, height=2,pady=30,padx=500) 
        self.keyLabelEntry.config(font=('Arial', 12,"bold"),bg="lightblue",fg="black")
        self.keyLabelEntry.pack(side="top",anchor="center")
        self.keyword_entry.pack(side="top",anchor="center")
        


        #SEARCH BUTTON
        self.button = Button(bottom_frame5, text="SEARCH",width=12,height=2,padx=1,pady=1,bg="lightgray",command=self.scrape)
        self.button.place(relx = 0.1, rely = 0.1, anchor = "w")



        #CLEAR BUTTON
        self.clear_btn = Button(bottom_frame5, text="CLEAR",width=12,height=2,padx=1,pady=1,bg="lightgray",command=self.clear)
        self.clear_btn.place(relx = 0.1, rely = 0.3, anchor = "w")

       

        #EXIT BUTTON 
        self.buttonext = Button(bottom_frame5, text="CLOSE",width=12,height=2,padx=1,pady=1,bg="lightgray",command=self.close)
        self.buttonext.place(relx = 0.1, rely = 0.5, anchor ="w")

        


        #CHECKBOXES
        self.checkbox_List = []
        #Checkbutton1 = IntVar()   
        #Checkbutton2 = IntVar()   
        #Checkbutton3 = IntVar()
        #Checkbutton4 = IntVar()   
        #Checkbutton5 = IntVar()   
        #Checkbutton6 = IntVar()
        #Checkbutton7 = IntVar()   
        #Checkbutton8 = IntVar()   
        #Checkbutton9 = IntVar()
        #Checkbutton10 = IntVar()   
        #Checkbutton11 = IntVar()   
        #Checkbutton12 = IntVar()
        #Checkbutton13 = IntVar()   
        #Checkbutton14 = IntVar()
        


        #self.cbx_range = Checkbutton(bottom_frame, text = "Range",variable = Checkbutton1,  onvalue = 1, offvalue = 0, height=2, width=10)
        #self.cbx_range.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_range.config(highlightbackground="white",background="lightblue",foreground="black")

        #self.cbx_alt = Checkbutton(bottom_frame, text = "Altitude", variable = Checkbutton2, onvalue = 1, offvalue = 0, height=2, width=10,) 
        #self.cbx_alt.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_alt.config(highlightbackground="white",background="lightblue",foreground="black")

        #self.cbx_speed = Checkbutton(bottom_frame, text = "Speed", variable = Checkbutton3, onvalue = 1, offvalue = 0, height=2, width=10,)
        #self.cbx_speed.pack(side=TOP,fill="both",anchor = "w")
        #self.cbx_speed.config(highlightbackground="white",background="lightblue",foreground="black") 

        #self.cbx_loadfac = Checkbutton(bottom_frame2, text = "Load Factor",variable = Checkbutton4,  onvalue = 1, offvalue = 0, height=2, width=10,) 
        #self.cbx_loadfac.pack(side=TOP,fill="both",anchor = "w")
        #self.cbx_loadfac.config(highlightbackground="white",background="lightblue",foreground="black") 

        #self.cbx_wamass = Checkbutton(bottom_frame2, text = "Warhead Mass", variable = Checkbutton5, onvalue = 1, offvalue = 0, height=2, width=10,) 
        #self.cbx_wamass.pack(side=TOP,fill="both",anchor = "w")
        #self.cbx_wamass.config(highlightbackground="white",background="lightblue",foreground="black") 

        #self.cbx_gui = Checkbutton(bottom_frame2, text = "Guidance Sys", variable = Checkbutton6, onvalue = 1, offvalue = 0, height=2, width=10)
        #self.cbx_gui.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_gui.config(highlightbackground="white",background="lightblue",foreground="black")

        #self.cbx_tel = Checkbutton(bottom_frame2, text = "Missiles per TEL",variable = Checkbutton7,  onvalue = 1, offvalue = 0, height=2, width=10) 
        #self.cbx_tel.pack(side=TOP,fill="both",anchor = "w")
        #self.cbx_tel.config(highlightbackground="white",background="lightblue",foreground="black") 


        #self.cbx_rad = Checkbutton(bottom_frame, text = "Radius", variable = Checkbutton9, onvalue = 1, offvalue = 0, height=2, width=10)
        #self.cbx_rad.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_rad.config(highlightbackground="white",background="lightblue",foreground="black")

        #self.cbx_wemass = Checkbutton(bottom_frame2, text = "Weight Mass",variable = Checkbutton10,  onvalue = 1, offvalue = 5, height=2, width=10)
        #self.cbx_wemass.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_wemass.config(highlightbackground="white",background="lightblue",foreground="black")

        #self.cbx_width = Checkbutton(bottom_frame, text = "Width",variable = Checkbutton11,  onvalue = 1, offvalue = 0, height=2, width=10) 
        #self.cbx_width.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_width.config(highlightbackground="white",background="lightblue",foreground="black")

        #self.cbx_height = Checkbutton(bottom_frame, text = "Height", variable = Checkbutton12, onvalue = 1, offvalue = 0, height=3, width=10) 
        #self.cbx_height.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_height.config(highlightbackground="white",background="lightblue",foreground="black")

        #self.cbx_emipwr = Checkbutton(bottom_frame2, text = "Emission Pwr", variable = Checkbutton13, onvalue = 1, offvalue = 0, height=2, width=10) 
        #self.cbx_emipwr.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_emipwr.config(highlightbackground="white",background="lightblue",foreground="black")

        #self.cbx_emifrq = Checkbutton(bottom_frame2, text = "Emission Freq", variable = Checkbutton14, onvalue = 1, offvalue = 0, height=2, width=10) 
        #self.cbx_emifrq.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_emifrq.config(highlightbackground="white",background="lightblue",foreground="black")

        #self.cbx_len = Checkbutton(bottom_frame, text = "Length", variable = Checkbutton8, onvalue = 1, offvalue = 0, height=2, width=10) 
        #self.cbx_len.pack(side=TOP,fill="both",anchor = "w") 
        #self.cbx_len.config(highlightbackground="white",background="lightblue",foreground="black")

        Properties = {"Range","Altitude","Speed","Load Factor","Warhead Mass","Guidance System","Radius","Weight Mass","Width","Height","Emission Power","Emission Frequency","Length"}
        self.Checkdict = {}
        i = 0
        for prop in Properties:
            if i%2 == 0 :
                self.Checkdict[prop] = IntVar()
                #Properties[prop] = Variable()
                l = Checkbutton(bottom_frame, text=prop, variable=self.Checkdict[prop])
                l.config(highlightbackground="white",background="lightblue",foreground="black")
                l.pack(side="top",anchor = "w")
                self.checkbox_List.append(l)
                i=i+1
            
            else :
                self.Checkdict[prop] = IntVar()
                #Properties[prop] = Variable()
                l = Checkbutton(bottom_frame3, text=prop, variable=self.Checkdict[prop])
                l.config(highlightbackground="white",background="lightblue",foreground="black")
                l.pack(side = "top",anchor = "w")
                self.checkbox_List.append(l)
                i=i+1

        #cols = ("Range","Altitude","Speed","Load Factor","Warhead Mass","Guidance System","Radius","Weight Mass","Width","Height","Emission Power","Emission Frequency","Length")
        #self.listBox = ttk.Treeview(self.frame_data, columns=cols, show='headings')
        
        #self.listBox.grid(row=1, column=0 )#columnspan=2)
        label = Label(root, text="Results",bg="lightblue",font=("Times New Roman",16)).place(x=50,y=350)
        


        #self.checkbox_List.append(Checkbutton1)
        #self.checkbox_List.append(Checkbutton2)
        #self.checkbox_List.append(Checkbutton2)
        #self.checkbox_List.append(Checkbutton3)
        #self.checkbox_List.append(Checkbutton4)
        #self.checkbox_List.append(Checkbutton5)
        #self.checkbox_List.append(Checkbutton6)
        #self.checkbox_List.append(Checkbutton7)
        #self.checkbox_List.append(Checkbutton8)
        #self.checkbox_List.append(Checkbutton9)
        #self.checkbox_List.append(Checkbutton10)
        #self.checkbox_List.append(Checkbutton11)
        #self.checkbox_List.append(Checkbutton12)
        #self.checkbox_List.append(Checkbutton13)
        #self.checkbox_List.append(Checkbutton14)


    def table_data(self,keyword,prop) :

            #label = Label(self.frame_data, text="RESULTS TABLE",font=("Times New Roman",16))#.grid(row=0, columnspan=3)
            self.listBox = ttk.Treeview(root, columns=prop, show='headings')
            
            yscrollbar = ttk.Scrollbar(root, orient='vertical', command=self.listBox.yview)
            xscrollbar = ttk.Scrollbar(root, orient='horizontal', command=self.listBox.xview)

            yscrollbar.place(x=1230, y=400, height=500)
            xscrollbar.place(x=50, y=900, width=1180)
            self.listBox.configure(yscroll=yscrollbar.set, xscroll=xscrollbar.set)

            for col in prop:
                self.listBox.heading(col, text=col)
                    
            self.listBox.place(x=50,y=400,height=500,width=1180)
            

            return self.listBox,yscrollbar,xscrollbar
             



    def scrape(self) :
        #try:
            keyword = self.keyword_input.get()
            print(keyword)

            prop = self.checked_prop(self.Checkdict)
            print(prop)
            self.table_data(keyword,prop)
            MyMain.main_func(self,keyword,prop)
            #insert_data()


            
            #main.main_func(keyword,prop)
            
                 
        #except :
                #messagebox.showwarning("No Results","There's nothing here,try diffrent input!")
                #self.keyword_input.set("")

    def clear(self) :
        self.keyword_input.set("")
        boxes = self.checkbox_List
        for box in boxes :
            box.set(0)


    def checked_prop(self,Checkdict) :

        checked_List = []
        print("No Input im here !")
        print(Checkdict)
        for key, value in Checkdict.items():
            if value.get() > 0:
                checked_List.append(key)

        return checked_List
        
    
    def close(self) :
        return 0

    
    #############################################
    # items #    Heads   #   Altitude #  Speed  #
    #############################################
    #s300   #   300nm    #     25     #    12   #
    #s300   #   390px    #     15     #    14   # 
    #s300   #   3S50     #     17     #    18   # 
    #############################################
        

 
    

if __name__ == '__main__':

    root = Tk()
    root.resizable(0,0)
    GUI=MyGUI(root)
    root.mainloop()