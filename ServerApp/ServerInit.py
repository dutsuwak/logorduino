import os
import socket
import time
from xml.dom import minidom
from threading import Thread

#from logorduino_parser import yacc
import logorduino_parser
# Get the token map from the lexer.  This is required.


'''--------------------------------------------------------------------------
                    Variables globales
 ----------------------------------------------------------------------------'''
global DEBUG,PUERTO,ServerOn,Server




'''--------------------------------------------------------------------------
                    Configuracion de XML y Json
 ----------------------------------------------------------------------------'''
def loadXMLParameters():
    global DEBUG,PUERTO,ServerOn

    ruta=os.getcwd()
    rutaFinal=str(ruta)+"/src/configs.xml"
    xmlDocParametrosIni = minidom.parse(rutaFinal)
    ServerOn=True

    pDebug = xmlDocParametrosIni.getElementsByTagName('DEBUG')
    load_DEBUG=pDebug[0].attributes['value'].value
    if(load_DEBUG == "true"):
        DEBUG = True
    else:
        DEBUG = False
    pPuerto = xmlDocParametrosIni.getElementsByTagName('PUERTO')
    PUERTO=int(pPuerto[0].attributes['value'].value)



'''--------------------------------------------------------------------------
                    Sockets concurrentes del servidor
 ----------------------------------------------------------------------------'''
def initServer():
    global DEBUG,PUERTO,ServerOn,Server

    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        if(DEBUG == True):
            print(".")#,
        Server.bind(('', PUERTO))
        Server.listen(5)
        #s.connect(('google.com',0)) 
        if(DEBUG == True):
            print("\nServer initialized on : "+str(socket.gethostbyname(socket.gethostname()))+":"+str(PUERTO))
        ServerOn=True
    except:
        print(".")#,
        PUERTO+=1
        initServer()




def listen():
    global DEBUG,ServerOn,Server

    while ServerOn:
        try:
            conn, addr = Server.accept()
            if(DEBUG):
                print("**User: "+str(addr)+" Connected**")
            b= Thread(target=handleClient, args=(conn,addr))
            b.daemon = True
            b.start()
        except:
            pass

    Server.close()
    if(DEBUG):
        print("- Server turn off -")


def handleClient(conn,addr):
    global DEBUG, ServerOn

    SessionOn= True
    while SessionOn:
        data = conn.recv(1024)
        data = data.decode("utf-8")
        data = data.split('\n')
        try:
            if(data[0] != ""):
                interpreter(data[0])
       #         if(data[0] == "xexit"):
        #            if(DEBUG== True):
         #               print("**usuario: "+str(addr)+" desconectado**")
          #          SessionOn=False
           #     elif(data[0]=="xkill"):
            #        ServerOn=False
             #   else:
              #      print("comando desconocido: "+data[0]+".   de :"+str(addr[0]))
        except:
            pass

    conn.close()
    #os._exit(0)

def interpreter(command) :
    print("ok1")
    result = logorduino_parser.yacc.parse(command)
    print("ok")
    print (result)


loadXMLParameters()
initServer()
listen()
