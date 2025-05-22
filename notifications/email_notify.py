import smtplib
import ssl
from email.message import EmailMessage

def send_email(subject, body, to, from_addr, smtp_server, smtp_port, smtp_user, smtp_pass, attachment_path=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to
    msg.set_content(body)

    # Attach CSV file if it exists
    if attachment_path:
        with open(attachment_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype='application',
                subtype='octet-stream',
                filename=attachment_path.split("/")[-1]
            )

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
