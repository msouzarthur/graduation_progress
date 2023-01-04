# author: @msouzarthur

import csv
import pandas as pd
import customtkinter
from tkinter import *
from tkinter import filedialog as fd
from pypdf import PdfReader

# coursesFile = r".\docs\lista_cursos.csv"
# studentFile = r".\docs\historico_aluno.pdf"
# courseFile = r".\docs\grade_curso.pdf"

columns = ['CODIGO','CADEIRA','STATUS','MEDIA']
degreeCourses = {
    'Ciência da Computação': 'https://cobalto.ufpel.edu.br/portal/cadastros/curriculoPublico/visualizar/100',
    'Engenharia de Computação': 3910,
    'Matemática': 'https://cobalto.ufpel.edu.br/portal/cadastros/curriculoPublico/visualizar/93',
    'Química': 'https://cobalto.ufpel.edu.br/portal/cadastros/curriculoPublico/visualizar/112',
}


class App(customtkinter.CTk):
        
    def button_click_event():
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Test")
        filename = fd.askopenfilename()
        print(filename)
        print("Number:", dialog.get_input())

    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("Grade de Cursos")
        btn_hist = customtkinter.CTkButton(self, text="Carregar Histórico") #, command=loadHist)
        
        optionmenu_var = customtkinter.StringVar(value="Selecionar Curso")  # set initial value

        combobox = customtkinter.CTkComboBox(
            master=self,
            values=coursesDict.keys(),
            command=optionmenu_callback,
            variable=optionmenu_var
        )

        combobox.pack(padx=20, pady=10)

        btn_hist.place(relx=0.5, rely=0.5, anchor=CENTER)
        entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        entry.pack(padx=20, pady=10)
        button = customtkinter.CTkButton(self, text="Open Dialog", command=App.button_click_event)
        button.place(relx=0.5, rely=0.5, anchor=CENTER)



def load_courses():
    # Dicionário de cursos
    print("carregando cursos", end=' ')
    coursesFile = r'C:\Users\arthu\Desktop\graduation_progress\docs\lista_cursos.csv'
    with open(coursesFile, 'r') as f:
        reader = csv.reader(f)
        coursesDict = dict((rows[0],rows[1]) for rows in reader)
    print(u"\u2713")
    return coursesDict

def optionmenu_callback(choice):
    print("clicked:", choice)
    print("code:", coursesDict[choice])

def extract_curriculum(target):
    curriculum = []
    target = target.split("\n")
    for t in target:
        if 'Semestre' in t or 'Total: ' in t or 'COMPLEMENTARES' in t:
            pass
        elif len(t.split(' '))>=5:
            cod = t.split(' ')[0]
            if 'Centro' in t:
                dsc = t.split('Centro')[0]
                dsc = dsc.split(' ',1)[-1]
            elif 'Departamento' in t:
                dsc = t.split('Departamento')[0]
                dsc = dsc.split(' ',1)[-1]
            type = t.split(' DISCIPLINA')[1].strip()
            type = type.split(' ')[0]
            credits = t.split(" DISCIPLINA")[0][-1].strip()
            curriculum.append([cod, dsc, type, credits])
    return curriculum    

def extract_content(target):
    content = []
    for page in target.pages:
        content.append(page.extract_text())
    return '\n'.join([str(page) for page in content])
    
def extract_id(target):
    cod = target.split("Curso: ")[1]
    return cod.split(" ")[0].strip()

def extract_disciplines(target):
    disciplines = []
    target = target.split('\n')
    for disc in target:
        if '/' not in disc and disc[0].isnumeric() and len(disc) > 8:
            cod = disc.split(" ")[0].strip()
            
            med = disc.split(" ")[-2].strip()
            if med == 'MAT':
                med = ''
                
            if 'APR' in disc:
                cad = disc.split(" APR")[0].strip()
                status = 'APR'
            if 'DSP' in disc:
                cad = disc.split(" DSP")[0].strip()
                status = 'DSP'
            if 'TRC' in disc:
                cad = disc.split(" TRC")[0].strip()
                status = 'TRC'
            if 'CANC' in disc:
                cad = disc.split(" CANC")[0].strip()
                status = 'CANC'
            if 'REP' in disc:
                cad = disc.split(" REP")[0].strip()
                status = 'REP'
            if 'INF' in disc:
                cad = disc.split(" INF")[0].strip()
                status = 'INF'
            cad = cad.split('- ')[-1].strip()
            disciplines.append([cod,cad,status,med])
    return disciplines

if __name__=='__main__':

    coursesDict = load_courses()
    
    app = App()
    app.mainloop()

    # Dataframe do histórico
    print('carregando histórico do aluno', end=' ')    
    reader = PdfReader(studentFile)
    studentHist = extract_content(reader)
    studentHist = extract_disciplines(studentHist)
    print(u"\u2713")

    # extrai id do curso
    graduationId = extract_id(reader.pages[0].extract_text())

    df_student = pd.DataFrame(data=studentHist,columns=columns)
