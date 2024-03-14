import tkinter
import threading
from tkinter import *
import  webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

#---------------------------------------------BACK--------------------------------------------------
def Monitoreo_Diario():#Funcion para abrir todas las pestañas que se usan en un monitoreo diario
    link_Piru="https://piru.cedi.com." \
              "ar"
    webbrowser.open(link_Piru)

    link_Zabbix_Cedi="https://newzbx.cedi.com.ar/zabbix/zabbix.php?show=1&name=&inventory%5B0%5D%5Bfield%5D=type&inven" \
                     "tory%5B0%5D%5Bvalue%5D=&evaltype=0&tags%5B0%5D%5Btag%5D=&tags%5B0%5D%5Boperator%5D=0&tags%5B0%5D%5Bvalue%5D=&show_tags=3&tag_name_format=0&tag_priority=&show_opdata=0&show_timeline=1&filter_name=&filter_show_counter=0&filter_custom_time=0&sort=clock&sortorder=DESC&age_state=0&show_suppressed=0&unacknowledged=0&compact_view=0&details=0&highlight_row=0&action=problem.view"
    webbrowser.open(link_Zabbix_Cedi)

    link_Zabbix_Bancor="http://monitoreobancor.bcocba.int/zabbix/zabbix.php?action=problem.view&page=1&from=2022-09-22+19%3A00%3A00&to=2022-09-23+07%3A00%3A00&filter_show=1&filter_application=&filter_name=&filter_severity=0&filter_age_state=1&filter_age=14&filter_inventory%5B0%5D%5Bfield%5D=type&filter_inventory%5B0%5D%5Bvalue%5D=&filter_evaltype=0&filter_tags%5B0%5D%5Btag%5D=&filter_tags%5B0%5D%5Boperator%5D=0&filter_tags%5B0%5D%5Bvalu" \
                       "e%5D=&filter_show_tags=3&filter_tag_name_format=0&filter_tag_priority=&filter_set=1"
    webbrowser.open(link_Zabbix_Bancor)

    link_Wsp="https://web.whatsapp.com"
    webbrowser.open(link_Wsp)

    link_Nagios="https://monitoreo.bancodelapampa.com.ar/nagvis/frontend/nagvis-j" \
                "s/index.php?mod=Map&act=view&show=CEDIINICIO"
    webbrowser.open(link_Nagios)

    link_Sigma="https://sigma.redlink.com.ar/portal/pages" \
               "/login.xhtml#protected"
    webbrowser.open(link_Sigma)

    link_BacklogSoporte="https://id.atlassian.com/login?co" \
                        "ntinue=https%3A%2F%2Fid.atlassian.com%2Fjoin%2Fuser-access%3Fresource%3Dari%253Acloud%253Ajira%253A%253Asite%252F308746af-bb71-4cc6-b863-afc1c1deffd5%26continue%3Dhttps%253A%252F%252Fceditech.atlassian.net%252Fjira%252Fdashboards%252F10005&application=jira"
    webbrowser.open(link_BacklogSoporte)

    link_Sharepoint="https://cediconsulting.sharepoint.com" \
                    "ComCenter/Documentos%20compartidos/Forms/AllItems.aspx?e=5%3Ab7e6307633564f3f8b02dafb965bd640&at=9&FolderCTID=0x0120009DF1E369BEF36745828899C18B696FBE&id=%2FComCenter%2FDocumentos%20compartidos%2FClientes%20Info%2FMonitoreo%202024%2FClientes%20Runbooks%20y%20procedimientos&viewid=43304eb5-7d9b-4446-86e4-408f9768268f"
    webbrowser.open(link_Sharepoint)

    link_MMG="https://mmg.service-now." \
             "com/login.do"
    webbrowser.open(link_MMG)

    link_Grafana="http://grafana.bancor.com.ar:" \
                 "3000/d/1Oaebh5Ik/app-estadistica-logs-iis-bancor-fondos?orgId=1&from=now-1h&to=now&var-Server=BFAPPWB01&var-Server=BFAPPWB02&var-Pagina=767_%2F767_VFHomeNG_API%2Fapi%2FsetCuotapartista"
    webbrowser.open(link_Grafana)

    link_BR="https://bancorioja.cloud.com/Citr" \
            "ix/StoreWeb/#/login"
    webbrowser.open(link_BR)
def Guardias_Soporte():#Funcion para abrir la pestaña donde esta la guadia de soporte
    link_Guardias_Soporte="https://cediconsulting-my.sharepoint.com/:x:/r/personal/mquinteros_cedi_com_ar" \
                          "/Documents/ADMINISTRACION%20SOPORTE/2022/Planificacion%20de%20Guardias.xlsx?d=w9258785b921045149b2b48727fb75a33&csf=1&web=1&e=VJtUPF"
    webbrowser.open(link_Guardias_Soporte)

def Contratos():#Funcion para abrir la pestaña donde estan los contratos
    link_Contratos="https://app.powerbi.com/groups/me/reports/c535d02f-161e-4ddb-9344-6ad5388cfeab" \
                   "/ReportSection8d3316eee6bd7e197886?ctid=adeee945-465d-469f-9c10-bbf55bed49ea&experience=power-bi"
    webbrowser.open(link_Contratos)

def Sharepoint_Runbooks():#Funcion para abrir la pestaña donde estan los runbook
    link_Sharepoint="https://cediconsulting.sharepoint.com/:f:/r/ComCenter/Documentos%20compartidos/Clientes%20Info/Moni" \
                    "toreo%202024?csf=1&web=1&e=DesmMo"
    webbrowser.open(link_Sharepoint)

def Inicio_Tareas_Automaticas():#Crear Tarea automatica
 print("go")
 ruta="F:\Tareas_Darias.xlsx"#Ruta del Archivo Excel
 print(ruta)
 path=pd.read_excel(ruta)
 print(ruta)

 # Especificar la ruta al perfil de usuario de Chrome
 # Asegúrate de reemplazar '<TuNombreDeUsuario>' con tu nombre de usuario real y 'Default' con el nombre de perfil correcto si es necesario.
 profile_path = r'C:\Users\Facu_\AppData\Local\Google\Chrome\User Data'  # Ejemplo para Windows

 chrome_options = Options()
 chrome_options.add_argument(f'user-data-dir={profile_path}')  # Utiliza tu perfil de Chrome

 # Inicializar el ChromeDriver
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
 ID_BOTON="2a84919f-59d8-4441-a975-2a8c2643b741"

 driver.execute_script("window.open('');")

 driver.switch_to.window(driver.window_handles[1])

 driver.get("https://teams.microsoft.com/v2/")#Abre
 time.sleep(7)

 boton = driver.find_element(By. ID,ID_BOTON)#Boton que lleva a Equipos de Teams
 boton.click()
 time.sleep(5)


 canal =driver.find_element(By.CSS_SELECTOR, "span.fui-StyledText ___12cxzrv f11d4kpn fvm675v f1p9o1ba f1sil6mw f1cmbuwj fz5stix f14d40fx".replace(" ","."))
 canal.click()
 time.sleep(5)#Boton que lleva el Canal de Prueba(el mismo tiene que estar anclado y en el primer espacio)

 def Tareas_automaticas():#Funcion que Genera la Tarea
    boton = driver.find_element(By.CSS_SELECTOR,
                                "button.fui-Button r1alrhcs ___1akj6hk ffp7eso f1p3nwhy f11589ue f1q5o8ev f1pdflbu f1phragk f15wkkf3 f1s2uweq fr80ssc f1ukrpxl fecsdlb f1rq72xc fnp9lpt f1h0usnq fs4ktlq f16h9ulv fx2bmrt f1d6v5y2 f1rirnrt f1uu00uk fkvaka8 f1ux7til f9a0qzu f1lkg8j3 fkc42ay fq7113v ff1wgvm fiob0tu f1j6scgf f1x4h75k f4xjyn1 fbgcvur f1ks1yx8 f1o6qegi fcnxywj fmxjhhp f9ddjv3 f17t0x8g f194v5ow f1qgg65p fk7jm04 fhgccpy f32wu9k fu5nqqq f13prjl2 f1czftr5 f1nl83rv f12k37oa fr96u23".replace(
                                    " ", "."))
    boton.click()
    input_1 = driver.find_element(By.CSS_SELECTOR, "input.fui-Input__input rvp2gzh".replace(" ", "."))
    time.sleep(3)
    input_1.send_keys(Tareas)

    input_2 = driver.find_element(By.CSS_SELECTOR, "p.ck-placeholder".replace(" ", "."))
    time.sleep(3)
    input_2.send_keys(Tarea)
    time.sleep(3)

    boton3 = driver.find_element(By.CSS_SELECTOR, "div.ui-flex e ___hir5vg0 f3rmtva f1cio4g9 fvaszet".replace(" ", "."))
    boton3.click()
    time.sleep(3)


 for i in range (len(path)):#Lector de excel(el mismo esta tiene una capacidad de diez acciones por carga)
    Tareas = path.loc[i,"Tareas"]
    Accion_1 = path.loc[i,"Accion-1"]
    Accion_1=str(Accion_1)
    if Accion_1!="nan":
        Tarea=Accion_1
        Tareas_automaticas()
    Accion_2 = path.loc[i,"Accion-2"]
    Accion_2 = str(Accion_2)
    if Accion_2!="nan":
        Tarea=Accion_2
        Tareas_automaticas()
    Accion_3 = path.loc[i,"Accion-3"]
    Accion_3 = str(Accion_3)
    if Accion_3!="nan":
        Tarea=Accion_3
        Tareas_automaticas()
    Accion_4 = path.loc[i,"Accion-4"]
    Accion_4 = str(Accion_4)
    if Accion_4!="nan":
        Tarea=Accion_4
        Tareas_automaticas()
    Accion_5 = path.loc[i,"Accion-5"]
    Accion_5 = str(Accion_5)
    if Accion_5!="nan":
        Tarea=Accion_5
        Tareas_automaticas()
    Accion_6 = path.loc[i,"Accion-6"]
    Accion_6 = str(Accion_6)
    if Accion_6!="nan":
        Tarea=Accion_6
        Tareas_automaticas()
    Accion_7 = path.loc[i,"Accion-7"]
    Accion_7 = str(Accion_7)
    if Accion_7!="nan":
        Tarea=Accion_7
        Tareas_automaticas()
    Accion_8 = path.loc[i,"Accion-8"]
    Accion_8 = str(Accion_8)
    if Accion_8!="nan":
        Tarea=Accion_8
        Tareas_automaticas()
    Accion_9 = path.loc[i,"Accion-9"]
    Accion_9 = str(Accion_9)
    if Accion_9!="nan":
        Tarea=Accion_9
        Tareas_automaticas()
    Accion_10 = path.loc[i,"Accion-10"]
    Accion_10 = str(Accion_10)
    if Accion_10!="nan":
        Tarea=Accion_10
        Tareas_automaticas()
 driver.quit()
#-------------------------------------------------------Front------------------------------------------------------
def ventana1():
    global ventana1
    ventana1= Tk()
    ventana1.geometry("250x250")
    ventana1.title("AI NOC")
    ventana1.config(bg="#344D53")
    Saludos = Label(ventana1, text="Buenas noches",bg="#A2B3B6")
    Saludos.grid(row=0, column=1)

    miLabel = Label(ventana1, text=" agente, que necesitaria?",bg="#A2B3B6")
    miLabel.grid(row=1, column=1)

    Button(ventana1, text="Procedimientos y Runbooks",bg="#17A9CB", width=20,command=Sharepoint_Runbooks).grid(row=2,column=1)

    Button(ventana1, text="Contratos",bg="#17A9CB", width=20, command=Contratos).grid(row=3, column=1)

    Button(ventana1, text="Planificacion de Guardias Soporte",bg="#17A9CB", width=30, command=Inicio_Tareas_Automaticas).grid(row=4, column=1)

    Button(ventana1, text="Monitoreo Diario", width=30,bg="#17A9CB", command=Monitoreo_Diario).grid(row=5, column=1)

    ventana1.mainloop()
def ventana2():
    global ventana2
    ventana2=Toplevel(ventana1)
    ventana2.geometry("600x600")
    ventana2.title("AI NOC")
    ventana2.config(bg="#344D53")
    Button(ventana2, text="Volver al inicio", width=20,command=volver_al_inicio_ventana2,bg="#17A9CB", ).grid(row=7,column=1)


    ventana2.mainloop()

def ventana3():
    global ventana3
    ventana3=Toplevel(ventana1)
    ventana3.geometry("600x600")
    ventana3.title("AI NOC")


    Button(ventana3, text="Volver al inicio", width=20,command=volver_al_inicio_ventana3 ).grid(row=1,column=0)


    ventana3.mainloop()

def volver_al_inicio_ventana2():
    ventana1.iconify()
    ventana1.deiconify()
    ventana2.destroy()

def volver_al_inicio_ventana3():
    ventana1.iconify()
    ventana1.deiconify()
    ventana3.destroy()



ventana1()
