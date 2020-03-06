# email_test.py
# team1

import smtplib, ssl

class email():
    def _init_(self):
        port = 587
        smtp_server = "smtp.gmail.com"
        sender_email = "teamOnePi411@gmail.com"
        receiver_email_1 = "dbies3@gmail.com"
        receiver_email_2 = "matthewrepplier@gmail.com"
        password = "team-one-pi"

    def send_email(msg1, msg2):
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email_1, msg1)
            server.sendmail(sender_email, receiver_email_2, msg2)

if __name__ == '__main__':
    # Initialize the keypad class
    e = email()
     
    e.send_email("1234", "5678")
