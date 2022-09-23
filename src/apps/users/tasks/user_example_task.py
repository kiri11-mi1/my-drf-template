from config import celery_app


@celery_app.task
def test_task_for_example():
    from ..models import User
    for user in User.objects.all():
        print(f'Info {user}')
