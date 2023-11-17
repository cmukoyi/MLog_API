import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

# Email configuration
smtp_server = "smtp.office365.com"
smtp_port = 587  # Port 587 is commonly used for email submission
smtp_from = "no-reply@connectedcar360.net"
smtp_to = "carlos.mukoyi@scopetechnology.com"
message_subject = "Test Email"
message_body = "This is a test email sent via Python."

# Get email credentials securely
smtp_username = input("Enter your email username: ")
smtp_password = getpass("Enter your email password: ")

# Create the MIME object
message = MIMEMultipart()
message["From"] = smtp_from
message["To"] = smtp_to
message["Subject"] = message_subject
message.attach(MIMEText(message_body, "plain"))

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Use TLS for secure communication
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(smtp_from, smtp_to, message.as_string())

print("Email sent successfully.")
