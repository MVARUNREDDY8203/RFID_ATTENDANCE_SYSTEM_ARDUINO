import openpyxl
import winsound
import smtplib, ssl
import serial
ser=serial.Serial("COM7",9600)

rfidTag=["9A 55 02 B0", "15 28 90 5C","23 5B E8 11","D3 37 F5 5C","A3 AA F1 0B"]
rfidName=["RFID TAG BLUE 1111", "M.VARUN REDDY", "WHITE CARD1111","RAYAN SINGH","RFID TAG BLUE 2222"]
rfidEmail=["espArduno@gmail.com","varunmr2003@gmail.com","espArduno@gmail.com","rayan.singh2021@vitstudent.ac.in","rayan.singh2021@vitstudent.ac.in"]


def isAuth(UID):        #function that returns index of the uid 
    for i in rfidTag:
        if i==UID:
            x=rfidTag.index(i)
            return x
    return -1

        
## EMAIL CONNECTION
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "esparduno@gmail.com"  # Sender email
password = "rsywlixcqxblfyhw"


modeInput=input("""
HELLO WORLD!, TO THE RFID ATTENDANCE SYSTEM

1. TO TAKE ATTENDANCE
2. TO QUIT PROGRAM
""")

if int(modeInput)==1:
    while True:
        index=-1
        line1 = ser.readline().decode().rstrip() #approximate line
        print("Approximate your card... ")
        line1 = ser.readline().decode().strip() #uid tag line
        print("UID : "+line1)
        index = isAuth(line1) # authorisation func call

        if index == -1:
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            print("Access denied")
            continue

        print("Hello, "+rfidName[index])

        #EMAIL SECTION:
        receiver_email = rfidEmail[index]  # Enter receiver address
        message = "Marked attendance for "##+dateStr2

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

else:
    exit()



