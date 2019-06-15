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
```
Montar um arquivo Excel (XLSX) com o seguinte formato
|Cronograma|Leiaute|Ano|Entrega|Entidade|Arquivo|
|----------|-------|---|-------|--------|-------|
|Nome do Cronograma|Nome do Leiaute|Ano 4 Dígitos|Tipo de Entrega|Nome da Entidade|Caminho para arquivo com dados a serem carregados|
```
Enviar Arquivo
```
argumentos = {'arquivos':'C:\\arquivos.xlsx','hm':True}
dici.enviar_dados(argumentos)
```
Olhar o Help
```
dici.help()
```