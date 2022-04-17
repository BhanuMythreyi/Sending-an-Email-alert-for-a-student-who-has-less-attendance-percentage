import smtplib
from email.message import EmailMessage

def sendingMail(receiver_mail_id,subject,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    sender_mail_id = 'sendermail@gmail.com'
    password = 'lofeoknpalhoewha'
    server.login(sender_mail_id,password)
    email = EmailMessage()
    email['From'] = sender_mail_id
    email['To'] = receiver_mail_id
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    print("Email sent successfully")

dictionary_of_Student_EmailIDs ={100: 'demodemo1@gmail.com',200:'demodemo2@gmail.com',300:'demodemo3@gmail.com'} 

def EmailInitiator(attendance_percentage,roll_number_of_student):
    if attendance_percentage<80:
        receiver_mail_id = dictionary_of_Student_EmailIDs[roll_number_of_student]
        subject = "Alert for Student's low attendance percentage"
        content = """Hello Dear Student,
        You are receiving this mail as you have low attendance for your regular classes of your course work. Currently your attendance percentage is """+str(int(attendance_percentage))+""", as you are aware of the fact that our university requires you to have a minimum of 75 percentage of overall attendance for attempting your semester end examinations, it is better that you focus on this issue now itself rather than getting tensed later.
        However, if you are facing any health issues or medical issues or any other acceptable issues, then you are requested and welcomed to talk about this with our principal or vice principle and submit that letter to your concerned department's HOD.
        You are also requested to understand the fact that attendance is mandotary so that you would listen to classes effectively and could perform well in your examinations even with a minimum preparation in the end.
        University is requesting you to understand the norms it has and take the necessary action as soon as possible
        
        Thank You"""
        sendingMail(receiver_mail_id,subject,content)

def Attendance_Percentage_calculator(roll_number_of_student):
    subjects = int(input("Enter the number of subjects the student is currently enrolled in the coursework: "))
    sum = 0
    for i in range(subjects):
        print("Enter the attendance percentage of subject ",i+1)
        percentage = int(input())
        sum += percentage

    Final_percentage = sum/subjects
    EmailInitiator(Final_percentage,roll_number_of_student)

RollNumber = int(input("Enter Student's Roll Number: "))
Attendance_Percentage_calculator(RollNumber)