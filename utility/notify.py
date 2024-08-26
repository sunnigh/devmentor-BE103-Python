import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from database.verification import EmailVerification


class EmailService:
    def __init__(self, from_address: str, password: str, smtp_server: str = 'smtp.gmail.com', smtp_port: int = 587):
        self.from_address = from_address
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, to_address: str, subject: str, body: str):
        msg = MIMEMultipart()
        msg['From'] = self.from_address
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_address, self.password)
            server.sendmail(self.from_address, to_address, msg.as_string())
            server.quit()
            print(f"Email sent successfully to {to_address}")
        except Exception as e:
            print(f"Failed to send email to {to_address}. Error: {str(e)}")

    def send_verification_code(self, to_address: str, code: str):
        subject = "Your Verification Code"
        body = f"Your verification code is {code}. This code is valid for 5 minutes."
        self.send_email(to_address, subject, body)


class VerificationService:
    def __init__(self, db: Session, email_service: EmailService):
        self.db = db
        self.email_service = email_service

    def generate_verification_code(self):
        return str(random.randint(100000, 999999))

    def send_verification_code(self, email: str):
        code = self.generate_verification_code()
        expiration_time = datetime.utcnow() + timedelta(minutes=5)

        # Save the verification code and expiration time to the database
        email_verification = EmailVerification(email=email, code=code, expires_at=expiration_time)
        self.db.add(email_verification)
        self.db.commit()

        # Send the verification code via email
        self.email_service.send_verification_code(email, code)

    def verify_code(self, email: str, code: str):
        # Check if the code is correct and not expired
        verification = self.db.query(EmailVerification).filter_by(email=email, code=code).first()
        if verification and verification.expires_at > datetime.utcnow():
            return {"message": "Verification successful"}
        else:
            raise HTTPException(status_code=400, detail="Invalid or expired verification code")
