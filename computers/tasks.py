from gb_demo import celery_app


@celery_app.task()
def send_admin_notification_task():
    pass
