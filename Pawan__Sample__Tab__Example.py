import PySimpleGUI as Pawan__Simple__GUI

#define layout
layout1 = [[Pawan__Simple__GUI.Text('Name', size=(10,1)),Pawan__Simple__GUI.Input('',key='eName')],
           [Pawan__Simple__GUI.Text('Date of Birth', size=(10,1)),Pawan__Simple__GUI.Input('',key='eDob')],
           [Pawan__Simple__GUI.Text('Phone No', size=(10,1)),Pawan__Simple__GUI.Input('',key='ePhone')],
           [Pawan__Simple__GUI.Text('Email ID', size=(10,1)),Pawan__Simple__GUI.Input('',key='eEmail')],
           [Pawan__Simple__GUI.Button('Save Personal Details')]]
layout2=[[Pawan__Simple__GUI.Text('Highest Qualfication', size=(15,1)),Pawan__Simple__GUI.Input('',key='eQual')],
           [Pawan__Simple__GUI.Text('Year of Qualifying', size=(15,1)),Pawan__Simple__GUI.Input('',key='eYoq')],
           [Pawan__Simple__GUI.Text('Grade', size=(15,1)),Pawan__Simple__GUI.Input('',key='eGrade')],
           [Pawan__Simple__GUI.Text('University/College', size=(15,1)),Pawan__Simple__GUI.Input('',key='eQUniv')],
         [Pawan__Simple__GUI.Button('Save Education Details')]]
layout3= [[Pawan__Simple__GUI.Text('Last Job', size=(10,1)),Pawan__Simple__GUI.Input('',key='eLastJ')],
           [Pawan__Simple__GUI.Text('From Date', size=(10,1)),Pawan__Simple__GUI.Input('',key='eJFdt')],
           [Pawan__Simple__GUI.Text('To Date', size=(10,1)),Pawan__Simple__GUI.Input('',key='eJTdt')],
           [Pawan__Simple__GUI.Text('Company Name', size=(10,1)),Pawan__Simple__GUI.Input('',key='eLJcmpy')],
          [Pawan__Simple__GUI.Button('Save Experience Details')]]
#Define Layout with Tabs         
tabgrp = [[Pawan__Simple__GUI.TabGroup([[Pawan__Simple__GUI.Tab('Personal Details', layout1, title_color='Red',border_width =10, background_color='Green',
                                tooltip='Personal details', element_justification= 'center'),
                    Pawan__Simple__GUI.Tab('Education', layout2,title_color='Blue',background_color='Yellow'),
                    Pawan__Simple__GUI.Tab('Experience', layout3,title_color='Black',background_color='Pink',
                           tooltip='Enter  your Lsst job experience')]], tab_location='centertop',
                       title_color='Red', tab_background_color='Purple',selected_title_color='Green',
                       selected_background_color='Gray', border_width=5), Pawan__Simple__GUI.Button('Close')]]  
        
#Define Sample__Window__Layout
Sample__Window__Layout =Pawan__Simple__GUI.Sample__Window__Layout("Tabs",tabgrp)
#Read  values entered by user
event,values=Sample__Window__Layout.read()
#access all the values and if selected add them to a string
Sample__Window__Layout.close()    