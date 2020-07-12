import smtplib 
from email.mime.text import MIMEText

def send_mail(email):
	port = 2525
	smtp_server = 'smtp.mailtrap.io'
	login = 'e0fd3f9cb02091'
	password = '1c8201f9b97752'
	message = f"<h3>New User email submission</h3><ul><li>Email: {email}</li></ul>"

	sender_email = 'email@example.com'
	receiver_email = 'email2@example.com'
	msg = MIMEText(message, 'html')
	msg['Subject'] = 'User Email'
	msg['From'] = sender_email
	msg['To'] = receiver_email

	# Send email
	with smtplib.SMTP(smtp_server, port) as server:
		server.login(login, password)
		server.sendmail(sender_email, receiver_email, msg.as_string())