# Python Script Columns Example
import PySimpleGUI as Pawan__Simple__GUI

#set the theme for the screen/window
Pawan__Simple__GUI.theme("DarkTanBlue")

#define layout
sz=(10,20)
col1=[[Pawan__Simple__GUI.Text('Column1', background_color='red', size=sz)]]
col2=[[Pawan__Simple__GUI.Text('Column2', background_color='green', size=sz)]]
col3=[[Pawan__Simple__GUI.Text('Column3', background_color='brown', size=sz)]]
col4=[[Pawan__Simple__GUI.Text('Column4', background_color='blue', size=sz)]]

layout = [[Pawan__Simple__GUI.Column(col1, element_justification='c' ), Pawan__Simple__GUI.Column(col2, element_justification='c')
          , Pawan__Simple__GUI.Column(col3, element_justification='c'), Pawan__Simple__GUI.Column(col4, element_justification='c')]]

Sample__Window__Layout =Pawan__Simple__GUI.Window("Column and Frame",layout)
event,values=Sample__Window__Layout.read()

Sample__Window__Layout.close()  