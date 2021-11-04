import PySimpleGUI as Pawan__Simple__GUI #This is the main Module to generate the User Interface


Pawan__Simple__GUI.theme('LightBlue2') # Here we set the Theme of the GUI (Colours and Appearance) using a list of Themes already built into the PySimpleGUI Module



layout = [  [Pawan__Simple__GUI.Text('Sample PyGUI Application by Pawan')],
            [Pawan__Simple__GUI.Text('Enter any text of your choice'), Pawan__Simple__GUI.InputText()],
            [Pawan__Simple__GUI.Button("Print Value in Text Box to Console",bind_return_key=True), Pawan__Simple__GUI.Cancel("Exit The Sample PySimpleGUI Application")], [Pawan__Simple__GUI.Text("Choose a file: "), Pawan__Simple__GUI.FileBrowse(file_types=(("JPG", "*.jpg"),))]]


#Here we set the main Window and add in the layout and provide the icon that is to be used. Please note we do not provide a path as icon was in the same folder as the python script.
Sample__Window__Layout = Pawan__Simple__GUI.Window('Sample PyGUI Application by Pawan', layout, icon = 'Happy.ico')

#we create a never-ending loop
while True:
	#We read all events and the values within the main Window
	event, values = Sample__Window__Layout.read()

	#If window is exited by X button (WINDOW_ClOSED) or via Exit Button(Exit The Sample PySimpleGUI Application)
	if event in (Pawan__Simple__GUI.WINDOW_CLOSED, 'Exit The Sample PySimpleGUI Application'):
		break #loop is broken up

	#We take in the value from Text Box that user entered
	TextBox__Value = values[0]
	if TextBox__Value == "":#If nothing was entered in text box
		print("No text inoput")
	else:
		print('You entered ', values[0])
Sample__Window__Layout.close() #To ensdsure proper window closure and cleanup
print("Application executed successfully")