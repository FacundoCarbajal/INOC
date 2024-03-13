import threading
import tkinter
from tkinter import *
import time
import  webbrowser
import pyautogui as pyto
#---------------------------------------------Funciones_de_botones_Runbooks----------------------------
def Monitoreo_Diario():
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
def Guardias_Soporte():
    link_Guardias_Soporte="https://cediconsulting-my.sharepoint.com/:x:/r/personal/mquinteros_cedi_com_ar" \
                          "/Documents/ADMINISTRACION%20SOPORTE/2022/Planificacion%20de%20Guardias.xlsx?d=w9258785b921045149b2b48727fb75a33&csf=1&web=1&e=VJtUPF"
    webbrowser.open(link_Guardias_Soporte)

def Contratos():
    link_Contratos="https://app.powerbi.com/groups/me/reports/c535d02f-161e-4ddb-9344-6ad5388cfeab" \
                   "/ReportSection8d3316eee6bd7e197886?ctid=adeee945-465d-469f-9c10-bbf55bed49ea&experience=power-bi"
    webbrowser.open(link_Contratos)

def Sharepoint_Runbooks():
    link_Sharepoint="https://cediconsulting.sharepoint.com/:f:/r/ComCenter/Documentos%20compartidos/Clientes%20Info/Moni" \
                    "toreo%202024?csf=1&web=1&e=DesmMo"
    webbrowser.open(link_Sharepoint)
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

    Button(ventana1, text="Planificacion de Guardias Soporte",bg="#17A9CB", width=30, command=Guardias_Soporte).grid(row=4, column=1)

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

print("aia")

ventana1()

