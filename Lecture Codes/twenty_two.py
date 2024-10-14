import smtplib
smtp_server ='smtp.gmail.com'
port = 587  #for TLS
sender_email = 'sumeetkapadia47@gmail.com'
password ='lmaoded'
server = smtplib.SMTP(smtp_server,port)
server.starttls()
server.login(sender_email,password)