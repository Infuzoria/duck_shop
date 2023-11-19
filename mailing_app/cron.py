import smtplib
from mailing_app.models import Newsletter, Client, Logs
from django.core.mail import send_mail
from datetime import datetime
from django.conf import settings


def start_mailing_job(user_id):

    periodicity = {'day': 1, 'week': 7, 'month': 31}
    is_successfully = False

    # Получили список рассылок пользователя
    all_newsletters = Newsletter.objects.filter(owner=user_id, is_active=True)

    # Проходимся по всем рассылкам и проверяем время
    for newsletter in all_newsletters:
        start_time_dtm = datetime.strptime(f'{datetime.now().date()} {newsletter.start_time}', '%Y-%m-%d %H:%M')
        stop_time_dtm = datetime.strptime(f'{datetime.now().date()} {newsletter.stop_time}', '%Y-%m-%d %H:%M')
        if newsletter.last_time:
            last_time_dtm = datetime.strptime(newsletter.last_time, '%Y-%m-%d %H:%M:%S.%f')
        else:
            last_time_dtm = None

        # Проверяем что время рассылки пришло
        if stop_time_dtm > datetime.now() > start_time_dtm and \
                ((last_time_dtm and (datetime.now() - last_time_dtm).days >= periodicity[newsletter.period]) or last_time_dtm is None):

            # Собираем все почты пользователей в список
            recipients = []
            for client in newsletter.client.all():
                recipients.append(client.email)

            # Отправляем письмо
            try:
                send_mail(newsletter.message.topic, newsletter.message.text, settings.EMAIL_HOST_USER, recipients, fail_silently=False,)
            except smtplib.SMTPSenderRefused:
                server_response = "Адрес отправителя отклонен"
            except smtplib.SMTPAuthenticationError:
                server_response = "Ошибка авторизации. Неправильное имя пользователя или пароль"
            except OSError:
                server_response = "Хост недоступен"
            else:
                is_successfully = True
                server_response = "OK"

            # Перезаписываем last_time в рассылке
            newsletter.last_time = str(datetime.now())
            newsletter.save()

            # Создаем логи
            for client in newsletter.client.all():
                Logs.objects.create(
                    date=newsletter.last_time,
                    status=is_successfully,
                    error_msg=server_response,
                    client=client,
                    newsletter=newsletter,
                )
