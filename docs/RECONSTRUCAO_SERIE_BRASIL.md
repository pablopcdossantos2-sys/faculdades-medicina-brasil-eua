# Reconstrução da série brasileira por registros individuais

**Status em 21/10/2026: pipeline preparado; série nacional reconstruída ainda não validada.**

## Fontes e limite material

O MEC descreve o [Cadastro e-MEC](https://www.gov.br/mec/pt-br/politica-regulacao-supervisao-educacao-superior/cadastro-nacional-de-cursos-e-ies) como base oficial que contém dados cadastrais e atos autorizativos de cursos e IES, inclusive informações sobre instituições extintas. A [consulta pública do e-MEC](https://capacitaemec.mec.gov.br/emec/nova) oferece pesquisa de cursos e instituições. O Inep explica que o Censo da Educação Superior usa o cadastro e-MEC e coleta dados de vagas, matrículas, ingressantes, concluintes e docentes ([página oficial do Censo](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-da-educacao-superior)).

**Importante:** localizar o cadastro público não equivale a obter um arquivo histórico nacional, completo e versionado, com cada curso, início efetivo e encerramento para todos os anos. Nesta rodada não foi possível recuperar, por uma interface de exportação verificável, uma extração completa e reproduzível dos registros individuais. Portanto, não seria correto afirmar que a série brasileira já foi reconstruída, nem inventar registros individuais a partir de totais agregados publicados.

## Artefatos adicionados

- `data/br-medical-schools-register-template.csv`: esquema mínimo para normalizar um registro por curso, com identificadores, datas efetivas e fonte.
- `scripts/rebuild_brazil_series.py`: script Python sem dependências externas para produzir uma série anual de cursos e instituições representadas a partir de um CSV normalizado.
- `data/medical-schools-benchmarks.csv`: removidos os valores brasileiros de 1959 (27) e 1969 (68), que eram estimativas derivadas de totais decenais e pressupunham ausência de encerramentos. O campo permanece sem valor até haver inventário por registro.

## Regras de reconstrução

1. Uma linha por código de curso, sem confundir curso, IES, campus/local de oferta e mantenedora.
2. Registrar datas no formato ISO `AAAA-MM-DD` e anexar URL do ato ou registro que sustenta cada data.
3. `effective_start_date` deve representar início efetivo documentado, não data da notícia, do reconhecimento posterior ou da consulta atual.
4. `closure_effective_date` deve refletir encerramento efetivo documentado; curso com status atual “extinto” não pode ser automaticamente removido de todos os anos anteriores.
5. Fusão, mudança de nome, transferência, mudança de código e múltiplos locais de oferta precisam de uma tabela de correspondência auditável; não deduplicar apenas pelo nome.
6. A saída do script conta cursos e IES representadas com datas conhecidas. Ela **não prova cobertura nacional**: registros sem data inicial são excluídos, e a completude de registros históricos precisa ser validada separadamente.
7. Comparar os resultados com os marcos publicados por Oliveira et al. (2019), o estudo FMUSP/SERES de 2025 e as Sinopses do Censo da Educação Superior. Diferenças devem ser explicadas por unidade, data de corte, curso extinto, curso autorizado versus ativo e escopo da fonte — não corrigidas por interpolação.

## Como executar

Depois de preencher um CSV normalizado usando o cabeçalho do modelo:

```bash
python scripts/rebuild_brazil_series.py caminho/para/exportacao_normalizada.csv --start-year 1808 --end-year 2025 --output data/br-medical-schools-annual-rebuilt.csv
```

A saída tem uma linha por ano, com contagem de cursos e de IES representadas. O script rejeita códigos de curso duplicados, datas malformadas e encerramentos anteriores ao início. A série resultante deve continuar marcada como derivada de inventário até que a cobertura e os casos históricos sejam auditados.

## Fontes norte-americanas históricas recuperadas

A tabela II do material da reunião anual da AAMC de 1974 foi localizada: [Average Size of Medical Schools, 1930–1974 (PDF)](https://www.aamc.org/download/370942/data/85th_annual_meeting_agenda_11-12-74.pdf). Ela informa 76 escolas em 1930–31, 77 em 1940–41, 79 em 1950–51, 86 em 1960–61 e 103 em 1970–71, com a definição “all medical schools”, e diz ter sido desenvolvida a partir das publicações anuais *Medical Education in the United States* do JAMA. Os URLs dessa fonte primária foram adicionados às cinco linhas históricas correspondentes do CSV. A definição histórica não deve ser mesclada sem ressalvas com a contagem moderna de escolas MD.

## Próximas ações necessárias para fechar a série

- Obter uma extração completa do cadastro de cursos de Medicina, incluindo registros extintos e atos autorizativos, ou reunir exportações arquivadas com datas de corte.
- Guardar o arquivo original imutável, a data de extração, os metadados e o hash SHA-256.
- Normalizar e revisar manualmente datas de início/encerramento e relações entre cursos/IES.
- Executar o script, comparar contagens com os marcos de 2018 e 2025 e só então atualizar gráfico e tabela pública.
