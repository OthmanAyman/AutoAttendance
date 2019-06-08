import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail():
    def __init__(self):

        self.sender_email = "Auto.Attendance2019@gmail.com"
        self.password = "AutoAttendance19"

        self.context = ssl.create_default_context()
        self.server = smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=self.context)
        self.server.login(self.sender_email, self.password)

    def send(self, email, student, subject, time):

        self.receiver_email = email
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "Attendance Recorded - no-reply"
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email

        self.student = student
        self.subject = subject
        self.time = time

        self.html = f"""\
        <html>
          <body>
            <p> Hi,<br>
               We inform you that we have recorded Attendance<br>
               for {self.student}  <br>
               in {self.subject} Subject <br>
               at {self.time} <br>
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


#
