# Observatório de Educação Médica — Brasil e Estados Unidos

Projeto de pesquisa comparativa sobre a evolução da oferta de escolas médicas e as diferenças regulatórias entre Brasil e Estados Unidos.

## Perguntas centrais
- Como evoluiu o número de escolas médicas nos dois países desde 1900?
- Quais regras, requisitos de acreditação, recursos financeiros e campos de prática condicionam a abertura e a continuidade de uma escola?
- Como separar expansão da graduação, capacidade de residência e qualidade da formação?

## Navegação
- [Página inicial](index.html)
- [Evolução histórica e gráfico](evolucao.html)
- [Tabela anual 1900–2025](serie-anual.html)
- [Como abrir uma escola: Brasil e EUA](criterios.html)
- [Fatores que influenciam a expansão](fatores.html)
- [Metodologia e referências](docs/METODOLOGIA.md)

## Política de evidências
As páginas citam fontes no texto pelo sistema autor-data e devem oferecer referências verificáveis. A série histórica distingue contagens publicadas de aproximações. Não há uma série anual exata e harmonizada para cada ano de 1900 ao presente nos materiais históricos identificados. Por isso, o gráfico exibe marcos documentados, sem inventar valores anuais. Lacunas não devem ser preenchidas por interpolação apresentada como observação.

## Análise dos fatores de expansão
A nova página [Fatores que influenciam a abertura de escolas médicas](fatores.html) organiza mecanismos a investigar no Brasil e nos EUA: regulação, campos clínicos, financiamento, acreditação, residência, capital privado e avaliação. As sínteses são pontos de partida; afirmações específicas devem ser conferidas em documentos primários vigentes, especialmente quando se referirem a políticas ou projetos legislativos de 2026.

## Validação automática
O workflow [Validar dados e páginas](.github/workflows/validate-site.yml) executa verificações básicas a cada push e pull request: leitura de HTML, existência de destinos de links locais e verificações elementares de arquivos CSV. Ele não substitui revisão acadêmica, validação semântica dos dados ou checagem de disponibilidade de links externos.

## Fontes principais
- Oliveira et al. (2019), estudo longitudinal sobre escolas médicas brasileiras entre 1808 e 2018, baseado no e-MEC.
- Fishbein (1940) e Barzansky (2010), história da contagem de escolas médicas nos EUA.
- AAMC/JAMA, séries históricas de escolas MD.
- AACOM, diretório de escolas osteopáticas DO.
- Lei nº 12.871/2013 e normas de acreditação LCME/COCA.

Consulte [docs/METODOLOGIA.md](docs/METODOLOGIA.md) para as limitações e referências completas.
