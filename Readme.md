# Test task API pay-trio

Необходимо​ ​ разработать​ ​ и ​ ​ реализовать​ ​ flask​ ​ сервис.

Сервис​ ​ состоит​ ​ из​ ​ одной​ ​ страницы​ ​ со​ ​ следующими​ ​ элементами:
- Сумма​ ​ оплаты​ ​ (поле​ ​ ввода​ ​ суммы)
- Валюта​ ​ оплаты​ ​ (выпадающий​ ​ список​ ​ со​ ​ значениями​ ​ USD,​ ​ EUR)
- Описание​ ​ товара​ ​ (многострочное​ ​ поле​ ​ ввода​ ​ информации)
- Оплатить​ ​ (кнопка)

## Installation
- Clone.  git clone https://github.com/LarisaShcherbachenko/TestTask-API-pay-trio.git

- Create virtualenv and install needded libraries from requirements.txt

```bash
virtualenv --python=python3.6 ~/venv
pip3 install -r requirements.txt
```

For running server use:

```bash
export FLASK_APP=main.py
flask run
```
