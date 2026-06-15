from django.core.mail import send_mail
from datetime import datetime

def trigger_email_view(email):
    send_mail(
        subject="Uzum market",
        message="Tabriklaymiz marketimizdan roxatdan otganingiz bilan",
        from_email="jasurmamatov0114@gmail.com",
        recipient_list=[f"{email}"],
        fail_silently=False,  # Set to True to suppress errors if transmission fails
    )
    return True


def trigger_email_view_login(email):
    send_mail(
        subject="Uzum marketda  xabarnoma",
        message=f"Akkountingizda login qilindi {datetime.now()} da. Agar siz bolmasangiz...",
        from_email="jasurmamatov0114@gmail.com",
        recipient_list=[f"{email}"],
        fail_silently=False,  # Set to True to suppress errors if transmission fails
    )
    return True