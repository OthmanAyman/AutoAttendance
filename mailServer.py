import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail():
    def __init__(self):

        self.sender_email = "Email@email.com"
        self.password = "************"

        self.context = ssl.create_default_context()
        try:
            self.server = smtplib.SMTP_SSL(
                "smtp.gmail.com", 465, context=self.context)
            self.server.login(self.sender_email, self.password)
        except Exception as e:
            print(e)

    def send(self, email, student, subject, time):

        self.receiver_email = email
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "no-reply -Attendance Team"
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email

        self.student = student
        self.subject = subject
        self.time = time.split(' ')
        self.time_date = self.time[0]
        self.time_hour = self.time[1]
        self.html = f"""\
        <html>
          <body>
            <p> Hi,<br>
               We want to inform you that we have recorded Attendance<br>
               for {self.student}  <br>
               in {self.subject} Subject <br>
               on {self.time_date} <br>
               at {self.time_hour} <br>
               best wishes , AutoAttendance team
            </p>

          </body>
        </html>
        """
        self.part = MIMEText(self.html, "html")
        self.message.attach(self.part)

        try:
            self.server.sendmail(
                self.sender_email, self.receiver_email, self.message.as_string())
            return "email has been sent"

        except Exception as e:
            return e

    def send_abs(self, email, student, subject, time):

        self.receiver_email = email
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "no-reply -Attendance Team"
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email

        self.student = student
        self.subject = subject
        self.time = time.split(' ')
        self.time_date = self.time[0]
        self.time_hour = self.time[1]
        self.html = f"""\
        <html>
          <body>
            <p> Hi,<br>
                We want to inform you that you: {self.student} <br>
                have missed the subject: {self.subject} <br>
               on {self.time_date} <br>
               hope you doing okey ..
               best wishes , AutoAttendance team
            </p>

          </body>
        </html>
        """
        self.part = MIMEText(self.html, "html")
        self.message.attach(self.part)

        try:
            self.server.sendmail(
                self.sender_email, self.receiver_email, self.message.as_string())
            return "email has been sent"

        except Exception as e:
            return e
