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

## Tutorial para obter os arquivos de entrada (ação externa necessária)

A próxima etapa depende de obter um arquivo exportado que não está disponível nesta sessão como download direto. Não é necessário executar Python nem editar o GitHub: basta baixar os arquivos oficiais e anexá-los à conversa para que possam ser inspecionados e processados.

### Rota A — consulta do Cadastro e-MEC

1. Abra **Cadastro Nacional de Cursos e IES — Ministério da Educação**: https://www.gov.br/mec/pt-br/politica-regulacao-supervisao-educacao-superior/cadastro-nacional-de-cursos-e-ies.
2. Entre no link para a consulta pública do e-MEC. Se o endereço direto não abrir, use o portal oficial do MEC acima ou https://emec.mec.gov.br/.
3. Na consulta de cursos, pesquise o curso **Medicina**. Se houver filtro de grau, modalidade ou situação, não exclua cursos só porque aparecem como extintos, desativados ou com situação diferente de “em atividade”. O objetivo é obter registros atuais e históricos disponíveis.
4. Abra os resultados e procure a opção de exportar/baixar ou converter a consulta em **Excel** ou **PDF**. A página de perguntas frequentes da SERES informa que os resultados de consulta podem ser convertidos em planilhas Excel ou PDF: https://www.gov.br/mec/pt-br/acesso-a-informacao/institucional/estrutura-organizacional/orgaos-especificos-singulares/secretaria-de-regulacao-e-supervisao-educacao-superior/perguntasfrequentes.
5. Se a consulta permitir exportar todos os resultados, salve o arquivo original sem alterar colunas, nomes ou códigos. Se só permitir exportar a página atual, repita para todas as páginas e mantenha os arquivos separados; não copie apenas os cursos que estão ativos.
6. Registre a data em que consultou o sistema. Se houver detalhes de cada curso, abra alguns registros e baixe/guarde os atos autorizativos que informem autorização, início, encerramento ou extinção. O registro atual do e-MEC não garante sozinho a data histórica de início efetivo.
7. Anexe aqui os arquivos Excel, CSV ou PDF obtidos. Não é necessário renomeá-los nem convertê-los.

### Rota B — dados anuais do Censo da Educação Superior (complementar)

Esta rota serve para verificar cursos registrados em cada edição do Censo, em especial para a parte recente da série; não substitui atos autorizativos nem prova, sozinha, a data exata de abertura ou encerramento.

1. Abra **Microdados do Censo da Educação Superior — Inep**: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior.
2. Baixe os pacotes ZIP anuais disponíveis. A página consultada lista anos de 1995 a 2024, incluindo o pacote de 2024. Para começar, priorize 2010–2024; se a conexão permitir, baixe também 1995–2009.
3. Guarde cada ZIP original. Não envie documentos com dados pessoais que não sejam necessários; a análise pretendida é de códigos e informações institucionais/de cursos.
4. Anexe os ZIPs à conversa. Se o tamanho total exceder o limite de anexos, envie primeiro 2024, 2020, 2015, 2010 e 2000, e informe quais anos não conseguiu obter. Depois podemos processar lotes menores.
5. Ao processar, vamos identificar o arquivo de cursos e os campos de código do curso, instituição, área/código de curso, situação e ano de referência. Os nomes e códigos dos campos variam por edição; serão verificados nos dicionários de cada ano, não presumidos.

### Se não houver exportação histórica completa: pedido formal de dados

Use o canal **Fala.BR — Plataforma Integrada de Ouvidoria e Acesso à Informação**: https://falabr.cgu.gov.br/ e selecione pedido de acesso à informação destinado ao Ministério da Educação/SERES. Pode copiar o texto abaixo e ajustar somente os dados de contato solicitados pelo portal:

> Solicito, em formato aberto (CSV ou XLSX), a extração dos registros do Cadastro e-MEC referentes a cursos de graduação em Medicina (bacharelado), incluindo cursos ativos, extintos, desativados, em extinção e demais situações existentes na base. Solicito, para cada registro, código do curso, código e nome da IES, município/UF, local de oferta quando disponível, situação atual, datas e números dos atos autorizativos, datas de início de funcionamento e de encerramento/extinção, e histórico de alterações de situação, código, denominação, IES ou local de oferta, caso esses campos estejam disponíveis. Solicito também o dicionário de dados, a data de extração e a descrição das limitações de cobertura histórica. Caso a base completa não possa ser fornecida, peço que indiquem os conjuntos de dados oficiais e as unidades responsáveis que permitam reconstruir a série histórica anual desde 1808, e que forneçam os registros disponíveis para cursos extintos.

Guarde o número de protocolo e a resposta. Se a Administração não possuir algum campo ou histórico solicitado, isso deve ser documentado como limitação, não preenchido por inferência.

### O que me enviar

- Preferencialmente: exportação e-MEC completa em XLSX/CSV, com cursos extintos incluídos e data de consulta.
- Complementarmente: ZIPs dos microdados do Censo da Educação Superior, com os dicionários/Leia-me incluídos nos pacotes.
- Se a exportação for impossível: resposta do pedido Fala.BR e/ou protocolo, para adequar a estratégia aos dados que o MEC efetivamente disponibiliza.

Quando os arquivos forem anexados, eu faço a inspeção dos esquemas, normalização, deduplicação auditável, cálculo de contagens anuais, comparação com fontes publicadas e atualização do gráfico/CSV. Não envie senha, login gov.br, documentos pessoais ou credenciais.

## Próximas ações necessárias para fechar a série

- Obter uma extração completa do cadastro de cursos de Medicina, incluindo registros extintos e atos autorizativos, ou reunir exportações arquivadas com datas de corte.
- Guardar o arquivo original imutável, a data de extração, os metadados e o hash SHA-256.
- Normalizar e revisar manualmente datas de início/encerramento e relações entre cursos/IES.
- Executar o script, comparar contagens com os marcos de 2018 e 2025 e só então atualizar gráfico e tabela pública.
