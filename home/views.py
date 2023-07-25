import boto3
from botocore.exceptions import NoCredentialsError
from django.shortcuts import render, redirect
from apscheduler.schedulers.background import BackgroundScheduler
from django.contrib.messages.views import SuccessMessageMixin
from .models import Image
from .forms import ImageForm
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from project.settings import (
     AWS_ACCESS_KEY_ID,
     AWS_S3_REGION,
     AWS_SECRET_ACCESS_KEY,
     URL_SQS,
)

class IndexView(SuccessMessageMixin, FormView):
    template_name = 'home/index.html'
    form_class = ImageForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        # Salva a imagem no banco de dados
        form.save()

        # Envia uma mensagem para a fila do SQS
        message_body = 'ENVIAR MENSAGEM PARA O SQS DA AWS'
        queue_url = 'https://sqs.us-east-2.amazonaws.com/913530390976/MyQueue'
        self.send_message(queue_url, message_body)

        # Agenda a função de recebimento de mensagens em segundo plano
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.receive_and_process_messages, 'interval', seconds=20)
        scheduler.start()

        return super().form_valid(form)

    def send_message(self, queue_url, message_body):
        try:
            # Cria um cliente do SQS
            sqs = boto3.client('sqs', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_S3_REGION)
            
            # Envia uma mensagem para a fila
            response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
            
            # Verifica se a mensagem foi enviada com sucesso
            if 'MessageId' in response:
                self.success_message = 'Mensagem enviada com sucesso para o SQS!'
            else:
                self.success_message = 'Erro ao enviar mensagem.'
        except NoCredentialsError:
            self.success_message = "Erro de autenticação ao acessar o serviço SQS."
        except Exception as e:
            self.success_message = f"Erro: {str(e)}"
    
    def receive_and_process_messages(self):

            # Cria um cliente do SQS
            sqs = boto3.client('sqs', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_S3_REGION)
            
            # Recebe uma mensagem da fila
            message, receipt_handle = self.receive_message(URL_SQS)
            if message is not None:
                print(f'Mensagem recebida: {message["Body"]}')
                # Aqui você pode processar a mensagem conforme necessário

                # Deleta a mensagem da fila após processamento
                self.delete_message(URL_SQS, receipt_handle)

    def receive_message(self, queue_url):
        try:
            # Cria um cliente do SQS
            sqs = boto3.client('sqs', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_S3_REGION)
            
            # Recebe uma mensagem da fila
            response = sqs.receive_message(
                QueueUrl=queue_url,
                AttributeNames=['SentTimestamp'],
                MaxNumberOfMessages=1,
                MessageAttributeNames=['All'],
                VisibilityTimeout=0,
                WaitTimeSeconds=10
            )

            if 'Messages' in response:
                message = response['Messages'][0]
                receipt_handle = message['ReceiptHandle']
                print(f'Received: {receipt_handle}')
                return message, receipt_handle
            else:
                print('Nenhuma mensagem na fila.')
                return None, None
        except NoCredentialsError:
            print("Erro de autenticação ao acessar o serviço SQS.")
            return None, None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None, None

    def delete_message(self, queue_url, receipt_handle):
        try:
            # Cria um cliente do SQS
            sqs = boto3.client('sqs', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_S3_REGION)

            # Deleta a mensagem da fila
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)

            print('Mensagem deletada com sucesso!')
        except NoCredentialsError:
            print("Erro de autenticação ao acessar o serviço SQS.")
        except Exception as e:
            print(f"Errorr: {str(e)}")

class ContextView(ListView):
    model = Image
    template_name = 'home/images.html'
    context_object_name = 'images'