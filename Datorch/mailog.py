from email.mime.text import MIMEText
import smtplib

def sendmail(subject, filename):
    #settings
    to_email = "aaaa@gmail.com"
    from_email = "bbbb@gmail.com"

    gmail_account = "aaaa@gmail.com"
    gmail_password = "cccc"
    
    # MIME
    subject = str(subject)
    with open(filename) as fp:
      msg = MIMEText(fp.read())
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    #send mail 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_account, gmail_password)
    server.send_message(msg)
    server.quit()	
