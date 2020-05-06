import sqlite3
import smtplib

def freq_area():

    conn = sqlite3.connect('tablessss.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("select count(*), hs_answer , hs_question from history group by hs_answer HAVING hs_answer not in ('Bye take care. See you soon :) ','','It was nice talking to you. See you soon :)','Hello','Hey there','Sorry, Can you be more specific?','Sorry I dint get you','how are you ?') and hs_question not in ('how are you ?') order by 1 desc limit 1")
    rows = c.fetchall()
    question = rows[0][2]
    emailBody = " Hi Team,\n\n The most frequently asked area is around :"+question+"\n\n Best Regards, \n Team ChatBot George"
    gmail_user = 'coolbot234567@gmail.com'
    gmail_password = 'msist123'

    sent_from = gmail_user
    to = ['gwsb234567@gmail.com']
    subject = 'Chatbot George Most frequently asked question'
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