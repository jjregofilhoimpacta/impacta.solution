import json
from datetime import datetime
import boto3

dynamodb = boto3.resource('dynamodb')

mensagens = dynamodb.Table('mensagens')


def lambda_handler(event, context):
    remetente = "nome_usuario"
    destinatario = "nome_dest"
    email = "email"
    msg = "msg"

    try:
        
        mensagens.put_item(
            Item={
                'remetente': remetente, # Chave de Partição  no Banco
                'destinatario' : destinatario,
                'email' : email,
                'msg' : msg,
              }
        )

        return {
       
            'statusCode': 200,
            'body': json.dumps('Cadastrado com Sucesso')
        }

    except:
        print('Erro: lambda function terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar inserir no BD')
        }
        