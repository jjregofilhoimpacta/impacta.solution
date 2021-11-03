import json
import boto3

def lambda_handler(event, context):
    try:
        s3 = boto3.resource('s3')
        f = s3.Object('impacta.solutionchat','PAG_02_CADASTRO.HTML')
        body = f.get()['Body'].read()
        return {
                'statusCode': 200,
                'body': json.dumps(str(body))
               }
    except:
        print('Lambda function terminada sem sucesso')
        return {
                'statusCode': 400,
                'body': json.dumps('Erro ao tentar processar mensagem')
               }




