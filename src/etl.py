import pandas as pd
import os
import requests
from pathlib import Path
from random import randint
from model import Pedidos,Produto, Cliente
from db import session

def gerar_numero_aleatorio():
    random_ip = ".".join(str(randint(0, 255)) for _ in range(4))
    return random_ip

def ler_arquivo_pedido(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    for _, row in df.iterrows():
        pedido = Pedidos(id_cliente =row['id_cliente'], id_produto=row['id_produto'], data_pedido = row['data_pedido'],
                         valor_total = row['valor_total'], status = row['status'])
        session.add(pedido)  # Adicionar o produto à sessão
    
    # Confirmar a transação no banco de dados
    session.commit()
    print("Dados inseridos com sucesso!")


def ler_arquivo_produto(path: Path) -> pd.DataFrame:
    df = pd.read_excel(path)
  
    for _, row in df.iterrows():
        produto = Produto(nome_produto=row['nome_produto'], categoria=row['categoria'])
        session.add(produto)  # Adicionar o produto à sessão
    
    # Confirmar a transação no banco de dados
    session.commit()
    print("Dados inseridos com sucesso!")


def ler_api (id: int) -> pd.DataFrame:
    response = requests.get(f'https://ipinfo.io/{id}/json')
    if response.status_code == 200:
        data = response.json()
        data_region = data['region']
        data_city = data['city']
        data_cep = data['postal']
        data_empresa = data['org']

        return Cliente(nome_empresa = data_empresa, estado = data_region, cidade = data_city, cep = data_cep)

    else:
        return None

def inserir_dados_api():

    cliente = ler_api(gerar_numero_aleatorio())
    if cliente:
        session.add(cliente)
        session.commit()
        print(f"Cliente {cliente.nome_empresa} inserido com sucesso!")
    else:
        print("Não foi possível obter dados da API.")


if __name__ == "__main__":
    url_excel = "./dados/produtos.xlsx"
    url_csv = "./dados/pedidos_2023.csv"
    df1 = ler_arquivo_pedido(url_csv)
    #df2 = ler_arquivo_produto(url_excel)

    

    #print(inserir_dados_api())

    print(df1)
    #print(df2)
