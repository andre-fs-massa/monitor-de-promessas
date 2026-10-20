# Classificação do censo do Paes 2024 (mandato 2025-2028 da chapa Paes/Cavaliere, em curso; corte 14/10/2026).
# chave: (status, confianca, evidencia, fonte_url, data_evidencia)
# Mandato em curso: promessa com medidas iniciadas = em_andamento; sem registro = nao_cumprida (reavaliar a cada corte).
SR = ("Busca na imprensa, em sites oficiais e no Diário Oficial do Município do Rio (2025–2026) em out/2026 "
      "não localizou registro de {}.")
DO = "https://doweb.rio.rj.gov.br/portal/edicoes/download/"
SEC = "https://agenda.prefeitura.rio/wp-content/uploads/sites/9/2026/08/Reuniao-de-Secretariado-agosto-2026.pdf"
JUV = "https://juv.prefeitura.rio/wp-content/uploads/sites/20/2026/04/Art.-2o-inciso-IV-Anexo-4_-Relatorio-anual-da-gestao_2025.docx.pdf"
D = {
 "conscientizacao": ("cumprida", "media", "A Lei 9.385, de 06/05/2026, sancionada pelo prefeito, criou o Programa Educação para Cidadania e para a Sustentabilidade na rede municipal. O projeto de lei foi de autoria de vereador.", DO + "14784/6", "2026-05"),
 # Saúde
 "super_centros": ("em_andamento", "alta", "O Super Centro Carioca de Saúde da Zona Oeste (Campo Grande) foi inaugurado em 18/03/2026; o da Zona Norte (Piedade, voltado a crianças e adolescentes) teve a pedra fundamental lançada em set/2026, com entrega prevista para 2027. Não foram localizados os projetos de Realengo e Jacarepaguá.", DO + "14947/1", "2026-09"),
 "autismo": ("em_andamento", "media", "Em set/2024 havia um Centro de Estímulo ao Desenvolvimento no TEA (Oscar Clark). O centro de Irajá, inaugurado em mar/2026, é o oitavo da rede, ou seja, cerca de 7 novos dos 8 prometidos.", "https://diariodorio.com/rio-inaugura-centro-de-reabilitacao-em-iraja-com-foco-em-autismo-e-fisioterapia/", "2026-03"),
 # Educação
 "tempo_integral": ("em_andamento", "alta", "O tempo integral chegou a 52,1% das matrículas da rede municipal em 2025 (Acordo de Resultados 2026, meta de 54% para 2026); a meta do plano é mais de 70%.", DO + "14815/7", "2026-05"),
 "creches": ("em_andamento", "alta", "A prefeitura criou 2.065 novas vagas em creches em 2025 e fixou a meta de 5.000 para 2026 (Acordo de Resultados 2026), de um total prometido de 13 mil.", DO + "14815/7", "2026-05"),
 "gets": ("em_andamento", "media", "A rede tinha 276 GETs em 2025 e 317 em set/2026, com meta de 350 em 2026 e 500 até 2028.", "https://www.correiodamanha.com.br/estado-do-rio/2026/09/317602-paes-pretente-por-no-estado-nova-educacao-tecnologica.html", "2026-09"),
 "programacao": ("em_andamento", "alta", "124.621 alunos tiveram aulas de lógica de programação em 2025; a meta para 2026 é de 144 mil (Acordo de Resultados 2026), de 200 mil prometidos.", DO + "14815/7", "2026-05"),
 "educ_especial": ("em_andamento", "alta", "A razão era de 3,6 alunos por mediador da educação especial em 2025, com meta de 3,4 em 2026 (Acordo de Resultados 2026); a promessa é de 1 para 3. Houve seleções de agentes de apoio em 2025 e 2026.", DO + "14815/7", "2026-05"),
 "climatizacao": ("nao_cumprida", "media", SR.format("climatização de todas as salas de aula (o Plano Estratégico 2025-2028 prevê climatizar 100% das salas até 2027, sem balanço de execução)"), DO + "7538/252", "2025-08"),
 # Transporte
 "brt_vlt": ("nao_cumprida", "media", "A LC 289/2025 autorizou trocar o BRT por VLT ou VLP na Transcarioca e na Transoeste, mas em jul/2026 o contrato de concessão seguia sem assinatura porque a prefeitura mudou o projeto para VLP (veículo leve sobre pneus), abandonando o sistema sobre trilhos prometido.", SEC, "2026-08"),
 "jae_tarifa": ("cumprida", "media", "Com a bilhetagem Jaé, a prefeitura criou a integração expressa ônibus-metrô (Resolução SMTR 3.824, abr/2025) e o Sistema de Transporte Unificado Complementar, que integra as vans ao Bilhete Único (Decreto 58.732, set/2026).", DO + "14960/5", "2026-09"),
 "faixa_azul": ("em_andamento", "alta", "Havia 6 km de motofaixas em 2025 e 19 km em mai/2026, com meta de 80 km em 2026 (Acordo de Resultados 2026); novas motofaixas foram decretadas em ago/2026.", "https://www.correiodamanha.com.br/rio-de-janeiro/2026/05/285697-prefeitura-implementa-mais-de-19-km-de-motofaixas.html", "2026-05"),
 "eletrificacao": ("em_andamento", "media", "A prefeitura e o BNDES preparam uma PPP de 175 ônibus elétricos (R$ 509 mi, operação a partir de 2027); a nova licitação dos ônibus paga mais às viações com frota elétrica; a meta de 2026 é concluir o edital do lote elétrico.", "https://diariodotransporte.com.br/2026/09/24/rio-de-janeiro-e-bndes-preparam-ppp-para-onibus-eletricos-em-projeto-que-envolve-r-13-bilhao-e-renovacao-da-frota-ate-2028/", "2026-09"),
 # Emprego e renda / Turismo
 "qualificacao": ("cumprida", "media", "A plataforma Oportunidades Cariocas reúne a oferta de capacitação de várias secretarias: tinha 1.451 cursos e 78.059 inscrições até ago/2026.", SEC, "2026-08"),
 "formalizacao": ("nao_cumprida", "media", SR.format("programa de incentivo à formalização com cursos e auxílio financeiro"), "", "2026-10"),
 "fundo_turismo": ("cumprida", "baixa", "O Fundo Municipal de Turismo já existia (Lei 2.929); o Decreto 57.057, de out/2025, criou o Programa de Fomento a Novas Rotas Aéreas Internacionais custeado por esse fundo, que já repassou recursos a companhia aérea em 2026.", "https://www.normasbrasil.com.br/norma/decreto-57057-2025-rio-de-janeiro_485506.html", "2025-10"),
 "bolsa_valores": ("em_andamento", "baixa", "A bolsa (Base Exchange) ainda não tinha autorização do Banco Central e da CVM em abr/2026 e prevê começar a operar em 2027; a prefeitura reduziu o ISS do setor de 5% para 2%. O prazo prometido (até 2026) ainda não venceu.", "https://timesbrasil.com.br/investimentos/bolsa/nova-bolsa-de-valores-base-exchange-no-rj-planeja-romper-o-monopolio-veja-entrevista-com-ceo/", "2026-04"),
 # Ordem pública
 "rondas_gm": ("nao_cumprida", "media", SR.format("ampliação das rondas escolares ou da Guarda Municipal em praças e parques (só ações pontuais, como a Operação Volta às Aulas de mar/2026)"), "", "2026-10"),
 "brt_seguro": ("nao_cumprida", "media", SR.format("expansão do programa BRT Seguro (só nomeações para a gerência do programa)"), "", "2026-10"),
 "gm_armada": ("cumprida", "alta", "A LC 282/2025 criou a Força Municipal, divisão armada da Guarda Municipal; cerca de 600 agentes formados começaram a atuar armados em 15/03/2026.", "https://www.cnnbrasil.com.br/nacional/sudeste/rj/guarda-municipal-armada-do-rio-comeca-a-atuar-neste-domingo/", "2026-03"),
 "iluminacao_cameras": ("em_andamento", "media", "O Civitas instalou 4.682 novas câmeras até ago/2026 (meta de 15 mil até 2028) e inaugurou nova sala de monitoramento; não foi localizado balanço da ampliação da iluminação pública.", SEC, "2026-08"),
 # Gestão
 "ppps": ("em_andamento", "baixa", "Há concessões e PPPs em preparação no mandato (PPP de ônibus elétricos de R$ 509 mi, nova licitação dos ônibus), mas não foi localizado balanço do investimento privado atraído.", "https://diariodotransporte.com.br/2026/09/24/rio-de-janeiro-e-bndes-preparam-ppp-para-onibus-eletricos-em-projeto-que-envolve-r-13-bilhao-e-renovacao-da-frota-ate-2028/", "2026-09"),
 "whatsapp_wifi": ("em_andamento", "media", "27% dos serviços mais pedidos estavam no WhatsApp em jul/2026 (meta de 100% em 2028); não foi localizada ampliação do Wi-Fi público.", SEC, "2026-08"),
 "selo_diamante": ("cumprida", "alta", "A prefeitura conquistou o Selo Diamante do Programa Nacional de Transparência Pública em dez/2025 (o primeiro foi em 2024, antes do mandato).", "https://en.prefeitura.rio/cidade/rio-alcanca-selo-diamante-no-programa-nacional-de-transparencia-publica-pelo-segundo-ano-consecutivo/", "2025-12"),
 # Meio ambiente
 "acari": ("em_andamento", "alta", "A dragagem começou em nov/2025 e as obras da 1ª fase de controle de enchentes do Rio Acari, em set/2026, com previsão até 2027.", "https://diariodorio.com/rio-de-janeiro/2026/09/12/prefeitura-do-rio-inicia-obras-contra-enchentes-no-rio-acari-primeira-fase-vai-ate-2027.html", "2026-09"),
 "reassentamento": ("nao_cumprida", "media", SR.format("programa de moradias para reassentar populações ribeirinhas"), "", "2026-10"),
 "sirenes": ("nao_cumprida", "media", "Em jul/2026 a cidade seguia com 165 sirenes em 103 comunidades, o mesmo sistema de antes do mandato; o Plano Estratégico prevê sirenes em novas áreas só para 2028.", DO + "14871/1", "2026-07"),
 "jardim_maravilha": ("em_andamento", "alta", "As obras de macrodrenagem do Jardim Maravilha pelo Novo PAC (R$ 340 mi, prazo de 3 anos) começaram em jun/2026.", "https://www.tribunadosertao.com.br/rj-em-foco/2026/06/22/926515-evento-com-lula-marca-formalizacao-de-obras-do-novo-pac-anunciadas-para-o-rio-desde-o-ano-passado", "2026-06"),
 "zn_verde": ("cumprida", "baixa", "Não há projeto com o nome ZN Verde, mas o programa Planta+Rio (dez/2025) prevê produzir 90 mil mudas e plantar 80 mil até 2028, com prioridade para a Zona Norte, e os plantios começaram em Ramos.", "https://ambienteclima.prefeitura.rio/wp-content/uploads/sites/81/2025/12/caderno_tecnico_planta_mais_rio.pdf", "2025-12"),
 # Assistência social
 "carioquinha": ("parcialmente_cumprida", "media", "Em out/2025 a prefeitura lançou o Cartão Primeira Infância Carioca (R$ 200 por mês), mas para crianças de 0 a 4 anos, e não de 0 a 6; atendia mais de 32 mil famílias em set/2026.", "https://www.correiodamanha.com.br/rio-de-janeiro/2026/09/321937-cartao-da-primeira-infancia-carioca-amplia-beneficio-para-mais-de-32-mil-familias.html", "2026-09"),
 "prato_feito": ("em_andamento", "media", "As cozinhas comunitárias do Prato Feito Carioca passaram a 75 em jun/2026 (meta de 100 até 2028); não foi localizada a criação do Restaurante Popular Carioca (a cidade segue com 3 restaurantes populares).", SEC, "2026-08"),
 "pop_rua": ("cumprida", "media", "Segundo a própria prefeitura, 9.950 pessoas em situação de rua foram acolhidas nas unidades de acolhimento em 2025 (Acordo de Resultados 2026), acima das 7 mil prometidas.", DO + "14815/13", "2026-05"),
 # Favelas
 "morar_carioca": ("em_andamento", "media", "Novas frentes do Morar Carioca começaram em 2025 e 2026 (Morro do Queto, Vila Nova Canaã, Praça Seca, Maré) e o Bairro Maravilha requalificou 38,8 km de vias em 2025, com meta de 88,8 km até 2026.", DO + "14815/12", "2026-05"),
 "casa_carioca": ("em_andamento", "baixa", "O Casa Carioca segue com orçamento (crédito suplementar em set/2026), mas não foi localizado o número de moradias reformadas no mandato.", DO + "14967/3", "2026-09"),
 "hub_favela": ("cumprida", "alta", "O programa HUB Favela Empreendedora foi criado pelo Decreto 55.602, de 01/01/2025, e recebeu projetos por chamamento público em 2025 e 2026.", DO + "13903/43", "2026-02"),
 # Mulher
 "empreend_feminino": ("em_andamento", "baixa", "A Rede Empreendedora Carioca, da Secretaria da Mulher, abriu nova edição de capacitação em 2026 e tem metas de feiras e formalização para 2026; não foi localizado balanço da ampliação.", DO + "14779/1", "2026-05"),
 "cartao_mulheres": ("nao_cumprida", "media", SR.format("ampliação do cadastro de mulheres chefes de família, mães e grávidas no Cartão Carioca"), "", "2026-10"),
 "maria_penha": ("nao_cumprida", "media", SR.format("ampliação da Ronda Maria da Penha (só a meta de botão de pânico no sistema da Ronda em 2026)"), DO + "14855/11", "2026-07"),
 # PCD
 "pcd_capacitacao": ("nao_cumprida", "media", SR.format("capacitação de pessoas com deficiência e familiares no mandato (o PPA 2026-2029 prevê 17.500 capacitados, sem execução informada)"), DO + "13868/28", "2026-01"),
 "pcd_transporte": ("nao_cumprida", "media", SR.format("transporte de pessoas com deficiência para consultas, exames e cirurgias"), "", "2026-10"),
 # Jovem
 "pacto_juventude": ("em_andamento", "alta", "O Pacto pela Juventude formou 2.160 jovens líderes em 2025, abaixo dos 3 mil por ano prometidos; a meta para 2026 é de 6 mil acumulados.", JUV, "2026-04"),
 "espacos_juventude": ("em_andamento", "alta", "Havia 7 Espaços da Juventude em 2025 (meta de 20) e Casas da Juventude só em duas áreas de planejamento (Centro e Pavuna).", JUV, "2026-04"),
 "rio_vestibular": ("nao_cumprida", "media", SR.format("atendimento a jovens no programa Rio Vestibular"), "", "2026-10"),
 # Cultura
 "jae_cultural": ("nao_cumprida", "media", SR.format("ampliação do Jaé Cultural (só a menção no Plano Estratégico 2025-2028)"), "", "2026-10"),
 "oficina_cultural": ("nao_cumprida", "media", SR.format("expansão do programa Oficina Cultural Carioca (há oficinas culturais apoiadas por editais de fomento de 2026, mas não identificadas como o programa)"), "", "2026-10"),
 # Esporte
 "museu_olimpico": ("em_andamento", "alta", "O Museu Olímpico foi inaugurado no Velódromo em ago/2025 (fechado depois de incêndio em abr/2026, com obras até nov/2026); as obras do Parque Imagine, legado olímpico, estão previstas para começar até dez/2026.", SEC, "2026-08"),
 "vilas_olimpicas": ("em_andamento", "alta", "Em jul/2026 a Vila Olímpica do Parque Oeste estava com 96,8% das obras (inauguração prevista para dez/2026), Rio das Pedras com 8% e Sepetiba com 21%; a da Cidade de Deus ainda não tinha terreno.", SEC, "2026-08"),
 "time_rio": ("em_andamento", "media", "O Time Rio apoiava 66 atletas em jul/2026, contra 63 na base de 2024; a meta do Plano Estratégico é ampliar em 10% até 2028.", SEC, "2026-08"),
}
