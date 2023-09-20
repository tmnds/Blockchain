# Blockchain and Cryptocurrency

#### What's Blockchain and Cryptocurrency?
O que é blockchain e Cryptocurrency, por quê utilizá-los, e como?

The blockchain is a distributed and decentralized ledger that stores data sych as transactions, and the is publicly shared across all the nodes of its network.

Blocks stores data likes ['transaction1', 'transaction2', ...], hash likes 0x000a9434feedxx2200  and last_hash likes 'hash-of-last-block'

![Blockchain]("C:\Users\Thales\Pictures\Screenshots\blockchain.png")

Ledger - Livro Razão

Blockchains normalmente são descentralizados, ou seja, não há uma instituição única que administra a chain, tornando-o conteúdo das transações mais seguro, pois, leva-se em consideração que todos os usuários da rede chain podem ter acessos a todas as transações.

Blockchain e Cryptocurrency são tecnologias distintas, apesar de andarem juntas.

Cryptocurrency é popularmente conhecido como uma moeda digital, ou digital medium of exchange. Blockchain é apenas uma camada do que se é utilizado para as cryptocurrencies. Existem 3 principais aspectos nas cryptocurrencies, sendo elas o Blockchain, Wallets e Mining.

Transações devem estar cryptografadas para evitar personificação e adulteração. Além disto, para registrar qualquer transação, precisa carimbar o dado transacional com sua assinatura (que basicamente, é baseada em um par de crypto keys, sendo uma pública e outra privada).

Para estas combinações, ainda é necessário a utilização de Wallets, que também fazem o uso do par de chaves pública e privada. Esta carteira irá possuir informações do saldo, e por fim, terá informações em relação ao endereço da sua carteira, para que transferências possam ser realizadas. As utilização das chaves privadas tornam as transações oficiais.

O último aspecto das cryptocurrencies é o conceito de Mining. Miners trabalham para adicionar transações a blockchain 


#### Proof of Work
...
#### Blockchain Collaboration

**Chain Validation**

É o conceito de validação da blockchain
O que significa?
Para realizar a validação dos blocos dentro da Chain, é fundamental que existam algumas regras;

1. O bloco deve possuir os campos corretos de validação, tais como, timestamp, data, last_hash, e hash;
2. O campo last_hash deve possuir uma referência do bloco que precede o bloco atual, isso é particularmente importante pois cria um link entre o bloco atual e toda blockchain;
3. O hash do bloco deve ser válido.
4. Proof of Work deve ser válido (Prova de Trabalho), o bloco deve ter o mesmo número de zeros de acordo com a dificuldade de geração do bloco


E por que é necessário o replacement?
O blockchain não é criado por apenas uma pessoa, mas por várias; Poder do blochain é multiplos nós; Tornando-se descentralizado e sem responsabilidade de gerenciamento de uma instituição, utilizando apenas o poder de processamento das máquinas que colaboram..


#### Real-Time Messaging Network throught Publisher and Subscriber

Padrão da rede recebe o conceito de várias mensagens através de canais. Estes canais carregam as mensagens que são enviadas através dos publishers.

Os publishers não se preocupam sobre quem está olhando os canais. Tudo que se preocupam é em garantir que as mensagens estão sendo enviadas através do canais.

Enquanto isto, os subscribers permanecem conectados em broadcast nos canais, e não se preocupa em quem está enviando a mensagem; Os subscribers podem escolher quais dos canais são consumidos.


Tecnologia utilizada é o PubNub.


#### Wallets, Keys and Transactions

Wallet is a core of the cryptocurrency with a few main aspects to it.

1. Balance
    It's how much currency an individual has collected in the blockchain history.
2. Private Key
    Used to Generate unique signatures.
3. Public Key
    Used to verify signatures.
4. Address
    Other individuals can send currency to that wallet.

Transactions are the objects that capture the information behind the exchange of currency between two individuals

# Developer Commands

**Remove all .pyc and .pyo files as well as __pycache__**
```terminal
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
```

**Remove .pyc files from Git remote repository**
```terminal
(git rm *.pyc) or (git rm -f *.pyc) to force
git commit -a -m 'all pyc files removed'
git push
```

**Install search lib**
```python
pip install pip-search
```

**How to search libs**
```python
pip_search <lib_name>
```

**Execution Policy ENV**
```terminal
Set-ExecutionPolicy Unrestricted -Force
```

**Creating a virtual environment**
```terminal
python -m venv <name>
```

**Activate the virtual environment**
```terminal
source blockchain-env/Scripts/activate
```

**Deactivate the virtual environment**
```terminal
deactivate
```

**Testing**
```python
echo $VIRTUAL_ENV

```

**Install all packages**

```python
pip install -r requirements.txt
```

**Execute modules inside folders**
```python
python -m <path_wihtout .py in the end>
Example: python -m backend.blockchain.block
```

**Run the tests**

Install de Lib
```python
pip install pytest
```

1. Create folder with name *tests*;
2. Run testst with the command
```python
python -m pytest <path_test>
```

**Run the application and API**

Make sure to activate the virtual environment.

```python
python3 -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```python
export PEER=True && python -m backend.ap
```