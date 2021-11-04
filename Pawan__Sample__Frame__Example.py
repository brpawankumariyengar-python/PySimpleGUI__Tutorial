import PySimpleGUI as Pawan__Simple__GUI
#set the theme for the screen/window
Pawan__Simple__GUI.theme("DarkTanBlue")
#define layout
options=[[Pawan__Simple__GUI.Frame('Choose your Bread',[[Pawan__Simple__GUI.Radio('Whole Wheat','rd_bread', key ='Whole Wheat'),
                                         Pawan__Simple__GUI.Radio('Multigrain','rd_bread', key='Multigrain'),
                                     Pawan__Simple__GUI.Radio('Normal','rd_bread', key='Normal'),
                                         Pawan__Simple__GUI.Radio('Stuffed','rd_bread', key='Stuffed'),
                                         Pawan__Simple__GUI.Radio('Healthy seeds','rd_bread', key='Healthy seeds')]],border_width=10)],
        [Pawan__Simple__GUI.Frame('Choose your Toppings',[[Pawan__Simple__GUI.Checkbox('Pepperoni',key='Pepperoni'),
                                           Pawan__Simple__GUI.Checkbox('Mushroom',key='Mushroom'),
                                         Pawan__Simple__GUI.Checkbox('Corn',key='Corn'),
                                           Pawan__Simple__GUI.Checkbox('Cherry Tomatoes',key='Cherry Tomatoes'),
                                           Pawan__Simple__GUI.Checkbox('Olives',key='Olives')]], title_location='ne', background_color='white' )],
        [Pawan__Simple__GUI.Frame('Choose your Sauces', [[Pawan__Simple__GUI.Checkbox('Onion',key='Onion Sauce'),
                                          Pawan__Simple__GUI.Checkbox('Paprika',key='Paprika'),
                                     Pawan__Simple__GUI.Checkbox('Schezwan',key='Schezwan'),
                                          Pawan__Simple__GUI.Checkbox('Tandoori',key='Tandoori')]],title_color='yellow', border_width=3)],
         [Pawan__Simple__GUI.Button('Submit', font=('Times New Roman',12))]]
choices = [[Pawan__Simple__GUI.Frame('Customise Your Pizza', layout= options)]]
        
items_chosen = [[Pawan__Simple__GUI.Text('You have Chosen')],
                [Pawan__Simple__GUI.Text("", size=(50,3),key='options')]]
              
# Create layout with two columns using precreated frames
layout = [[Pawan__Simple__GUI.Column(choices, element_justification='c'), Pawan__Simple__GUI.Column(items_chosen, element_justification='c')]]

#Define Window
Sample__Window__Layout =Pawan__Simple__GUI.Window("Column and Frame",layout)
#Read  values entered by user
event,values=Sample__Window__Layout.read()
#access all the values and if selected add them to a string
strx=""
for val in values:
    if Sample__Window__Layout.find_element(val).get()==True:
        strx=strx+ " "+ val+","
        print(strx)

while True:
    event, values = Sample__Window__Layout.read()  # Read  values entered by user
    if event == Pawan__Simple__GUI.WIN_CLOSED:  # If window is closed by user terminate While Loop
        break
    if event == 'Submit':# If submit button is clicked display chosen values
        Sample__Window__Layout['options'].update(strx)  # output the final string
#Close Window
Sample__Window__Layout.close()    