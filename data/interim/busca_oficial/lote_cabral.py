"""Lote de buscas no Diário Oficial do RJ (Parte I, 2011-2014) para o censo do Cabral 2010.

python -I data/interim/busca_oficial/lote_cabral.py  -> grava cabral_rj_2010.json ao lado (retoma se interrompido)
"""
import json, socket, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
from busca_rj import ioerj  # noqa: E402

socket.setdefaulttimeout(120)
SAIDA = Path(__file__).with_name("cabral_rj_2010.json")
ANOS = ["2011", "2012", "2013", "2014"]

TERMOS = {
 "transp_convenios": ["Projeto Transparência convênios"],
 "pregoes60": ["pregão eletrônico percentual"],
 "boletim_pessoal": ["boletim prestação de contas pessoal"],
 "divida_ativa": ["Portal da Dívida Ativa"],
 "ecf_web": ["Emissor de Cupom Fiscal internet"],
 "simul_divida": ["simulação da dívida"],
 "elearning": ["ensino a distância servidores Ceperj"],
 "concurso500": ["concurso Especialista em Políticas Públicas e Gestão Governamental"],
 "sala_situacao": ["Sala de Situação"],
 "erp": ["Enterprise Resource Planning"],
 "sigrh": ["SIGRH folha de pagamento"],
 "biometria": ["Identidade Funcional biometria"],
 "sispat": ["SISPAT imóveis"],
 "rioprev_audit": ["recadastramento Rioprevidência"],
 "processos_virtuais": ["processo administrativo eletrônico"],
 "acordo_resultados": ["Acordo de Resultados"],
 "iso_subfin": ["ISO 9001 Subsecretaria de Finanças"],
 "samu120": ["ambulâncias SAMU aquisição"],
 "clinica_familia50": ["Clínica da Família construção"],
 "hiperdia10": ["Centro de Referência Hipertensão Diabetes"],
 "clinica_mae5": ["Clínica da Mãe"],
 "aids3": ["Centro de Referência AIDS construção"],
 "cancer5": ["Centro de Diagnóstico Câncer"],
 "politrauma_centros": ["Centro de Politrauma"],
 "pesq_envelhecimento": ["Centro de Pesquisa do Envelhecimento"],
 "pesq_crack": ["Centro de Pesquisa crack"],
 "hto_paraiba": ["Hospital Traumatologia Ortopedia Paraíba do Sul"],
 "hosp_mae": ["Hospital da Mãe"],
 "hosp_politrauma": ["Hospital Politraumatizados"],
 "hosp_cardio": ["Hospital Cardiologia Queimados"],
 "hosp_alta_vr": ["Hospital Regional Volta Redonda"],
 "hosp_transplantes": ["Hospital de Transplantes"],
 "upp_social": ["UPP Social"],
 "delegacia_legal": ["Programa Delegacia Legal conclusão"],
 "vigilancia": ["Sistema de Vigilância Eletrônica"],
 "cicc": ["Centro Integrado de Comando e Controle inauguração"],
 "cidade_policia": ["Cidade da Polícia"],
 "siad": ["Sistema Integrado de Análise de Dados"],
 "comissao_eventos": ["Comissão Estadual de Segurança Grandes Eventos"],
 "sem_carceragem": ["carceragem desativação"],
 "presidios_ppp": ["parceria público-privada complexo penitenciário"],
 "olimpico_equip": ["Projeto Olímpico escolas"],
 "laptops": ["laptops alunos Olimpíada"],
 "emi20": ["Ensino Médio Integrado parceria"],
 "emi200": ["Ensino Médio Inovador"],
 "arca": ["Arte Culinária Agricultura Sustentável"],
 "casa_educador": ["Casa do Educador"],
 "merito": ["bonificação resultado servidores Educação"],
 "escolas50": ["construção unidade escolar ensino médio"],
 "reforma200": ["reforma unidades escolares Seeduc"],
 "bolsa_licenciatura": ["bolsa licenciatura ensino médio universidade estadual"],
 "pac2_7com": ["PAC 2 Jacarezinho"],
 "mcmv40": ["Minha Casa Minha Vida terreno CEHAB"],
 "morar_melhor": ["Morar Melhor"],
 "morar_seguro": ["Morar Seguro"],
 "nucleos60": ["Núcleos Habitacionais Integrados"],
 "vilas_idade": ["Vila da Melhor Idade"],
 "reforma_conj": ["reforma conjuntos habitacionais"],
 "reg_upp": ["regularização fundiária UPP"],
 "porto_caxias": ["Porto das Caixas abastecimento"],
 "pinheiral": ["Pinheiral abastecimento de água"],
 "rio_ostras": ["Rio das Ostras Barra de São João água"],
 "seropedica": ["esgotamento sanitário Seropédica"],
 "ferreiros": ["São Sebastião dos Ferreiros"],
 "arco": ["Arco Metropolitano"],
 "via_light": ["Via Light Avenida Brasil"],
 "transbaixada": ["Transbaixada"],
 "rodovias_impl": ["pavimentação rodovia estadual DER"],
 "rodovias_rest": ["restauração rodovia estadual DER"],
 "maracana": ["Maracanã reforma"],
 "linha4": ["Linha 4 Metrô"],
 "linha3": ["Linha 3 Metrô Niterói"],
 "trens90": ["aquisição trens SuperVia"],
 "trens_reforma": ["modernização trens SuperVia"],
 "estacoes": ["estações SuperVia reforma"],
 "barcas11": ["embarcações barcas aquisição"],
 "barcas150": ["barcas passageiros"],
 "barra_furado": ["Barra do Furado"],
 "acu_acessos": ["Porto do Açu acesso rodoviário"],
 "aeroportos": ["aeroporto reforma Itaperuna"],
 "aero_vale": ["aeroporto Volta Redonda"],
 "formacao450": ["Faetec vagas formação inicial"],
 "tecnico30": ["Faetec cursos técnicos vagas"],
 "tecnologo": ["Faetec tecnólogo vagas"],
 "idiomas": ["cursos de idiomas gratuitos Copa"],
 "lixoes": ["Lixão Zero encerramento"],
 "esgoto60": ["Pacto pelo Saneamento esgoto"],
 "mata17": ["conectividade fragmentos mata atlântica"],
 "licenca_prazo": ["prazo licença ambiental Inea dias"],
 "ar_copa": ["qualidade do ar Copa"],
 "rios100": ["Limpa Rio dragagem"],
 "concurso_inea": ["concurso Inea"],
 "sede_inea": ["sede Inea construção"],
 "lic_municipios": ["convênio licenciamento ambiental municipal"],
 "alerta_cheias": ["sistema de alerta de cheias"],
 "veic_emissao": ["inspeção veicular emissão licenciamento"],
 "aeronave": ["aeronave Inea"],
 "passivos1": ["Canal do Fundão"],
 "passivos2": ["Cidade dos Meninos"],
 "araruama": ["Lagoa de Araruama Arraial do Cabo"],
 "saquarema": ["Lagoa de Saquarema molhe"],
 "jacarepagua": ["lagoas Jacarepaguá dragagem"],
 "iguacu2": ["Projeto Iguaçu"],
 "psam": ["Programa de Saneamento Ambiental dos Municípios do Entorno da Baía de Guanabara"],
 "aterros11": ["aterro sanitário consórcio"],
 "guardaparques": ["guarda-parques"],
 "uc250": ["criação Parque Estadual"],
 "mudas30": ["mudas plantadas"],
 "rio_clima": ["Instituto Rio Clima"],
 "banco_carbono": ["Banco de Carbono"],
 "redes_saberes": ["Redes de Saberes"],
 "balcao_direitos": ["Balcão de Direitos"],
 "ciacs": ["Centro Integrado de Atendimento ao Cidadão"],
 "crj": ["Centro de Referência da Juventude"],
 "restaurantes12": ["Restaurante Cidadão"],
 "gastronomia": ["Restaurante Cidadão gastronomia"],
 "um_lar": ["Um Lar para Mim"],
 "sos_desap": ["SOS Desaparecidos"],
 "comite_tortura": ["Comitê Prevenção Combate Tortura"],
 "centros_exc": ["Centro de Excelência esporte"],
 "voluntarios": ["voluntários Rio 2016 capacitação"],
 "pracas20": ["Praça da Juventude"],
 "obs_turismo": ["Observatório do Turismo"],
 "plano_turismo": ["Plano Diretor de Turismo"],
 "capac_prodetur": ["Prodetur capacitação"],
 "qualif_turismo": ["qualificação profissional turismo"],
 "pulseiras": ["pulseira pictogramas"],
 "rio_passaporte": ["Rio Passaporte"],
 "estradas15": ["Estradas da Produção"],
 "cecaf": ["Centro de Comercialização da Agricultura Familiar"],
 "ceasa10": ["Ceasa resultado"],
 "rio_rural2": ["Rio Rural microbacias"],
 "celulose": ["Rio Floresta celulose"],
 "pesca": ["parque industrial pesca"],
 "agroenergia": ["Rio Agroenergia"],
 "rio_cafe": ["Rio Café"],
 "upp600": ["Unidade de Polícia Pacificadora criação"],
 "efetivo52": ["concurso Soldado Polícia Militar vagas"],
 "pac2_uh": ["PAC 2 unidades habitacionais"],
}


def main():
    dados = json.loads(SAIDA.read_text(encoding="utf-8")) if SAIDA.exists() else {}
    for chave, consultas in TERMOS.items():
        if chave in dados:
            continue
        dados[chave] = {"ioerj": {}}
        for termos in consultas:
            for ano in ANOS:
                try:
                    total, itens = ioerj(termos, ano)
                    dados[chave]["ioerj"][f"{termos}|{ano}"] = {"total": total, "itens": itens}
                except Exception as e:  # noqa: BLE001
                    dados[chave]["ioerj"][f"{termos}|{ano}"] = {"erro": str(e)}
        SAIDA.write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
        print(chave, {k.split("|")[1]: v.get("total", v.get("erro")) for k, v in dados[chave]["ioerj"].items()}, flush=True)


if __name__ == "__main__":
    main()
