<h1>Redes de Computadores</h1>

  Projeto da disciplina de Redes de Computadores, que consiste em criar uma aplicação simples utilizando qualquer framework e realizar o deploy na AWS utilizando o serviço EC2. A aplicação será acessível através de um domínio e terá as seguintes funcionalidades: fazer o upload de um arquivo, enviar esse arquivo para um bucket no Amazon S3 e enviar uma mensagem para uma fila do Amazon SQS assim que o arquivo for enviado com sucesso.

## Visão Geral

Neste projeto, vamos criar uma aplicação web que permitirá aos usuários fazer o upload de arquivos. Os arquivos enviados serão armazenados no Amazon S3, e uma mensagem será enviada para uma fila do Amazon SQS para notificar o sucesso do upload.

## Pré-Requisitos

Antes de começar, você precisará ter o seguinte configurado:

1. Uma conta AWS (Amazon Web Services).
2. Um ambiente de desenvolvimento configurado com as credenciais da AWS.
3. Um domínio registrado ou configurado para o seu aplicativo.

## Configuração

1. **Configuração da AWS:**

   Certifique-se de ter as credenciais da AWS configuradas em seu ambiente de desenvolvimento. Isso pode ser feito configurando as variáveis de ambiente ou usando as configurações padrão do AWS CLI.

2. **Configuração do Amazon S3:**

   Crie um bucket no Amazon S3 onde os arquivos enviados serão armazenados. Anote o nome do bucket para configuração posterior.

3. **Configuração do Amazon SQS:**

   Crie uma fila no Amazon SQS para receber as mensagens de notificação de sucesso do upload. Anote o URL da fila para configuração posterior.

4. **Configuração do Domínio:**

   Configure seu domínio para apontar para o IP público da sua instância EC2 após o deploy.

## Desenvolvimento da Aplicação

1. Crie uma aplicação web simples utilizando o framework de sua escolha. Certifique-se de incluir a funcionalidade de upload de arquivos na aplicação.

2. Implemente a lógica para enviar os arquivos para o Amazon S3 após o upload bem-sucedido.

3. Implemente a lógica para enviar uma mensagem para a fila do Amazon SQS com informações sobre o arquivo enviado com sucesso.

4. Configure o domínio para apontar para o IP público da instância EC2 após o deploy.

## Deploy na AWS com EC2

1. Crie uma instância EC2 na AWS usando a imagem desejada (por exemplo, uma imagem Linux).

2. Configure a instância EC2 com as permissões necessárias para acessar o Amazon S3 e o Amazon SQS.

3. Implante sua aplicação na instância EC2 e configure-a para ser executada como um serviço web.

4. Abra as portas necessárias na instância EC2 para permitir o tráfego HTTP ou HTTPS, dependendo da configuração do seu aplicativo.

5. Configure o seu domínio para apontar para o IP público da instância EC2.

## Testando a Aplicação

Após o deploy da aplicação na AWS, acesse o seu domínio e teste a funcionalidade de upload de arquivos. Verifique se os arquivos são armazenados no Amazon S3 e se uma mensagem é enviada para a fila do Amazon SQS após o upload bem-sucedido.


