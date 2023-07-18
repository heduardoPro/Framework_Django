import boto3
from botocore.exceptions import NoCredentialsError
from django.shortcuts import render, redirect
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

class IndexView(FormView):
    template_name = 'home/index.html'
    form_class = ImageForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form.save()
        
        try:
            # Create an instance of the SQS client
            sqs = boto3.client(
                'sqs',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                region_name=AWS_S3_REGION
            )

            # Send a message to the queue
            queue_url = URL_SQS
            message_body = 'Envio de imagem para fila'
            response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)

            # Check the response
            if 'MessageId' in response:
                print('Mensagem enviada com sucesso!')
            else:
                print('Erro ao enviar a mensagem.')

        except NoCredentialsError:
            message = "Erro de autenticação ao acessar o serviço S3."
        except Exception as e:
            message = f"Erro ao acessar a imagem no S3: {str(e)}"

        return super().form_valid(form)

class ContextView(ListView):
    model = Image
    template_name = 'home/images.html'
    context_object_name = 'images'