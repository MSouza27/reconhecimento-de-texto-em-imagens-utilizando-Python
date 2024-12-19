# Projeto: Reconhecimento de Texto com OCR e Visão Computacional

Este projeto implementa uma solução para reconhecimento de texto em imagens usando a biblioteca **Tesseract OCR** integrada com **OpenCV**. O código processa imagens de uma pasta específica, realiza a extração de texto, busca termos específicos nos textos extraídos e destaca as ocorrências diretamente nas imagens.

## Funcionalidades

- Percorre automaticamente todos os arquivos em uma pasta especificada.
- Realiza o pré-processamento e a exibição de imagens.
- Utiliza o **Tesseract OCR** para extração de texto em português (`lang='por'`).
- Armazena os textos extraídos em um arquivo de texto.
- Realiza buscas de ocorrências de termos específicos nos textos.
- Adiciona caixas delimitadoras e destaca palavras diretamente nas imagens.

---

## Tecnologias Utilizadas

- **Python**
- **OpenCV**: Manipulação e exibição de imagens.
- **Tesseract OCR**: Extração de texto.
- **NumPy**: Manipulação de arrays e imagens.
- **Matplotlib**: Exibição de imagens.
- **Pillow**: Inserção de texto nas imagens.
- **Regex (re)**: Busca e validação de termos nos textos extraídos.

---

## Configuração do Ambiente

1. **Instalar Dependências**:
   Certifique-se de ter o Python e as seguintes bibliotecas instaladas:
   ```bash
   pip install numpy opencv-python pytesseract pillow matplotlib
   ```

2. **Instalar o Tesseract OCR**:
   - No macOS:
     ```bash
     brew install tesseract
     ```
   - No Windows:
     Baixe e instale a versão do Tesseract [aqui](https://github.com/tesseract-ocr/tesseract).
   - Configure o caminho do Tesseract no código:
     ```python
     config_tesseract = "--tessdata-dir /opt/homebrew/share/tessdata"
     ```

3. **Estrutura de Arquivos**:
   Organize as imagens que deseja processar na pasta especificada no código:
   ```plaintext
   /Projeto
     ├── Imagens/
     │   ├── Projeto/
     │   │   ├── imagem1.jpg
     │   │   ├── imagem2.png
     │   │   └── ...
     ├── calibri.ttf
   ```

---

## Como Executar

1. Configure o caminho das imagens no código:
   ```python


2. Ajuste o caminho da fonte para escrita nas imagens:
   ```python


3. Execute o script:
   ```bash
   python main.py
   ```

4. Verifique os resultados:
   - Textos extraídos salvos no arquivo `resultados_ocr.txt`.
   - Ocorrências destacadas diretamente nas imagens processadas.

---

## Resultados Esperados

- **Texto Extraído**: Um arquivo contendo todos os textos extraídos das imagens.
- **Busca de Termos**: Exibe no console o número de ocorrências do termo buscado.
- **Destacando Palavras nas Imagens**: Cria imagens processadas com caixas delimitadoras e texto destacado.

---

## Exemplo de Aplicação

### Entrada
- Imagem contendo texto em português.

### Saída
- Texto extraído:
  ```plaintext
  ==================
  imagem1.jpg
  Texto extraído da imagem 1.
  ```
- Imagem processada com texto destacado.

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do repositório.
2. Crie um branch para sua feature:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. Submeta um pull request.

---

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
