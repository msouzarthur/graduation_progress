# author: @msouzarthur

import csv, os
import pandas as pd
import customtkinter
from tkinter import *
from tkinter import filedialog as fd
from pypdf import PdfReader
from PIL import Image

columns = ['CODIGO','CADEIRA','STATUS','MEDIA']

class CourseFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="COURSE", **kwargs):   

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.book_image             = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(128, 128))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
            
        self.header_name = header_name

        if graduationId == 0:
            msg_2 = "CARREGAR GRADE CURRICULAR"
            course = "SELECIONE O CURSO"
            btn_course_image = self.download_image
        else:
            msg_2 = "ATUALIZAR GRADE CURRICULAR"
            course = coursesDict.get(graduationId)
            btn_course_image = self.refresh_image

        self.label_course_img = customtkinter.CTkLabel(self, text="", image=self.book_image)
        self.label_course_img.pack(padx=20, pady=60)
        
        self.label_course_name = customtkinter.CTkLabel(self, text=course)
        self.label_course_name.pack(padx=20, pady=10)
        
        self.button_course = customtkinter.CTkButton(self, text=msg_2,  compound="left", image=btn_course_image)
        self.button_course.pack(padx=20, pady=10)

class GraduationFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="COURSE", **kwargs):    

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.book_image             = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(128, 128))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
            
        self.header_name = header_name

        if graduationId == 0:
            msg_2 = "CARREGAR GRADE CURRICULAR"
            course = "SELECIONE O CURSO"
            btn_course_image = self.download_image
        else:
            msg_2 = "ATUALIZAR GRADE CURRICULAR"
            course = coursesDict.get(graduationId)
            btn_course_image = self.refresh_image

        self.label_course_img = customtkinter.CTkLabel(self, text="", image=self.book_image)
        self.label_course_img.pack(padx=20, pady=60)
        
        self.label_course_name = customtkinter.CTkLabel(self, text=course)
        self.label_course_name.pack(padx=20, pady=10)
        
        self.button_course = customtkinter.CTkButton(self, text=msg_2,  compound="left", image=btn_course_image)
        self.button_course.pack(padx=20, pady=10)

class LoginFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="LOGIN", **kwargs):
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.profile_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(128, 128))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        if studentName == 'CARREGUE SEU HISTÓRICO':
            msg_1 = "CARREGAR HISTÓRICO"
            btn_student_image = self.download_image
        else:
            msg_1 = "ATUALIZAR HISTÓRICO"
            btn_student_image = self.refresh_image

        self.label_student_img = customtkinter.CTkLabel(self, text="", image=self.profile_image)
        self.label_student_img.pack(padx=20, pady=60)
        
        self.label_student_name = customtkinter.CTkLabel(self, text=studentName)
        self.label_student_name.pack(padx=20, pady=10)
        
        self.button_student = customtkinter.CTkButton(self, text=msg_1, compound='left', image=btn_student_image)
        self.button_student.pack(padx=20, pady=10)
   
class NavigationFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="LOGIN", **kwargs):

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.home_image_small       = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
        self.profile_image_small    = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(20, 20))
        self.book_image_small       = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(20, 20))
        self.settings_image_small   = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "settings.png")), size=(20, 20))
        
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        
        self.home_btn = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="MENU",
                                                fg_color="transparent", text_color=("gray10", "gray90"), 
                                                hover_color=("gray70", "gray30"), image=self.home_image_small, anchor="w")
        self.home_btn.pack(pady=8)
        
        self.profile_btn = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="ALUNO",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), 
                                                      hover_color=("gray70", "gray30"), anchor="w", image=self.profile_image_small)
        self.profile_btn.pack(pady=8)
        
        self.graduation_btn = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="CURSO",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), 
                                                      hover_color=("gray70", "gray30"), anchor="w", image=self.book_image_small)
        self.graduation_btn.pack(pady=8)

        self.settings_btn = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="ESTATÍSTICAS",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), 
                                                      hover_color=("gray70", "gray30"), anchor="w", image=self.settings_image_small)
        self.settings_btn.pack(pady=8)

class StudentFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="PROFILE", **kwargs):

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.profile_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(128, 128))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        if studentName == 'CARREGUE SEU HISTÓRICO':
            msg_1 = "CARREGAR HISTÓRICO"
            btn_student_image = self.download_image
        else:
            msg_1 = "ATUALIZAR HISTÓRICO"
            btn_student_image = self.refresh_image

        self.label_student_img = customtkinter.CTkLabel(self, text="", image=self.profile_image)
        self.label_student_img.pack(padx=20, pady=60)
        
        self.label_student_name = customtkinter.CTkLabel(self, text=studentName)
        self.label_student_name.pack(padx=20, pady=10)
        
        self.button_student = customtkinter.CTkButton(self, text=msg_1, compound='left', image=btn_student_image)
        self.button_student.pack(padx=20, pady=10)

class HomeFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="HOME", **kwargs):

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.home_image_small       = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
        self.profile_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(128, 128))
        self.profile_image_small    = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(20, 20))
        self.book_image             = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(128, 128))
        self.book_image_small       = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(20, 20))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
        
        # configure grid layout      
        Grid.columnconfigure(self, (0,1,2,3,4),weight=1)
        Grid.rowconfigure(self, (0,1), weight=1)
        
        # create login frame
        self.login_frame = LoginFrame(self, header_name="USUÁRIO")
        self.login_frame.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        # create course frame
        self.course_frame = CourseFrame(self, header_name="CURSO")
        self.course_frame.grid(row=0, column=3, padx=(0,30), pady=(30,0))
        
        # create button 
        self.home_frame_button = customtkinter.CTkButton(self, text="CONTINUAR")
        self.home_frame_button.grid(row=1, column=2, padx=0, pady=30, sticky="W")
        
class StatisticsFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="HOME", **kwargs):

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.home_image_small       = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
        self.profile_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(128, 128))
        self.profile_image_small    = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(20, 20))
        self.book_image             = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(128, 128))
        self.book_image_small       = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(20, 20))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
        

class App(customtkinter.CTk):

    def __init__(self):

        super().__init__()

        self.title("graduation progress")
        self.geometry("1000x600")

        # configure grid layout      
        Grid.columnconfigure(self, (0,1,2),weight=1)
        Grid.rowconfigure(self, (0,1), weight=1)
        
        # create home frame
        self.home_frame = HomeFrame(self, header_name="HOME")
        self.home_frame.home_frame_button.configure(command=self.statistics_button_event)
        self.home_frame.login_frame.button_student.configure(command=self.student_button_event)
        self.home_frame.course_frame.button_course.configure(command=self.graduation_button_event)
        self.home_frame.grid(pady=30)

        # create navigation frame
        self.navigation_frame = NavigationFrame(self, header_name="SIDEMENU")
        self.navigation_frame.grid(row=0, column=0, sticky="NSW", rowspan=2)
        self.navigation_frame.home_btn.configure(command=self.home_button_event)
        self.navigation_frame.profile_btn.configure(command=self.student_button_event)
        self.navigation_frame.graduation_btn.configure(command=self.graduation_button_event)
        self.navigation_frame.settings_btn.configure(command=self.statistics_button_event)

        # create statistic frame
        self.statistics_frame = StatisticsFrame(self, corner_radius=0, fg_color="transparent")
        self.statistics_frame.grid(pady=30)

        # create student frame
        self.student_frame = StudentFrame(self, corner_radius=0, fg_color="transparent")
        self.student_frame.grid(pady=30)

        # create graduation frame
        self.graduation_frame = CourseFrame(self, corner_radius=0, fg_color="transparent")
        self.graduation_frame.grid(pady=30)
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):

        self.navigation_frame.home_btn.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.navigation_frame.profile_btn.configure(fg_color=("gray75", "gray25") if name == "student" else "transparent")
        self.navigation_frame.graduation_btn.configure(fg_color=("gray75", "gray25") if name == "graduation" else "transparent")
        self.navigation_frame.settings_btn.configure(fg_color=("gray75", "gray25") if name == "statistics" else "transparent")

        if studentName == 'CARREGUE SEU HISTÓRICO':
            self.home_frame.home_frame_button.configure(fg_color="transparent", text="CARREGUE SEU HISTÓRICO")
        if graduationId == 0:
            self.home_frame.home_frame_button.configure(fg_color="transparent", text="SELECIONE SEU CURSO")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew", pady=30)
        else:
            self.home_frame.grid_forget()
        if name == "student":
            self.student_frame.configure(fg_color=("gray75", "gray25"))
            self.student_frame.grid(row=0, column=1, sticky="nsew", pady=30)
        else:
            self.student_frame.grid_forget()
        if name == "graduation":
            self.graduation_frame.configure(fg_color=("gray75", "gray25"))
            self.graduation_frame.grid(row=0, column=1, sticky="nsew", pady=30)
        else:
            self.graduation_frame.grid_forget()
        if name == "statistics":
            self.statistics_frame.configure(fg_color=("gray75", "gray25"))
            self.statistics_frame.grid(row=0, column=1, sticky="nsew", pady=30)
        else:
            self.statistics_frame.grid_forget()
        
    def home_button_event(self):
        self.select_frame_by_name("home")

    def student_button_event(self):
        self.select_frame_by_name("student")

    def graduation_button_event(self):
        self.select_frame_by_name("graduation")
    
    def statistics_button_event(self):
        self.select_frame_by_name("statistics")


def load_courses():
    # courses dictionary
    print("carregando cursos", end=' ')
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"docs/courses_file.csv")
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            coursesDict = dict((rows[0],rows[1]) for rows in reader)
        print(u"\u2713") #charmap error
        return coursesDict
    except:
        pass
        print(u"\u2717") #charmap error

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

def extract_name(target):
    # Nome: Matrícula: Aluno: Curso: Ano/semestre:
    name = target.split("Nome: ")[1]
    name = name.split("Curso: ")[0]
    return name.strip()

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

def load_student_file():
    global studentName, graduationId
    studentFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"docs/historico_aluno.pdf")
    print('carregando historico do aluno', end=' ')    
    try:
        reader = PdfReader(studentFile)
        studentHist = extract_content(reader)
        studentName = extract_name(studentHist)
        graduationId = extract_id(studentHist)
        studentHist = extract_disciplines(studentHist)
        print(u"\u2713") #charmap error
        return studentHist
    except:
        pass
        print(u"\u2717") #charmap error
    
if __name__=='__main__':

    studentName = 'CARREGUE SEU HISTÓRICO'
    graduationId = 0

    studentFile = load_student_file() 
    coursesDict = load_courses()

    app = App()
    app.mainloop()
    