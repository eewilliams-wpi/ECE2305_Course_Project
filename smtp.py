import smtplib

from_addr = 'noreply.myiotmailbox@gmail.com'
to_addr = ''
message = "You've got mail!"
passwd = 'M4ilb0xP4ssw0rd'

data = '\r\n'.join(['From: ' + from_addr, 'To: ' + to_addr, 'Subject:', "", message])

with open('user.txt', 'r') as file:
	to_addr = file.read().replace('\n', '')

def send():
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(from_addr,passwd)
	server.sendmail(from_addr, to_addr, message)
	server.quit()

if __name__=='__main__':
    send()
