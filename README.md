**Install search lib**
```python
pip install pip-search
```

**How to search libs**
```python
pip_search <lib_name>
```

**Creating a virtual environment**
```terminal
python -m venv <name>
```

**Activate the virtual environment**
```terminal
source blockchain-env/Scripts/activate
```

**Testando**
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
