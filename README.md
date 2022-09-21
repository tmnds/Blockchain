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
