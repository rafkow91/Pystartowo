class MailSender():
    def __init__(self, mailbox: dict = None) -> None:
        if mailbox is not None:
            self.mailbox = mailbox
        else:
            self.mailbox = {
                'user': 'user',
                'password': 'pass',
                'ssl': True,
                'port': 443,
                'host': 'mail.mail'
            }
        
    def send_mail(title):
        print(f'send mail\n\tTitle: ')