# Classificação do censo do Paes 2020 (mandato 2021-2024, encerrado).
# chave: (status, confianca, evidencia, fonte_url, data_evidencia)
SR = ("Busca na imprensa, em sites oficiais e no Diário Oficial do Município do Rio (2021–2024) em out/2026 "
      "não localizou registro de {}.")
DO = "https://doweb.rio.rj.gov.br/portal/edicoes/download/"
BAL = "https://transparencia.prefeitura.rio/wp-content/uploads/sites/100/2023/07/Balanco-de-Entregas-2021-2024.pdf"
D100 = "https://doweb.rio.rj.gov.br/apifront/portal/edicoes/imprimir_materia/703152/4791"
D = {
 "avenida_brasil": ("cumprida", "media", "O BRT Transbrasil foi concluído e o eixo da Avenida Brasil atraiu 15 investimentos privados até 2024, acima da meta de 10 do Plano Estratégico 2021-2024 (balanço da própria prefeitura).", BAL, "2024-12"),
 "convenios_etica": ("nao_cumprida", "media", SR.format("convênios com o Ministério Público, o Tribunal de Contas ou a Transparência Internacional. A prefeitura criou o Programa Carioca de Integridade Pública (Decreto 48.349/2021) e a Controladoria assinou acordo com a CGU em 2023, que não são os convênios prometidos"), "", "2026-10"),
 "salarios_em_dia": ("cumprida", "media", "A prefeitura passou a publicar decretos anuais com o calendário de pagamento dos servidores e quitou, de forma escalonada até 2022, o 13º salário de 2020 deixado em atraso pela gestão anterior.", DO + "5975/3", "2023-08"),
 "acordo_resultados": ("cumprida", "alta", "O Decreto 48.798, de abr/2021, retomou o Programa de Acordos de Resultados; de 2022 a 2024, 99% dos servidores participaram do programa (balanço da própria prefeitura).", "https://fazenda.prefeitura.rio/wp-content/uploads/sites/12/2022/10/1.Dec-48798_2021-AR2021.pdf", "2021-04"),
 "cartao_familia": ("nao_cumprida", "media", SR.format("ampliação dos recursos ou reajuste do Cartão Família Carioca; houve só um pagamento emergencial extra em 2021 (Auxílio Carioca, média de R$ 240 por família)"), "https://agenciabrasil.ebc.com.br/economia/noticia/2021-03/covid-19-cidade-do-rio-tera-auxilio-para-900-mil-pessoas", "2021-03"),
 "restaurantes_populares": ("nao_cumprida", "media", "A prefeitura seguiu com os mesmos 3 restaurantes populares (Bangu, Campo Grande e Bonsucesso) e não abriu farmácias populares; a expansão do combate à fome foi feita por cozinhas comunitárias.", DO + "6753/67", "2024-09"),
 "frentes_trabalho": ("cumprida", "media", "O plano dos 100 dias previu a retomada das frentes de trabalho nas comunidades (Guardiões dos Rios, Agentes Comunitários de Saúde, Garis Comunitários), e o número de trabalhadores comunitários em favelas cresceu 96% até 2024 (meta de 30%, balanço da própria prefeitura).", BAL, "2024-12"),
 "conscientizacao": ("nao_cumprida", "media", SR.format("programa de conscientização para a cidadania nas escolas e espaços públicos no mandato (a promessa foi repetida no plano de 2024 e o programa só foi criado por lei em 2026)"), "", "2026-10"),
 "plano_100_dias": ("cumprida", "alta", "O Decreto 48.393, de 01/01/2021, instituiu o Plano de Ações para os 100 primeiros dias, com 25 ações (preparar as Clínicas da Família para a vacinação, planejar a volta às aulas, Plano BRT com Dignidade); a prefeitura fez a intervenção no BRT em mar/2021.", D100, "2021-01"),
}
