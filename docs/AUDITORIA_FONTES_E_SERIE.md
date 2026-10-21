# Auditoria de fontes e revisão da série histórica

**Data da revisão:** 21 de outubro de 2026  
**Escopo:** fontes primárias para regras brasileiras e dados recentes; revisão da unidade de contagem; atualização da série anual norte-americana.

## Resultado executivo

Esta revisão melhora a rastreabilidade, mas não transforma a série em um censo anual harmonizado dos dois países. O CSV data/medical-schools-benchmarks.csv preserva a distinção entre marcos históricos, valores derivados, séries por ano acadêmico e indicadores com escopos diferentes.

## Correções implementadas

1. **EUA — série MD atualizada:** o artigo de Barzansky e Walker, publicado no *JAMA* em 29/09/2026, informa 156 escolas MD em 2023–2024, 157 em 2024–2025 e 158 em 2025–2026. Esses valores foram acrescentados ao CSV, à tabela anual e ao gráfico. Fonte: [JAMA 2026](https://jamanetwork.com/journals/jama/fullarticle/2854662), DOI [10.1001/jama.2026.16297](https://doi.org/10.1001/jama.2026.16297).
2. **Contagem AAMC separada:** os 160 programas do FY2025 incluem acreditação preliminar, provisória ou plena; a tabela financeira também informa 153 programas com acreditação plena. Portanto, 160 não é sinônimo de 160 escolas plenamente acreditadas, nem substitui a contagem anual do artigo do *JAMA*. Fonte: [AAMC — receitas de escolas médicas, FY2025](https://www.aamc.org/data-reports/data/i-revenue-us-medical-schools-source-fiscal-year-2025).
3. **Brasil — referência de 2025:** a FMUSP divulgou 494 escolas médicas e 50.974 vagas anuais, com base em dados da SERES/MEC fornecidos em 15/09/2025 via LAI. O valor permanece classificado como marco publicado, não como uma série histórica reconstruída por instituição. Fonte: [FMUSP, 06/10/2025](https://www.fm.usp.br/fmusp/imprensa/06-102025--brasil-ultrapassa-50-mil-vagas-anuais-em-medicina-apos-abertura-de-77-novos-cursos-alertam-pesquisadores-da-fmusp).
4. **Portaria SERES/MEC nº 531/2023:** a descrição do site foi corrigida para explicitar que o ato disciplina processos de autorização de novos cursos e aumento de vagas instaurados por força de decisão judicial, no contexto da ADC 81/DF. Não é correto generalizá-la como o único rito para toda autorização. A página também não afirma uma regra universal de leitos por vaga sem apontar dispositivo e âmbito de aplicação. Fonte: [texto oficial da Portaria](https://www.gov.br/mec/pt-br/assuntos/es/cursos-de-medicina/regulacao-e-supervisao/documentos/PORTARIASERES_MECN531DE22DEDEZEMBRODE2023.pdf).
5. **MP nº 1.370/2026:** em 21/10/2026, a ficha oficial da Câmara registra aprovação pela Câmara em 15/10/2026 e remessa ao Senado, com Projeto de Lei de Conversão nº 14/2026. O texto foi descrito como em tramitação, não como lei definitivamente sancionada. Fonte: [ficha de tramitação da Câmara](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2634542).
6. **AACOM/DO:** a página institucional informa 48 colégios osteopáticos acreditados e 75 locais de ensino. Colégios e locais de ensino são unidades diferentes; a contagem DO permanece separada da série MD. Fonte: [AACOM — Colleges of Osteopathic Medicine](https://www.aacom.org/become-a-doctor/prepare-for-medical-school/us-colleges-of-osteopathic-medicine).

## Como interpretar o CSV

O arquivo de dados inclui os campos source_url e source_accessed_on. Links diretos foram acrescentados quando uma fonte identificável foi localizada. A ausência de URL direta em algumas linhas antigas é intencional: indica que a referência exata que sustenta aquele número ainda precisa ser localizada, e não que o número tenha sido verificado nesta rodada.

- **Marcos históricos** não devem ser lidos como censos anuais se a própria fonte descreve uma década, período ou classificação antiga.
- **Valores derivados para o Brasil em 1959 e 1969** continuam aproximados, pois partem de totais decenais e pressupõem ausência de encerramentos. Não são observações anuais exatas.
- **Contagens dos EUA antes da série moderna** usam categorias históricas variáveis, como *medical colleges* ou escolas de ciências médicas básicas. Não se deve unir esses dados aos programas MD modernos sem ressalva.
- **Anos sem dado brasileiro validado** continuam com travessão na tabela. Não foram interpolados.
- **A série norte-americana por ano acadêmico** pode ter ano inicial diferente do ano civil que a representa na coluna year; a coluna academic_year registra esse recorte.
- **Brasil 2025 (494)** e **EUA MD 2025–2026 (158)** são referências recentes, mas não representam unidades perfeitamente equivalentes.

## Verificações estruturais realizadas

- Conferi os sete arquivos HTML do site e não encontrei destinos locais de links ou recursos ausentes.
- O CSV contém 44 registros, cabeçalho com 11 campos e número consistente de campos por linha.
- A validação de links e do CSV foi realizada sobre os arquivos do repositório. A execução bem-sucedida do GitHub Actions ainda não foi confirmada; o status de verificações retornado pelo GitHub não apresentou checks associados ao commit consultado.

## Pendências de pesquisa — não ocultadas

1. Localizar a tabela primária exata que sustenta os benchmarks norte-americanos de 1930–1970; até lá, as URLs diretas dessas linhas permanecem em branco.
2. Reconstruir a série brasileira por instituição, com datas de abertura, encerramento, fusão, mudança de nome e status anual.
3. Verificar, em cada edição do e-MEC ou conjunto administrativo utilizado, se “escola”, “curso” e “instituição” correspondem à mesma unidade. O estudo da FMUSP é uma estimativa institucional divulgada a partir de dados via LAI, não um inventário longitudinal aberto no repositório.
4. Comparar de forma documentada o diretório DO com as séries históricas MD sem somar locais de ensino a colégios.
5. Manter atualizada a tramitação da MP nº 1.370/2026 e distinguir aprovação parlamentar, sanção e publicação de lei.

## Fontes verificadas nesta revisão

- [Lei nº 12.871/2013 — Planalto](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12871.htm): o art. 3º descreve chamamento público para autorizações de cursos privados de Medicina no regime legal correspondente e critérios de necessidade social e estrutura do SUS.
- [Portaria SERES/MEC nº 531/2023 — MEC](https://www.gov.br/mec/pt-br/assuntos/es/cursos-de-medicina/regulacao-e-supervisao/documentos/PORTARIASERES_MECN531DE22DEDEZEMBRODE2023.pdf): escopo específico em processos instaurados por força de decisão judicial, critérios de rede SUS, termo de adesão e contrapartida.
- [MPV 1.370/2026 — Câmara dos Deputados](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2634542): situação legislativa consultada em 21/10/2026.
- [JAMA 2026 — MD-granting schools](https://jamanetwork.com/journals/jama/fullarticle/2854662): série anual mais recente localizada para 2023–2026.
- [AAMC FY2025](https://www.aamc.org/data-reports/data/i-revenue-us-medical-schools-source-fiscal-year-2025): contagem por status de acreditação usada na série financeira.
- [FMUSP 2025](https://www.fm.usp.br/fmusp/imprensa/06-102025--brasil-ultrapassa-50-mil-vagas-anuais-em-medicina-apos-abertura-de-77-novos-cursos-alertam-pesquisadores-da-fmusp): contagem brasileira de 2025 e metodologia baseada em dados da SERES/MEC via LAI.
- [AACOM](https://www.aacom.org/become-a-doctor/prepare-for-medical-school/us-colleges-of-osteopathic-medicine): contagem atual de colégios e locais de ensino DO.
