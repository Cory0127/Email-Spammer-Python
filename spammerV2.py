import smtplib, ssl

default = 5

print ("Welcome to Theo's Awesome Email Spammer V2.0!")
print ("All you have to do is input the number of emails, message, and email information!")

num_emails = input("How many offensive emails do YOU want to send? Type 0 for default (" + str(default) + ") --> ")
num_emails = int(num_emails)
if num_emails == 0:
    num_emails = default

email_A = input("Please enter YOUR email address --> ")
password_A = input("Please enter the correct password to your email --> ")
email_B = input("Please enter the VICTIM'S email address --> ")
message = input("Please enter your spam message -->")
smtp_server = "smtp.gmail.com"
port = 587

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(email_A, password_A)
    for i in range(num_emails):
            server.sendmail(email_A, email_B, message)

print(email_B + "'s email has been SPAMMED!")