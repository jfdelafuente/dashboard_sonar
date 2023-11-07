# python-template

## Poetry

$ poetry init

Si estamos creando un nuevo proyecto podemos también ejecutar directamente:
poetry new mi-proyecto

## Linting our code

📚 Ahora que tenemos algunas pruebas, el siguiente paso lógico es comenzar a modificar nuestro código. Linting es el proceso de verificar nuestro código en busca de posibles errores y/o falta de formato. Existen muchos linters (pylint, flake8, black, etc.).

$ poetry add --group lint flake8 black isort mypy

- Code Formating: utilizamos la combinación de black y isort. Añadimos la configuración en pyproject.toml.
- Code Linting: flake8. Añadimos la configuración en el fichero setup.cfg (tb se podría crear un .flake8)
- Static Type Checker: mypy. Añadimos la configuración en el fichero setup.cfg (tb en pyprojecto.toml)

A few examples of linting your code include:

$ poetry run mypy hello_world_cli/cli.py

$ poetry run flake8 hello_world_cli/cli.py

$ poetry run black hello_world_cli/cli.py

## Testing: PyTest

📚 Las pruebas garantizan que nuestro código se comporte como se esperaba. Como ya sabrás. Hay muchos tipos de pruebas (pruebas unitarias, pruebas de integración, pruebas de un extremo a otro, etc…) pero en este artículo daremos un ejemplo de pruebas unitarias. Las pruebas unitarias son pruebas que verifican la unidad más pequeña de su código (es decir, una función o un método).

We can add the most common python tests package, pytest

$ poetry add --group test pytest

and the pytest coverage package to shows the code coverage

$ poetry add --group test pytest-cov pytest-sugar

Also, we need to add the test path for the pytest in the setup.cfg(o en pyprojecto.toml)
After running them, we can run:

$ poetry run pytest --cov --cov-fail-under=100
$ poetry run pytest --cov=informe_sonar --cov-report term-missing --cov-report=html

o sin pytest-sugar:

$ poetry run pytest -p no:sugar

## Automatización de las comprobaciones locales con pre-commit

📚 Ahora que comprendemos el linting y las pruebas, podemos comenzar a automatizar nuestras comprobaciones. El objetivo de automatizar nuestras comprobaciones es asegurarnos de que nuestro código esté siempre en buen estado. La confirmación previa es una excelente alternativa ya que básicamente nos impide enviar código incorrecto o mal formateado (como su nombre indica).

🛠️ Para instalar la confirmación previa, podemos ejecutar el siguiente comando:

Install the pre-commit using poetry:

$ poetry add --group dev pre-commit

Create a file called .pre-commit-config.yaml and then run the installation for the pre-commit

$ poetry run pre-commit install

Now, you can try to run the pre-commit using

$ poetry run pre-commit run --all-files

la confirmación previa está ejecutando las comprobaciones que definimos en el 
fidhero .pre-commit-config.yaml.

and every time you commit, the pre-commit config will also runs.
You can always run:

git add .
git commit --no-verify -m "feat: ..."

mas info en: "https://jairoandres.com/pre-commit-para-mejorar-las-revisiones-de-codigo/"

## Automatice las comprobaciones remotas con GitHub Actions

📚 Ahora que tenemos algunas pruebas y algunos linters, podemos comenzar a automatizar nuestras comprobaciones en el lado del servidor. Si bien existen muchas herramientas que pueden ayudarnos a automatizar nuestras comprobaciones (GitHub Actions, Travis CI, Circle CI, etc.), yo personalmente uso y recomiendo Github Actions (también conocido como GHA).

pendiente: "https://armandsauzay.medium.com/python-project-setup-a-step-by-step-guide-to-industry-best-practices-dbce717b2d12#4-add-some-code"

## Automatiza nuestro lanzamiento con GitHub Actions

📚 Hemos hablado brevemente sobre linting (usando black, flake8, isort y mypy) y pruebas (usando pytest). La versión es un concepto igualmente importante que nos permite dar versiones a instantáneas específicas de nuestro código. Conceptualmente, asigna un sha de confirmación con un número (v1.2.3).

pendiente: "https://armandsauzay.medium.com/python-project-setup-a-step-by-step-guide-to-industry-best-practices-dbce717b2d12#4-add-some-code"

## Otros

.commitlintrc.yaml: extiende @commitlint/config-conventional, lo que significa que toma la configuración de confirmación predeterminada (con mensajes de confirmación “fix: …” y “feat: …”

.releaserc.json: configuración de complementos sobre cómo liberar nuestro código. Consulte la sección Lanzamiento a continuación para obtener más detalles.

## Bibliografía

### 🐍 Setting up Python Projects: Part I: Mastering the Art of Python Project Setup: A Step-by-Step Guide

 "https://towardsdatascience.com/setting-up-python-projects-part-i-408603868c08"

### Set Up Flask Environment

$ # CMD
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "Development"
$ $env:FLASK_DEBUG = "true"

Start the app

$ flask run

At this point, the app runs at http://127.0.0.1:5000/.

## ✨ Start the app in Docker

> **Step 1** - Download the code from the GH repository (using `GIT`) 

$ # Get the code
$ git clone https://github.com/appseed-projects/<YOUR_BUILD_ID>.git
$ cd <YOUR_BUILD_ID>

> **Step 2** - Edit `.env` and set `DEBUG=True`. This will activate the `SQLite` persistance.

DEBUG=True

> **Step 3** - Start the APP in `Docker`

$ docker-compose up --build

Visit `http://localhost:5085` in your browser. The app should be up & running.
