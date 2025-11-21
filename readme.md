# ssclient

`ssclient` — Python-клиент для работы с HTTP API облака [Serverspace](https://serverspace.io/). Библиотека выделена из [s2ctl] (https://github.com/itglobalcom/s2ctl) в отдельный проект.
Библиотека упрощает интеграцию с API: берёт на себя авторизацию, формирование запросов, обработку ответов и ошибок.


## Установка

### Из исходников (Git)

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/sadfox/ssclient.git
   cd ssclient
   ```

2. Установите библиотеку:

   ```bash
   # обычная установка
   pip install .

   # или установка в editable-режиме для разработки
   pip install -e .
   ```


### Как зависимость в другом проекте (requirements.yml)

Если другой проект управляет зависимостями через `requirements.yml` (или аналогичный файл в YAML-формате), вы можете подключить `ssclient` как Git-зависимость.


```yaml
dependencies:
  - name: ssclient
    repo: git+https://github.com/sadfox/ssclient.git
    version: main  # или конкретный тег/коммит
```

Либо, если ваш тулчейн ожидает «сырую» строку для pip:

```yaml
dependencies:
  - "git+https://github.com/sadfox/ssclient.git@main#egg=ssclient"
```

После этого зависимости устанавливаются стандартным способом для вашего проекта, например:

```bash
# пример, команда зависит от используемого инструмента
pip install -r requirements.txt          # если requirements.yml генерирует requirements.txt
```


## Быстрый старт

### 1. Получите API-ключ

1. Зайдите в панель управления Serverspace.
2. Перейдите в настройки проекта.
3. Создайте/скопируйте API-ключ.

### 2. Использование в коде

Пример синхронного клиента:

```python
from ssclient.client import SSClient
from ssclient.http_client import HttpClient

http_client = HttpClient(
    apikey="YOUR_API_KEY",
    host="https://api.serverspace.io",
)

ss_client = SSClient(http_client)

# пример: получить информацию о текущем проекте
project = ss_client.project.get()
print(project.id, project.state)

# пример: вывести список серверов
for server in ss_client.servers.list():
    print(server.id, server.name, server.state)
```

или

```python
from ssclient.http_client_factory import SSClientFactory

ss_client = SSClientFactory.create(apikey="YOUR_API_KEY")

# пример: получить информацию о текущем проекте
project = ss_client.project.get()
print(project.id, project.state)

# пример: вывести список серверов
for server in ss_client.servers.list():
    print(server.id, server.name, server.state)
```

## Совместимость

- Python 3.8+ (уточните фактическую минимальную версию в `pyproject.toml`).
- Поддерживаются Linux, macOS и Windows (зависит от стека зависимостей и CI).


## Ссылки

- Облако Serverspace: <https://serverspace.io/>
- Панель управления: <https://control.serverspace.io/>
- Документация по API: `https://serverspace.io/api/` (пример, замените на фактический URL)
