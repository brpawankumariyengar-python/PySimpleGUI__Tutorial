#Sample Script to demonstrate all the ELEMENTS athat are most commonly used

import PySimpleGUI as Pawan__Simple__GUI

Layout = [
[Pawan__Simple__GUI.Button("This__Is__A__Buttton")],
[Pawan__Simple__GUI.Text("This is a Label")],
[Pawan__Simple__GUI.InputText("This is a Text Box")]
]


Sample__Window__Layout = Pawan__Simple__GUI.Window('Sample PyGUI Application by Pawan', Layout, icon = 'Happy.ico')
Sample__Window__Layout.read()