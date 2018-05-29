# Identificador de caracteres

en-US====================================================





pt-BR=====================================================

## Sobre a atividade
Esta é uma atividade de PDI para a universidade Federal da Paraíba e tem o objetovo de desenvolver as técnicas de Processamento digital de imagens aprendidas no curso.

### Como funciona

Inicialmente o planejamento era de usar uma tecnologia similar ao do QR-CODE e consertar a angulação da imagem de entrada.

Depois da imagem já está na posição correta, aplicamos um KNN da imagem de entrada com um conjunto de imagens previamentes avaliadas (conjunto de teste), ou seja, aplicamos uma técnica de IA, mesmo que de forma rudimentar


Feito isso, poderíamos redimensionar a imagem e converter para ascii.
Convertemos a imagem para ASCII porque é muito mais fácil calcular uma distância euclidiana de uma string do que de uma imagem

#### Trainamento
- ir para a pasta core
```sh
cd core
```

- Rodar o arquivo de treinamento
```sh
python pre-processing/trainning.py
```

## Grupo
- Luiz Henrique Freire Barros
- Alisson Galiza
- Aline Araujo
- Alisson Lacerda

## Dependencias
```sh
sudo pip install Pillow
```

(TODO: usa o numpy. Ver se é padrão do ubuntu)

[OpenCV](https://docs.opencv.org/3.0-beta/index.html)
```
sudo apt-get install python-opencv
```