const { mandatos, promessas, status: ORDEM } = window.DADOS;

const ROTULO = {
  cumprida: "Cumprida",
  parcialmente_cumprida: "Parcialmente cumprida",
  nao_cumprida: "Não cumprida",
  em_andamento: "Em andamento",
  interrompida: "Interrompida (fim antecipado do mandato)",
  nao_avaliada: "Não avaliada",
};
const PLURAL = {
  cumprida: "Cumpridas",
  parcialmente_cumprida: "Parciais",
  nao_cumprida: "Não cumpridas",
  em_andamento: "Em andamento",
  interrompida: "Interrompidas",
};
const COR = {
  cumprida: "var(--s-cumprida)",
  parcialmente_cumprida: "var(--s-parcial)",
  nao_cumprida: "var(--s-nao)",
  em_andamento: "var(--s-andamento)",
  interrompida: "var(--s-interrompida)",
  nao_avaliada: "var(--s-naoavaliada)",
};
const CONF = { alta: "confiança alta", media: "confiança média", baixa: "confiança baixa" };

// Impacto fiscal (presidentes): as categorias técnicas viram seis grupos simples para o eleitor
const IMPACTO = {
  despesa_aumenta: { rot: "Aumenta a despesa", cor: "var(--i-despesa)" },
  despesa_reduz: { rot: "Reduz a despesa", cor: "var(--i-despesa)" },
  receita_aumenta: { rot: "Aumenta a receita", cor: "var(--i-receita)" },
  receita_reduz: { rot: "Reduz a receita", cor: "var(--i-receita)" },
  neutro: { rot: "Neutro (efeitos se compensam)", cor: "var(--i-neutro)" },
  sem_impacto: { rot: "Sem impacto direto no orçamento", cor: "var(--i-neutro)" },
};
const SEM_IMPACTO_DETALHE = {
  sem_impacto_direto: "medida regulatória ou sem gasto relevante",
  regra_fiscal: "regra fiscal: muda o limite de gastos, não um gasto específico",
  fora_do_orcamento: "pago por estatal ou fundo fora do Orçamento da União",
  sem_impacto_primario: "não gera gasto nem receita no resultado primário",
  indireto_estatal: "efeito indireto, via lucros e dividendos de estatal",
  sem_valor_proprio: "resultado de outros programas, já contados neles",
};
const grupoImpacto = (p) => (p.impacto ? (IMPACTO[p.impacto.impacto_fiscal] ? p.impacto.impacto_fiscal : "sem_impacto") : "");
const num = (v) => parseFloat(v || "0");
const fmtBi = (v) => `R$ ${num(v).toLocaleString("pt-BR", { maximumFractionDigits: 1 })} bi`;

function blocoImpacto(lista, m) {
  const com = lista.filter((p) => p.impacto);
  if (!com.length) return "";
  const de = (g) => com.filter((p) => grupoImpacto(p) === g);
  // Valores do mandato: soma, ano a ano, da diferença em relação ao ano anterior ao mandato
  const somaAc = (ps) => ps.reduce((s, p) => s + num(p.impacto.valor_acumulado_rs_bi), 0);
  const comValor = (ps) => ps.filter((p) => p.impacto.valor_acumulado_rs_bi).length;
  const tile = (g, valor, det) => `
    <div class="kpi"><div class="rotulo"><i class="ponto" style="background:${IMPACTO[g].cor}"></i>${IMPACTO[g].rot}</div>
      <div class="valor">${valor}</div><div class="det">${det}</div></div>`;
  const tiles = ["despesa_aumenta", "despesa_reduz", "receita_aumenta", "receita_reduz"]
    .filter((g) => de(g).length)
    .map((g) => {
      const ps = de(g);
      const n = comValor(ps);
      const unicas = somaAc(ps.filter((p) => p.impacto.recorrente === "nao"));
      const extra = unicas ? ` · inclui ${fmtBi(unicas)} de receitas ou gastos únicos, contados uma vez` : "";
      return tile(g, n ? `${g.endsWith("reduz") ? "−" : "+"}${fmtBi(somaAc(ps))}` : "sem valor",
        `${ps.length} promessa(s), ${n} com valor oficial no mandato${extra}`);
    });
  const sem = com.length - ["despesa_aumenta", "despesa_reduz", "receita_aumenta", "receita_reduz"].reduce((s, g) => s + de(g).length, 0);
  tiles.push(tile("sem_impacto", sem, "promessas regulatórias, regras fiscais, estatais ou efeitos neutros"));
  const [recMais, recMenos, despMais, despMenos] =
    ["receita_aumenta", "receita_reduz", "despesa_aumenta", "despesa_reduz"].map((g) => somaAc(de(g)));
  const saldoAc = recMais - recMenos - despMais + despMenos;
  const anosAc = com.filter((p) => p.impacto.valor_acumulado_rs_bi)
    .flatMap((p) => p.impacto.periodo_acumulado.match(/\d{4}/g) || []).sort();
  const periodo = anosAc.length ? (anosAc[0] === anosAc[anosAc.length - 1] ? anosAc[0] : `${anosAc[0]} a ${anosAc[anosAc.length - 1]}`) : "";
  const contaAc = [
    recMais && `Receitas a mais ${fmtBi(recMais)}`,
    recMenos && `menos receitas a menos ${fmtBi(recMenos)}`,
    despMais && `menos despesas a mais ${fmtBi(despMais)}`,
    despMenos && `mais despesas cortadas ${fmtBi(despMenos)}`,
  ].filter(Boolean).join(", ").replace(/^(menos|mais) (.)/, (_, _1, c) => c.toUpperCase());
  const emCurso = m && m.situacao_mandato === "em_curso";
  const pendentes = com.filter((p) => p.impacto.valor_incremental_rs_bi && !p.impacto.valor_acumulado_rs_bi && p.impacto.periodo_acumulado);
  const acumulado = periodo ? `
    <div class="resultado acumulado ${saldoAc < 0 ? "deficit" : "superavit"}">
      <div class="rotulo">Resultado das promessas para as contas do governo no mandato (${periodo}${emCurso ? ", mandato em curso" : ""})</div>
      <div class="valor">${saldoAc < 0 ? "Déficit" : "Superávit"} de ${fmtBi(Math.abs(saldoAc))}</div>
      <div class="det">${contaAc}. ${saldoAc < 0
        ? "As promessas implementadas aumentaram mais os gastos do que a arrecadação."
        : "As promessas implementadas aumentaram mais a arrecadação do que os gastos."} É o efeito dessas promessas, não o déficit ou superávit total do governo.${
        emCurso ? ` Só anos completos; ${anosAc[anosAc.length - 1] * 1 + 1} ainda está em curso.` : ""}${
        pendentes.length === 1 ? " Não inclui 1 promessa que só começa a valer depois desse período."
          : pendentes.length ? ` Não inclui ${pendentes.length} promessas que só começam a valer depois desse período.` : ""}</div>
    </div>` : "";
  return `
    <div class="impacto-resumo">
      <h4>Impacto no orçamento federal</h4>
      ${acumulado}
      <div class="kpis">${tiles.join("")}</div>    </div>`;
}

function celulaImpacto(p) {
  const i = p.impacto;
  if (!i) return "";
  const g = grupoImpacto(p);
  const receita = g.startsWith("receita");
  const ano = i.ano_ref ? ` (${i.ano_ref})` : "";
  const linhas = [];
  if (i.valor_incremental_rs_bi && g !== "neutro")
    linhas.push(g.endsWith("reduz")
      ? `<strong>−${fmtBi(i.valor_incremental_rs_bi)}/ano</strong> ${receita ? "de receita" : "de despesa"} a menos${ano}`
      : `<strong>+${fmtBi(i.valor_incremental_rs_bi)}/ano</strong> ${receita ? "de receita" : "de despesa"} a mais${ano}`);
  if (i.recorrente === "nao") linhas.push(`<span class="conf">valor único, não se repete todo ano</span>`);
  if (i.valor_total_rs_bi) linhas.push(`${g === "sem_impacto" ? "Valor envolvido" : "Custo total do programa"}: ${fmtBi(i.valor_total_rs_bi)}${ano}`);
  if (i.valor_acumulado_rs_bi && g !== "sem_impacto" && g !== "neutro")
    linhas.push(`Acumulado no mandato: ${g.endsWith("reduz") ? "−" : "+"}${fmtBi(i.valor_acumulado_rs_bi)} (${i.periodo_acumulado.replace("-", "–")})`);
  else if (i.periodo_acumulado && !i.valor_acumulado_rs_bi) linhas.push(`<span class="conf">Acumulado no mandato: ainda não (${i.periodo_acumulado})</span>`);
  if (i.compensacao_rs_bi) linhas.push(`<span class="compensa">Compensação atrelada: isenção que reduz a receita em ${fmtBi(i.compensacao_rs_bi)}</span>`);
  if (g === "sem_impacto") linhas.push(`<span class="conf">${SEM_IMPACTO_DETALHE[i.impacto_fiscal]}</span>`);
  const links = [
    i.fonte_oficial && `<a href="${esc(i.fonte_oficial)}" target="_blank" rel="noopener">fonte oficial</a>`,
    i.fonte_comparacao && `<a href="${esc(i.fonte_comparacao)}" target="_blank" rel="noopener">comparação</a>`,
  ].filter(Boolean).join(" · ");
  return `<span class="chip"><i class="ponto" style="background:${IMPACTO[g].cor}"></i>${IMPACTO[g].rot}</span>
    ${linhas.map((l) => `<div class="imp-linha">${l}</div>`).join("")}
    <details class="imp-det"><summary>como calculamos</summary>${esc(i.explicacao)} <span class="conf">(${CONF[i.confianca]})</span>${links ? `<div>${links}</div>` : ""}</details>`;
}
const CPPG = ["cumprida", "parcialmente_cumprida", "nao_cumprida"];

// Textos que mudam conforme o cargo
const CARGO = {
  presidente: { aba: "Presidência", plural: "presidentes", singular: "presidente", legislativo: "Congresso", legCurto: "Congresso" },
  governador: { aba: "Governos estaduais", plural: "governadores", singular: "governador", legislativo: "Legislativo estadual", legCurto: "Legislativo" },
  prefeito: { aba: "Prefeituras", plural: "prefeitos", singular: "prefeito", legislativo: "Legislativo municipal", legCurto: "Legislativo" },
};
// Rota no endereço de cada cargo: #presidencia, #governadores/RJ, #prefeituras/RJ-Rio%20de%20Janeiro
const ROTA = { presidente: "presidencia", governador: "governadores", prefeito: "prefeituras" };
const ESTADOS = {
  AC: "Acre", AL: "Alagoas", AP: "Amapá", AM: "Amazonas", BA: "Bahia", CE: "Ceará", DF: "Distrito Federal",
  ES: "Espírito Santo", GO: "Goiás", MA: "Maranhão", MT: "Mato Grosso", MS: "Mato Grosso do Sul", MG: "Minas Gerais",
  PA: "Pará", PB: "Paraíba", PR: "Paraná", PE: "Pernambuco", PI: "Piauí", RJ: "Rio de Janeiro", RN: "Rio Grande do Norte",
  RS: "Rio Grande do Sul", RO: "Rondônia", RR: "Roraima", SC: "Santa Catarina", SP: "São Paulo", SE: "Sergipe", TO: "Tocantins",
};

// Onde o mandato vale: estado (governador) ou município (prefeito)
const chaveLugar = (m) => (m.cargo === "prefeito" ? `${m.uf}-${m.municipio}` : m.uf);
const nomeLugar = (m) => (m.cargo === "prefeito" ? `${m.municipio} (${m.uf})` : ESTADOS[m.uf]);

const pct = (n, d) => (d ? Math.round((n / d) * 100) : 0);
const fmtData = (iso) => iso.split("-").reverse().join("/");
const el = (html) => {
  const t = document.createElement("template");
  t.innerHTML = html.trim();
  return t.content.firstElementChild;
};
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const $ = (id) => document.getElementById(id);

function resumo(lista) {
  const cont = Object.fromEntries(ORDEM.map((s) => [s, 0]));
  lista.forEach((p) => cont[p.status]++);
  return { cont, total: lista.length, avaliadas: lista.length - cont.nao_avaliada };
}

// Colunas de taxa: só os status que aparecem no recorte exibido
const colunasDe = (lista) => ORDEM.filter((s) => s !== "nao_avaliada" && lista.some((p) => p.status === s));
const thTaxas = (cols) => cols.map((s) => `<th class="num">${PLURAL[s]}</th>`).join("");
const tdTaxas = (cols, r) => cols.map((s) => `<td class="num" data-label="${PLURAL[s]}">${pct(r.cont[s], r.avaliadas)}%</td>`).join("");

function kpis(cols, r) {
  const tiles = [
    ["Promessas testáveis", r.total, `${r.avaliadas} avaliadas`, null],
    ...cols.filter((s) => CPPG.includes(s) || r.cont[s] > 0).map((s) => [
      s === "parcialmente_cumprida" ? "Parcialmente cumpridas" : PLURAL[s],
      `${pct(r.cont[s], r.avaliadas)}%`,
      `${r.cont[s]} de ${r.avaliadas}`,
      s,
    ]),
  ];
  return tiles
    .map(([rot, val, det, s]) => `
      <div class="kpi">
        <div class="rotulo">${s ? `<i class="ponto" style="background:${COR[s]}"></i>` : ""}${rot}</div>
        <div class="valor">${val}</div>
        <div class="det">${det}</div>
      </div>`)
    .join("");
}

function barra(r) {
  const presentes = ORDEM.filter((s) => r.cont[s] > 0);
  const partes = presentes
    .map((s) => `<span style="width:${(r.cont[s] / r.total) * 100}%;background:${COR[s]}" title="${ROTULO[s]}: ${r.cont[s]}"></span>`)
    .join("");
  const legenda = presentes
    .map((s) => `<span><i class="ponto" style="background:${COR[s]}"></i>${ROTULO[s]} ${r.cont[s]}</span>`)
    .join("");
  return `<div class="barra" role="img" aria-label="Distribuição de status">${partes}</div><div class="legenda">${legenda}</div>`;
}

// Proporção que depende do Legislativo e desempenho de cada grupo
// Tabelas do consolidado que o leitor pode expandir e recolher (fechadas por padrão; a escolha vale ao trocar de aba)
const aberta = {};
const recolhivel = (chave, titulo, html) =>
  `<details class="recolhe" data-chave="${chave}"${aberta[chave] ? " open" : ""}><summary>${titulo}</summary>${html}</details>`;

function blocoLegislativo(lista, cols, leg, chave) {
  const dep = lista.filter((p) => p.depende_legislativo === "sim");
  const linha = (rot, g) => `<tr><td class="titulo">${rot}</td><td class="num" data-label="Promessas">${g.length}</td>${tdTaxas(cols, resumo(g))}</tr>`;
  return `
    <div class="congresso">
      <div class="congresso-topo">
        <span class="congresso-valor">${pct(dep.length, lista.length)}%</span>
        <span>das promessas dependem do ${leg} (${dep.length} de ${lista.length})</span>
      </div>
      <div class="barra fina" role="img" aria-label="Promessas que dependem do ${leg}">
        <span style="width:${pct(dep.length, lista.length)}%;background:var(--congresso)"></span>
      </div>
      ${(chave ? (h) => recolhivel(chave, `Tabela: dependem do ${leg} × só do Executivo`, h) : (h) => h)(`<div class="tabela-scroll"><table class="resp">
        <thead><tr><th>Grupo</th><th class="num">Promessas</th>${thTaxas(cols)}</tr></thead>
        <tbody>${linha(`Dependem do ${leg}`, dep)}${linha("Só do Executivo", lista.filter((p) => p.depende_legislativo !== "sim"))}</tbody>
      </table></div>`)}
      ${chave ? "" : notaOutroEnte(lista)}
    </div>`;
}

// Promessas cuja execução cabe por lei a outro ente federativo
function notaOutroEnte(lista) {
  const n = lista.filter((p) => p.outro_ente).length;
  if (!n) return "";
  return `<p class="meta nota-ente"><span class="tag-ente">outro ente</span> ${n} de ${lista.length} promessas são de competência de outro ente federativo (União, estados ou municípios): quem prometeu só pode financiar, induzir ou cooperar.</p>`;
}

// Mandato interrompido mostra mês e ano da saída (ex.: 2023–03/2026)
const periodo = (m) => {
  const ini = m.mandato_inicio.slice(0, 4);
  if (!m.mandato_fim_efetivo) return `${ini}–${m.mandato_fim.slice(0, 4)}`;
  const [ano, mes] = m.mandato_fim_efetivo.split("-");
  return `${ini}–${mes}/${ano} (previsto até ${m.mandato_fim.slice(0, 4)})`;
};

const local = (p) => [`p. ${p.pagina}`, p.paragrafo && `§${p.paragrafo}`].filter(Boolean).join(", ");
const doMandato = (m) => promessas.filter((p) => p.mandato_id === m.id);

function renderConsolidado(lista, cargo) {
  const txt = CARGO[cargo];
  const daVez = promessas.filter((p) => lista.some((m) => m.id === p.mandato_id));
  const cols = colunasDe(daVez);
  const r = resumo(daVez);
  const emCurso = lista.filter((m) => m.situacao_mandato === "em_curso").length;
  const interrompidos = lista.filter((m) => m.situacao_mandato === "interrompido").length;

  $("t-consolidado").textContent =
    cargo === "presidente" ? "Consolidado dos presidentes" : `Consolidado dos ${txt.plural} · ${nomeLugar(lista[0])}`;
  $("nota-consolidado").textContent =
    `${lista.length} ${lista.length === 1 ? txt.singular : txt.plural} analisado(s), ${r.total} promessas testáveis no total.` +
    (emCurso ? ` ${emCurso} mandato(s) ainda em curso: os números mudam até o fim do mandato.` : "") +
    (interrompidos ? ` ${interrompidos} mandato(s) encerrado(s) antes do prazo, avaliado(s) até a data de saída.` : "");
  $("kpis-consolidado").innerHTML = kpis(cols, r);
  $("barra-consolidado").innerHTML = barra(r) + blocoLegislativo(daVez, cols, txt.legislativo, "legislativo");

  const linhas = lista.map((m) => {
    const lm = doMandato(m);
    const rm = resumo(lm);
    const dep = lm.filter((x) => x.depende_legislativo === "sim").length;
    return `<tr>
      <td class="titulo">${esc(m.nome)} <span class="meta">(${m.eleicao})</span>${m.motivo_interrupcao ? ` <span class="tag-impeachment">${esc(m.motivo_interrupcao)}</span>` : ""}</td>
      <td data-label="Mandato">${periodo(m)}</td>
      <td class="num" data-label="Promessas">${rm.total}</td>
      <td class="num" data-label="Dependem do ${txt.legCurto}">${pct(dep, rm.total)}%</td>
      ${tdTaxas(cols, rm)}
    </tr>`;
  });
  $("t-comparativo").textContent = `Tabela: comparativo por ${txt.singular}`;
  $("comparativo").innerHTML = `
    <thead><tr><th>${txt.singular[0].toUpperCase() + txt.singular.slice(1)}</th><th>Mandato</th><th class="num">Promessas</th><th class="num">Dependem do ${txt.legislativo}</th>${thTaxas(cols)}</tr></thead>
    <tbody>${linhas.join("")}</tbody>`;
}

function linhaPromessa(p, leg, comImpacto) {
  const fonte = p.fonte_url ? `<a href="${esc(p.fonte_url)}" target="_blank" rel="noopener">fonte</a>` : "";
  const impacto = comImpacto ? `<td class="imp">${celulaImpacto(p)}</td>` : "";
  return `<tr>
    <td><div>${esc(p.promessa)}</div><div class="trecho">${local(p)}: “${esc(p.trecho_literal)}”</div></td>
    <td>${esc(p.area)}</td>
    <td><span class="chip"><i class="ponto" style="background:${COR[p.status]}"></i>${ROTULO[p.status]}</span>
      <div class="conf">${CONF[p.confianca]}</div>
      ${p.depende_legislativo === "sim" ? `<span class="tag-congresso">Depende do ${leg}</span>` : ""}
      ${p.outro_ente ? `<span class="tag-ente" title="A execução cabe por lei a outro ente federativo">Competência: ${esc(p.outro_ente)}</span>` : ""}</td>
    <td class="evid">${esc(p.evidencia)} ${fonte}</td>
    ${impacto}
  </tr>`;
}

// "competencia" e "impacto" são derivados; os demais filtros usam o próprio campo
const valorFiltro = (p, campo) =>
  campo === "competencia" ? (p.outro_ente ? "outro" : "propria") : campo === "impacto" ? grupoImpacto(p) : p[campo];

function renderMandato(m) {
  const leg = CARGO[m.cargo].legislativo;
  const lista = doMandato(m);
  const cols = colunasDe(lista);
  const r = resumo(lista);
  const areas = [...new Set(lista.map((x) => x.area))].sort();
  const comImpacto = lista.some((x) => x.impacto);
  const gruposImpacto = Object.keys(IMPACTO).filter((g) => lista.some((x) => grupoImpacto(x) === g));
  const situacao = {
    em_curso: `Mandato em curso · dados até ${fmtData(m.data_corte)}`,
    encerrado: "Mandato encerrado",
    interrompido: `Mandato interrompido (${m.motivo_interrupcao}) em ${fmtData(m.mandato_fim_efetivo || "")} · avaliado até essa data`,
  }[m.situacao_mandato];
  const onde = m.cargo === "presidente" ? "" : ` · ${nomeLugar(m)}`;

  const card = el(`
    <article class="card">
      <div class="card-topo">
        <div>
          <h3>${esc(m.nome)}</h3>
          <div class="meta">${esc(m.partido)} · Coligação ${esc(m.coligacao)}${onde} · eleição de ${m.eleicao} · mandato ${periodo(m)}</div>
        </div>
        <span class="selo ${m.situacao_mandato}">${situacao}</span>
      </div>
      ${m.observacao_mandato ? `<p class="aviso">${esc(m.observacao_mandato)}</p>` : ""}
      <div class="kpis">${kpis(cols, r)}</div>
      ${barra(r)}
      ${blocoLegislativo(lista, cols, leg)}
      ${blocoImpacto(lista, m)}
      <p class="meta">Plano: <a href="${esc(m.url_tse)}">${esc(m.arquivo_plano)}</a> (TSE)</p>
      <div class="filtros">
        <select data-f="status" aria-label="Filtrar por status"><option value="">Todos os status</option>
          ${ORDEM.filter((s) => r.cont[s]).map((s) => `<option value="${s}">${ROTULO[s]} (${r.cont[s]})</option>`).join("")}</select>
        <select data-f="area" aria-label="Filtrar por área"><option value="">Todas as áreas</option>
          ${areas.map((a) => `<option>${esc(a)}</option>`).join("")}</select>
        <select data-f="depende_legislativo" aria-label="Filtrar por dependência do ${leg}"><option value="">Com e sem ${CARGO[m.cargo].legCurto}</option>
          <option value="sim">Dependem do ${CARGO[m.cargo].legCurto}</option><option value="nao">Só do Executivo</option></select>
        ${lista.some((x) => x.outro_ente) ? `<select data-f="competencia" aria-label="Filtrar por competência"><option value="">Qualquer competência</option>
          <option value="propria">Competência própria</option><option value="outro">Competência de outro ente</option></select>` : ""}
        ${comImpacto ? `<select data-f="impacto" aria-label="Filtrar por impacto fiscal"><option value="">Qualquer impacto fiscal</option>
          ${gruposImpacto.map((g) => `<option value="${g}">${IMPACTO[g].rot} (${lista.filter((x) => grupoImpacto(x) === g).length})</option>`).join("")}</select>` : ""}
      </div>
      <div class="tabela-scroll">
        <table class="promessas${comImpacto ? " com-impacto" : ""}"><thead><tr><th>Promessa</th><th>Área</th><th>Status</th><th>Evidência</th>${comImpacto ? "<th>Impacto fiscal</th>" : ""}</tr></thead><tbody></tbody></table>
      </div>
    </article>`);

  const tbody = card.querySelector("table.promessas tbody");
  const filtros = card.querySelectorAll(".filtros select");
  const atualizar = () => {
    const f = Object.fromEntries([...filtros].map((s) => [s.dataset.f, s.value]));
    tbody.innerHTML = lista
      .filter((x) => Object.entries(f).every(([campo, valor]) => !valor || valorFiltro(x, campo) === valor))
      .map((x) => linhaPromessa(x, leg, comImpacto))
      .join("");
  };
  filtros.forEach((s) => s.addEventListener("change", atualizar));
  atualizar();
  return card;
}

// Cartões criados uma vez, para preservar filtros ao alternar
const cartoes = new Map(mandatos.map((m) => [m.id, renderMandato(m)]));
// Estados ou municípios com mandatos de cada cargo, em ordem alfabética
const lugaresDe = (cargo) =>
  [...new Map(mandatos.filter((m) => m.cargo === cargo).map((m) => [chaveLugar(m), nomeLugar(m)])).entries()]
    .sort((a, b) => a[1].localeCompare(b[1]));

const abas = $("abas-cargo");
const seletorLugar = $("seletor-uf");
const seletorMandato = $("seletor-mandato");
abas.innerHTML = Object.entries(CARGO)
  .filter(([c]) => mandatos.some((m) => m.cargo === c))
  .map(([c, t]) => `<button type="button" role="tab" data-cargo="${c}">${t.aba}</button>`)
  .join("");

function lerEndereco() {
  const [rota, lugar] = location.hash.slice(1).split("/");
  const cargo = Object.keys(ROTA).find((c) => ROTA[c] === rota && lugaresDe(c).length) || "presidente";
  if (cargo === "presidente") return { cargo, lugar: "BR" };
  const chaves = lugaresDe(cargo).map(([k]) => k);
  const pedido = decodeURIComponent(lugar || "");
  return { cargo, lugar: chaves.includes(pedido) ? pedido : chaves[0] };
}

const irPara = (cargo, lugar) =>
  (location.hash = cargo === "presidente" ? ROTA.presidente : `${ROTA[cargo]}/${encodeURIComponent(lugar || lugaresDe(cargo)[0][0])}`);

function render() {
  const { cargo, lugar } = lerEndereco();
  const lista = mandatos
    .filter((m) => m.cargo === cargo && (cargo === "presidente" || chaveLugar(m) === lugar))
    .sort((a, b) => b.eleicao - a.eleicao);

  abas.querySelectorAll("button").forEach((b) => b.setAttribute("aria-selected", b.dataset.cargo === cargo));
  seletorLugar.hidden = cargo === "presidente";
  seletorLugar.setAttribute("aria-label", cargo === "prefeito" ? "Escolher município" : "Escolher estado");
  seletorLugar.innerHTML = lugaresDe(cargo).map(([k, nome]) => `<option value="${esc(k)}">${esc(nome)}</option>`).join("");
  seletorLugar.value = lugar;
  $("t-mandatos").textContent = `Por ${CARGO[cargo].singular}`;
  renderConsolidado(lista, cargo);

  seletorMandato.innerHTML = lista
    .map((m) => `<option value="${m.id}">${esc(m.nome)} (eleição de ${m.eleicao})</option>`)
    .join("");
  $("lista-mandatos").replaceChildren(cartoes.get(lista[0].id));
}

abas.addEventListener("click", (e) => {
  const cargo = e.target.dataset?.cargo;
  if (cargo) irPara(cargo);
});
seletorLugar.addEventListener("change", () => irPara(lerEndereco().cargo, seletorLugar.value));
seletorMandato.addEventListener("change", () => $("lista-mandatos").replaceChildren(cartoes.get(seletorMandato.value)));
window.addEventListener("hashchange", render);
$("consolidado").addEventListener("toggle", (e) => {
  if (e.target.matches?.("details.recolhe")) aberta[e.target.dataset.chave] = e.target.open;
}, true);
render();
