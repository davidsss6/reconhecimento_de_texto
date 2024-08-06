
# 📝 Projeto de Reconhecimento de Texto

## 📜 Descrição
Este projeto realiza o reconhecimento de texto em imagens utilizando as bibliotecas Tesseract e OpenCV em Python. O objetivo é aplicar os conceitos aprendidos durante o curso para desenvolver uma aplicação prática e funcional de reconhecimento de texto.

## 🛠️ Tecnologias Utilizadas
- 🧠 ChatGPT
- 🐍 Python
- 👁️ OpenCV
- 🔍 Tesseract-OCR
- 🖼️ Pillow

## 📈 Processo

Como o curso não foi profundo o suficiente em alguns conceitos, usei o ChatGPT para me ajudar na interpretação e montagem do projeto.

![Tela do Projeto](https://github.com/davidsss6/reconhecimento_de_texto/blob/main/tela_01.png)

Montei um projeto de reconhecimento de texto que utiliza tecnologias comuns e eficazes para essa tarefa. O código foi escrito em Python, uma das linguagens mais populares para tarefas de IA, juntamente com bibliotecas como Tesseract (para reconhecimento de texto) e OpenCV (para manipulação de imagens).

Usei o Visual Studio Code para desenvolver o projeto e o GitHub para armazenar e compartilhar o código.

Após confeccionar o código e instalar as bibliotecas necessárias, rodei localmente em minha máquina para testar o funcionamento.

![Tela do Projeto](https://github.com/davidsss6/reconhecimento_de_texto/blob/main/tela_02.png)

O resultado foi o reconhecimento dos textos que estavam nessa imagem:

![Tela do Projeto](https://github.com/davidsss6/reconhecimento_de_texto/blob/main/tela_03.png)

Para este arquivo de texto:

![Tela do Projeto](https://github.com/davidsss6/reconhecimento_de_texto/blob/main/tela_04.png)

Após certificar o funcionamento correto do código, fiz o upload para meu repositório no GitHub.

### 💡 Insights e Aprendizados

- **Precisão do Reconhecimento**: A precisão do reconhecimento de texto pode variar com base na qualidade e no tipo de imagem. Imagens de alta resolução e com bom contraste tendem a produzir melhores resultados.
- **Pré-processamento de Imagem**: Converter as imagens para escala de cinza e aplicar técnicas de limiarização pode melhorar significativamente os resultados do OCR.
- **Integração com Tesseract**: Aprender a integrar o Tesseract-OCR com Python foi uma experiência valiosa, permitindo explorar o poder do reconhecimento de texto em várias aplicações.

### 🚀 Possibilidades Futuras

- **Melhorar a Precisão**: Implementar técnicas adicionais de pré-processamento de imagem, como remoção de ruído e correção de inclinação.
- **Interface de Usuário**: Desenvolver uma interface gráfica para facilitar o uso da aplicação por usuários não técnicos.

## 📦 Como Usar

Coloque no diretório input uma imagem da qual voce queira extrair o texto. Ao rodar no terminal o comando "python recognize_text.py" ele já reconhece esta imagem e extrai dela o texto em um arquivo .txt que é salvo no diretório "output". Lembrando que para o correto funcionamento e necessário instalar as bibliotecas necessárias. 

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
