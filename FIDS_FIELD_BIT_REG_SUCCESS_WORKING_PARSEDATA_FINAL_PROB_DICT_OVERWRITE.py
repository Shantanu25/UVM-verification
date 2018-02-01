#! /usr/bin/env python
#

import sys
import os

cwd = os.getcwd()

def mkedir(A):     #this is a function that makes a directory of the argument name passed
  os.makedirs(A)

org_seqR    = "sequencer" 
org_seq_itm = "sequence_item"
org_seq     = "sequence"
org_drv     = "driver"
org_mon     = "monitor"
org_sb      = "scoreboard"
org_agnt    = "agent"
org_env	    = "environment"
org_test    = "test"



try:
    from Tkinter import *
    import tkinter.filedialog # import askopenfilename          #fenilshu
    import re                                                   #fenilshu
except ImportError:
    from tkinter import *
    import tkinter.filedialog #import askopenfilename          #fenilshu
    import re                                                  #fenilshu
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import FIDS_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    FIDS_support.set_Tk_var()
    top = FIDS (root)
    FIDS_support.init(root, top)
    root.mainloop()

w = None
def create_FIDS(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    FIDS_support.set_Tk_var()
    top = FIDS (w)
    FIDS_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_FIDS():
    global w
    w.destroy()
    w = None


class FIDS:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("860x486+394+73")
        top.title("FIDS")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        #filename = askopenfilename()

        self.Label1 = Label(top)
        self.Label1.place(relx=0.01, rely=0.12, height=31, width=138)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''DUT NAME''')
        self.Label1.configure(width=138)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.19, rely=0.13, relheight=0.06, relwidth=0.14)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=FIDS_support.DUTN)
        self.Entry1.configure(width=124)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.52, rely=0.46, height=54, width=265)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''GENERATE UVM ENVIRONMENT''')
        self.Button1.configure(width=265)
        #############This button trigger UVM environment ##############
        self.Button1.configure(command=event_click)
        #self.Button1.configure(command=event_close)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.52, rely=0.65, height=54, width=125)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Extract system RDL file''')
        self.Button2.configure(width=125)
        ##############Open file def which open RDL file and extract date######
        self.Button2.configure(command=open_file)

        #self.Button3 = Button(top)
        #self.Button3.place(relx=0.69, rely=0.65, height=54, width=125)
        #self.Button3.configure(activebackground="#d9d9d9")
        #self.Button3.configure(activeforeground="#000000")
        #self.Button3.configure(background="#d9d9d9")
        #self.Button3.configure(disabledforeground="#a3a3a3")
        #self.Button3.configure(foreground="#000000")
        #self.Button3.configure(highlightbackground="#d9d9d9")
        #self.Button3.configure(highlightcolor="black")
        #self.Button3.configure(pady="0")
        #self.Button3.configure(text='''Generate RAL model''')
        #self.Button3.configure(width=125)
        #self.Button3.configure(command=gen_ral)
        

        self.Label2 = Label(top)
        self.Label2.place(relx=0.01, rely=0.21, height=31, width=144)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''INTERFACE NAME''')
        self.Label2.configure(width=144)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.19, rely=0.21, relheight=0.06, relwidth=0.14)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(textvariable=FIDS_support.INTERFACEN)
        self.Entry2.configure(width=124)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.07, rely=0.0, height=51, width=664)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''UVM verification environment builder and register testing tool''')
        self.Label3.configure(width=664)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.01, rely=0.29, height=31, width=134)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''MODPORT NAME''')
        self.Label4.configure(width=134)

        self.Label5 = Label(top)
        self.Label5.place(relx=0.01, rely=0.37, height=31, width=134)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''SEQUENCE_ITEM NAME''')
        self.Label5.configure(width=134)

        self.Label6 = Label(top)
        self.Label6.place(relx=0.01, rely=0.45, height=31, width=134)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''SEQUENCE NAME''')
        self.Label6.configure(width=134)

        self.Label7 = Label(top)
        self.Label7.place(relx=0.01, rely=0.53, height=31, width=134)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''SEQUENCER NAME''')
        self.Label7.configure(width=134)

        self.Label8 = Label(top)
        self.Label8.place(relx=0.01, rely=0.62, height=31, width=134)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''DRIVER NAME''')
        self.Label8.configure(width=134)

        self.Label9 = Label(top)
        self.Label9.place(relx=0.01, rely=0.7, height=31, width=134)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''MONITOR NAME''')
        self.Label9.configure(width=134)

        self.Label10 = Label(top)
        self.Label10.place(relx=0.52, rely=0.12, height=31, width=134)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''SCOREBOARD NAME''')
        self.Label10.configure(width=134)

        self.Label11 = Label(top)
        self.Label11.place(relx=0.52, rely=0.21, height=31, width=134)
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''AGENT NAME''')
        self.Label11.configure(width=134)

        self.Label12 = Label(top)
        self.Label12.place(relx=0.51, rely=0.29, height=31, width=154)
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''ENVIRONMENT NAME''')
        self.Label12.configure(width=154)

        self.Label13 = Label(top)
        self.Label13.place(relx=0.52, rely=0.37, height=31, width=134)
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''TEST NAME''')
        self.Label13.configure(width=134)

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.19, rely=0.29, relheight=0.06, relwidth=0.14)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=FIDS_support.MODPORTN)
        self.Entry3.configure(width=124)

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.19, rely=0.37, relheight=0.06, relwidth=0.14)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(textvariable=FIDS_support.SEQUENCE_ITEMN)
        self.Entry4.configure(width=124)

        self.Entry5 = Entry(top)
        self.Entry5.place(relx=0.19, rely=0.45, relheight=0.06, relwidth=0.14)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(textvariable=FIDS_support.SEQUENCEN)
        self.Entry5.configure(width=124)

        self.Entry6 = Entry(top)
        self.Entry6.place(relx=0.19, rely=0.53, relheight=0.06, relwidth=0.14)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(textvariable=FIDS_support.SEQUENCERN)
        self.Entry6.configure(width=124)

        self.Entry7 = Entry(top)
        self.Entry7.place(relx=0.19, rely=0.62, relheight=0.06, relwidth=0.14)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(textvariable=FIDS_support.DRIVERN)
        self.Entry7.configure(width=124)

        self.Entry8 = Entry(top)
        self.Entry8.place(relx=0.19, rely=0.7, relheight=0.06, relwidth=0.14)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(textvariable=FIDS_support.MONITORN)
        self.Entry8.configure(width=124)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Entry9 = Entry(top)
        self.Entry9.place(relx=0.7, rely=0.12, relheight=0.06, relwidth=0.13)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(highlightbackground="#d9d9d9")
        self.Entry9.configure(highlightcolor="black")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(selectbackground="#c4c4c4")
        self.Entry9.configure(selectforeground="black")
        self.Entry9.configure(textvariable=FIDS_support.SCOREBOARDN)
        self.Entry9.configure(width=114)

        self.Entry10 = Entry(top)
        self.Entry10.place(relx=0.7, rely=0.2, relheight=0.06, relwidth=0.13)
        self.Entry10.configure(background="white")
        self.Entry10.configure(disabledforeground="#a3a3a3")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(highlightbackground="#d9d9d9")
        self.Entry10.configure(highlightcolor="black")
        self.Entry10.configure(insertbackground="black")
        self.Entry10.configure(selectbackground="#c4c4c4")
        self.Entry10.configure(selectforeground="black")
        self.Entry10.configure(textvariable=FIDS_support.AGENTN)
        self.Entry10.configure(width=114)

        self.Entry11 = Entry(top)
        self.Entry11.place(relx=0.7, rely=0.28, relheight=0.06, relwidth=0.13)
        self.Entry11.configure(background="white")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(highlightbackground="#d9d9d9")
        self.Entry11.configure(highlightcolor="black")
        self.Entry11.configure(insertbackground="black")
        self.Entry11.configure(selectbackground="#c4c4c4")
        self.Entry11.configure(selectforeground="black")
        self.Entry11.configure(textvariable=FIDS_support.ENVIRONMENTN)
        self.Entry11.configure(width=114)

        self.Entry12 = Entry(top)
        self.Entry12.place(relx=0.7, rely=0.37, relheight=0.06, relwidth=0.13)
        self.Entry12.configure(background="white")
        self.Entry12.configure(disabledforeground="#a3a3a3")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(foreground="#000000")
        self.Entry12.configure(highlightbackground="#d9d9d9")
        self.Entry12.configure(highlightcolor="black")
        self.Entry12.configure(insertbackground="black")
        self.Entry12.configure(selectbackground="#c4c4c4")
        self.Entry12.configure(selectforeground="black")
        self.Entry12.configure(textvariable=FIDS_support.TESTN)
        self.Entry12.configure(width=114)




#def gen_ral():
  #print("fenil")



#####################Open RDL file and extract data###############
def open_file():
  
    filename = tkinter.filedialog.askopenfilename()
    print (filename) #get realpath of RDL file
    f = open(filename, 'r') #open in read mode

    #for line in f:
    #    print(line, end='') #print whole file after read - open



    ##########EXTRACT MAP NAME & ADDRESS HERE #####################
    with open(filename,'r') as searchfile:
      for line in searchfile:
        if re.search('map',line,re.I):
          MAP_NAME = re.findall(r'map\ (.*?)\@',line)
          MAP_BASE_ADDRESS = re.findall(r'x(.*?)\ ',line)
          print("MAP_NAME :", MAP_NAME)
          print("MAP_BASE_ADDRESS :", MAP_BASE_ADDRESS)
    ########## EXTRACT MAP NAME & ADDRESS HERE #########################


    ########## EXTRACT MAP TITLE, RESET, FWACCESS, HWACCESS HERE########
    infile = open(filename)
    currentstatus = False
    for line in infile:

      if line.startswith("map"):
        currentstatus = True

      if currentstatus:
        if re.search('title',line,re.I):
          MAP_TITLE = re.findall(r'title\(\"(.*?)\"\)\;',line)
          print("MAP_TITLE :", MAP_TITLE)
        if re.search('reset',line,re.I):
          MAP_RESET = re.findall(r'reset\((.*?)\)\;',line)
          print("MAP_RESET :", MAP_RESET)
        if re.search('fwaccess',line,re.I):
          MAP_FWACCESS = re.findall(r'fwaccess\((.*?)\)\;',line)
          print("MAP_FWACCESS :", MAP_FWACCESS)
        if re.search('hwaccess',line,re.I):
          MAP_HWACCESS = re.findall(r'hwaccess\((.*?)\)\;',line)
          print("MAP_HWACCESS :", MAP_HWACCESS)
      
      if line.isspace():
        currentstatus = False
    ########## EXTRACT MAP TITLE, RESET, FWACCESS, HWACCESS HERE########



    ########## GET NO OF REGISTER IN THE RDL FILE ####################
    NO_OF_REG = open(filename, 'r').read().count("reg")    
    print("NO_OF_REG : ", NO_OF_REG)
    ########## GET NO OF REGISTER IN THE RDL FILE ####################





            
    ########## CREATE LIST OF ALL REGISTERS ######################
    infileagain = open(filename)
    status = False
    default_reg = []
    for line in infileagain:

      if "reg " in line:
        status = True
      
      if status:
        if re.search('reg ',line,re.I):
          REG_NAME_i = re.findall(r'reg\ (.*?)\ \{',line)
          default_reg.append(REG_NAME_i)      
      
      if line.isspace():
        status = False
    for i in range (NO_OF_REG):
      print ("default_reg_[{}][0] : {}".format(i, default_reg[i][0]))
    ########## CREATE LIST OF ALL REGISTERS ######################  






############## HANDLES FOR REG, FIELD, BIT LINES IN THE RDL FILE #######
    infile = open(filename)
    currentstatus1 = False  ##### HANDLE OF REG IN RDL
    bit_status = False      ##### HANDLE OF BIT IN RDL
    field_status = False    ##### HANDLE OF FIELD IN RDL
    count_curl = 0          ##### INTERNAL VARIABLE WHICH COUNT CURLY BRACKET
    REG_ALL = {}            ##### DICTIONARY FOR REG DETAILED DATA
    for line in infile:
      
      if re.search('reg ',line,re.I):
        #print("count_curl_reg",count_curl)
        REG=re.findall(r'reg\ (.*?)\ \{',line)
        print("all_reg : ", REG_ALL)
        if re.search('{',line,re.I):
          count_curl = count_curl + 1
          #print("count_curl_vadhar",count_curl)
          if count_curl==1:
            currentstatus1 = True
            #print("currentstatus1 : ", currentstatus1)
          
      elif re.search('bit',line,re.I):
        if re.search('{',line,re.I):
          count_curl = count_curl + 1
          #print("count_curl_bit_vadhar",count_curl)
          if count_curl==2:
            bit_status = True
            #print("bit_status : ", bit_status)
      elif re.search('field',line,re.I):
        if re.search('{',line,re.I):
          count_curl = count_curl + 1
          #print("count_curl",count_curl)
          if count_curl==2:
            field_status = True
            #print("field_status : ", field_status)
      
      if re.search('}',line,re.I):
        count_curl = count_curl - 1
        #print("count_curl_bit_ghatad",count_curl)
        if count_curl == 0:
          currentstatus1 = False
          #print("currentstatus1 : ", currentstatus1)
        elif count_curl==1:
          bit_status = False
          field_status = False
          #print("bit_status : ", bit_status)
          #print("field_status : ", field_status)
      
      #if field_status:
        #print(line,end = '')
          
      #if bit_status:
        #print(line,end = '')
          
      if (currentstatus1 and not bit_status and not field_status):
        #print(line, end='')
        if re.search('reg ',line,re.I):
          REG_NAME=re.findall(r'reg\ (.*?)\@',line)
          REG_ADDRESS=re.findall(r'x(.*?)\ \{',line)
          REG_ALL['NAME'] = REG_NAME
          #REG_ALL['NAME'].append(REG_NAME)
          REG_ALL['ADDRESS'] = REG_ADDRESS
        if re.search('title',line,re.I):
          REG_TITLE=re.findall(r'title\(\"(.*?)\"\)',line)
          REG_ALL['TITLE'] = REG_TITLE
        if re.search('hwaccess',line,re.I):
          REG_HWACCESS=re.findall(r'hwaccess\((.*?)\)',line)
          REG_ALL['HWACCESS'] = REG_HWACCESS
        if re.search('reset',line,re.I):
          REG_RESET=re.findall(r'reset\((.*?)\)',line)
          REG_ALL['RESET'] = REG_RESET
        

    print("all_reg : ",REG_ALL)

########## HANDLES FOR REG, FIELD, BIT LINES IN THE RDL FILE #######
        

############################ Whole FIDS_TRY CODE #################
def event_click():
    DUTNAME = FIDS_support.DUTN.get()
    INTERFACENAME = FIDS_support.INTERFACEN.get()
    MODPORTNAME = FIDS_support.MODPORTN.get()
    SEQUENCE_ITEMNAME = FIDS_support.SEQUENCE_ITEMN.get()
    SEQUENCENAME = FIDS_support.SEQUENCEN.get()
    SEQUENCERNAME = FIDS_support.SEQUENCERN.get()
    DRIVERNAME = FIDS_support.DRIVERN.get()
    MONITORNAME = FIDS_support.MONITORN.get()
    SCOREBOARDNAME = FIDS_support.SCOREBOARDN.get()
    AGENTNAME = FIDS_support.AGENTN.get()
    ENVIRONMENTNAME = FIDS_support.ENVIRONMENTN.get()
    TESTNAME = FIDS_support.TESTN.get()

    #print (DUTNAME)
    #print (INTERFACENAME)
    #print (MODPORTNAME)
    #print (SEQUENCE_ITEMNAME)
    #print (SEQUENCENAME)
    #print (SEQUENCERNAME)
    #print (DRIVERNAME)
    #print (MONITORNAME)
    #print (SCOREBOARDNAME)
    #print (AGENTNAME)
    #print (ENVIRONMENTNAME)
    #print (TESTNAME)




    dut     = DUTNAME

    interf  = INTERFACENAME
    mp      = MODPORTNAME
    seq_itm = SEQUENCE_ITEMNAME
    seq     = SEQUENCENAME
    seqR    = SEQUENCERNAME
    drv     = DRIVERNAME
    mon     = MONITORNAME
    sb      = SCOREBOARDNAME
    agnt    = AGENTNAME
    env	    = ENVIRONMENTNAME
    test    = TESTNAME


    #this is the function that will make a class and write down all the contents of the class according to its type
    #the first argument is a variable that is taken as input from the user and the second argument is the original name of uvm base class stored in variable that starts with org

    def makeintf(intf, md_prt):
     final_intf = cwd+'/'+dut+'/'+dut+'_'+intf
     f_intf = open('%s.sv'%final_intf, 'w')
     
     f_intf.write("""
     
     // this is a simple interface for testing the DUT
     
     interface {0}_{1} ();
       
       
     endinterface : {0}_{1}  
     
     
     """.format(dut, intf, md_prt))
     



    def makeclass(user_input,original_class):
      final = cwd +'/'+dut+'/'+dut+'_'+user_input
      f = open('%s.sv'%final, 'w')
      
      if user_input == seq_itm:  #if class is uvm sequence item
        f.write(""" 
        class {0}_{1} extends uvm_{2};
          
          
        `uvm_object_utils_begin({0}_{1})
          
        //Define `uvm_field....
          
        `uvm_object_utils_end
        
        function new (string name "{0}_{1}");
        super.new(name);
        endfunction : new
          
        // This is a {2} class
        // Write your code from here onwards

        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class))
            
      elif user_input == seq:  #if class is uvm sequence
        f.write(""" 
        class {0}_{1} extends uvm_{2} #({0}_{3});
        
        `uvm_object_utils({0}_{1})
          
        {0}_{3} req; // this is my object handler
        
        function new (string name = "{0}_{1}");
        super.new(name);
        endfunction : new 
          
        
          
        // This is a {2} class
        // Write your code from here onwards

        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class,seq_itm))    

      elif user_input == seqR:   # if class is uvm sequencer 
          
        f.write(""" 
        class {0}_{1} extends uvm_{2} #({0}_{3});
          
        `uvm_component_utils({0}_{1})
          
        function new (string name = "{0}_{1}");
        super.new(name);
        endfunction : new 
         
        // This is a {2} class
        // Write your code from here onwards

        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class,seq_itm))
            
            
      elif user_input == drv:   # if class is uvm driver
          
        f.write(""" 
        class {0}_{1} extends uvm_{2} #({0}_{3});
          
        `uvm_component_utils({0}_{1})
         {0}_{3} req; // handler 
         
         
         virtual {0}_{4} v_{0}_{4}; 
        function new (string name = "{0}_{1}" , uvm_component parent = null);
        super.new(name, parent);
        endfunction : new         // this is new function 
         
        
        
        // UVM Connect Phase
         
        function void connect_phase(uvm_phase phase);
        
        if (!uvm_config_db #(virtual {0}_{4} ) :: get(null, " ", "{0}_{4}", this.v_{0}_{4})) begin
        `uvm_error("connect", "Virtual Interface not found")
        end
        
        endfunction : connect_phase;
        
        // UVM Run Phase
        
        task run_phase(uvm_phase phase);
         begin
             fork
             forever
             begin
             
             seq_item_port.get_next_item(req);
             
             // Write your Driver code and logic here
            
             seq_item_port.item_done();
            
             end
             join_none
             end
        endtask : run_phase
            
        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class,seq_itm,interf))
          
      elif user_input == mon:   # if class is uvm monitor
          
        f.write(""" 
        class {0}_{1} extends uvm_{2} ;
          
        `uvm_component_utils({0}_{1})
        
        uvm_analysis_port #({0}_{3}) afx;
        
        {0}_{3} req; // handler 
         
         
        virtual {0}_{4} v_{0}_{4}; 
        
        // Class Constructor
        
        function new (string name = "{0}_{1}" , uvm_component parent = null);
        super.new(name, parent);
        endfunction : new         
        
        // UVM Build Phase
        
        function void build_phase (uvm_phase phase);
         begin
         
            afx = new("afx", this);
            
         end
        endfunction : build_phase 
        
        // Connect Phase
        
        function void connect_phase(uvm_phase phase);
        
         if (!uvm_config_db #(virtual {0}_{4} ) :: get(null, " ", "{0}_{4}", this.v_{0}_{4})) begin
         `uvm_error("connect", "Virtual Interface not found")
         end
        
        endfunction : connect_phase;
        
        // UVM Run Phase
        
        task run_phase(uvm_phase phase);
         begin
             fork
             forever
             begin
             
             // Write your Monitor code and logic here
            
            
             end
             join_none
          end
         endtask : run_phase
        
        
        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class,seq_itm,interf))
                   
      elif user_input == sb:   # if class is uvm score board
        
        f.write(""" 
        class {0}_{1} extends uvm_{2};
        
        uvm_tlm_analysis_fifo #({0}_{3}) af_resp;
        
        {0}_{3} resp; // handler
         
        `uvm_component_utils({0}_{1})
        
          // Class Constructor
        
        function new (string name = "{0}_{1}" , uvm_component parent = null);
        super.new(name, parent);
        endfunction : new 
        
        // Build Phase 
        
        function void build_phase (uvm_phase phase);
          begin
         
            af_resp = new("af_resp", this);
            
          end
        endfunction : build_phase 
        
        // UVM Run Phase
        
        task run_phase(uvm_phase phase);
         begin
             fork
             forever
             begin
             
             af_resp.get(resp)
             
             
             
             // Write your Score Board code and logic here
            
             
            
             end
             join_none
          end
        endtask : run_phase
        
          
          
        // This is a {2} class
        // Write your code from here onwards

        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class,seq_itm))
        
       
      elif user_input == agnt:   # if class is uvm agent
      
      
       f.write(""" 
        class {0}_{1} extends uvm_{2};
        
        {0}_{4} seq_agent;
        {0}_{5} seqR_agent;
        {0}_{6} driver_agent;
        {0}_{7} monitor_agent;
        {0}_{8} sb_agent;
         
        `uvm_component_utils_begin({0}_{1})
          `uvm_field_object(seq_agent    , UVM_ALL_ON)
          `uvm_field_object(seqR_agent   , UVM_ALL_ON)
          `uvm_field_object(driver_agent , UVM_ALL_ON)
          `uvm_field_object(monitor_agent, UVM_ALL_ON)
          
        
        `uvm_component_utils_end
        
        function void build_phase(uvm_phase phase);
            begin
             
             super.build_phase(phase);
             seq_agent = {0}_{4}::type_id::create("seq_agent", this);
             seqR_agent = {0}_{5}::type_id::create("seqR_agent", this);
             driver_agent = {0}_{6}::type_id::create("{0}_{6}", this);
             monitor_agent = {0}_{7}::type_id::create("{0}_{7}", this);
             sb_agent = {0}_{8}::type_id::create("{0}_{8}", this);
            
            end
        
        
        endfunction: build_phase;
        
        function void connect_phase(uvm_phase phase);
        
            driver_agent.seq_item_port.connect(seqR_agent.seq_item_export);
            monitor_agent.afx.connect(sb_agent.af_resp.analysis_export);
          
        endfunction : connect_phase  
        
        task run_phase(uvm_phase phase);
            
            phase.raise_objection(this, "start of test");
            //// test check this one
            phase.drop_objection(this, "end of test");
        
        endtask : run_phase;
        
        function new(string name = "{0}_{1}", uvm_component parent = null);
            super.new(name, parent);
        endfunction
        

        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class,seq_itm, seq, seqR, drv, mon, sb))    
        
    # ////////////////// UVM env ///////////////////
       
      elif user_input == env:   # if class is uvm agent
      
      
       f.write(""" 
        class {0}_{1} extends uvm_{2};
        
        {0}_{3} agent_env;
         
        `uvm_component_utils_begin({0}_{1})
          `uvm_field_object(agent_env    , UVM_ALL_ON) 
        `uvm_component_utils_end
        
        function void build_phase(uvm_phase phase);
            begin
             
             super.build_phase(phase);
             agent_env = {0}_{3}::type_id::create("agent_env", this);
            
            end
        
        
        endfunction: build_phase;
        
        function void connect_phase(uvm_phase phase);
        
         super.connect_phase(phase);
     
        endfunction : connect_phase  
        
        
        function new(string name = "{0}_{1}", uvm_component parent = null);
            super.new(name, parent);
        endfunction
        

        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class,agnt))    
     
    #/////////////////// UVM Test ///////////////////////////////

      elif user_input == test:   #if class is uvm test
       
       
       f.write(""" 
        class {0}_{1} extends uvm_{2};
        
        {0}_{3} env_test;
         
        `uvm_component_utils_begin({0}_{1})
        `uvm_field_object(env_test , UVM_ALL_ON) 
        `uvm_component_utils_end
        
        function void build_phase(uvm_phase phase);
            begin
             
             super.build_phase(phase);
             env_test = {0}_{3}::type_id::create("env_agent", this);
            
            end
        
        
        endfunction: build_phase;
        
        
        
        function new(string name = "{0}_{1}", uvm_component parent = null);
            super.new(name, parent);
        endfunction
        

        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class,env))    
       
             
      else:
      
       f.write("""
        class {0}_{1} extends uvm_{2};
          
        // This is a {2} class
        // Write your code from here onwards

        endclass : {0}_{1}
          
          """.format(dut,user_input,original_class,seq_itm)) 
      
        
        

    mkedir(dut)

    makeintf(interf, mp)

    makeclass(seq_itm, org_seq_itm)

    makeclass(seq, org_seq)

    makeclass(seqR, org_seqR)

    makeclass(drv, org_drv)

    makeclass(mon, org_mon)

    makeclass(sb, org_sb)

    makeclass(agnt, org_agnt)

    makeclass(env, org_env)

    makeclass(test, org_test)




def vp_start_gui():
  '''Starting point when module is the main routine.'''
  global val, w, root
  root = Tk()
  FIDS_support.set_Tk_var()
  top = FIDS (root)
  FIDS_support.init(root, top)
  root.mainloop()

w = None
def create_FIDS(root, *args, **kwargs):
  '''Starting point when module is imported by another program.'''
  global w, w_win, rt
  rt = root
  w = Toplevel (root)
  FIDS_support.set_Tk_var()
  top = FIDS (w)
  FIDS_support.init(w, top, *args, **kwargs)
  return (w, top)

def destroy_FIDS():
  global w
  w.destroy()
  w = None
  top.geometry("860x486+394+73")
  top.title("test")
  top.configure(background="#d9d9d9")
  top.configure(highlightbackground="#d9d9d9")  
  top.configure(highlightcolor="black")




    

if __name__ == '__main__':
    vp_start_gui()

#add default args in all the functions - Oct 21

