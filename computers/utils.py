import requests
from django.conf import settings


def send_admin_notification(employee, computer_count, msg=None):
    message = msg if msg else f"{computer_count} computers have been assigned to {employee}"

    data = {
        "level": "warning",
        "employeeAbbreviation": "mmu",
        "message": message
    }

    response = requests.post(f"{settings.ADMIN_NOTIFICATION_URL}", json=data)
    if response.status_code in [200, 201]:
        print("Notification Sent Successfully")
    else:
        print("Notification failed")
