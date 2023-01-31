# author: @msouzarthur

import csv, os, shutil, customtkinter, tkinter, time, webbrowser
import pandas as pd
from tkinter import filedialog as fd
from tkinter import ttk
from pypdf import PdfReader
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class CourseFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="COURSE", **kwargs):   

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.book_image             = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(128, 128))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
            
        self.header_name = header_name

        self.label_course_img = customtkinter.CTkLabel(self, text="", image=self.book_image)
        self.label_course_img.pack(padx=20, pady=60)
        
        self.label_course_name = customtkinter.CTkLabel(self, 
                                                        text=studentDict.get("Curso"))
        self.label_course_name.pack(padx=20, pady=10)
        
        self.button_course = customtkinter.CTkButton(self, 
                                                    text="ATUALIZAR GRADE CURRICULAR" if logged else "CARREGAR GRADE CURRICULAR",
                                                    compound="left",   
                                                    image=self.refresh_image if logged else self.download_image)
        self.button_course.pack(padx=20, pady=10)

class CurriculumTable(customtkinter.CTkFrame):
    
    def __init__(self, *args, header_name="TABLE", **kwargs):
        
        super().__init__(*args, **kwargs)
                
        import sv_ttk

        root = tkinter.Frame()
        
        tree = ttk.Treeview(self, columns=('CÓDIGO', 'CADEIRA', 'CRÉDITOS', 'TIPO'), show='headings')
        cols = ('CÓDIGO', 'CADEIRA', 'CRÉDITOS', 'TIPO')
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')

        for index, row in dfCurriculum.iterrows():
            tree.insert("",0,text=index,values=list(row))
            
        tree.grid(row=0, column=0, sticky='nsew')
        sv_ttk.set_theme("dark")

class GraduationFrame(customtkinter.CTkFrame):

    def set_value_obr(self, event):
        if int(self.entry_hour_obr.get()) > 100:
            hour_obr = int(self.entry_hour_obr.get())

    def set_value_opt(self, event):
        if int(self.entry_hour_opt.get()) >= 0:
            hour_opt = int(self.entry_hour_opt.get())

    def __init__(self, *args, header_name="COURSE", **kwargs):    

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.book_image             = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(64, 64))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
            
        self.header_name = header_name

        # create top frame
        self.top_frame = customtkinter.CTkFrame(self)
        self.top_frame.configure(fg_color="transparent")
        self.top_frame.pack(pady=35)
        
        self.top_frame_left = customtkinter.CTkFrame(self.top_frame)
        self.top_frame_left.configure(fg_color="transparent")
        self.top_frame_left.pack(padx=30, side="left")

        self.top_frame_right = customtkinter.CTkFrame(self.top_frame)
        self.top_frame_right.configure(fg_color="transparent")
        self.top_frame_right.pack(padx=30, side="right")

        self.label_course_img = customtkinter.CTkLabel(self.top_frame_left, text="", image=self.book_image)
        self.label_course_img.pack()
        
        self.label_course_name = customtkinter.CTkEntry(self.top_frame_right, placeholder_text=studentDict.get("Curso"))
        self.label_course_name.configure(state='disabled', width=200)
        self.label_course_name.pack(pady=5)
        
        self.entry_hour_obr = customtkinter.CTkEntry(self.top_frame_right, placeholder_text="horas obrigatórias: "+str(hour_obr))
        self.entry_hour_obr.configure(width=200)
        self.entry_hour_obr.pack(pady=5)
        self.entry_hour_obr.bind("<Return>", self.set_value_obr)

        self.entry_hour_opt = customtkinter.CTkEntry(self.top_frame_right, placeholder_text="horas optativas: "+str(hour_opt))
        self.entry_hour_opt.configure(width=200)
        self.entry_hour_opt.pack(pady=5)
        self.entry_hour_opt.bind("<Return>", self.set_value_opt)

        # create body frame
        self.body_frame = customtkinter.CTkFrame(self)
        self.body_frame.configure(fg_color="transparent")
        self.body_frame.pack()
        
        self.grade_table = CurriculumTable(self.body_frame)
        self.grade_table.configure(fg_color="transparent")
        self.grade_table.pack()

        # combo_default = customtkinter.StringVar(value=coursesDict.get(studentDict.get("ID Curso")))  
        # self.combobox = customtkinter.CTkComboBox(self.body_frame_label,
        #                                     values=coursesDict.values(),
        #                                     # command=self.combobox_callback,
        #                                     variable=combo_default)
        # self.combobox.pack(pady=0, anchor="w", side="left", fill=tkinter.BOTH, expand=True)
        # self.combobox.configure(width=300)
        
        # self.refresh_button = customtkinter.CTkButton(self.body_frame_label, 
        #                                             text="", 
        #                                             image=self.refresh_image,
        #                                             anchor="w")
        #                                             # command = self.refresh_button_callback(self.table_frame))
        # self.refresh_button.configure(width=25)
        # self.refresh_button.pack(padx=5, pady=0, side="right")
        
        self.bottom_frame = customtkinter.CTkFrame(self)
        self.bottom_frame.configure(fg_color="transparent")
        self.bottom_frame.pack()

        self.label_warning = customtkinter.CTkLabel(self.bottom_frame, 
                                                    text="ATENÇÃO: A grade curricular pode estar desatualizada.\nEntre em contato com o desenvolvedor para atualizá-la")
        self.label_warning.pack()

        # button to include a curriculum
        # self.button_course = customtkinter.CTkButton(self.bottom_frame, 
        #                                           text="ATUALIZAR GRADE CURRICULAR" if logged else "CARREGAR GRADE CURRICULAR",
        #                                           compound="left",
        #                                           image=self.refresh_image if logged else self.download_image)
        # self.button_course.pack(padx=20)

class LoginFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="LOGIN", **kwargs):
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.profile_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(128, 128))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.label_student_img = customtkinter.CTkLabel(self, text="", image=self.profile_image)
        self.label_student_img.pack(padx=20, pady=60)
        
        self.label_student_name = customtkinter.CTkLabel(self, 
                                                        text=studentDict.get("Nome") if logged else "CARREGUE SEU HISTÓRICO")
        self.label_student_name.pack(padx=20, pady=10)
        
        self.button_student = customtkinter.CTkButton(self, 
                                                    text="ATUALIZAR HISTÓRICO" if logged else "CARREGAR HISTÓRICO", 
                                                    compound='left', 
                                                    image=self.refresh_image if logged else self.download_image)
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
        self.profile_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(64,64))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        
        # create top frame
        self.top_frame = customtkinter.CTkFrame(self)
        self.top_frame.configure(fg_color="transparent")
        self.top_frame.pack(pady=35)

        self.top_frame_left = customtkinter.CTkFrame(self.top_frame)
        self.top_frame_left.configure(fg_color="transparent")
        self.top_frame_left.pack(padx=30, side="left")

        self.top_frame_right = customtkinter.CTkFrame(self.top_frame)
        self.top_frame_right.configure(fg_color="transparent")
        self.top_frame_right.pack(padx=30, side="right")

        self.student_img = customtkinter.CTkLabel(self.top_frame_left, 
                                                        text="", 
                                                        image=self.profile_image)
        self.student_img.configure(fg_color="transparent")
        self.student_img.pack(padx=20, fill="x")

        self.student_name = customtkinter.CTkEntry(self.top_frame_right, placeholder_text=studentDict.get("Nome") if logged else "SEM DADOS")
        self.student_name.configure(width=200, state='disabled')
        self.student_name.pack(pady=5, fill="x", anchor="e")
            
        self.student_status = customtkinter.CTkEntry(self.top_frame_right, placeholder_text=studentDict.get("Curso") if logged else "SEM DADOS")
        self.student_status.configure(width=200, state='disabled')
        self.student_status.pack(pady=5, fill="x", anchor="e")

        # create body frame
        self.body_frame = customtkinter.CTkFrame(self)
        self.body_frame.configure(fg_color="transparent")
        self.body_frame.pack(padx=60, pady=(40,0), fill="x")
            
        if logged:
            for data in studentDict:
                if data == "ID Curso" or data == "Nome": 
                    pass
                else:
                    self.data_frame = customtkinter.CTkFrame(self.body_frame)
                    self.data_frame.configure(fg_color="transparent")
                    self.data_frame.pack(fill="x")
                    self.label_content = customtkinter.CTkLabel(self.data_frame, text=str.upper(data))
                    self.label_content.pack(padx=(150,0), pady=15, side="left", anchor="e")
                    self.label_value = customtkinter.CTkLabel(self.data_frame, text=studentDict.get(data))
                    self.label_value.pack(padx=(0,150), pady=15, side="right", anchor="w")
            
        self.button_student = customtkinter.CTkButton(self.body_frame, 
                                                    text="ATUALIZAR HISTÓRICO" if logged else "SELECIONAR ARQUIVO", 
                                                    compound='left', 
                                                    image=self.refresh_image if logged else self.download_image, 
                                                    command=self.select_pdf_file)
        self.button_student.pack(padx=20, pady=15, anchor="s")

        self.button_help = customtkinter.CTkButton(self.body_frame, 
                                                    text="onde consigo meu histórico?",
                                                    command=self.callback)
        self.button_help.pack(pady=15)

    def callback(self):
        webbrowser.open_new(r"https://cobalto.ufpel.edu.br/academico/alunos/historicoAluno")

    def select_pdf_file(self):
        global studentDict, studentHist, app
        filename = fd.askopenfilename(
            title='Escolha o Arquivo',
            initialdir='/',
            filetypes=[('PDF files', '*.pdf')]
        )
        studentDict = extract_dict(filename)
        studentHist = load_student_file(filename) 
        final_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),r"docs/historico_aluno.pdf")
        shutil.move(filename, final_path)
        app.destroy()
        final_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),r"script.py")
        os.system(final_path)

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
        tkinter.Grid.columnconfigure(self, (0,1,2,3,4),weight=1)
        tkinter.Grid.rowconfigure(self, (0,1), weight=1)
        
        # create login frame
        self.login_frame = LoginFrame(self, header_name="USUÁRIO")
        self.login_frame.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        # create course frame
        self.course_frame = CourseFrame(self, header_name="CURSO")
        self.course_frame.grid(row=0, column=3, padx=(0,30), pady=(30,0))
        
        # create button 
        self.home_frame_button = customtkinter.CTkButton(self, text="CONTINUAR")
        self.home_frame_button.grid(row=1, column=2, padx=0, pady=30, sticky="W")
        
class GradeTable(customtkinter.CTkFrame):
    
    def __init__(self, *args, header_name="TABLE", **kwargs):
        
        super().__init__(*args, **kwargs)
                
        import sv_ttk

        root = tkinter.Frame()
        
        tree = ttk.Treeview(self, columns=('CÓDIGO', 'CADEIRA', 'STATUS', 'NOTA'), show='headings')
        cols = ('CÓDIGO', 'CADEIRA', 'STATUS', 'NOTA')
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')

        for index, row in studentHist.iterrows():
            tree.insert("",0,text=index,values=list(row))

        tree.grid(row=0, column=0, sticky='nsew')
        sv_ttk.set_theme("dark")

class StatisticsFrame(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="STATISTICS", **kwargs):

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"img")
        self.home_image_small       = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
        self.profile_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(128, 128))
        self.profile_image_small    = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profile.png")), size=(20, 20))
        self.book_image             = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(128, 128))
        self.book_image_small       = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "books.png")), size=(20, 20))
        self.refresh_image          = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "refresh.png")), size=(20, 20))
        self.download_image         = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "download.png")), size=(20, 20))

        super().__init__(*args, **kwargs)
    
        self.header_name = header_name

        # create first frame 
        self.top_frame_indicators = customtkinter.CTkFrame(self)
        self.top_frame_indicators.configure(fg_color="transparent")
        self.top_frame_indicators.pack(pady=(30,15), fill="x")
 
        higher_grade = studentHist.media.max()
        lower_grade = studentHist.media.min()
        mean_grade = studentHist.media.mean()
        count_higher = 0
        count_lower = 0
        IRA = (
            studentHist.media*studentHist.creditos
            ).sum() / studentHist.creditos.sum()

        count_higher = studentHist.media.value_counts()[studentHist.media.max()]
        count_lower = studentHist.media.value_counts()[studentHist.media.min()]

        self.higher_grade_label = customtkinter.CTkLabel(self.top_frame_indicators, 
                                                        text="{:0.2f}\nMAIOR NOTA ({})".format(higher_grade, count_higher) if count_higher > 1 else "{:0.2f}\nMAIOR NOTA".format(higher_grade))
        self.higher_grade_label.configure(fg_color="#1F6AA5", corner_radius=10, font=('arial',14))
        self.higher_grade_label.pack(padx=20, ipadx=10, ipady=10, side="left", fill=tkinter.BOTH, expand=True)

        self.lower_grade_label = customtkinter.CTkLabel(self.top_frame_indicators, 
                                                        text="{:0.2f}\nMENOR NOTA ({})".format(lower_grade, count_lower) if count_lower > 1 else "{:0.2f}\nMENOR NOTA".format(lower_grade))
        self.lower_grade_label.configure(fg_color="#1F6AA5", corner_radius=10, font=('arial',14))
        self.lower_grade_label.pack(padx=20, ipadx=10, ipady=10, side="left", fill=tkinter.BOTH, expand=True)

        self.mean_grade_label = customtkinter.CTkLabel(self.top_frame_indicators, text="{:0.2f}\nMÉDIA GERAL".format(mean_grade))
        self.mean_grade_label.configure(fg_color="#1F6AA5", corner_radius=10, font=('arial',14))
        self.mean_grade_label.pack(padx=20, ipadx=10, ipady=10, side="right", fill=tkinter.BOTH, expand=True)
        
        self.ira_label = customtkinter.CTkLabel(self.top_frame_indicators, text="{:0.2f}\nIRA".format(IRA))
        self.ira_label.configure(fg_color="#1F6AA5", corner_radius=10, font=('arial',14))
        self.ira_label.pack(padx=20, ipadx=10, ipady=10, side="right", fill=tkinter.BOTH, expand=True)
        
        # create second frame
        self.graph_frame = customtkinter.CTkFrame(self)
        self.graph_frame.pack()

        self.left_graph_frame = customtkinter.CTkFrame(self.graph_frame)
        self.left_graph_frame.pack(side="left")
        self.mid_graph_frame = customtkinter.CTkFrame(self.graph_frame)
        self.mid_graph_frame.pack(side="left")
        self.right_graph_frame = customtkinter.CTkFrame(self.graph_frame)
        self.right_graph_frame.pack(side="left")
        
        dfCurriculum['concluida'] = dfCurriculum['codigo'].isin(studentHist['codigo'])

        obr_total_credits = dfCurriculum[(dfCurriculum['concluida']) & (dfCurriculum['status']=='OBRIGATÓRIA')].creditos.sum()
        opt_total_credits = dfCurriculum[(dfCurriculum['concluida']) & (dfCurriculum['status']=='OPTATIVA')].creditos.sum()

        df_graph = pd.DataFrame(
            [
                [hour_obr-obr_total_credits*credit, hour_opt-opt_total_credits*credit, hour_obr+hour_opt],
                [obr_total_credits*credit, opt_total_credits*credit, (opt_total_credits+obr_total_credits)*credit]
            ],
            columns=['obrigatória', 'optativa','total'],
            index=['não concluído','já concluído']
        )

        fig_size = (1.5,1.5)

        # first graph  
        fig = Figure(figsize=fig_size, dpi=100)
        fig.patch.set_facecolor('#404040')
        ax = fig.add_subplot()
        tot_graph = df_graph.plot.pie(y='total', subplots=True, ax=ax, legend=False, autopct='%1.1f%%', 
            explode=(0, 0.1), shadow=True, startangle=0, labels=None, colors=['red','green']
        )
        canvas_tot = FigureCanvasTkAgg(fig, self.left_graph_frame)
        canvas_tot.draw()
        canvas_tot.get_tk_widget().pack(side='left', ipadx=20, ipady=10)

        # second graph
        fig = Figure(figsize=fig_size, dpi=100)
        fig.patch.set_facecolor('#404040')
        ax = fig.add_subplot()
        obr_graph = df_graph.plot.pie(y='obrigatória', subplots=True, ax=ax, legend=False, autopct='%1.1f%%', 
            explode=(0, 0.1), shadow=True, startangle=0, labels=None, colors=['red','green']
        )
        canvas_obr = FigureCanvasTkAgg(fig, self.mid_graph_frame)
        canvas_obr.draw()
        canvas_obr.get_tk_widget().pack(side='left', ipadx=20, ipady=10)

        # third graph 
        fig = Figure(figsize=fig_size, dpi=100)
        fig.patch.set_facecolor('#404040')
        ax = fig.add_subplot()
        opt_graph = df_graph.plot.pie(y='optativa', subplots=True, ax=ax, legend=True, autopct='%1.1f%%', 
            explode=(0, 0.1), shadow=True, startangle=0, labels=None, colors=['red','green']
        )
        canvas_opt = FigureCanvasTkAgg(fig, self.right_graph_frame)
        canvas_opt.draw()
        canvas_opt.get_tk_widget().pack(side='left', ipadx=20, ipady=10)

        # create third frame
        self.body_frame = customtkinter.CTkFrame(self)
        self.body_frame.configure(fg_color="transparent")
        self.body_frame.pack()

        self.grade_table = GradeTable(self.body_frame)
        self.grade_table.configure(fg_color="transparent")
        self.grade_table.pack()
            
        '''
        -----------------------------------------------------
        | maior nota       menor nota                media  |
        | g.quantidade     g.obriga                  g.opta |
        |
        | tabela de notas
        | cod cadeira nota
        |
        -----------------------------------------------------

        '''
        
class App(customtkinter.CTk):

    def __init__(self):

        super().__init__()

        self.title("graduation progress")
        self.geometry("1000x600")

        # configure grid layout      
        tkinter.Grid.columnconfigure(self, (0,1,2),weight=1)
        tkinter.Grid.rowconfigure(self, (0,1), weight=1)
        
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
        self.statistics_frame = StatisticsFrame(self, fg_color="transparent")
        self.statistics_frame.grid(pady=30)

        # create student frame
        self.student_frame = StudentFrame(self, fg_color="transparent")
        self.student_frame.grid(pady=30)

        # create graduation frame
        self.graduation_frame = GraduationFrame(self, fg_color="transparent")
        self.graduation_frame.grid(pady=30)
        
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):

        self.navigation_frame.home_btn.configure(fg_color=("#242424") if name == "home" else "transparent")
        self.navigation_frame.profile_btn.configure(fg_color=("#242424") if name == "student" else "transparent")
        self.navigation_frame.graduation_btn.configure(fg_color=("#242424") if name == "graduation" else "transparent")
        self.navigation_frame.settings_btn.configure(fg_color=("#242424") if name == "statistics" else "transparent")

        if not logged:
            self.home_frame.home_frame_button.configure(fg_color="transparent", text="CARREGUE SEU HISTÓRICO")
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

def load_courses(file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"docs/courses_file.csv")):
    # courses dictionary
    print("carregando cursos")
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            coursesDict = dict((rows[0],rows[1]) for rows in reader)
        return coursesDict
    except:
        pass
        print("<error> erro ao carregar cursos")

def save_curriculum(target):
    driver = webdriver.Edge(os.path.join(os.path.dirname(os.path.realpath(__file__)),r'driver/msedgedriver.exe'))
    driver.get("https://cobalto.ufpel.edu.br/portal/cadastros/curriculoPublico")
    
    time.sleep(1.5)
    search = driver.find_element(By.ID, "txtCodigo")
    search.click()
    search.send_keys(target, Keys.ENTER)

    time.sleep(1.5)
    content = driver.find_elements(By.TAG_NAME, "tr")
    content[2].click()

    time.sleep(1.5)
    content = driver.find_elements(By.TAG_NAME, "tr")
    content.pop(0)

    curriculumList = []

    for x in content:
        if "COMPLEMENTARES" not in x.text:
            if len(x.text)>40:
                x = x.text.split('\n')[0].strip()

                cod = x.split(" ")[0].strip()

                crd = x.split("DISCIPLINA")[0].strip()
                crd = crd.split(" ")[-1].strip()

                typ = x.split("DISCIPLINA")[1].strip()
                typ = typ.split(" ")[0].strip()

                cad = x.replace(cod,'')

                if 'Departamento' in cad:
                    cad = cad.split('Departamento')[0].strip()
                if 'Centro' in cad:
                    cad = cad.split('Centro')[0].strip()
                if 'Departamento' in cad:
                    cad = cad.split('Departamento')[0].strip()

                curriculumList.append([cod,cad,crd,typ])
    
    driver.close()

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"docs", studentDict.get("ID Curso")+".csv")    
    
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(curriculumList)
    
def load_curriculum(course_id , file_path = r'C:\Users\arthu\Desktop\graduation_progress\docs\cursos'):
    print("carregando grade curricular do curso")

    file_path = os.path.join(file_path, course_id+".csv")

    if os.path.exists(file_path):
        dfCurriculum = pd.read_csv(file_path, encoding='latin-1')
        return dfCurriculum
    else:
        print("<error> erro ao localizar arquivo")
        print("<error> curso nao suportado")

def extract_content(target):
    content = []
    for page in target.pages:
        content.append(page.extract_text())
    return '\n'.join([str(page) for page in content])
    
def extract_disciplines(target):
    disciplines = []
    target = target.split('\n')
    for disc in target:
        if '/' not in disc and disc[0].isnumeric() and len(disc) > 8:
            cod = disc.split(" ")[0].strip()
            med = disc.split(" ")[-2].strip()
            med = med.replace(",",".")

            if ' APR ' in disc:
                var = " APR "
            if ' DSP ' in disc:
                var = " DSP "
            if ' TRC ' in disc:
                var = " TRC "
            if ' CANC ' in disc:
                var = " CANC "
            if ' REP ' in disc:
                var = " REP "
            if ' INF ' in disc:
                var = " INF "
            if med == 'MAT':
                med = ''
                cred = ''
                cad = disc.split(" MAT")[0].strip()
                status = "MAT"
            else:
                cred =  disc.split(var)[1].strip().split()[0][-1::]
                cad = disc.split(var)[0].strip()
                status = var.strip()
            cad = cad.split('- ')[-1].strip()
            disciplines.append([cod,cad,status,med, cred])
    
    return disciplines

def load_student_file(file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"docs/historico_aluno.pdf")):
    print('carregando historico do aluno')    
    try:
        reader = PdfReader(file_path)
        studentHist = extract_content(reader)
        studentHist = extract_disciplines(studentHist)
        df = pd.DataFrame(studentHist, columns=['codigo','cadeira','situacao','media','creditos'])
        df['codigo'] = pd.to_numeric(df['codigo'], errors='coerce')
        df['creditos'] = pd.to_numeric(df['creditos'], errors='coerce')
        df['media'] = pd.to_numeric(df['media'], errors='coerce')
        return df
    except:
        pass
        print("<error> erro ao carregar historico do aluno")
    
def extract_target(target, file, delimiter="\n"):
    try:
        data = file.split(target)[1]
        data = data.split(delimiter)[0]
        return data.strip()
    except:
        print(target)
        print("<error> erro ao extrair conteudo")
        print("<error> revise os parametros")
        pass

def extract_dict(file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"docs/historico_aluno.pdf")):
    global logged
    print('carregando dados do aluno')    
    try:
        target = PdfReader(file_path)
        target = extract_content(target)
        studentDict = {
            'Nome':extract_target("Nome:", target),
            'Matrícula':extract_target("Matrícula:", target, " N"),
            'Curso':extract_target("Curso:",target," ("),
            'ID Curso':extract_target("Curso:",target," -"),
            'Vínculo':extract_target("Situação do Aluno:",target,"Ór"),
            'Ingresso':extract_target("Ano/semestre:",target,"Pro")
        }
        logged = True
        return studentDict
    except:
        pass
        logged = False
        print("<error> erro ao carregar dados do aluno")
        
if __name__=='__main__':

    credit = 17
    hour_obr = 3196
    hour_opt = 272

    logged = False
    studentDict = extract_dict()
    studentHist = load_student_file() 
    coursesDict = load_courses()
    
    if logged:
        dfCurriculum = load_curriculum(studentDict.get("ID Curso"))

    app = App()
    app.mainloop()
    