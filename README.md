# COMPUTER GRAPHIC PROJECT - License Plates

**Computação Gráfica - UNILASALLE**

*Pedro Henrique Canabarro, Felipe Lemos Oliveira, Everton Santos de Castro*


## Problema

O dataset utilizado contém imagens **poluídas** visualmente, com **veículos em segundo plano** ou parcialmente visíveis, o que dificulta a identificação correta da placa. A proposta do projeto é criar um pipeline que filtre, detecte e recorte automaticamente as placas, mesmo sob essas condições.

- **Dataset**: [Kaggle - License Plates Dataset](https://www.kaggle.com/datasets/trainingdatapro/license-plates-1-209-438-ocr-plates)

## Descrição do Projeto

Este projeto tem como objetivo realizar a **detecção e recorte automático de placas de veículos** a partir de imagens fornecidas por um dataset público. Ele faz parte da disciplina de Computação Gráfica e utiliza técnicas de pré-processamento de imagem e análise de contornos para localizar placas em imagens reais.

## Tecnologias Utilizadas

- Python 3
- OpenCV (cv2)
- Processamento de imagem:
  - Conversão para escala de cinza
  - Filtro bilateral
  - Detecção de bordas com Canny
  - Análise de contornos
  - Verificação de aspect ratio para identificar possíveis placas

## Estrutura do Projeto

📁 dataset/ -- Pasta com as imagens originais
📁 output/ -- Pasta onde as imagens com as placas recortadas serão salvas 
📄 main.py -- Script principal de processamento 
📄 requirements.txt -- Dependências do projeto

## Como Executar

1. **Instale as dependências**

```bash
pip install -r requirements.txt
```
2. **Adicione suas imagens à pasta dataset/.**
3. **Execute o script principal**
```bash
python main.py
```
4. **As imagens com as placas detectadas serão salvas na pasta output/.**

## Resultado Esperado

Cada imagem da pasta `dataset`, tenta localizar a placa e, se encontrada, a recorta com uma margem de segurança e salva em `output/`.

Ao final da execução, o terminal irá apresentar um resumo indicando:

- Quantas imagens foram processadas no total
- Quantas tiveram a placa detectada com sucesso
- Quais não puderam ser processadas por falha na detecção

## Organização do grupo

- Desenvolvimento de Código:
- Documentação:
- Testes e Organização de Diretórios:

