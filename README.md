

## Análise de Logs Nanodegree

Este projeto é um exercício de análise de logs de acesso a um site de notícias fictício. Através de código SQL ele responde a três perguntas:

  

1. Quais são os três artigos mais populares de todos os tempos? Quais artigos foram os mais acessados?

2. Quem são os autores de artigos mais populares de todos os tempos? Isto é, quando você organizar todos os artigos que cada autor escreveu, quais autores obtiveram mais views?

3. Em quais dias mais de 1% das requisições resultaram em erros?

  

Para tanto, utilizei o arquivo project-news.py escrito em Pyhton 2.7.12. ele pode ser executado com o seguinte comando:

  

    python project-news.py

  

Ele foi escrito com comando SQL e para a terceira questão foram criadas as seguintes VIEWS:

  

    "CREATE VIEW total AS SELECT date(time) as day, count(id) AS views FROM log GROUP BY day")

    "CREATE VIEW error AS SELECT date(time) as day, count(id) AS views FROM log WHERE status = '404 NOT FOUND' GROUP BY day")

Os resultados gerados são listados no arquivo [RESULTS.txt](https://github.com/denisprado/analise-log/blob/master/RESULTS.txt)