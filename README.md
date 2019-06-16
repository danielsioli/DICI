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

Salve o arquivo no formato Excel XLSX.

Os cronogramas e leiautes precisam já estar cadastrados no DICI.

Exemplo:

|Cronograma|Leiaute|Ano|Entrega|Entidade|Arquivo|
|----------|-------|---|-------|--------|-------|
|Acessos SMP 2019|Acessos SMP|2019|MES_2|CLARO S.A. (40.432.544/0001-47)|C:\claro.csv|
|Cronograma Marca|Cronograma Marca|2019|Pontual|AGENCIA NACIONAL DE TELECOMUNICACOES - SEDE (02.030.715/0001-12)|C:\marca.xml|
|Credenciadas do SMP|Credenciadas do SMP|2019|Pontual|AGENCIA NACIONAL DE TELECOMUNICACOES - SEDE (02.030.715/0001-12)|C:\credenciadas.csv|

Mantenha o chromedriver.exe (http://chromedriver.chromium.org/downloads) no %PATH% ou na pasta do seu projeto.

Enviar dados para o servidor de produção
```
dici.enviar_dados('C:\\arquivos.xlsx')
```
Enviar dados para o servidor de homologação
```
dici.enviar_dados('C:\\arquivos.xlsx', hm=True)
```
Endereço do servidor de produção
```
dici.servidor_producao
```
Endereço do servidor de homologação
```
dici.servidor_homologacao
```
Tipos de entrega aceitas
```
dici.entregas
```
Tipos de arquivos de dados aceitos
```
dici.formatos
```