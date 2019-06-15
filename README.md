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

Montar um arquivo Excel (XLSX) com o seguinte formato. Pode ser adicionadas quantas linhas forem necessárias.

|Cronograma|Leiaute|Ano|Entrega|Entidade|Arquivo|
|----------|-------|---|-------|--------|-------|
|Nome do Cronograma|Nome do Leiaute|Ano 4 Dígitos|Tipo de Entrega|Nome da Entidade|Caminho para arquivo com dados a serem carregados|

Manter o chromedriver.exe no %PATH% ou na pasta do seu projeto.

Enviar Arquivo
```
dici.enviar_dados('C:\\arquivos.xlsx')
```