import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def emailAdmin(toaddr2,sub,file,body2):
            fromaddr = "coolbot234567@gmail.com"
           
            toaddr=toaddr2

            msg = MIMEMultipart()

            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = sub

            body=body2;

            msg.attach(MIMEText(body, 'plain'))

            filename = file
            attachment = open(filename, "rb")

            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "msist123")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
