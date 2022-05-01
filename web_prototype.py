from tkinter import*

class main:
    def __init__(self,master,*args,**kwargs):
        self.master=master
        def btn_blue():
            root.config(bg="#0060bc")
            self.blue.config(bg="#0060bc",activebackground="#0060bc")
            self.black.config(bg="#0060bc",activebackground="#0060bc")
            self.red.config(bg="#0060bc",activebackground="#0060bc")
            self.txt.config(bg='#0060bc')
            self.txt1.config(bg='#0060bc')
            self.pepsi.config(bg="#0060bc")
            self.btn.config(bg="#0060bc",activebackground="#0060bc")
            self.blue_lab=Label(self.master,image=self.image,bg="#0060bc",bd=0)
            self.blue_lab.place(x=900,y=100)
            self.btn_developer.config(bg="#0060bc",activebackground="#0060bc")
            self.btn_home.config(bg="#0060bc",activebackground="#0060bc")
            self.about.config(bg="#0060bc",activebackground="#0060bc")
            self.contact.config(bg="#0060bc",activebackground="#0060bc")
                                        
        def btn_black():
            root.config(bg="#1f1f1f")
            self.blue.config(bg="#1f1f1f",activebackground="#1f1f1f")
            self.black.config(bg="#1f1f1f",activebackground="#1f1f1f")
            self.red.config(bg="#1f1f1f",activebackground="#1f1f1f")
            self.txt.config(bg='#1f1f1f')
            self.txt1.config(bg='#1f1f1f')
            self.pepsi.config(bg="#1f1f1f")
            self.btn.config(bg="#1f1f1f",activebackground="#1f1f1f")
            self.black_lab=Label(self.master,image=self.image2,bg="#1f1f1f",bd=0)
            self.black_lab.place(x=900,y=100)
            self.btn_developer.config(bg="#1f1f1f",activebackground="#1f1f1f")
            self.btn_home.config(bg="#1f1f1f",activebackground="#1f1f1f")
            self.about.config(bg="#1f1f1f",activebackground="#1f1f1f")
            self.contact.config(bg="#1f1f1f",activebackground="#1f1f1f")
                                   
        def btn_red():
            root.config(bg="#e40b2c")
            self.blue.config(bg="#e40b2c",activebackground="#e40b2c")
            self.black.config(bg="#e40b2c",activebackground="#e40b2c")
            self.red.config(bg="#e40b2c",activebackground="#e40b2c")
            self.txt.config(bg='#e40b2c')
            self.txt1.config(bg='#e40b2c')
            self.pepsi.config(bg="#e40b2c")
            self.btn.config(bg="#e40b2c",activebackground="#e40b2c")
            self.red_lab=Label(self.master,image=self.image3,bg="#e40b2c",bd=0)
            self.red_lab.place(x=900,y=100)
            self.btn_developer.config(bg="#e40b2c",activebackground="#e40b2c")
            self.btn_home.config(bg="#e40b2c",activebackground="#e40b2c")
            self.about.config(bg="#e40b2c",activebackground="#e40b2c")
            self.contact.config(bg="#e40b2c",activebackground="#e40b2c")            
           
        self.a=1
        self.b=0
        self.image=PhotoImage(file='blue.png')
        self.image_logo=self.image.subsample(5,5)
        self.blue=Button(self.master,image=self.image_logo,bg="#0060bc",activebackground="#0060bc",command=btn_blue,bd=0)
        self.blue.place(x=600,y=600)
        self.blue.bind("<Enter>",self.hover_in_blue)
        self.blue.bind("<Leave>",self.hover_out_blue)
        self.hover_function_blue()
        self.blue_lab=Label(self.master,image=self.image,bg="#0060bc",bd=0)
        self.blue_lab.place(x=900,y=100)
        
        self.pepsi_logo=PhotoImage(file="pepse.png")
        self.pepsi=Label(self.master,image=self.pepsi_logo,bd=0,bg='#0060bc')
        self.pepsi.place(x=70,y=20)

        self.c=1
        self.d=0
        self.image2=PhotoImage(file='black.png')
        self.image2_logo=self.image2.subsample(5,5)
        self.black=Button(self.master,image=self.image2_logo,bg="#0060bc",activebackground="#0060bc",bd=0,command=btn_black)
        self.black.place(x=510,y=600)
        self.black.bind("<Enter>",self.hover_in_black)
        self.black.bind("<Leave>",self.hover_out_black)
        self.hover_function_black()

        self.e=1
        self.f=0
        self.image3=PhotoImage(file='red.png')
        self.image3_logo=self.image3.subsample(5,5)
        self.red=Button(self.master,image=self.image3_logo,bg="#0060bc",activebackground="#0060bc",bd=0,command=btn_red)
        self.red.place(x=690,y=600)
        self.red.bind("<Enter>",self.hover_in_red)
        self.red.bind("<Leave>",self.hover_out_red)
        self.hover_function_red()

        self.btn_home=Button(root,text="Home",bg="#0060bc",fg="white",borderwidth=0,activeforeground="white",activebackground="#0060bc",cursor="hand2",font=('arial 11'))
        self.btn_home.place(x=915,y=24)    
        self.btn_developer=Button(root,text="Team of Developers",bg="#0060bc",fg="white",borderwidth=0,activeforeground="white",activebackground="#0060bc",cursor="hand2",font=('arial 11'))
        self.btn_developer.place(x=1060,y=24)
        self.contact=Button(root,text="Contact Us",bg="#0060bc",fg="white",borderwidth=0,activeforeground="white",activebackground="#0060bc",cursor="hand2",font=('arial 11'))
        self.contact.place(x=970,y=24)
        self.about=Button(root,text="About",bg="#0060bc",fg="white",borderwidth=0,activeforeground="white",activebackground="#0060bc",cursor="hand2",font=('arial 11'))
        self.about.place(x=1210,y=24)

        self.txt=Label(self.master,text="That's What I",font=('sanserif 55 bold'),bg="#0060bc",fg="white")
        self.txt.place(x=100,y=250)
        self.txt1=Label(self.master,text="LIke",font=('sanserif 55 bold'),bg="#0060bc",fg="white")
        self.txt1.place(x=100,y=340)

        self.view=PhotoImage(file="view.png")
        self.btn=Button(self.master,image=self.view,bd=0,bg="#0060bc",cursor="hand2",activebackground="#0060bc")
        self.btn.place(x=90,y=540)
        
    def hover_in_blue(self,ev):
        self.a=0
    def hover_out_blue(self,ev):
        self.a=1
    def hover_function_blue(self):
        if self.a==0:
            if self.b!=-8:
                self.b-=1
                self.blue.place(y=600+self.b)
        if self.a==1:
            if self.b!=0:
                self.b+=1
                self.blue.place(x=600,y=600+self.b)
        self.blue.after(20,self.hover_function_blue)


    def hover_in_black(self,ev):
        self.c=0
    def hover_out_black(self,ev):
        self.c=1
    def hover_function_black(self):
        if self.c==0:
            if self.d!=-8:
                self.d-=1
                self.black.place(y=600+self.d)
        if self.c==1:
            if self.d!=0:
                self.d+=1
                self.black.place(y=600+self.d)
        self.black.after(30,self.hover_function_black)

    def hover_in_red(self,ev):
        self.e=0
    def hover_out_red(self,ev):
        self.e=1
    def hover_function_red(self):
        if self.e==0:
            if self.f!=-8:
                self.f-=1
                self.red.place(y=600+self.f)
        if self.e==1:
            if self.f!=0:
                self.f+=1
                self.red.place(y=600+self.f)
        self.red.after(30,self.hover_function_red)
    
root=Tk()
root.geometry("1200x700+70+20")
run=main(root)
root.config(bg="#0060bc")
root.attributes("-fullscreen",True)
root.mainloop()
