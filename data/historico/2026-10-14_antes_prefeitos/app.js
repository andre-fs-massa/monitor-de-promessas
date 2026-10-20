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
const CPPG = ["cumprida", "parcialmente_cumprida", "nao_cumprida"];

// Textos que mudam conforme o cargo
const CARGO = {
  presidente: { aba: "Presidência", plural: "presidentes", singular: "presidente", legislativo: "Congresso", legCurto: "Congresso" },
  governador: { aba: "Governos estaduais", plural: "governadores", singular: "governador", legislativo: "Legislativo estadual", legCurto: "Legislativo" },
};
const ESTADOS = {
  AC: "Acre", AL: "Alagoas", AP: "Amapá", AM: "Amazonas", BA: "Bahia", CE: "Ceará", DF: "Distrito Federal",
  ES: "Espírito Santo", GO: "Goiás", MA: "Maranhão", MT: "Mato Grosso", MS: "Mato Grosso do Sul", MG: "Minas Gerais",
  PA: "Pará", PB: "Paraíba", PR: "Paraná", PE: "Pernambuco", PI: "Piauí", RJ: "Rio de Janeiro", RN: "Rio Grande do Norte",
  RS: "Rio Grande do Sul", RO: "Rondônia", RR: "Roraima", SC: "Santa Catarina", SP: "São Paulo", SE: "Sergipe", TO: "Tocantins",
};

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
function blocoLegislativo(lista, cols, leg) {
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
      <div class="tabela-scroll"><table class="resp">
        <thead><tr><th>Grupo</th><th class="num">Promessas</th>${thTaxas(cols)}</tr></thead>
        <tbody>${linha(`Dependem do ${leg}`, dep)}${linha("Só do Executivo", lista.filter((p) => p.depende_legislativo !== "sim"))}</tbody>
      </table></div>
      ${notaOutroEnte(lista)}
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

function renderConsolidado(lista, cargo, uf) {
  const txt = CARGO[cargo];
  const daVez = promessas.filter((p) => lista.some((m) => m.id === p.mandato_id));
  const cols = colunasDe(daVez);
  const r = resumo(daVez);
  const emCurso = lista.filter((m) => m.situacao_mandato === "em_curso").length;
  const interrompidos = lista.filter((m) => m.situacao_mandato === "interrompido").length;

  $("t-consolidado").textContent =
    cargo === "presidente" ? "Consolidado dos presidentes" : `Consolidado dos governadores · ${ESTADOS[uf]}`;
  $("nota-consolidado").textContent =
    `${lista.length} ${lista.length === 1 ? txt.singular : txt.plural} analisado(s), ${r.total} promessas testáveis no total.` +
    (emCurso ? ` ${emCurso} mandato(s) ainda em curso: os números mudam até o fim do mandato.` : "") +
    (interrompidos ? ` ${interrompidos} mandato(s) encerrado(s) antes do prazo, avaliado(s) até a data de saída.` : "");
  $("kpis-consolidado").innerHTML = kpis(cols, r);
  $("barra-consolidado").innerHTML = barra(r) + blocoLegislativo(daVez, cols, txt.legislativo);

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
  $("comparativo").innerHTML = `
    <thead><tr><th>${txt.singular[0].toUpperCase() + txt.singular.slice(1)}</th><th>Mandato</th><th class="num">Promessas</th><th class="num">Dependem do ${txt.legislativo}</th>${thTaxas(cols)}</tr></thead>
    <tbody>${linhas.join("")}</tbody>`;
}

function linhaPromessa(p, leg) {
  const fonte = p.fonte_url ? `<a href="${esc(p.fonte_url)}" target="_blank" rel="noopener">fonte</a>` : "";
  return `<tr>
    <td><div>${esc(p.promessa)}</div><div class="trecho">${local(p)}: “${esc(p.trecho_literal)}”</div></td>
    <td>${esc(p.area)}</td>
    <td><span class="chip"><i class="ponto" style="background:${COR[p.status]}"></i>${ROTULO[p.status]}</span>
      <div class="conf">${CONF[p.confianca]}</div>
      ${p.depende_legislativo === "sim" ? `<span class="tag-congresso">Depende do ${leg}</span>` : ""}
      ${p.outro_ente ? `<span class="tag-ente" title="A execução cabe por lei a outro ente federativo">Competência: ${esc(p.outro_ente)}</span>` : ""}</td>
    <td class="evid">${esc(p.evidencia)} ${fonte}</td>
  </tr>`;
}

// "competencia" é derivado de outro_ente; os demais filtros usam o próprio campo
const valorFiltro = (p, campo) => (campo === "competencia" ? (p.outro_ente ? "outro" : "propria") : p[campo]);

function renderMandato(m) {
  const leg = CARGO[m.cargo].legislativo;
  const lista = doMandato(m);
  const cols = colunasDe(lista);
  const r = resumo(lista);
  const areas = [...new Set(lista.map((x) => x.area))].sort();
  const situacao = {
    em_curso: `Mandato em curso · dados até ${fmtData(m.data_corte)}`,
    encerrado: "Mandato encerrado",
    interrompido: `Mandato interrompido (${m.motivo_interrupcao}) em ${fmtData(m.mandato_fim_efetivo || "")} · avaliado até essa data`,
  }[m.situacao_mandato];
  const onde = m.cargo === "governador" ? ` · ${ESTADOS[m.uf]}` : "";

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
      <p class="meta">Plano: <a href="${esc(m.url_tse)}">${esc(m.arquivo_plano)}</a> (TSE, dados abertos)</p>
      <div class="filtros">
        <select data-f="status" aria-label="Filtrar por status"><option value="">Todos os status</option>
          ${ORDEM.filter((s) => r.cont[s]).map((s) => `<option value="${s}">${ROTULO[s]} (${r.cont[s]})</option>`).join("")}</select>
        <select data-f="area" aria-label="Filtrar por área"><option value="">Todas as áreas</option>
          ${areas.map((a) => `<option>${esc(a)}</option>`).join("")}</select>
        <select data-f="depende_legislativo" aria-label="Filtrar por dependência do ${leg}"><option value="">Com e sem ${CARGO[m.cargo].legCurto}</option>
          <option value="sim">Dependem do ${CARGO[m.cargo].legCurto}</option><option value="nao">Só do Executivo</option></select>
        ${lista.some((x) => x.outro_ente) ? `<select data-f="competencia" aria-label="Filtrar por competência"><option value="">Qualquer competência</option>
          <option value="propria">Competência própria</option><option value="outro">Competência de outro ente</option></select>` : ""}
      </div>
      <div class="tabela-scroll">
        <table class="promessas"><thead><tr><th>Promessa</th><th>Área</th><th>Status</th><th>Evidência</th></tr></thead><tbody></tbody></table>
      </div>
    </article>`);

  const tbody = card.querySelector("table.promessas tbody");
  const filtros = card.querySelectorAll(".filtros select");
  const atualizar = () => {
    const f = Object.fromEntries([...filtros].map((s) => [s.dataset.f, s.value]));
    tbody.innerHTML = lista
      .filter((x) => Object.entries(f).every(([campo, valor]) => !valor || valorFiltro(x, campo) === valor))
      .map((x) => linhaPromessa(x, leg))
      .join("");
  };
  filtros.forEach((s) => s.addEventListener("change", atualizar));
  atualizar();
  return card;
}

// Cartões criados uma vez, para preservar filtros ao alternar
const cartoes = new Map(mandatos.map((m) => [m.id, renderMandato(m)]));
const ufsGov = [...new Set(mandatos.filter((m) => m.cargo === "governador").map((m) => m.uf))]
  .sort((a, b) => ESTADOS[a].localeCompare(ESTADOS[b]));

const abas = $("abas-cargo");
const seletorUf = $("seletor-uf");
const seletorMandato = $("seletor-mandato");
abas.innerHTML = Object.entries(CARGO)
  .filter(([c]) => mandatos.some((m) => m.cargo === c))
  .map(([c, t]) => `<button type="button" role="tab" data-cargo="${c}">${t.aba}</button>`)
  .join("");
seletorUf.innerHTML = ufsGov.map((uf) => `<option value="${uf}">${ESTADOS[uf]}</option>`).join("");

// Estado da página vem do endereço: #presidencia ou #governadores/RJ
function lerEndereco() {
  const [rota, uf] = location.hash.slice(1).split("/");
  if (rota === "governadores" && ufsGov.length) return { cargo: "governador", uf: ufsGov.includes(uf) ? uf : ufsGov[0] };
  return { cargo: "presidente", uf: "BR" };
}

function render() {
  const { cargo, uf } = lerEndereco();
  const lista = mandatos
    .filter((m) => m.cargo === cargo && (cargo === "presidente" || m.uf === uf))
    .sort((a, b) => b.eleicao - a.eleicao);

  abas.querySelectorAll("button").forEach((b) => b.setAttribute("aria-selected", b.dataset.cargo === cargo));
  seletorUf.hidden = cargo !== "governador";
  seletorUf.value = uf;
  $("t-mandatos").textContent = `Por ${CARGO[cargo].singular}`;
  renderConsolidado(lista, cargo, uf);

  seletorMandato.innerHTML = lista
    .map((m) => `<option value="${m.id}">${esc(m.nome)} (eleição de ${m.eleicao})</option>`)
    .join("");
  $("lista-mandatos").replaceChildren(cartoes.get(lista[0].id));
}

abas.addEventListener("click", (e) => {
  const cargo = e.target.dataset?.cargo;
  if (cargo) location.hash = cargo === "governador" ? `governadores/${seletorUf.value || ufsGov[0]}` : "presidencia";
});
seletorUf.addEventListener("change", () => (location.hash = `governadores/${seletorUf.value}`));
seletorMandato.addEventListener("change", () => $("lista-mandatos").replaceChildren(cartoes.get(seletorMandato.value)));
window.addEventListener("hashchange", render);
render();
