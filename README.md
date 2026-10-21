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
- [Auditoria de fontes e série histórica](docs/AUDITORIA_FONTES_E_SERIE.md)
- [Protocolo para reconstrução da série brasileira por registros e-MEC](docs/RECONSTRUCAO_SERIE_BRASIL.md)

## Política de evidências
As páginas citam fontes no texto pelo sistema autor-data e devem oferecer referências verificáveis. A série histórica distingue contagens publicadas de aproximações. Não há uma série anual exata e harmonizada para cada ano de 1900 ao presente nos materiais históricos identificados. Por isso, o gráfico exibe marcos documentados, sem inventar valores anuais. Lacunas não devem ser preenchidas por interpolação apresentada como observação.

## Análise dos fatores de expansão
A página [Fatores que influenciam a abertura de escolas médicas](fatores.html) organiza mecanismos a investigar no Brasil e nos EUA. A auditoria de outubro de 2026 atualizou a série MD dos EUA com dados JAMA para 2023–24, 2024–25 e 2025–26; recuperou a tabela histórica da AAMC para 1930–1974; retirou dois valores brasileiros derivados sem comprovação de ausência de encerramentos; e preparou um pipeline de reconstrução por registros individuais do e-MEC. O pipeline aguarda uma extração histórica completa e auditável, portanto a série brasileira ainda não é apresentada como reconstruída. Consulte [docs/AUDITORIA_FONTES_E_SERIE.md](docs/AUDITORIA_FONTES_E_SERIE.md) para fontes e pendências.

## Validação automática
O workflow [Validar dados e páginas](.github/workflows/validate-site.yml) executa verificações básicas a cada push e pull request: leitura de HTML, existência de destinos de links locais e verificações elementares de arquivos CSV. Ele não substitui revisão acadêmica, validação semântica dos dados ou checagem de disponibilidade de links externos.

## Fontes principais
- Oliveira et al. (2019), estudo longitudinal sobre escolas médicas brasileiras entre 1808 e 2018, baseado no e-MEC.
- Fishbein (1940) e Barzansky (2010), história da contagem de escolas médicas nos EUA.
- AAMC/JAMA, séries históricas de escolas MD.
- AACOM, diretório de escolas osteopáticas DO.
- Lei nº 12.871/2013 e normas de acreditação LCME/COCA.

Consulte [docs/METODOLOGIA.md](docs/METODOLOGIA.md) para as limitações e referências completas.
