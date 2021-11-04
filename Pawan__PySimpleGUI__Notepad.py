#A minimalist Notepad built with the PySimpleGUI 

import PySimpleGUI as Pawan__Simple__GUI
import pathlib
Pawan__Simple__GUI.ChangeLookAndFeel('BrownBlue') # change style

WIN_W = 90
WIN_H = 25
file = None

menu_layout = [['File', ['New (Ctrl+N)', 'Open (Ctrl+O)', 'Save (Ctrl+S)', 'Save As', '---', 'Exit']],
              ['Tools', ['Charecter Count'],]]

layout = [[Pawan__Simple__GUI.Menu(menu_layout)],
          [Pawan__Simple__GUI.Text('<<< New File >>>', font=('Verdana', 10), size=(WIN_W, 1), key='_INFO_')],
          [Pawan__Simple__GUI.Multiline(font=('Verdana', 12), size=(WIN_W, WIN_H), key='_BODY_')]]

Sample__Window__Layout = Pawan__Simple__GUI.Window('Notepad', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
Sample__Window__Layout.maximize()
Sample__Window__Layout['_BODY_'].expand(expand_x=True, expand_y=True)

def Charecter_Count():
    Main__String__Entered = values['_BODY_']
    Charecter__Count__Int = len(Main__String__Entered)
    hu = "Charecter Count is:    " + str(Charecter__Count__Int)
    Sample__Window__Layout['_INFO_'](hu)

def new_file():
    '''Reset body and info bar, and clear filename variable'''
    Sample__Window__Layout['_BODY_'].update(value='')
    Sample__Window__Layout['_INFO_'].update(value='<<< New File >>>')
    file = None
    return file

def open_file():
    '''Open file and update the infobar'''
    filename = Pawan__Simple__GUI.popup_get_file('Open', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        Sample__Window__Layout['_BODY_'].update(value=file.read_text())
        Sample__Window__Layout['_INFO_'].update(value=file.absolute())
        return file

def save_file(file):
    '''Save file instantly if already open; otherwise use `save-as` popup'''
    if file:
        file.write_text(values.get('_BODY_'))
    else:
        save_file_as()

def save_file_as():
    '''Save new file or save existing file with another name'''
    filename = Pawan__Simple__GUI.popup_get_file('Save As', save_as=True, no_window=True)
    if filename:
        file = pathlib.Path(filename)
        file.write_text(values.get('_BODY_'))
        Sample__Window__Layout['_INFO_'].update(value=file.absolute())
        return file

while True:
    event, values = Sample__Window__Layout.read()
    if event in('Exit', None):
        break
    if event in ('New (Ctrl+N)', 'n:78'):
        file = new_file()
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()
    if event in ('Save (Ctrl+S)', 's:83'):
        save_file(file)
    if event in ('Save As',):
        file = save_file_as()   
    if event in ('Charecter Count',):
        Charecter_Count()