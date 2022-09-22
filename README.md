# Blockchain Concepts
...
### Proof of Work
...
### Blockchain Collaboration - Chain Validation

Para realizar a validação dos blocos dentro da Chain, é fundamental que existam algumas regras;

A primeira regra, o bloco deve possuir todos os campos de validação, tais como, timestamp, hash, last_hash e data

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
