<h1 align="center">Fubanguy - The Game</h1>

<p align="center">
  <img src="src/infra/assets/images/fubanguy_logo.png" alt="fubanguy-logo" width="120px" height="120px"/>
  <br>
  <em>Fubanguy! Esse game é fuminante cara! Personagens muito locos, só as lendas!

Imagina só, você controlando o Tiringa, Maike da SWAT,  Ninja e muito mais! Cada personagem tem suas manhas e golpes especiais que vão fazer você dar muita risada e se surpreender.

Os cenários são insanos também, meu parceiro! Você vai lutar no "Bar", na "Favela" e até no "QGs". É espetaculoso!

Nesse game você pode jogar de 2 kkkk, então chama seu parceiro e prepare-se para dar muita risada.

Fubanguy reune toda a zoeira e insanidade BR direto pro mundo dos games. Vlw meu parceiro! É nóis!
  <br>
</p>


## [Download](https://drive.google.com/file/d/1TCiYlrGc-fikG-mqr2OSc628dPrULmJV/view?usp=sharing)

## Materiais Teóricos e Práticos

### Linguagem de Programação
 - [Pygame Docs](https://www.pygame.org/docs/)

### Loops
  - [Python Docs - Event Loop](https://docs.python.org/3/library/asyncio-eventloop.html)

### Colisão
  - [Collisions in Pygame - Beginner Tutorial](https://www.youtube.com/results?search_query=pygame+rect+collidelist)
  - [Github - Collision and Intersection](https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md)

### Física
 - [How to Code Realistic Physics in Python Games! PyGame Tutorial (Gravity, Bounce, Throw, Friction)](https://www.youtube.com/watch?v=5j0uU3aJxJM)

 ### Encapsulamento
 - [Conceito de encapsulamento](https://cursos.alura.com.br/forum/topico-conceito-de-encapsulamento-104406)
 - [Canal Python Nexus](https://youtu.be/bhg5EISbV0k?si=kEaRCwm6kvuiX_M_)

 ### POO em Python
 - [Como Funcionam Classes e Programação Orientada a Objetos em Python](https://youtu.be/97A_Cyyh-eU?si=x4lyXuLIW6aObW3g)
 - [Python 3.13.0 documentation](https://docs.python.org/3/)

 ### Clean Architecture 
 - [Software Architeture PDF](https://agorism.dev/book/software-architecture/%28Robert%20C.%20Martin%20Series%29%20Robert%20C.%20Martin%20-%20Clean%20Architecture_%20A%20Craftsman%E2%80%99s%20Guide%20to%20Software%20Structure%20and%20Design-Prentice%20Hall%20%282017%29.pdf)

## Vídeos
- [Yago Macinelli](https://drive.google.com/drive/folders/1ZUe_18Ijkr9uaW1NkSsxhdJIPJtEtRfp?usp=sharing)
- [Márcio Carvalho](https://drive.google.com/drive/folders/1MZ06If6TC8BfHqw3X1e86InFENjaXA33?usp=sharing)

### Local Development

To contribute to Angular docs, you can setup a local environment with the following commands:

```bash
# Clone Fubanguy repo
git clone https://github.com/yamacinelli/fubanguy.git

# Navigate to project directory
cd fubanguy
```

## Development Setup

3. Create and activate the virtual environment:

```bash
python3 -m venv venv
```
* Linux
```bash
source venv/bin/activate
```
* Windows
* ```open powershell with administrator privileges```

```powershell
Set-ExecutionPolicy AllSigned
```
* ```Activate```
```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Settings for vscode


Download and import the profile containing the extensions into vscode, [Extentions](https://drive.google.com/file/d/1FIF-ZdqTT4A0Ocv8bIXZG7sMWGT3OkfF/view)

* ```settings.json```
```json
{
    "files.autoSave": "afterDelay",
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python3",
    "python.autoComplete.extraPaths": ["${workspaceFolder}/src"],
    "python.envFile": "${workspaceFolder}/.env",
    "python.analysis.extraPaths": ["${workspaceFolder}/src"],
}
```

* ```launch.json```
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: main.py",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/src/main.py",
            "console": "integratedTerminal",
        },
    ]
}
```

## Set Workspace

- Download and install pyenv for Windows or Mac or Linux
- Install and configure version python global
```bash
pyenv install x.xx.xx
```
```bash
pyenv global x.xx.xx
```

- Active a version in yor root project dir
```bash
pyenv local x.xx.xx
```

- Download and configuration `Poetry` this instalations  must be make every python version.
```bash
pip install poetry
```
- Create project with poretry
```besh
poetry new name_project
```
- Creates a basic pyproject.toml file in the current directory.
```bash
poetry init
```

- Configure the poetry for create the virtual envs inner project
```bash
poetry config virtualenvs.in-project true
```

- Create and activate venvs with poetry
```bash
poetry shell
```
- Install libs with poetry
```bash
poetry add lib_name
```
- For after clone this project to github
```bash
poetry install
```

- For more information about poetry
```bash
poetry list
```

## Build .exe
- Remove dir dist and build in your root
```bash
pyinstall main.spec
```

## Project structure

```plaintext
fubanguy/
│
├── src/
│   ├── main.py                         # Entrada principal do sistema
│   ├── domain/
│   │   └── entities/
│   │       ├── fighter.py              # Entidade Fighter
│   │       └── stage.py                # Entidade Stage
│   ├── core/
│   │   ├── value_object/
│   │   │   └── transform.py            # Objetos de Valor
│   │   └── interfaces/                 # Diretório para Portas (Interfaces)
│   │       ├── display_interface.py    # Interface para Display (Output Port)
│   │       ├── controls_interface.py   # Interface para Controls (Input Port)
│   │       └── music_interface.py      # Interface para Music (Output Port)
│   ├── application/
│   │   └── use_cases/
│   │       ├── fight_use_case.py      # Caso de Uso para lutas
│   │       └── game_engine.py         # Motor do jogo que gerencia o loop principal
│   └── infra/
│       └── frameworks/
│           └── py_game/
│               ├── pygame_controls.py # Adaptador para Controls usando Pygame
│               ├── pygame_display.py  # Adaptador para Display usando Pygame
│               └── pygame_music.py    # Adaptador para Music usando Pygame
└── README.md
```

**Love Fubanguy? Give our repo a star :star: :arrow_up:.**

Made with :blue_heart: by MÁRCIO :wave: [See my LinkedIn](https://www.linkedin.com/in/marciojcarvalho/) and YAGO :wave: [See my LinkedIn](https://www.linkedin.com/in/yago-macinelli-569560140?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
