import sqlite3
import smtplib

def weeklyCount():
    
    conn = sqlite3.connect('tablessss.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("select count(*) from history where hs_answer in ('Sorry, Can you be more specific?','Sorry I dint get you') and hs_datestamp > datetime('now', 'start of day', 'weekday 6', '-7 day')")
    rows = c.fetchall()
    counter=rows[0][0]
    emailBody = " Hi Team,\n\n The number of unanswered questions for the past week is:"+str(counter)+"\n\n Best Regards, \n Team ChatBot George"
    gmail_user = 'coolbot234567@gmail.com'
    gmail_password = 'msist123'

    sent_from = gmail_user
    to = ['gwsb234567@gmail.com']
    subject = "Chatbot George Unanswered Questions Count Weekly"
    body = emailBody

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        #print ('Email sent!')
    except:
        print ('Something went wrong...')
    conn.close()