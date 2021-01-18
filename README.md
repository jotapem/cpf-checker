# What is the CPF
CPF (*Cadastro de Pessoas Físicas*, Natural Persons Register in English) is an individual taxpayer document number, which acts as social security indentification for brazilian individuals. It has 11 digits: the last 2 digits are defined in terms of the previous 9, and act as verification digits. Every digit in the CPF is an algarism in base 10 (number ranging from 0 to 9).

# How does CPF verification works
We can represent a CPF as below:

![CPF-repr](https://latex.codecogs.com/gif.latex?d_1%20d_2%20d_3.%20d_4%20d_5%20d_6%20.%20d_7%20d_8%20d_9%20%5Ctext%7B-%7D%20v_1%20v_2)


Therefore we can define the verification digits in function of the document's first 9 digits, as follows (in which `a mod b` denotes the remainder of the integer division of `a` per `b`):

![CPF-v1](https://latex.codecogs.com/gif.latex?v_1%20%3D%20%2810d_1%20&plus;%209d_2%20&plus;%208d_3%20&plus;%207_d4%20&plus;%206e_5%20&plus;%205e_6%20&plus;%204e_7%20&plus;%203e_8%20&plus;%202e_9%29%20%5Ctext%7B%20mod%20%7D%2011)


![CPF-v2](https://latex.codecogs.com/gif.latex?v_2%20%3D%20%2811d_1%20&plus;%2010d_2%20&plus;%209d_3%20&plus;%208_d4%20&plus;%207e_5%20&plus;%206e_6%20&plus;%205e_7%20&plus;%204e_8%20&plus;%203e_9%20&plus;%202v_1%29%20%5Ctext%7B%20mod%20%7D%2011)

# Usage

## Requirements
Besides a Python 3 interpreter, this project requires the `requests` Python library, as evidenced by the project's `Pipfile`.

### Pipenv
One recommended (but not required) tool for handling the project's dependencies is `pipenv`, which installation instructions can be found at https://pypi.org/project/pipenv/ (acessed at 15 jan 2021 03:05:24 -03).


## Demo
Once you have the requirements installed in your system, you can call the script with `pipenv run python demo.py [cpf_1, ..., cpf_n]`.

Alternatively, you can initialize the Python's environment and then call the script, as in:
```
pipenv shell
python demo.py [cpf_1, ..., cpf_n]
```

If you are not using `pipenv`, but has an appropriate Python environment, you can just call `python demo.py [cpf_1, ..., cpf_n]` after initializing your environment.

### Tested system configurations
(Contributions to this section is highly appreciated)

* (@jotapem)
    1. OS: Ubuntu 20.04.1
    2. Interpreter: Python 3.8.5
    3. Pipenv: 11.9.0

# References
- https://transferwise.com/gb/blog/cpf-cnpj-meaning-brazil (acessed at 18 jan 2021 10:23:58 -03)
- https://www.somatematica.com.br/faq/cpf.php#:~:text=Regra%20Pr%C3%A1tica&text=Logo%2C%20um%20CPF%20tem%2011,verificador%20do%20n%C3%BAmero%20do%20CPF (acessed at 14 jan 2021 01:35:56 -03)
