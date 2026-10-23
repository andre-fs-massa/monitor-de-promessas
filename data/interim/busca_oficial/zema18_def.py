# Censo do plano de Romeu Zema (governo de Minas Gerais, 2018): uma tupla por promessa testável.
# (trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente, termo de busca)
# Entraram as ações (➢) com objeto concreto de cada área, a premissa de não aumentar impostos e as medidas de
# "mudança cultural"; ficaram de fora diagnósticos, "mitos" e verbos vagos (incentivar, fomentar, promover).
P = [
    # Gestão de Estado
    ("Atualmente existem 21 secretarias de estado, sendo que algumas delas realizam funções e serviços semelhantes.", "Reduzir o número de secretarias (21) e extinguir cargos comissionados desnecessários", "Gestão pública", "acao", "sim", "", "reforma administrativa"),
    ("será implementado o \"Parecer de Seleção\", que institui critérios técnicos, transparentes", "Implantar seleção técnica e transparente (\"Parecer de Seleção\") para cargos de confiança", "Gestão pública", "acao", "nao", "", "Transforma Minas"),
    ("Além disso, serão feitas auditorias patrimoniais aleatórias dos agentes públicos", "Fazer auditorias patrimoniais aleatórias dos agentes públicos", "Gestão pública", "acao", "nao", "", "evolução patrimonial"),
    ("programas de seguros do tipo", "Exigir seguros do tipo performance bond nas contratações públicas", "Gestão pública", "acao", "nao", "", "seguro-garantia"),
    ("O primeiro ponto a ser considerado é a regularização dos pagamentos atrasados das transferências constitucionais", "Regularizar os repasses constitucionais atrasados aos municípios", "Finanças públicas", "acao", "nao", "", "repasses municípios"),
    ("relacionando as pesquisas públicas aos critérios de bonificação", "Avaliar órgãos e servidores por pesquisas com a população, ligadas à bonificação", "Gestão pública", "acao", "nao", "", "avaliação de desempenho"),
    ("Esta alternativa compreende na elaboração de concessões, parcerias-público privadas e ações de desestatização", "Fazer concessões, PPPs e desestatizações (ferrovias, rodovias, portos secos)", "Estatais", "acao", "sim", "", "concessão"),
    ("é possível resgatá-la a partir da instituição de previdência privada complementar aos novos e antigos servidores.", "Instituir previdência complementar para novos servidores, com opção para os atuais", "Previdência", "acao", "sim", "", "previdência complementar"),
    ("Assim, haverá o retorno da sede do governo para a Cidade Administrativa", "Manter a sede do governo na Cidade Administrativa", "Gestão pública", "acao", "nao", "", "Cidade Administrativa"),
    ("destinando o uso do Palácio da Liberdade para um museu de regalias", "Transformar o Palácio da Liberdade em museu", "Cultura", "acao", "nao", "", "Palácio da Liberdade"),
    ("o salário do governador será reduzido", "Reduzir o salário do governador", "Gestão pública", "acao", "sim", "", "subsídio governador"),
    ("o Palácio das Mangabeiras não será utilizado como moradia", "Não usar o Palácio das Mangabeiras como moradia", "Gestão pública", "acao", "nao", "", "Mangabeiras"),
    ("● Não haverá aumento da carga tributária;", "Não aumentar a carga tributária", "Finanças públicas", "resultado", "nao", "", "alíquota ICMS"),
    # Geração de riqueza
    ("É necessário acabar e dar transparência a este sistema para dar lugar à livre concorrência", "Dar transparência aos incentivos e subsídios fiscais concedidos a empresas", "Finanças públicas", "acao", "nao", "", "benefícios fiscais transparência"),
    ("Assim, é preciso permitir a criação de autenticações, selos e certificações privadas para quaisquer tipos de atividades.", "Permitir selos e certificações privadas no lugar de regulação estatal", "Ambiente de negócios", "acao", "sim", "", "certificação"),
    ("é mais eficiente inverter a lógica dos licenciamentos, presumindo", "Inverter a lógica do licenciamento, presumindo a boa-fé do empreendedor e punindo depois", "Ambiente de negócios", "acao", "nao", "", "liberdade econômica"),
    ("é necessário estabelecer medidas para que a função das Juntas/Conservatória seja meramente o registro", "Limitar a Junta Comercial ao registro e proibir exigência de autenticação de documentos", "Ambiente de negócios", "acao", "nao", "", "Junta Comercial"),
    ("haverá abertura para aporte de capital privado, serão criados conselhos independentes", "Abrir as estatais remanescentes ao capital privado, com conselhos independentes", "Estatais", "acao", "nao", "", "estatais governança"),
    # Segurança pública
    ("O estado pode propiciar cadastros voluntários de outros bens duráveis facilmente", "Criar cadastro voluntário de bens duráveis para dificultar a receptação", "Segurança pública", "acao", "nao", "", "cadastro de bens"),
    ("deve-se começar a reunir e monitorar dados sobre os resultados dos inquéritos policiais de homicídios no estado", "Monitorar indicadores de esclarecimento dos inquéritos de homicídio", "Segurança pública", "acao", "nao", "", "homicídio"),
    ("o uso de tornozeleiras eletrônicas nos casos de crimes mais brandos", "Ampliar penas alternativas com tornozeleiras eletrônicas e revisar a população carcerária", "Segurança pública", "acao", "nao", "", "monitoração eletrônica"),
    ("O uso de aplicativos que permitem que celulares com câmeras sejam acoplados aos coletes de policiais", "Adotar câmeras acopladas ao uniforme dos policiais", "Segurança pública", "acao", "nao", "", "câmeras corporais"),
    ("A aplicação do método Apac e os modelos de parcerias público-privadas podem ser aprimorados e expandidos", "Expandir as APACs e as PPPs prisionais", "Segurança pública", "acao", "nao", "", "Apac"),
    ("Minas Gerais pode adotar sistemas de categorização e centralização de informações iguais a de outros estados", "Integrar os sistemas de informação das polícias, como o Infocrim de SP", "Segurança pública", "acao", "nao", "", "integração sistemas"),
    ("tendo em vista a criação de um", "Criar setor de inteligência para a violência no campo", "Segurança pública", "acao", "nao", "", "segurança rural"),
    ("é por meio da expansão de câmeras inteligentes instaladas em fronteiras", "Instalar câmeras inteligentes nas divisas (cerco eletrônico) e usar drones e GPS nas viaturas", "Segurança pública", "acao", "nao", "", "cerco eletrônico"),
    # Educação
    ("é possível realizar PPPs com vistas a reformas e/ou construções de estabelecimentos escolares", "Fazer PPPs para reformar ou construir escolas", "Educação", "acao", "nao", "", "PPP escolas"),
    ("Assim, é necessária uma mudança na forma de alocação de recursos às escolas, priorizando num primeiro momento", "Mudar a distribuição de recursos às escolas, priorizando as mais precárias", "Educação", "acao", "nao", "", "recursos escolas"),
    ("afetando o montante de recursos recebidos pelas escolas e bonificações aos professores, diretores e outros colaboradores.", "Premiar escolas e profissionais pela evolução do desempenho", "Educação", "acao", "nao", "", "bonificação educação"),
    ("Uma alternativa para destinação dos espaços ociosos é a realização de parcerias com escolas privadas", "Ceder escolas estaduais ociosas a escolas privadas em troca de bolsas", "Educação", "acao", "nao", "", "escolas ociosas"),
    ("Pelo programa que se propõe neste plano, estudantes de baixa renda terão acesso a uma quantia de recursos de uso restrito", "Criar voucher educacional para estudantes de baixa renda", "Educação", "acao", "nao", "", "voucher"),
    ("Realizar parcerias entre o setor público, incluindo municípios interessados, e o privado para levar o ensino rural de qualidade", "Fazer parcerias (Senar, Sebrae, Senai) para cursos temáticos nas escolas rurais", "Educação", "acao", "nao", "", "educação do campo"),
    ("adotar programas e aplicativos que permitam um acompanhamento mais contínuo dos responsáveis legais", "Adotar aplicativo ou sistema online para os pais acompanharem os alunos", "Educação", "acao", "nao", "", "aplicativo pais"),
    # Saúde
    ("Realizar os ajustes fiscais e as realocações de despesas necessárias para garantir o pagamento em dia dos fornecedores e servidores da área de saúde", "Pagar em dia salários, fornecedores e repasses aos municípios na saúde", "Saúde", "acao", "nao", "", "repasses saúde"),
    ("colocando em funcionamento os Hospitais Regionais e garantindo maior cobertura do SAMU", "Pôr em funcionamento os hospitais regionais inacabados", "Saúde", "acao", "nao", "", "hospital regional"),
    ("40% dos municípios mineiros ainda estão sem cobertura do SAMU.", "Ampliar a cobertura do SAMU", "Saúde", "acao", "nao", "", "SAMU"),
    ("Delegação da administração dos equipamentos da saúde para", "Delegar a gestão de unidades de saúde a Organizações Sociais e PPPs", "Saúde", "acao", "nao", "", "organização social"),
    ("alterando para uma lógica de contrato global de desempenho e qualidade", "Mudar a contratualização dos hospitais para pagamento por desempenho e qualidade", "Saúde", "acao", "nao", "", "Valora Minas"),
    ("é preciso investir na implantação de prontuários eletrônicos e implementar centros de atendimento online", "Implantar prontuário eletrônico e centros de telemedicina", "Saúde", "acao", "nao", "", "telessaúde"),
]
