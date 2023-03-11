# Daily News

Projeto final para entrega do módulo de Extração de Dados do curso de Engenharia de Dados - Santader Coder`s.
Curso fornecido pela ADA em parceria com o Banco Santander.

## Escopo

Escopo definido no arquivo "Projeto ED - Coleta de dados.pdf"

## Objetivo

1 - Realiza o consumo de notícias através de uma API pública.

2 - Disponibilizar o arquivo com da notícia em um diretório local

3 - Realizar uma "análise de sentimento" da notícia através de outra API pública

4 - Realizar tratamentos iniciais no arquivo

5 - Disponibilizar a informação diariamente

6 - Realizar o agendamento da execução desse fluxo utilizando o Airflow ou o Cron

### Realizado

Todas as etapas de 1 a 6 foram realizadas.
Durante o desenvolvimento foram observados diversos pontos de otimização que serão desenvolvidos em breve.
O schedule inicialmente foi feito utilizando o cron em uma máquina virtual Linux (ubuntu), contudo posteiormente será substituído por uma dag no Airflow.

### Fluxo
1 - Script News_colector.py - Responsável pela coleta das 5 notícias principais dos países Brasil, USA e Portugal, tratamento e registro dos arquivos no filesystem com extensão .parquet.

2 - Script Feeling_analysis.py - Resposável pelo consumo dos arquivos .parquet, aplicação da "análise de sentimento", adição dessa informação no dataframe e registro dos arquivos no filsystem local. Tanto em formato .parquet quanto .csv.
