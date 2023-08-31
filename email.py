import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail SMTP configuration
smtp_server = 'artur.sahakyan5@gmail.com'
smtp_port = 587
email_sender = 'artur.sahakyan5@gmail.com'
email_password = 'your_email_password'
email_receiver = 'artur.sahakyan5@gmail.com'

def get_current_ip_tables():
    return subprocess.check_output(['iptables-save']).decode('utf-8')

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, msg.as_string())
    server.quit()

if __name__ == '__main__':
    try:
        previous_ip_tables = get_current_ip_tables()

        while True:
            current_ip_tables = get_current_ip_tables()
            
            if current_ip_tables != previous_ip_tables:
                subject = 'IP Tables Change Detected'
                body = 'New IP addresses added to IP tables:\n\n' + current_ip_tables
                
                send_email(subject, body)
                
                previous_ip_tables = current_ip_tables
                
    except KeyboardInterrupt:
        pass
