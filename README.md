# pyDICI
Pacote para enviar dados ao DICI

## Install 

```
pip install pyDICI
```

## Use
Importar pacote
```
import pyDICI as dici
```
Arquivo Excel

Montar um arquivo Excel (XLSX) com o seguinte formato. Podem ser adicionadas quantas linhas forem necessárias.

|Cronograma|Leiaute|Ano|Entrega|Entidade|Arquivo|
|----------|-------|---|-------|--------|-------|
|Nome do Cronograma|Nome do Leiaute|Ano 4 Dígitos|Tipo de Entrega|Nome da Entidade|Caminho para arquivo com dados a serem carregados|

Exemplo

|Cronograma|Leiaute|Ano|Entrega|Entidade|Arquivo|
|----------|-------|---|-------|--------|-------|
|Acessos SMP 2019|Acessos SMP|2019|MES_2|CLARO S.A. (40.432.544/0001-47)|C:\claro.csv|
|Cronograma Marca|Cronograma Marca|2019|Pontual|AGENCIA NACIONAL DE TELECOMUNICACOES - SEDE (02.030.715/0001-12)|C:\marca.csv|

Manter o chromedriver.exe (http://chromedriver.chromium.org/downloads) no %PATH% ou na pasta do seu projeto.

Enviar Arquivo
```
dici.enviar_dados('C:\\arquivos.xlsx')
```