# Supletivo Data Hackers: AWS CDK

Material criado para a aula de AWS CDK do Supletivo Data Hackers.

O objetivo é criar uma aplicação que utiliza o AWS CDK para criar uma stack de infraestrutura na AWS. Essa stack será composta por um bucket S3, uma função Lambda e um API Gateway.

#TODO: insert link to video

**[Confira aqui o conteúdo gravado]()**

## Objetivos da demo

1. Criar uma stack de infraestrutura na AWS utilizando o AWS CDK
    1. Mostrar como o CDK gera o template CloudFormation
    1. Mostrar como o CDK faz o deploy da stack
    1. Mostrar como trabalhar com diferentes ambientes (dev, prod, etc)
1. Criar um bucket S3
1. Criar uma função Lambda que:
    1. Recebe um input e escreve um arquivo no bucket S3
    1. Lê o arquivo do bucket S3 e retorna o conteúdo
1. Criar um API Gateway
    1. Criar um endpoint para escrever um arquivo no bucket S3
    1. Criar um endpoint para ler um arquivo do bucket S3
1. Criar um teste para a função Lambda
1. Criar um teste para a infraestrutura

## Requisitos

1. Para instalar esse projeto você precisa ter o Python Poetry instalado. Para instalar o Poetry, siga as instruções do [site oficial](https://python-poetry.org/docs/#installing-with-the-official-installer)
1. Você também precisa instalar o AWS CDK. Para isso, também siga as instruções do [site oficial](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html).
1. Por fim, você precisa ter uma conta na AWS e configurar as credenciais de acesso. Para isso, siga as instruções do [site oficial](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).
    1. Crie um perfil para acessar as suas credenciais. Para isso, crie um arquivo `~/.aws/credentials` com o seguinte conteúdo:

        ```ini
        [my_profile]
        aws_access_key_id = <your_access_key_id>
        aws_secret_access_key = <your_secret_access_key>
        ```

    1. Crie um arquivo `~/.aws/config` com o seguinte conteúdo:

        ```ini
        [profile my_profile]
        region=us-east-1
        output=json
        ```

## Instalação

Simplesmente rode:

```bash
make init
```

Esse comando irá criar um ambiente virtual Python e instalar todas as dependências necessárias para rodar o projeto. Também vai rodar os testes para garantir que tudo está funcionando.

Acesse o ambiente virtual com:

```bash
source .venv/bin/activate
```

## Rodando o projeto

Após modificar o seu stack, você pode rodar o seguinte comando para ver o template CloudFormation gerado:

```bash
make synth
```

E para fazer o deploy da stack:

```bash
cdk deploy --profile my_profile
```
