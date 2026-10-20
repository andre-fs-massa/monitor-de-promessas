# Classificação do censo do Paes 2012 (mandato 2013-2016, encerrado).
# chave: (status, confianca, evidencia, fonte_url, data_evidencia)
SR = ("Busca na imprensa, em sites oficiais e no Diário Oficial do Município do Rio (2013–2016) em out/2026 "
      "não localizou registro de {}.")
DO = "https://doweb.rio.rj.gov.br/portal/edicoes/download/"
RAG = "https://saude.prefeitura.rio/wp-content/uploads/sites/47/2023/03/RAG-2016.pdf"
AR15 = "Resultados de 2015 do Acordo de Resultados (Diário Oficial de 11/04/2016)"
AR16 = "Metas de 2016 do Acordo de Resultados, com valores de referência (Diário Oficial de 20/04/2016)"
AFP = "https://www.aosfatos.org/noticias/eduardo-paes-infla-dados-legado-prefeitura-rio/"
D = {
 # Educação
 "ideb": ("nao_cumprida", "media", "A rede municipal não chegou a 6,0 nos anos iniciais nem a 5,0 nos anos finais em 2015: em 2013 tinha 5,3 e 4,4, e a própria prefeitura chamou de maiores notas da série histórica o 6,0 (anos iniciais) e o 5,2 (anos finais) alcançados só em 2023.", "https://educacao.prefeitura.rio/noticias/rio-alcanca-maior-ideb-da-historia-nos-anos-iniciais-e-esta-entre-as-capitais-que-mais-avancaram-no-pais/", "2016-09"),
 "alfabetizacao": ("nao_cumprida", "baixa", AR16 + ": 90,7% das crianças estavam alfabetizadas em 2014 (meta: 95%); não foi localizado o resultado de 2016.", DO + "3083/11", "2014-12"),
 "analf_funcional": ("cumprida", "media", AR16 + ": o analfabetismo funcional entre alunos do 4º ao 6º ano era de 2,4% em 2014, abaixo dos 5% prometidos (a meta interna passou a ser de até 2,5%).", DO + "3083/11", "2014-12"),
 "tempo_integral": ("parcialmente_cumprida", "baixa", "Em 2015 só 19,4% dos alunos estavam em tempo integral (" + AR16 + "); em set/2016 a Secretaria de Educação informou 535 escolas (36% da rede) em tempo integral, sem dizer o percentual de alunos.", "https://ipp.prefeitura.rio/wp-content/uploads/sites/64/2023/02/Conselho-Ata-14-09-2016-Final.pdf", "2016-09"),
 "segundo_segmento": ("parcialmente_cumprida", "baixa", AR16 + ": 95,7% dos alunos concluíam o 2º segmento até os 16 anos em 2014 (meta: 96%), a 0,3 ponto da meta; não foi localizado o resultado de 2016.", DO + "3083/11", "2014-12"),
 "vagas_infantil": ("parcialmente_cumprida", "baixa", "A rede tinha 40.585 vagas novas de educação infantil desde 2009 em 2015 (" + AR16 + "; o plano informa cerca de 15 mil criadas até 2012), ou seja, cerca de 25 mil em 2013–2015; não foi localizado o total de 2016 nem o número de EDIs abertos.", DO + "3083/11", "2015-12"),
 "ingles": ("cumprida", "media", "Em dez/2016 todos os alunos do 1º ao 9º ano tinham aulas de inglês pelo Rio Criança Global (uma aula semanal do 1º ao 3º ano e dois tempos do 4º ao 9º); o 9º ano entrou a partir de 2014, como previsto.", DO + "3283/1", "2016-12"),
 # Saúde
 "clinicas_familia": ("parcialmente_cumprida", "media", "A rede passou de cerca de 70 Clínicas da Família previstas para o fim de 2012 para 115 em dez/2016 (Relatório Anual de Gestão 2016), cerca de 45 novas contra 62 prometidas; só 14 das 54 reformas tinham sido feitas até 2015.", RAG, "2016-12"),
 "psf_70": ("parcialmente_cumprida", "media", "Segundo o Ministério da Saúde, a cobertura da atenção primária chegou a 68,62% em dez/2016, último mês do mandato (os 70% só foram atingidos em jan/2017); o CEBES aponta 59,5% de cobertura das Clínicas da Família em dez/2016.", AFP, "2016-12"),
 "padi": ("nao_cumprida", "alta", "Em dez/2016 o PADI tinha 16 equipes (meta: 46), segundo comunicado da Secretaria Municipal de Saúde no Diário Oficial.", DO + "3296/71", "2016-12"),
 "medicos_2mil": ("nao_cumprida", "media", SR.format("balanço da contratação de 2 mil médicos (a meta constava do Acordo de Resultados de 2016, sem resultado publicado)"), DO + "3083/11", "2026-10"),
 "consultas_eletivas": ("cumprida", "media", AR15 + ": 93% das consultas eletivas foram feitas dentro do tempo adequado em 2015 (meta 2015: 89%; meta do plano: 90%).", DO + "3075/10", "2015-12"),
 "cer_espera": ("cumprida", "media", AR15 + ": o tempo de espera nas emergências (CER) caiu de 69 minutos em 2011 para 39 minutos em 2015, redução de 43% (meta: 25%).", DO + "3075/10", "2015-12"),
 "leitos_cnes": ("cumprida", "media", AR15 + ": a meta de não haver pacientes em leitos não cadastrados no CNES foi aprovada em 2015, com a exceção prevista de 3% acima da capacidade no Hospital Lourenço Jorge.", DO + "3075/10", "2015-12"),
 "mortalidade_infantil": ("nao_cumprida", "alta", "A mortalidade infantil foi de 12,9 por mil nascidos vivos em 2016 (meta: menos de 10), segundo o Relatório Anual de Gestão 2016 da Secretaria Municipal de Saúde.", RAG, "2016-12"),
 "mortalidade_materna": ("nao_cumprida", "alta", "A mortalidade materna foi de 71,6 por 100 mil nascidos vivos em 2016 (meta: menos de 41), segundo o Relatório Anual de Gestão 2016 da Secretaria Municipal de Saúde.", RAG, "2016-12"),
 "saude_inteligente": ("parcialmente_cumprida", "baixa", "O prontuário eletrônico já cobria 96% das equipes de Saúde da Família em 2012 e a rede tinha Central de Regulação em 2016, mas não foi localizada a telemedicina em toda a rede nem a regulação 24h de todas as unidades.", RAG, "2016-12"),
 # Meio ambiente
 "esgoto_ap5": ("nao_cumprida", "alta", AR15 + ": a cobertura de esgoto com coleta e tratamento na AP 5 era de 22,13% em 2015 (meta do plano: 55% até 2016).", DO + "3075/8", "2015-12"),
 "reflorestamento": ("parcialmente_cumprida", "baixa", AR15 + ": a referência era de 1.221 ha reflorestados em 2014 e a meta de 1.500 ha até 2016, mas em 2015 só foram assinados contratos para 79,51 ha; não há balanço de 2016 das novas áreas.", DO + "3075/10", "2015-12"),
 "arvores": ("nao_cumprida", "media", SR.format("balanço do plantio de 500 mil árvores"), "", "2026-10"),
 "ciclovias": ("parcialmente_cumprida", "media", "A malha cicloviária tinha 438,9 km em jan/2016, segundo a Secretaria de Meio Ambiente (meta: 450 km); não foi localizado balanço final da malha nem dos 1.000 bicicletários.", "https://www.jb.com.br/rio/noticias/2016/01/17/ciclovia-da-av-niemeyer-e-inaugurada-oficialmente.html", "2016-01"),
 "reciclavel": ("nao_cumprida", "media", SR.format("coleta de 25% do lixo reciclável"), "", "2026-10"),
 "gee": ("nao_cumprida", "media", SR.format("redução de 16% das emissões de gases de efeito estufa; a prefeitura fez inventários de emissões (2011, 2013 e um terceiro em 2016), sem divulgar o cumprimento da meta"), DO + "3288/66", "2016-12"),
 "macrodrenagem": ("parcialmente_cumprida", "media", AR15 + ": os reservatórios da Praça Niterói e da Praça Varnhagen (bacia da Guanabara) foram executados, mas o desvio do Rio Joana teve cronograma só parcialmente cumprido e foi suspenso em out/2016 com cerca de 80% feitos; não foram localizadas as obras do rio Cação Vermelho.", DO + "3075/8", "2016-10"),
 "plano_clima": ("nao_cumprida", "media", SR.format("plano de adaptação às mudanças climáticas ou plano municipal de gestão costeira concluídos no mandato"), "", "2026-10"),
 "pracas_15min": ("nao_cumprida", "media", SR.format("balanço da reforma de 170 mil m² de praças e parques no programa 15 Minutos Verdes"), "", "2026-10"),
 # Moradia
 "morar_carioca": ("nao_cumprida", "media", AR15 + ": o Morar Carioca chegou a 75.346 domicílios urbanizados em 2015, quase sem avanço sobre 2014 (74.552) e muito abaixo da meta de levar urbanização a mais 81 mil domicílios; o programa foi em grande parte abandonado.", DO + "3075/11", "2015-12"),
 "mcmv_50mil": ("parcialmente_cumprida", "baixa", AR15 + ": foram contratadas 77.365 moradias de interesse social desde 2009 até 2015 (meta interna: 86 mil em 2015 e 100 mil até 2016); não foi localizado quanto foi contratado só em 2013–2016.", DO + "3075/11", "2015-12"),
 "risco_zero": ("nao_cumprida", "alta", AR15 + ": só 106 famílias foram retiradas de áreas de alto risco em 2015 (meta: 6.434), de um total de 29.536 famílias mapeadas em 2011.", DO + "3075/11", "2015-12"),
 "favelas_5pct": ("nao_cumprida", "media", SR.format("medição da redução de 5% das áreas ocupadas por favelas"), "", "2026-10"),
 "bairro_maravilha": ("parcialmente_cumprida", "baixa", "O programa seguiu ativo (a meta de 2016 era concluir 90 km do Bairro Maravilha Oeste), mas não foi localizado balanço dos 582 km recuperados e 173 km implantados.", DO + "3083/11", "2016-04"),
 "porto_maravilha": ("parcialmente_cumprida", "media", "As principais obras ficaram prontas para os Jogos (Orla Conde em mai/2016, túneis e vias), mas a PPP estava com cerca de 88% de execução e o fundo que a pagava declarou falta de recursos em 2016; as obras restantes pararam em 2017.", "https://apublica.org/2018/02/porto-maravilha-corre-o-risco-de-parar-novamente-em-2018/", "2016-12"),
 "upp_social": ("cumprida", "media", "A UPP Social, rebatizada de Rio+Social em ago/2014, atendia mais de 711 mil pessoas em 208 comunidades com UPP, sob coordenação do IPP.", "https://unhabitat.org/sites/default/files/documents/2019-04/riosocial_programme_-_summary_report_bilingual.pdf", "2016-12"),
 "parque_olimpico": ("cumprida", "alta", "O Parque Olímpico da Barra foi implantado por PPP de 15 anos com a concessionária Rio Mais e sediou os Jogos de 2016.", "https://www.jb.com.br/pais/2018/11/957024-bndes-aprova-processo-que-definira-concessao-do-parque-olimpico.html", "2016-08"),
 "rio_branco": ("parcialmente_cumprida", "media", "Com o VLT, o trecho da Av. Rio Branco entre a Nilo Peçanha e a Santa Luzia virou área exclusiva de pedestres, ciclistas e VLT, mas o trecho entre a Presidente Vargas e a Nilo Peçanha voltou a receber carros em mai/2016; não houve o fechamento completo prometido.", "https://www.rio.rj.gov.br/dlstatic/10112/6169601/4162746/140616_11h.pdf", "2016-06"),
 "cidade_nova": ("nao_cumprida", "media", SR.format("operação urbana consorciada da Cidade Nova"), "", "2026-10"),
 # Transportes
 "brt_tempo": ("cumprida", "media", AR15 + ": o tempo de viagem nos corredores BRT caiu 55,72% (meta: 50%) e nos BRS 26,5% (meta: 20%), embora um corredor BRS tenha ficado abaixo de 15% em parte dos dias.", DO + "3075/9", "2015-12"),
 "acidentes": ("cumprida", "alta", AR15 + ": a taxa de vítimas de trânsito caiu de 912,83 (2008) para 672,33 por 100 mil veículos em 2015, redução de 26,35% (meta: 15%).", DO + "3075/9", "2015-12"),
 "bilhete_unico": ("parcialmente_cumprida", "media", "O Bilhete Único Carioca já integrava ônibus e trem e passou a integrar metrô e BRT em set/2016, mas a integração com VLT, barcas e ônibus convencionais com o metrô não estava disponível no fim do mandato.", "https://diariodotransporte.com.br/2016/09/25/integracao-entre-metro-e-brt-no-rio-de-janeiro-comeca-nesta-segunda-feira-26/", "2016-09"),
 "alta_capacidade": ("nao_cumprida", "media", SR.format("medição da parcela de usuários de transporte público que usam trem, metrô ou BRT"), "", "2026-10"),
 "brts": ("parcialmente_cumprida", "alta", "A TransCarioca foi inaugurada em 2014 e a TransOlímpica em 2016, mas a TransBrasil não ficou pronta no mandato (só foi inaugurada em 2024).", "https://moovit.com/pt/blog/rj-inauguracao-do-terminal-gentileza-e-do-brt-transbrasil/", "2016-12"),
 "frota_onibus": ("nao_cumprida", "alta", "A meta de 100% da frota climatizada até 2016 não foi cumprida (43% da frota convencional tinha ar-condicionado em 2017); a Justiça multou o ex-prefeito e o ex-secretário de Transportes pelo descumprimento.", "https://diariodotransporte.com.br/2017/12/10/ex-prefeito-eduardo-paes-e-multado-em-r-200-mil-por-descumprir-meta-de-ar-condicionado-nos-onibus-do-rio/", "2017-12"),
 "taxis": ("nao_cumprida", "baixa", AR15 + ": em 2015 a prefeitura só publicou a normatização e iniciou o curso e a avaliação dos taxistas; não foi localizado balanço de 100% dos táxis no padrão do Rio Boa Praça.", DO + "3075/10", "2015-12"),
 "vlt": ("cumprida", "alta", "O VLT Carioca foi inaugurado em 05/06/2016, ligando a Rodoviária ao Aeroporto Santos Dumont e passando por Praça Mauá, Rio Branco e Praça XV.", "https://www.alstom.com/pt/press-releases-news/2016/6/sistema-de-vlt-integrado-da-alstom-inicia-sua-operacao-no-rio-de-janeiro-antes-dos-jogos-esportivos", "2016-06"),
 "racionalizacao": ("cumprida", "media", "A racionalização foi executada: em out/2015, 51 linhas de ônibus foram extintas, 25 criadas e 26 encurtadas (o processo foi suspenso pelo prefeito seguinte em jan/2017).", "https://diariodotransporte.com.br/2017/01/01/marcelo-crivella-suspende-racionalizacao-de-linhas-de-onibus-no-rio-de-janeiro/", "2015-10"),
 "plano_mobilidade": ("cumprida", "media", "O Plano de Mobilidade Urbana Sustentável foi elaborado: diagnóstico em jun/2016, apresentação ao Conselho Municipal de Política Urbana em set/2016 e relatório síntese em dez/2016.", "https://www.rio.rj.gov.br/documents/5450795/7289937/P7+-+Revisao+Relatorio+Sintese+20161221+rev.pdf", "2016-12"),
 # Investimentos
 "zn_zo": ("nao_cumprida", "media", SR.format("balanço da parcela dos recursos da prefeitura aplicada nas Zonas Norte e Oeste"), "", "2026-10"),
 "investir_34bi": ("nao_cumprida", "media", SR.format("balanço do total investido em 2013–2016 comparado aos R$ 34,3 bilhões prometidos"), "", "2026-10"),
 # Cultura
 "producoes_350": ("cumprida", "alta", AR15 + ": o Programa de Fomento à Produção Cultural apoiou 806 projetos em 2015 (meta do plano: 350 por ano).", DO + "3075/8", "2015-12"),
 "frequencia_cultura": ("nao_cumprida", "baixa", AR15 + ": os equipamentos municipais de cultura tiveram 2,77 milhões de visitantes em 2015 (2,39 milhões em 2014); não foi localizado o público de 2011 para conferir se dobrou.", DO + "3075/8", "2015-12"),
 "porto_cultura": ("parcialmente_cumprida", "baixa", "A região do Porto ganhou o Museu de Arte do Rio (2013), o Museu do Amanhã (2015), a restauração do Centro Cultural José Bonifácio e o Circuito da Herança Africana, mas não foi localizado balanço das 15 iniciativas; em 2015 o IRPH recuperou só 3 das 7 obras previstas na zona portuária.", DO + "3075/7", "2015-12"),
 "imoveis_tiradentes": ("parcialmente_cumprida", "media", AR15 + ": o IRPH chegou a 16 obras de recuperação no centro histórico em 2015 (meta 2015 aprovada; o plano prometia 17 imóveis na Praça Tiradentes e na Lapa).", DO + "3075/7", "2015-12"),
 "polo_portuario": ("parcialmente_cumprida", "media", "O Centro Cultural José Bonifácio foi restaurado e reaberto em nov/2013 como referência da cultura afro-brasileira e o Circuito da Herança Africana foi implantado, mas não foi localizada a Cidade do Teatro nos Galpões da Gamboa.", "https://riotur.rio/?p=1148", "2013-11"),
 "escritorio_cultura": ("cumprida", "alta", AR15 + ": o Escritório de Projetos Culturais foi implementado e fez 50 capacitações de produtores e gestores culturais em 2015.", DO + "3075/8", "2015-12"),
 # Desenvolvimento social
 "pobreza_50": ("nao_cumprida", "media", SR.format("medição da redução da população abaixo da linha de pobreza"), "", "2026-10"),
 "pobreza_beneficiarios": ("nao_cumprida", "media", SR.format("medição da pobreza entre os beneficiários do Bolsa Família e do Cartão Família Carioca"), "", "2026-10"),
 "caps": ("parcialmente_cumprida", "baixa", AR15 + ": a cobertura de saúde mental chegou a 58% em 2015 (40% em 2012, segundo o plano; meta: 60%), e a rede tinha 33 CAPS em dez/2016 (17 em 2012); não foi localizado o resultado final de 60% nem o total de residências terapêuticas.", DO + "3075/10", "2015-12"),
 "cfc_saude": ("nao_cumprida", "media", SR.format("medição do atendimento pelo Saúde da Família de 100% dos beneficiários do Cartão Família Carioca nas áreas cobertas"), "", "2026-10"),
 "rio_em_forma": ("nao_cumprida", "baixa", AR15 + ": a meta de ampliar o Rio em Forma na rede municipal não foi validada em 2015; não foi localizada a cobertura de todas as Escolas do Amanhã.", DO + "3075/10", "2015-12"),
 # Ordem pública
 "uops": ("parcialmente_cumprida", "media", AR15 + ": eram 11 UOPs e 2.872 guardas nas ruas em 2015 (metas do plano: 14 UOPs e 3,3 mil guardas); não foi localizado o resultado de 2016.", DO + "3075/9", "2015-12"),
 "recapeamento": ("parcialmente_cumprida", "baixa", "Até 2015 a Seconserva tinha recapeado cerca de 1.100 km (" + AR16 + "), com meta de chegar a 1.460 km em 2016; não foi localizado o resultado final.", DO + "3083/11", "2016-04"),
 "calcadas": ("nao_cumprida", "media", SR.format("balanço de 700 mil m² de calçadas e 5 mil rampas do Rio Acessível"), "", "2026-10"),
 "apagamento": ("cumprida", "alta", AR15 + ": o índice de lâmpadas apagadas foi de 0,88% em 2015 (meta: menos de 2%).", DO + "3075/7", "2015-12"),
 "plano_iluminacao": ("parcialmente_cumprida", "baixa", AR15 + ": a RioLuz cadastrou 45.120 pontos de iluminação (cerca de 10% do parque) em 2015; não foi localizado o Plano Diretor de Iluminação Pública.", DO + "3075/7", "2015-12"),
 # Gestão
 "investimento_15": ("cumprida", "baixa", "Segundo a própria prefeitura, a taxa de investimento chegou a 16,1% do orçamento (e o peso da dívida caiu de 9% para 4%) entre 2009 e 2016; não foi localizada verificação independente.", "https://monitormercantil.com.br/paes-olimpiadas-nao-causaram-crise-estadual/", "2016-12"),
 "central_1746": ("parcialmente_cumprida", "media", AR15 + ": a Central 1746 fez 4,3 milhões de atendimentos em 2015 (meta do plano: 3,5 milhões), mas a satisfação ficou em 70,2% (meta: 85%).", DO + "3075/7", "2015-12"),
 "compras_10": ("parcialmente_cumprida", "baixa", AR15 + ": o projeto de compras estratégicas reduziu em R$ 32,7 milhões os gastos conduzidos em 2015; não foi localizada a redução de até 10% no preço unitário das principais compras.", DO + "3075/7", "2015-12"),
 "receita_15": ("nao_cumprida", "media", AR15 + ": a meta de receita tributária de 2015 (R$ 9,03 bi, aprovada) era só 6,5% acima de 2014 (R$ 8,48 bi), bem abaixo do crescimento de 15,5% ao ano prometido.", DO + "3075/10", "2015-12"),
 "rede_datacenter": ("parcialmente_cumprida", "media", AR15 + ": a IplanRio conectou 1.958 unidades administrativas em alta velocidade em 2015 (meta do plano: 2.000 pontos); não foi localizado o novo Datacenter.", DO + "3075/7", "2015-12"),
 "regionais_33": ("nao_cumprida", "media", AR15 + ": em 2015 só havia um projeto piloto de centro de atendimento, na Região Administrativa de Madureira, das 33 prometidas.", DO + "3075/7", "2015-12"),
 "smgpm": ("cumprida", "baixa", "A prefeitura manteve o monitoramento de metas do Plano Estratégico 2013-2016 pelos Acordos de Resultados (Decreto 36.906/2013) e fez 51 reuniões de monitoramento em 2015, mas não foi localizado ato que institua o sistema com esse nome.", DO + "3075/7", "2015-12"),
 "nota_carioca": ("nao_cumprida", "baixa", "A Nota Carioca chegou ao 26º sorteio em dez/2016 (o 11º foi em mar/2013), com cerca de 4 sorteios por ano; não foi localizado registro de 5.000 premiados por ano.", "https://www.normasbrasil.com.br/norma/resolucao-2915-2016-rio-de-janeiro_334331.html", "2016-12"),
 "codigo_tributario": ("nao_cumprida", "media", SR.format("consolidação das leis tributárias municipais em um único ato normativo"), "", "2026-10"),
 # Desenvolvimento econômico
 "alvaras": ("parcialmente_cumprida", "media", AR15 + ": em 2015, 70,7% dos alvarás e licenças eram emitidos por meio eletrônico e 98,7% dos alvarás de baixo risco saíam em até 3 dias (meta do plano: 100% eletrônicos até 2016).", DO + "3075/8", "2015-12"),
 "energia_1bi": ("nao_cumprida", "media", SR.format("balanço dos investimentos de empresas de energia e P&D atraídos"), "", "2026-10"),
 "hotel_7mil": ("parcialmente_cumprida", "media", "A oferta hoteleira cresceu muito além de 7 mil quartos (de cerca de 31 mil em 2010 para 60 a 62 mil em 2016), mas não foi localizado registro de ocupação acima de 80%.", "https://apublica.org/colecaoparticular/2017/12/hoteis-foram-ceus-olimpiada/", "2016-12"),
 "economia_criativa": ("nao_cumprida", "media", SR.format("medição da fatia do emprego na economia criativa"), "", "2026-10"),
 "condominio_industrial": ("nao_cumprida", "media", SR.format("condomínio industrial na Zona Oeste ou parque tecnológico municipal para o setor de energia"), "", "2026-10"),
 "centro_convencoes": ("nao_cumprida", "media", SR.format("PPP para centro de convenções na Zona Portuária"), "", "2026-10"),
 "agencia_criativa": ("nao_cumprida", "media", SR.format("agência de capacitação e investimento para a indústria criativa"), "", "2026-10"),
}
