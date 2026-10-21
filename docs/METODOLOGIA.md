# Metodologia e política de evidências

## Pergunta e unidades de análise

O projeto compara a trajetória da educação médica no Brasil e nos Estados Unidos. A unidade deve ser declarada em cada dado: curso, instituição que concede diploma, escola, campus/local de ensino, vaga autorizada, ingressante, graduado ou posição de residência. Esses conceitos não são intercambiáveis.

A série histórica atualmente publicada é de **marcos documentados**, não de observações anuais completas. A edição de 2026 de Barzansky e Walker atualiza a série norte-americana MD para 2023–24 (156), 2024–25 (157) e 2025–26 (158); esses valores foram incorporados à base. A contagem AAMC de 160 no FY2025 abrange programas com acreditação preliminar, provisória ou plena e permanece separada. A contagem brasileira de 494 escolas em 2025 é uma estimativa divulgada pela FMUSP a partir de dados da SERES/MEC obtidos via LAI, não uma série longitudinal anual. O estudo de Oliveira et al. (2019) reconstrói a trajetória brasileira a partir de dados do e-MEC até agosto de 2018; fontes norte-americanas usam categorias históricas diferentes e a AAMC contemporânea conta programas MD, enquanto a AACOM conta colégios e locais de ensino DO.

## Regras de comparação

1. Não combinar MD e DO sem informar o critério e evitar somar locais de ensino a instituições.
2. Não interpretar contagens de “escolas criadas” como escolas ativas sem confirmação.
3. Marcar aproximações derivadas de totais decenais como aproximações, não censos anuais.
4. Não interpolar valores ausentes e apresentá-los como observações.
5. Uma linha entre pontos no gráfico serve apenas como guia visual; não comprova a contagem nos anos intermediários.
6. Para construir a série anual brasileira, usar o esquema `data/br-medical-schools-register-template.csv` e o pipeline `scripts/rebuild_brazil_series.py`; registrar código do curso/IES, datas efetivas, atos autorizativos, fonte primária, mudanças de nome, fusões e encerramentos. O script não substitui a auditoria de cobertura e não torna uma extração parcial em censo nacional.
7. Para alegações causais, testar explicações concorrentes: legislação, financiamento, setor público/privado, população, distribuição geográfica, capacidade de hospitais e campos clínicos, além de mudanças na demanda por médicos.
8. Manter uma URL direta para cada observação sempre que a fonte for identificável. Se o documento primário exato não foi localizado, deixar a URL vazia e registrar a pendência em docs/AUDITORIA_FONTES_E_SERIE.md; não substituir uma fonte específica por um link genérico e apresentá-lo como comprovação.
9. Para séries por ano acadêmico, preencher academic_year e conservar esse recorte ao descrever o dado. Não comparar diretamente contagens anuais com um número de programas cobertos por um levantamento financeiro de exercício fiscal sem explicar a diferença de escopo.

## Citações e referências ABNT

- Citações indiretas no sistema autor-data: por exemplo, (BRASIL, 2013) ou (OLIVEIRA et al., 2019).
- Citações diretas somente quando o trecho for necessário e a localização puder ser verificada; em páginas sem paginação, indicar artigo ou seção.
- Cada página de conteúdo deve terminar com referências completas, com URL e data de acesso.
- Não atribuir uma afirmação a uma fonte que não a sustente diretamente.
- Conferir os metadados bibliográficos (autoria, título, ano, volume, número, páginas e DOI) antes da publicação acadêmica formal.

## Referências

ASSOCIATION OF AMERICAN MEDICAL COLLEGES (AAMC). *U.S. Medical School Revenues*. Washington, DC, 2026. Disponível em: https://www.aamc.org/data-reports/faculty-institutions/report/us-medical-school-revenues. Acesso em: 20 out. 2026.

ASSOCIATION OF AMERICAN OSTEOPATHIC COLLEGES (AACOM). *U.S. Colleges of Osteopathic Medicine*. [S. l.], [s. d.]. Disponível em: https://www.aacom.org/become-a-doctor/prepare-for-medical-school/us-colleges-of-osteopathic-medicine. Acesso em: 20 out. 2026.

BARZANSKY, Barbara. Abraham Flexner and the era of medical education reform. *Academic Medicine*, v. 85, supl. 1, p. S19-S25, 2010. DOI: https://doi.org/10.1097/ACM.0b013e3181f12bd1. Disponível em: https://pubmed.ncbi.nlm.nih.gov/20736546/. Acesso em: 20 out. 2026.

BRASIL. *Lei nº 12.871, de 22 de outubro de 2013*. Institui o Programa Mais Médicos e dá outras providências. Brasília, DF: Presidência da República, 2013. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12871.htm. Acesso em: 20 out. 2026.

FACULDADE DE MEDICINA DA UNIVERSIDADE DE SÃO PAULO (FMUSP). Brasil ultrapassa 50 mil vagas anuais em Medicina após abertura de 77 novos cursos, alertam pesquisadores da FMUSP. São Paulo, 6 out. 2025. Disponível em: https://fm.usp.br/fmusp/contato/lista_imprensa_desc?pagina_atual_lista_imprensa_desc=1&secao_id=43. Acesso em: 20 out. 2026.

FISHBEIN, Morris. Medical education—1905 to 1940. *JAMA*, v. 114, n. 13, p. 1147-1151, 1940. DOI: https://doi.org/10.1001/jama.1940.02810130009004. Disponível em: https://jamanetwork.com/journals/jama/article-abstract/1159981. Acesso em: 20 out. 2026.

JONAS, Harry S.; ETZEL, Sylvia I.; BARZANSKY, Barbara. Educational programs in US medical schools. *JAMA*, v. 266, n. 7, p. 913-920, 1991. DOI: https://doi.org/10.1001/jama.1991.03470070041005. Disponível em: https://jamanetwork.com/journals/jama/article-abstract/391205. Acesso em: 20 out. 2026.

LIAISON COMMITTEE ON MEDICAL EDUCATION (LCME). *Functions and Structure of a Medical School: Standards for Accreditation of Medical Education Programs Leading to the MD Degree*. Washington, DC, [s. d.]. Disponível em: https://lcme.org/. Acesso em: 20 out. 2026.

ASSOCIATION OF AMERICAN MEDICAL COLLEGES (AAMC). Average size of medical schools, 1930–1974. Tabela II no material da reunião anual de 1974. Disponível em: https://www.aamc.org/download/370942/data/85th_annual_meeting_agenda_11-12-74.pdf. Acesso em: 21 out. 2026.\n\nMINISTÉRIO DA EDUCAÇÃO (MEC). Cadastro Nacional de Cursos e IES. Disponível em: https://www.gov.br/mec/pt-br/politica-regulacao-supervisao-educacao-superior/cadastro-nacional-de-cursos-e-ies. Acesso em: 21 out. 2026.\n\nOLIVEIRA, Bruno Luciano Carneiro Alves de et al. Evolução, distribuição e expansão dos cursos de Medicina no Brasil (1808-2018). *Trabalho, Educação e Saúde*, Rio de Janeiro, v. 17, n. 1, e0018318, 2019. DOI: https://doi.org/10.1590/1981-7746-sol00183. Disponível em: https://www.scielo.br/j/tes/a/SGBd4Hbk5ghWD3yg6vqt3Jk/. Acesso em: 20 out. 2026.
