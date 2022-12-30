#!/usr/bin/env python
# coding: utf-8
# author: msouzarthur

import pandas as pd
import time, os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_disc(target):
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
            type = t.split('DISCIPLINA')[1].strip()
            type = type.split(' ')[0]
            curriculum.append([cod, dsc, type])
    return curriculum            

link_cc = "https://cobalto.ufpel.edu.br/portal/cadastros/curriculoPublico/visualizar/100" 
link_ec = "https://cobalto.ufpel.edu.br/portal/cadastros/curriculoPublico/visualizar/138"
cols = ['código','cadeira','tipo']

try:
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
except:
    driver = webdriver.Chrome(ChromeDriverManager().install())

print('atualizando grade curricular: ciência da computação')
driver.get(link_cc)
time.sleep(2)
element = driver.find_elements(By.TAG_NAME, "table")
curriculum_cc = get_disc(element[1].text)

print('atualizando grade curricular: engenharia da computação')
driver.get(link_ec)
time.sleep(2)
element = driver.find_elements(By.TAG_NAME, "table")
curriculum_ec = get_disc(element[1].text)

driver.close()

print('salvando arquivos')
df_cc = pd.DataFrame(data = curriculum_cc, columns = cols)

df_cc.to_csv(
    os.path.join(Path(__file__).parent,'docs\gc_cc.csv'), 
    sep=';'
    )
df_ec = pd.DataFrame(data = curriculum_ec, columns = cols)
df_ec.to_csv(
    os.path.join(Path(__file__).parent,'docs\gc_ec.csv'), 
    sep=';'
    )