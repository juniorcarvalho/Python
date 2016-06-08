from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Júnior Carvalho', cpf='04539428659',
                    email='joseadolfojr@gmail.com', phone='21.99601.6875')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'joseadolfojr@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['joseadolfojr@gmail.com', 'joseadolfojr@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = ['Júnior Carvalho', '04539428659', 'joseadolfojr@gmail.com', '21.99601.6875', ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

