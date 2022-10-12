# Blockchain Concepts
...
### Proof of Work
...
### Blockchain Collaboration

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


### Real-Time Messaging Network throught Publisher and Subscriber

Padrão da rede recebe o conceito de várias mensagens através de canais. Estes canais carregam as mensagens que são enviadas através dos publishers.

Os publishers não se preocupam sobre quem está olhando os canais. Tudo que se preocupam é em garantir que as mensagens estão sendo enviadas através do canais.

Enquanto isto, os subscribers permanecem conectados em broadcast nos canais, e não se preocupa em quem está enviando a mensagem; Os subscribers podem escolher quais dos canais são consumidos.


Tecnologia utilizada é o PubNub.

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
source blockchain_env/Scripts/activate
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