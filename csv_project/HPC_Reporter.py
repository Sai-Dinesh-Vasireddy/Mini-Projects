from tkinter import *
from tkcalendar import *
import csv
import pandas as pd
from matplotlib import *
from matplotlib import pyplot as plt
from tkinter import messagebox
global Temp

################################ GRAPH SNOW ################################################################################################################################################################################################################################################################
def Graph1():
    try:
        d=pd.read_csv('HPC_SNOW_Report.csv')
        print(d)
    except:
        print('File Does Not Exist')

        
def Graph2():
    try:
        d2 = pd.read_csv('HPC_JIRA_Report.csv')
        print(d2)
    except:
        print('File Does Not Exist')
################################  CSV  SNOW   FILE    WRITING   ############################################################################################################################################################################################################################################
def csvfile_SNOW():
    with open('HPC_SNOW_Report.csv', 'a+' , newline = "") as s:
        w = csv.writer(s)
        w.writerow([Request_Incident_Num_Var.get(),Requested_User_Var.get(),Assignedto_S_Var.get(),Request_Open_Date_S_Var.get(),State_Var.get(),Request_Closed_Date_S_Var.get(),Time_Worked_S_Var.get(),Des_1.get(0.0,'end'),Note_1.get(0.0,'end')])
        messagebox.showinfo('Success','Submitted')
def csvfile_JIRA():
    with open('HPC_JIRA_Report.csv' , 'a+' , newline = "") as j:
        try :
            Temp = '-'
            Temp = impediments_text.get(0.0,'end')
        except:
            pass
        wr = csv.writer(j)
        wr.writerow([Task_Number_Var.get(),Sprint_Number_Var.get(),Sprint_Date_F_Var.get(),Sprint_Date_T_Var.get(),Assignedto_J_Var.get(),Worklog_J_Date_Var.get(),Worklog_J_Time_Var.get(),Deployed_Date_Var.get(),Impediments_Var.get(),Temp,Des_2.get(0.0,'end'),Comment.get(0.0,'end')])
        messagebox.showinfo('Success','Submitted')



global Task_Number_Var
global Sprint_Number_Var
global Sprint_Date_Var
global Assignedto_J_Var
global Description_J_Var                   ####### JIRA SECTION VARIABLES ##################################################################################################################################################################################################################################
global Comments_J_Var
global Worklog_J_Var
global Deployed_Date_Var
global Impediments_Var
global Worklog_J_Time_Var
global Worklog_J_Date_Var

global graph_s_f_Var
global graph_s_t_Var

global graph_j_f_Var
global graph_j_t_Var


####################################### IMPEDIMENTS FUNCTION DEFINITION ####################################################################################################################################################################################################################################
def impediments(event):
    global impediments_text
    global reason
    global impediments_text
    
    if Impediments_Var.get() == 'Yes':
        reason = Label(screen , text ="Reason ")
        reason.place(x = 750 , y = 200)
        impediments_text = Text(screen , width = 20 , height = 3)
        impediments_text.place(x= 750,y= 220)
    if Impediments_Var.get() == 'No':
        try:
            reason.destroy()
            impediments_text.destroy()
        except:
            pass



####################################### CALENDAR 1 REQ_OPEN_DATE ###########################################################################################################################################################################################################################################
def calendar1():
    def calval():
        calval_var1 = cal.get()
        Request_Open_Date_S_Var.set(calval_var1)
        cal_entry1 = Entry(screen , textvariable = Request_Open_Date_S_Var).place(x= 150 , y = 140)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var1
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()

####################################### CALENDAR 2 SPRINT_F ################################################################################################################################################################################################################################################
def calendar2():
    def calval():
        calval_var2 = cal.get()
        Sprint_Date_F_Var.set(calval_var2)
        cal_entry2 = Entry(screen , textvariable = Sprint_Date_F_Var).place(x= 660 , y = 105)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var2
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()

######################################### CALENDAR 3 SPRINT_TO #############################################################################################################################################################################################################################################
def calendar3():
    def calval():
        calval_var3 = cal.get()
        Sprint_Date_T_Var.set(calval_var3)
        cal_entry3 = Entry(screen , textvariable = Sprint_Date_T_Var).place(x= 840 , y = 105)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var3
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()


####################################### CALENDAR 4 WORKLOG_DATE ############################################################################################################################################################################################################################################
def calendar4():
    def calval():
        calval_var4 = cal.get()
        Worklog_J_Date_Var.set(calval_var4)
        cal_entry4 = Entry(screen , textvariable = Worklog_J_Date_Var).place(x= 615 , y = 165)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var4
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()

####################################### CALENDAR 5 REQ_C_DATE ##############################################################################################################################################################################################################################################
def calendar5():
    def calval():
        calval_var5 = cal.get()
        Request_Closed_Date_S_Var.set(calval_var5)
        cal_entry4 = Entry(screen , textvariable = Request_Closed_Date_S_Var).place(x= 150 , y = 170)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var5
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()
####################################### CALENDAR 6 DEPLOYED DATE ###########################################################################################################################################################################################################################################
def calendar6():
    def calval():
        calval_var6 = cal.get()
        Deployed_Date_Var.set(calval_var6)
        cal_entry4 = Entry(screen , textvariable = Deployed_Date_Var).place(x= 630 , y = 195)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var6
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()


####################################### CALENDAR 7 DEPLOYED DATE ###########################################################################################################################################################################################################################################
def calendar7():
    def calval():
        calval_var7 = cal.get()
        graph_s_f_Var.set(calval_var7)
        cal_entry4 = Entry(screen , textvariable = graph_s_f_Var).place(x= 110 , y = 500)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var7
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()

####################################### CALENDAR 8 DEPLOYED DATE ###########################################################################################################################################################################################################################################
def calendar8():
    def calval():
        calval_var8 = cal.get()
        graph_s_t_Var.set(calval_var8)
        cal_entry4 = Entry(screen , textvariable = graph_s_t_Var).place(x= 320 , y = 500)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var8
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()

####################################### CALENDAR 9 DEPLOYED DATE ###########################################################################################################################################################################################################################################
def calendar9():
    def calval():
        calval_var9 = cal.get()
        graph_j_f_Var.set(calval_var9)
        cal_entry4 = Entry(screen , textvariable = graph_j_f_Var).place(x= 610 , y = 500)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var9
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()

####################################### CALENDAR 10 DEPLOYED DATE ##########################################################################################################################################################################################################################################
def calendar10():
    def calval():
        calval_var10 = cal.get()
        graph_j_t_Var.set(calval_var10)
        cal_entry4 = Entry(screen , textvariable = graph_j_t_Var).place(x= 820 , y = 500)
        cal.destroy()
        btn3.destroy()
        top.destroy()
    global calval_var10
    top = Toplevel(screen)
    cal = DateEntry(top , width = 15 , background = "blue",foreground = "red" ,borderwidth = 3)
    cal.pack(padx = 10 , pady = 10)
    btn3= Button(top , text ="Done", command = calval)
    btn3.pack()




    
#######################################   FOR HEADING AND DIMENSIONS   #####################################################################################################################################################################################################################################
def Head(name,w,ht,bgcolor,fgcolor):
    h=Label(screen ,text = name , width = w,height = ht,bg= bgcolor , fg=fgcolor)
    h.pack()

def SecHead(name,w,ht,bgcolor,fgcolor,xp):
    sec=Label(screen , text = name , width = w , height = ht , bg = bgcolor, fg= fgcolor)
    sec.place(x=xp,y='22')
           
global screen
screen=Tk()
screen.title("HPC Reporting Tool Kit")
screen.geometry('1000x900')
Head('HPC Reporting Tool','1080','1','yellow','black')


##################################### FOR SECTION HEADING   ################################################################################################################################################################################################################################################
SecHead('SNOW','100','1','skyblue','black','-100')
SecHead('JIRA','72','1','skyblue','black','500')  

########## FOR SECTION LABLE HANDLING#######################################################################################################################################################################################################################################################################
c1 = Label(screen , text = ' ',width =1000,bg = 'skyblue')
c1.place(x = '800',y = '22')

###################################  FOR SECTION DIVISION ##################################################################################################################################################################################################################################################
line_01=Label(screen , text=' ',width = 1 , height =100, bg='skyblue').place(x='495', y= '22')
line_02=Label(screen , text=' ',width =2000, height = 2, bg='skyblue').place( x = '0' , y = '460')
line_03=Label(screen , text='''S
N
O
W


''',font='Helvetica 18 bold',width = 1 , height =10, bg='yellow').place(x='0', y= '496')
line_04=Label(screen , text='''J
I
R
A


''',font='Helvetica 18 bold',width = 1 , height =10, bg='yellow').place(x='508', y= '496')

#w1 = 0
#w2 = 0
#while w1<=455:
#    line=Label(screen , text=' ', bg='black')
#    line.place(x = '495' , y = w1+22)
#    w1+=1
#while w2 <= 1080:
#    line=Label(screen , text=' ', bg='black')
#    line.place(x = w2 , y = '500')
#    w2+=1


#for i in range(1):
#   line=Label(screen , text=' ', bg='black')
#   line.place(x = '495' , y = i+22)
#for i in range(2000):
#    line=Label(screen , text='                ',width = 1,height = 0,bg='black')
#    line.place(x = i , y = '452') 

######################################   FOR LABELS    #####################################################################################################################################################################################################################################################

def labels(name,xp,yp):
    l = Label(screen , text = name)
    l.place(x = xp,y = yp)

########################## LABELS ON SNOW SECTION ##########################################################################################################################################################################################################################################################
    
labels('Request/Incident :',10,45)
labels('Requested User :',10,75)
labels('Assigned To :',10,105)
labels('Request Open Date :',10,135)
labels('Request Closed Date :',10,165)
labels('State :',10,195)
labels('Time Worked :',10,225)
labels('Description :',10,255)
labels('Note :',10,355)

############################# LABELS ON JIRA SECTION #######################################################################################################################################################################################################################################################

labels('Task/Story Number :',520,45)
labels('Sprint Number :',520,75)

labels('Sprint Date :',520,105)
labels('From',600,105)
labels('To',800,105)

labels('Assigned To :',520,135)
labels('Work Log :',520,165)
labels('Deployed Date :',520,195)
labels('Impediments [Y/N] :',520,225)
labels('Description :',520,255)
labels('Comments :',520,355)

##########################GRAPH LABELS FROM/TO #############################################################################################################################################################################################################################################################
labels('From ',50,500)
labels('To ',275,500)
labels('From ', 550 , 500)
labels('To' , 775 , 500)
###################### FOR NOTE,DESCRIPTION AND COMMENT  ###################################################################################################################################################################################################################################################

Des_1 = Text(screen , width = 40 , height = 4)
Des_1.place(x='20', y='280')########## FOR DESCRIPTION IN SNOW #############################################################################################################################################################################################################################################


Note_1 = Text(screen, width = 40 , height = 4 )
Note_1.place(x='20',y='380')###########FOR NOTE IN SNOW ####################################################################################################################################################################################################################################################


Des_2=Text(screen , width =40 , height =4)
Des_2.place(x= '530',y='280')########## FOR DESCRIPTION IN JIRA ############################################################################################################################################################################################################################################


Comment=Text(screen , width=40 , height = 4)
Comment.place(x='530', y= '380')########## FOR COMMENTS IN JIRA ############################################################################################################################################################################################################################################




##################################FOR 1ST DESCRIPTION BOX ENTRY#############################################################################################################################################################################################################################################



################################### GLOBAL DECLARATION OF USER INPUT VARIABLES #############################################################################################################################################################################################################################

global Request_Incident_Num_Var 
global Requested_User_Var
global Assignedto_S_Var
global Request_Open_Date_S_Var
global State_Var
global Request_Closed_Date_S_Var           ####### SNOW SECTION VARIABLES ##################################################################################################################################################################################################################################
global Time_Worked_S_Var
global Description_S_Var
global Notes_S_Var




global Task_Number_Var
global Sprint_Number_Var
global Sprint_Date_Var
global Assignedto_J_Var
global Description_J_Var                   ####### JIRA SECTION VARIABLES ##################################################################################################################################################################################################################################
global Comments_J_Var
global Worklog_J_Var
global Deployed_Date_Var
global Impediments_Var
global Worklog_J_Time_Var
global Worklog_J_Date_Var

global graph_s_f_Var
global graph_s_t_Var

global graph_j_f_Var
global graph_j_t_Var



Assigned_list = ['Dhanush','Gowri','Krishna','Shiwangi']
state_list = ['open' , 'inprogress' , 'onhold' , 'closed']
boollist=['Yes','No']
############################################################################################################################################################################################################################################################################################################


################################## ASSIGNING VARIABLES #####################################################################################################################################################################################################################################################

Request_Incident_Num_Var = StringVar(screen)
Requested_User_Var = StringVar(screen)


Assignedto_S_Var = StringVar(screen)
Assignedto_S_Var.set('Dhanush')


Request_Open_Date_S_Var = StringVar(screen)                ##### SNOW SECTION ASSIGNMENT####################################################################################################################################################################################################################


State_Var = StringVar(screen)
State_Var.set('open')

Request_Closed_Date_S_Var = StringVar(screen)

Time_Worked_S_Var = StringVar(screen)
Time_Worked_S_Var.set('Enter Hours(Ex: 2)')


Task_Number_Var = StringVar(screen)

Sprint_Number_Var = StringVar(screen)

Sprint_Date_F_Var = StringVar(screen)
Sprint_Date_T_Var = StringVar(screen)


Assignedto_J_Var = StringVar(screen)
Assignedto_J_Var.set('Dhanush')

Worklog_J_Var = StringVar(screen)

Worklog_J_Time_Var = StringVar(screen)
Worklog_J_Time_Var.set("Enter Hours(Ex: 2)")

Worklog_J_Date_Var = StringVar(screen)

Deployed_Date_Var = StringVar(screen)

Impediments_Var = StringVar(screen)
Impediments_Var.set('No')


graph_s_f_Var = StringVar()
graph_s_t_Var = StringVar()

graph_j_f_Var = StringVar()
graph_j_t_Var = StringVar()

############################################################################################################################################################################################################################################################################################################
entry_1 = Entry(screen , textvariable = Request_Incident_Num_Var).place( x = 150 , y = 45)
entry_2 = Entry(screen , textvariable = Requested_User_Var).place( x = 150 , y = 75)

listentry1 = OptionMenu(screen,Assignedto_S_Var,*Assigned_list).place( x = 150, y = 100)


listentry2 = OptionMenu(screen,State_Var,*state_list).place( x = 150, y = 190)

entry_3 = Entry(screen , textvariable = Time_Worked_S_Var).place( x = 150 , y = 225)



################################# second section ###########################################################################################################################################################################################################################################################
entry_4 = Entry(screen , textvariable =Task_Number_Var).place (x = 660 , y = 45)
entry_5 = Entry(screen , textvariable =Sprint_Number_Var).place (x = 660 , y = 75)

listentry3 = OptionMenu(screen,Assignedto_J_Var,*Assigned_list).place( x = 660, y = 130)

entry_6 = Entry(screen , textvariable =Worklog_J_Time_Var).place(x = 750 , y = 165)

listentry3 = OptionMenu(screen,Impediments_Var,*boollist,command = impediments).place(x = 660 , y = 220)

calendar_button1 = Button(screen , text = ':',bg = 'cyan',command = calendar1)
calendar_button1.place(x = 280 , y = 135)

calendar_button2 = Button(screen , text = ':',bg = 'cyan', command = calendar2)
calendar_button2.place(x = 635 , y = 100)

calendar_button3 = Button(screen , text = ':',bg = 'cyan', command = calendar3)
calendar_button3.place(x = 820 , y = 100)

calendar_button4 = Button(screen , text = ':',bg = 'cyan', command = calendar4)
calendar_button4.place(x = 595 , y = 160)

calendar_button5 = Button(screen , text = ':',bg = 'cyan',command = calendar5)
calendar_button5.place(x = 280 , y = 165)

calendar_button6 = Button(screen , text = ':',bg = 'cyan',command = calendar6)
calendar_button6.place(x = 610 , y = 195)

calendar_button7 = Button(screen , text = ':',bg = 'cyan',command = calendar7)
calendar_button7.place(x = 90 , y = 500)

calendar_button8 = Button(screen , text = ':',bg = 'cyan',command = calendar8)
calendar_button8.place(x = 300 , y = 500)

calendar_button9 = Button(screen , text = ':',bg = 'cyan',command = calendar9)
calendar_button9.place(x = 590 , y = 500)

calendar_button10 = Button(screen , text = ':',bg = 'cyan',command = calendar10)
calendar_button10.place(x = 800 , y = 500)





#################################  SUBMIT BUTTON ###########################################################################################################################################################################################################################################################

submit = Button(screen,text = 'Submit' , width = 40 , height = 1 , bg = 'yellow' , fg ='black' , command = csvfile_SNOW)
submit.place(x = 100 , y = 465)



submit = Button(screen,text = 'Submit' , width = 40 , height = 1 , bg = 'yellow' , fg ='black' , command = csvfile_JIRA)
submit.place(x = 600 , y = 465)
############################################################################################################################################################################################################################################################################################################

################################### GRAPH GENERATING BUTTONS ###############################################################################################################################################################################################################################################

G_B_1 = Button(screen , text = 'Generate Graph' , bg = 'yellow' , command = Graph1).place( x = 360 , y = 575)
G_B_2 = Button(screen , text = 'Generate Graph' , bg = 'yellow' , command = Graph2).place( x = 860 , y = 575)




