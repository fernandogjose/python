import boto3

from boto3.dynamodb.conditions import Attr

# conectando com o banco e tabela
dynamo_client = boto3.resource(service_name='dynamodb',
                               region_name='us-east-2',
                               aws_access_key_id='AKIA6CNRKGYV5HI3BBB3',
                               aws_secret_access_key='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')

tabela_usuarios = dynamo_client.Table('usuarios')

# inserindo um registro
print('Inserindo registros')
print('---')
tabela_usuarios.put_item(Item={
    'usuario_id': '1',
    'data_de_nascimento': '1981-06-08',
    'nome': 'Fernando'
})

tabela_usuarios.put_item(Item={
    'usuario_id': '2',
    'data_de_nascimento': '1981-12-17',
    'nome': 'Priscila'
})

# listando todos os registros
print('')
print('---')
print('Listando todos os registros')
print('---')
print('Total de usuários: ', len(tabela_usuarios.scan()['Items']))
for item in tabela_usuarios.scan()['Items']:
    print('usuario sem filtro - usuario_id:', item['usuario_id'])
    print('usuario sem filtro - data_de_nascimento:',
          item['data_de_nascimento'])
    print('usuario sem filtro - nome:', item['nome'])
    print('')

# filtrando os registros
print('')
print('---')
print('Filtrando registros por nome')
print('---')
usuarios = tabela_usuarios.scan(Select="ALL_ATTRIBUTES",
                                FilterExpression=Attr("nome").eq("Fernando"))
print('Total de registros encontrados', len(usuarios['Items']))
for usuario in usuarios['Items']:
    print('usuario com filtro - usuario_id:', usuario['usuario_id'])
    print('usuario com filtro - data_de_nascimento:',
          usuario['data_de_nascimento'])
    print('usuario com filtro - nome:', usuario['nome'])
    print('')

# filtrando os registros por nome e data_nascimento
print('')
print('---')
print('Filtrando registros por nome e data_de_nascimento')
print('---')
usuarios = tabela_usuarios.scan(Select="ALL_ATTRIBUTES",
                                FilterExpression=Attr("nome").eq("Priscila") &
                                                 Attr("data_de_nascimento").eq("1981-12-17"))
print('Total de registros encontrados', len(usuarios['Items']))
for usuario in usuarios['Items']:
    print('usuario com filtro - usuario_id:', usuario['usuario_id'])
    print('usuario com filtro - data_de_nascimento:',
          usuario['data_de_nascimento'])
    print('usuario com filtro - nome:', usuario['nome'])
    print('')
