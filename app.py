# app.py
# Streamlit – Diseño de Estructuras de Concreto (modo claro + edición avanzada de Ab y As)
import math
import io
from decimal import Decimal, getcontext
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# === Precisión alta para áreas ===
getcontext().prec = 28  # precisión alta para mm y mm²

st.set_page_config(page_title="Concreto - Hoja rápida", layout="wide")

# ======= MODO CLARO + estilos (incluye AG Grid del data_editor) =======
st.markdown("""
<style>
/* === Arreglo títulos/labels y stepper de NumberInput === */

/* 1) Títulos (labels) bien visibles */
[data-testid="stNumberInput"] label,
[data-testid="stSelectbox"] label,
[data-testid="stTextInput"] label,
[data-testid="stRadio"] > div > label {
  color:#0f172a !important;
  font-weight:700 !important;
  opacity:1 !important;
}

/* 2) Caja del input (texto) clara */
[data-testid="stNumberInput"] input {
  background:#ffffff !important;
  color:#111827 !important;
  border:1px solid #e5e7eb !important;
}

/* 3) Panel derecho de – / + claro (BaseWeb stepper) */
[data-testid="stNumberInput"] > div > div:last-child {
  background:#ffffff !important;
  border:1px solid #e5e7eb !important;
  border-left:none !important;        /* que se vea unido a la caja */
  border-radius:0 10px 10px 0 !important;
}

/* 4) Botoncitos – / + claros */
[data-testid="stNumberInput"] button {
  background:#ffffff !important;
  color:#111827 !important;
  border:none !important;
  box-shadow:none !important;
}

/* 5) Estados hover/focus */
[data-testid="stNumberInput"] input:focus {
  outline:none !important;
  box-shadow:0 0 0 2px rgba(59,130,246,.25) !important;  /* azul suave */
  border-color:#93c5fd !important;
}
[data-testid="stNumberInput"] button:hover {
  background:#f9fafb !important;
}

/* 6) Captions/ayudas bajo los labels más legibles */
small, .stCaption, .st-emotion-cache-1y4p8pa {
  color:#495266 !important;
  opacity:1 !important;
}
/* === Botón Browse files claro === */
[data-testid="stFileUploaderDropzone"] button {
  background:#ffffff !important;
  color:#111827 !important;
  border:1px solid #e5e7eb !important;
  border-radius:6px !important;
  padding:6px 14px !important;
  font-weight:500 !important;
}
[data-testid="stFileUploaderDropzone"] button:hover {
  background:#f9fafb !important;
  border-color:#cbd5e1 !important;
}

/* Base claro */
html, body, .stApp { background:#ffffff !important; color:#111827 !important; }
html { color-scheme: light !important; }
.block-container, [data-testid="stHeader"], [data-testid="stToolbar"] {
  background:#ffffff !important; color:#111827 !important;
}
/* =======================
   FIX DEFINITIVO DATA EDITOR (AG Grid) EN BLANCO
   ======================= */

/* 1) Fuerza variables de color incluso si Streamlit aplica su tema oscuro */
[data-testid="stDataEditor"] .ag-theme-streamlit-light,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark {
  --ag-background-color:#ffffff !important;
  --ag-foreground-color:#111827 !important;
  --ag-border-color:#e5e7eb !important;
  --ag-header-background-color:#f3f4f6 !important;
  --ag-header-foreground-color:#111827 !important;
  --ag-odd-row-background-color:#fafafa !important;
  --ag-even-row-background-color:#ffffff !important;
  --ag-selected-row-background-color:#fee2e2 !important;
  --ag-input-focus-border-color:#93c5fd !important;
}

/* 2) Aplica fondo/colores a todo el wrapper y subcapas (gana a las reglas del tema) */
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-root-wrapper,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-root-wrapper,
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-root,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-root,
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-header,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-header,
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-header-viewport,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-header-viewport,
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-body,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-body,
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-body-viewport,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-body-viewport,
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-center-cols-container,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-center-cols-container,
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-row,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-row,
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-cell,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-cell {
  background:#ffffff !important;
  color:#111827 !important;
  border-color:#e5e7eb !important;
}

/* 3) Encabezado y zebra */
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-header,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-header {
  background:#f3f4f6 !important;
  color:#111827 !important;
  border-bottom:1px solid #e5e7eb !important;
}
[data-testid="stDataEditor"] .ag-theme-streamlit-light .ag-row.ag-row-odd .ag-cell,
[data-testid="stDataEditor"] .ag-theme-streamlit-dark  .ag-row.ag-row-odd .ag-cell {
  background:#fafafa !important;
}

/* 4) Botón "Browse files" claro (por si no lo tomaba) */
[data-testid="stFileUploaderDropzone"] button{
  background:#ffffff !important;
  color:#111827 !important;
  border:1px solid #e5e7eb !important;
}
[data-testid="stFileUploaderDropzone"] button:hover{
  background:#f9fafb !important;
}

/* 5) Labels/títulos de inputs siempre legibles */
[data-testid="stNumberInput"] label,
[data-testid="stSelectbox"]  label,
[data-testid="stTextInput"]  label,
[data-testid="stRadio"] > div > label {
  color:#0f172a !important;
  font-weight:700 !important;
  opacity:1 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
  width:280px !important; background:#fafafa !important; color:#111827 !important;
  border-right:1px solid #f1f5f9 !important;
}
section[data-testid="stSidebar"] * { color:#111827 !important; }
section[data-testid="stSidebar"] .stMarkdown small,
section[data-testid="stSidebar"] .st-emotion-cache-12ttj6m { color:#334155 !important; }

/* Inputs/selects (blancos) */
input, textarea, select, .stNumberInput input, .stTextInput input {
  background:#ffffff !important; color:#111827 !important; border:1px solid #e5e7eb !important;
}
.stSelectbox [data-baseweb="select"] div {
  background:#ffffff !important; color:#111827 !important; border-color:#e5e7eb !important;
}
.stSelectbox [data-baseweb="select"] svg { color:#111827 !important; }

/* Radios y labels con contraste (evita "apagados") */
.stRadio label, .stRadio [role="radiogroup"] * { color:#111827 !important; opacity:1 !important; }

/* Tabs (navegación visible) */
.stTabs [data-baseweb="tab-list"]{
  background:#ffffff !important; border-bottom:1px solid #e5e7eb !important; padding-bottom:2px !important;
}
.stTabs [data-baseweb="tab"]{
  color:#1f2937 !important; opacity:1 !important; font-weight:600 !important; padding:10px 14px !important;
}
.stTabs [role="tab"][aria-selected="true"]{
  color:#0f172a !important; font-weight:800 !important;
}
.stTabs [data-baseweb="tab-highlight"]{ background:#ef4444 !important; height:2px !important; }

/* Caption/ayudas con mejor legibilidad */
small, .stCaption, .stMarkdown p[style*="font-size: 0.8rem"],
.st-emotion-cache-16idsys, .st-emotion-cache-1y4p8pa {
  color:#4b5563 !important;
}

/* File Uploader claro */
[data-testid="stFileUploaderDropzone"]{
  background:#ffffff !important; color:#111827 !important;
  border:1px dashed #e5e7eb !important; border-radius:12px !important;
}
[data-testid="stFileUploaderDropzone"] *{ color:#111827 !important; }

/* Tablas (st.table) claras + bordes + encabezado gris */
[data-testid="stTable"] table { border-collapse:collapse !important; width:100%; }
[data-testid="stTable"] th{
  background:#f3f4f6 !important; color:#111827 !important;
  border:1px solid #e5e7eb !important; font-weight:700 !important;
}
[data-testid="stTable"] td{
  background:#ffffff !important; color:#111827 !important; border:1px solid #e5e7eb !important;
}

/* ===== Data Editor (AG Grid) – CLARO real ===== */
[data-testid="stDataEditor"] .ag-root-wrapper{
  --ag-background-color:#ffffff;
  --ag-foreground-color:#111827;
  --ag-border-color:#e5e7eb;
  --ag-header-background-color:#f3f4f6;
  --ag-header-foreground-color:#111827;
  --ag-odd-row-background-color:#fafafa;
  --ag-even-row-background-color:#ffffff;
  --ag-input-border-color:#e5e7eb;
}
/* Captions globales bien visibles (incluye los de cuerpo y sidebar) */
[data-testid="stCaption"],            /* versiones nuevas */
[data-testid="stCaptionContainer"],   /* fallback */
.stCaption,                           /* alias */
.stMarkdown p[style*="font-size: 0.8rem"],
small {
  color:#0f172a !important;     /* azul oscuro legible */
  opacity:1 !important;         /* sin transparencia */
}

/* Si quieres que además lleve una pastilla clara detrás */
.caption-chip {
  display:inline-block;
  color:#0f172a; 
  background:#eff6ff;           /* azul muy clarito */
  border:1px solid #bfdbfe;     /* borde sutil */
  padding:6px 10px; 
  border-radius:8px; 
  font-size:0.90rem; 
  font-weight:600;
}
[data-testid="stDataEditor"] .ag-root-wrapper,
[data-testid="stDataEditor"] .ag-root,
[data-testid="stDataEditor"] .ag-header,
[data-testid="stDataEditor"] .ag-header-viewport,
[data-testid="stDataEditor"] .ag-body,
[data-testid="stDataEditor"] .ag-body-viewport,
[data-testid="stDataEditor"] .ag-center-cols-container,
[data-testid="stDataEditor"] .ag-row,
[data-testid="stDataEditor"] .ag-cell{
  background:var(--ag-background-color) !important;
  color:var(--ag-foreground-color) !important;
  border-color:var(--ag-border-color) !important;
}
[data-testid="stDataEditor"] .ag-header { background:var(--ag-header-background-color) !important; }
[data-testid="stDataEditor"] .ag-row.ag-row-odd .ag-cell{ background:var(--ag-odd-row-background-color) !important; }
[data-testid="stDataEditor"] .ag-row.ag-row-even .ag-cell{ background:var(--ag-even-row-background-color) !important; }

/* Botones */
.stButton>button, .stDownloadButton>button{
  color:#111827 !important; background:#ffffff !important; border:1px solid #e5e7eb !important; border-radius:8px !important;
}
.stButton>button:hover, .stDownloadButton>button:hover{ background:#f9fafb !important; }

/* Títulos */
h1, h2, h3 { color:#0f172a !important; font-weight:800 !important; }

/* Tarjeta informativa clara */
.card-info{
  background:#eaf3ff; border:1px solid #bfdbfe; color:#0f172a; border-radius:12px; padding:14px 16px;
}
.card-info b{ color:#0f172a; }
</style>
""", unsafe_allow_html=True)

# === Matplotlib claro ===
plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "text.color": "black",
    "axes.labelcolor": "black",
    "xtick.color": "black",
    "ytick.color": "black",
})

# ========================= Utilidades =========================
PI_D = Decimal(str(math.pi))

def area_exacta_mm2(d_mm: float) -> float:
    d = Decimal(str(d_mm))
    return float((PI_D * d * d) / Decimal(4))

def diametro_desde_area_mm(Ab_mm2: float) -> float:
    Ab = Decimal(str(Ab_mm2))
    return float(((Decimal(4)*Ab)/PI_D).sqrt())

def fmt(x, nd=3):
    try:
        xv = float(x)
        if math.isnan(xv) or math.isinf(xv):
            return "–"
    except:
        return "–"
    s = f"{xv:,.{nd}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def calc_Ec(fc_mpa: float, metodo: int, wc_kg_m3):
    if metodo == 1:
        try:
            wc = float(wc_kg_m3)
            if 1440 <= wc <= 2560:
                return 0.043 * (wc**1.5) * math.sqrt(max(fc_mpa, 0.0))
        except:
            pass
    return 4700.0 * math.sqrt(max(fc_mpa, 0.0))

# —— Tablas bonitas (zebra) ——
def zebra_rows(df: pd.DataFrame):
    return pd.DataFrame(
        [["background-color: #ffffff" if i % 2 == 0 else "background-color: #f9fafb" for _ in df.columns]
         for i in range(len(df))],
        columns=df.columns
    )
def pretty_table(df: pd.DataFrame, right_cols=None, precision=3):
    sty = (df.style
           .format({c: f"{{:,.{precision}f}}" for c in df.select_dtypes('number').columns})
           .set_table_styles([
               {'selector': 'th', 'props': [('background', '#f3f4f6'),
                                            ('color', '#111827'),
                                            ('border', '1px solid #e5e7eb'),
                                            ('font-weight', '700')]},
               {'selector': 'td', 'props': [('border', '1px solid #e5e7eb'),
                                            ('color', '#111827')]},
           ], overwrite=False)
           .apply(zebra_rows, axis=None)
          )
    if right_cols:
        sty = sty.set_properties(subset=right_cols, **{'text-align': 'right'})
    return sty

# ========================= Estado inicial =========================
default_bars = pd.DataFrame({
    "Barra":  [3, 4, 5, 6, 7, 8, 9, 10],
    "d_mm":   [9.525, 12.70, 15.875, 19.05, 22.225, 25.40, 28.575, 31.75],
})
default_bars["Ab_mm2"] = default_bars["d_mm"].apply(area_exacta_mm2)

if "bars_df" not in st.session_state:
    st.session_state.bars_df = default_bars.copy()

if "inputs" not in st.session_state:
    st.session_state.inputs = dict(
        bx=300.0, by=400.0, r=40.0,
        fc=21.0, fy=420.0, Es=200_000.0,
        metodoEc=2, wc=None,
        N=3, barra=5,
        sigma_elast=10.5, sigma_fis=2.1,
        usar_area_limites="Ac",
        Ab_override=None,
        As_override=None,
    )

# ========================= Import/Export =========================
def normalize_catalog_df(df: pd.DataFrame) -> pd.DataFrame:
    barra_col = None; d_col = None; ab_col = None
    for c in df.columns:
        n = str(c).lower()
        if barra_col is None and ("barra" in n or n.strip() in ("#", "no", "nro", "número", "numero")): barra_col = c
        if d_col is None and ("diam" in n or "d_mm" in n or "diametro" in n): d_col = c
        if ab_col is None and ("ab" in n or "area" in n or "área" in n): ab_col = c
    if barra_col is None: raise ValueError("El archivo debe contener columna de 'Barra'.")
    out = pd.DataFrame({"Barra": df[barra_col].astype(int)})
    if ab_col is not None:
        out["Ab_mm2"] = pd.to_numeric(df[ab_col], errors="coerce")
        out["d_mm"] = out["Ab_mm2"].apply(lambda x: diametro_desde_area_mm(x) if pd.notna(x) else None)
    if d_col is not None:
        dvals = pd.to_numeric(df[d_col], errors="coerce")
        out["d_mm"] = out.get("d_mm", dvals).fillna(dvals)
    out["Ab_mm2"] = out["d_mm"].apply(area_exacta_mm2)
    return out.dropna(subset=["d_mm"]).sort_values("Barra").reset_index(drop=True)

def apply_inputs_df(df_inputs: pd.DataFrame):
    if df_inputs.shape[1] < 2: return
    col_param, col_val = df_inputs.columns[:2]
    for _, row in df_inputs.iterrows():
        key = str(row[col_param]).strip()
        if key in st.session_state.inputs:
            val = row[col_val]
            try:
                if key in ("N","barra","metodoEc"): st.session_state.inputs[key] = int(val)
                else: st.session_state.inputs[key] = float(val)
            except: pass

def sidebar_import_export_ui():
    up = st.sidebar.file_uploader("Cargar (.xlsx, .xls, .csv)", type=["xlsx","xls","csv"])
    if up is not None:
        try:
            if up.name.lower().endswith(".csv"):
                df = pd.read_csv(up); st.session_state.bars_df = normalize_catalog_df(df)
            else:
                xls = pd.ExcelFile(up)
                hoja_barras = next((nm for nm in xls.sheet_names if any(k in nm.lower() for k in ("barra","refuerzo","catalog"))), xls.sheet_names[0])
                df_b = pd.read_excel(xls, sheet_name=hoja_barras)
                st.session_state.bars_df = normalize_catalog_df(df_b)
                hoja_inputs = next((nm for nm in xls.sheet_names if any(k in nm.lower() for k in ("input","param"))), None)
                if hoja_inputs: apply_inputs_df(pd.read_excel(xls, sheet_name=hoja_inputs))
            st.sidebar.success("Archivo cargado.")
        except Exception as e:
            st.sidebar.error(f"Error al importar: {e}")

    if st.sidebar.button("💾 Exportar a Excel"):
        def build_inputs_df():
            keys = ("bx","by","r","fc","fy","Es","metodoEc","wc","N","barra",
                    "sigma_elast","sigma_fis","usar_area_limites","Ab_override","As_override")
            return pd.DataFrame([(k, st.session_state.inputs.get(k)) for k in keys], columns=["param","valor"])
        buff = io.BytesIO()
        with pd.ExcelWriter(buff, engine="xlsxwriter") as wr:
            st.session_state.bars_df[["Barra","d_mm","Ab_mm2"]].to_excel(wr, index=False, sheet_name="barras")
            build_inputs_df().to_excel(wr, index=False, sheet_name="inputs")
        st.sidebar.download_button("Descargar concreto_config.xlsx", data=buff.getvalue(),
                                   file_name="concreto_config.xlsx",
                                   mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# ========================= Sidebar =========================
with st.sidebar:
    st.markdown("### Diseño")
    choice = st.radio("Navegación", options=["Diseño", "Parámetros de Acero de Refuerzo"], index=0)
    st.markdown("#### Importar / Exportar")
    sidebar_import_export_ui()

# ========================= Páginas =========================
def page_catalogo():
    st.subheader("Parámetros de Acero de Refuerzo (Catálogo)")
    st.caption("Edita **Diámetro (mm)** o **Abarra (mm²)**; el otro campo se recalcula automáticamente. Ab = π·d²/4 (exacto).")
    df = st.session_state.bars_df.copy()
    edited = st.data_editor(
        df,
        column_config={
            "Barra":  st.column_config.NumberColumn(format="%d", step=1),
            "d_mm":   st.column_config.NumberColumn("Diámetro (mm)", format="%.6f", step=0.001),
            "Ab_mm2": st.column_config.NumberColumn("Abarra (mm²)", format="%.6f", step=0.001),
        },
        hide_index=True, use_container_width=True, key="bars_editor_page", height=380
    )
    # reconciliar d <-> Ab
    def reconcile(row):
        d_old, ab_old = row["d_mm"], row["Ab_mm2"]
        ab_from_d = area_exacta_mm2(d_old)
        d_from_ab = diametro_desde_area_mm(ab_old)
        if abs(ab_old - ab_from_d) > abs(d_old - d_from_ab):
            d_new = d_from_ab; ab_new = area_exacta_mm2(d_new)
        else:
            d_new = d_old; ab_new = ab_from_d
        return pd.Series({"d_mm": d_new, "Ab_mm2": ab_new})
    edited[["d_mm","Ab_mm2"]] = edited.apply(reconcile, axis=1)
    st.session_state.bars_df = edited.sort_values("Barra").reset_index(drop=True)

def page_diseno():
    st.title("DISEÑO DE ESTRUCTURAS DE CONCRETO")

    # ----- Tabs de parámetros
    tab_sec, tab_mat, tab_ref, tab_lim = st.tabs(["Sección", "Materiales", "Refuerzo", "Límites / Ec"])

    with tab_sec:
        c1, c2, c3 = st.columns(3)
        bx = c1.number_input("bx (mm)", value=float(st.session_state.inputs["bx"]), step=1.0)
        by = c2.number_input("by (mm)", value=float(st.session_state.inputs["by"]), step=1.0)
        r  = c3.number_input("r (mm) recubrimiento inferior", value=float(st.session_state.inputs["r"]), step=1.0)

    with tab_mat:
        c1, c2, c3 = st.columns(3)
        fc = c1.number_input("f'c (MPa)", value=float(st.session_state.inputs["fc"]), step=0.1)
        fy = c2.number_input("fy (MPa)",  value=float(st.session_state.inputs["fy"]), step=1.0)
        Es = c3.number_input("Es (MPa)",  value=float(st.session_state.inputs["Es"]), step=100.0)

    with tab_ref:
        c1, c2, c3 = st.columns(3)
        N  = c1.number_input("Número de barras N", value=int(st.session_state.inputs["N"]), min_value=1, step=1)
        barra_list = st.session_state.bars_df["Barra"].astype(int).tolist()
        barra = c2.selectbox("Barra (catálogo)", options=barra_list,
                             index=max(0, barra_list.index(int(st.session_state.inputs["barra"]))
                                       if int(st.session_state.inputs["barra"]) in barra_list else 0))
        allow_adv = c3.toggle("Edición avanzada Ab/As", value=False, help="Permite sobreescribir Ab (Abarra) y As manualmente.")

        bars_df = st.session_state.bars_df
        row_sel = bars_df[bars_df["Barra"] == barra]
        if row_sel.empty: row_sel = bars_df.iloc[[0]]
        d_mm_cat = float(row_sel["d_mm"].iloc[0]); Ab_cat = float(row_sel["Ab_mm2"].iloc[0])

        if allow_adv:
            Ab_override = st.number_input("Abarra (mm²)", value=float(st.session_state.inputs.get("Ab_override") or Ab_cat),
                                          step=0.001, format="%.6f")
            d_from_override = diametro_desde_area_mm(Ab_override)
            st.text_input("Diámetro derivado (mm)", value=f"{d_from_override:.6f}", disabled=True)
            As_override = st.number_input("As (mm²)", value=float(st.session_state.inputs.get("As_override") or Ab_cat*N),
                                          step=0.001, format="%.6f")
            N_sugerido = max(1, int(round(As_override / Ab_override))) if Ab_override > 0 else N
            st.caption(f"Sugerencia N≈As/Ab = **{N_sugerido}**")
            st.session_state.inputs["Ab_override"] = Ab_override
            st.session_state.inputs["As_override"] = As_override
            Ab_sel, As_sel, d_mm_sel = Ab_override, As_override, d_from_override
        else:
            st.session_state.inputs["Ab_override"] = None
            st.session_state.inputs["As_override"] = None
            Ab_sel, As_sel, d_mm_sel = Ab_cat, Ab_cat * N, d_mm_cat

        # Tarjeta clara con texto oscuro (Abarra/As bien visibles)
        st.markdown(f"""
        <div class="card-info">
          <div style="font-weight:700;margin-bottom:6px">🔩 Refuerzo</div>
          <div>- <b>Barra:</b> #{barra}</div>
          <div>- <b>Diámetro:</b> {d_mm_sel:.6f} mm</div>
          <div>- <b>Abarra (Ab):</b> {Ab_sel:.6f} mm²</div>
          <div>- <b>As (N·Ab):</b> {As_sel:.6f} mm²</div>
        </div>
        """, unsafe_allow_html=True)

    with tab_lim:
        st.markdown("**Módulo de Elasticidad (Ec)** – Selecciona el método")
        metodoEc = st.radio("Método",
                            options=[1,2],
                            format_func=lambda m: "Método 1 (con densidad wc: Ec = 0.043·wc^1.5·√f'c)" if m==1
                                                 else "Método 2 (Concreto normal: Ec = 4700·√f'c)",
                            index=1 if st.session_state.inputs["metodoEc"]==2 else 0)
        wc = None
        if metodoEc == 1:
            wc = st.number_input("wc (kg/m³) – válido 1440 a 2560",
                                 value=float(st.session_state.inputs["wc"] or 0.0), step=1.0)
        c1, c2, c3 = st.columns(3)
        sigma_elast = c1.number_input("Límite elástico σc (MPa)", value=float(st.session_state.inputs["sigma_elast"]), step=0.1)
        sigma_fis   = c2.number_input("Límite de fisuración fr (MPa)", value=float(st.session_state.inputs["sigma_fis"]), step=0.1)
        usar_area_limites = c3.selectbox("Área para Le/Lf", options=["Ac","Ag"], index=0 if st.session_state.inputs["usar_area_limites"]=="Ac" else 1)

    # Persistir
    st.session_state.inputs.update(dict(
        bx=bx, by=by, r=r, fc=fc, fy=fy, Es=Es,
        metodoEc=metodoEc, wc=wc if metodoEc==1 else None,
        N=N, barra=barra, sigma_elast=sigma_elast, sigma_fis=sigma_fis,
        usar_area_limites=usar_area_limites
    ))

    # ----- Cálculos base -----
    Ag = bx * by
    Ec = calc_Ec(fc, metodoEc, st.session_state.inputs["wc"])
    n  = Es / Ec if Ec > 0 else float("nan")

    Ab, As, d_mm = Ab_sel, As_sel, d_mm_sel
    Ac = max(0.0, Ag - As)
    area_lim = Ac if usar_area_limites == "Ac" else Ag
    Pn = 0.85 * fc * Ac + As * fy
    Le = sigma_elast * area_lim
    Lf = sigma_fis   * area_lim

    # ----- Output + Croquis -----
    colL, colR = st.columns([0.9, 1.1], gap="large")
    with colL:
        st.subheader("Output")
        df_out = pd.DataFrame({"Magnitud": ["Ec (MPa)", "n", "Ag (mm²)", "Ac (mm²)", "Abarra (mm²)", "As (mm²)"],
                               "Valor":    [Ec, n, Ag, Ac, Ab, As]})
        st.table(pretty_table(df_out, right_cols=["Valor"], precision=6))

        st.subheader("Refuerzo de Acero")
        df_ref = pd.DataFrame({"Nro. Barras":[int(N)], "Barra":[f"#{barra}"],
                               "Diámetro":[f"{d_mm:.6f} mm"], "Abarra":[f"{Ab:.6f} mm²"], "As":[f"{As:.6f} mm²"]})
        st.table(pretty_table(df_ref))

    with colR:
        st.subheader("Croquis (con dimensiones)")
        fig, ax = plt.subplots(figsize=(6.8, 5.0))
        ax.add_patch(plt.Rectangle((0, 0), bx, by, fill=False))
        ax.annotate(f"bx = {fmt(bx,0)} mm", (bx/2, -by*0.07), ha="center", va="top")
        ax.annotate(f"by = {fmt(by,0)} mm", (bx*1.04, by/2), rotation=90, va="center")
        ySteel = r
        ax.plot([r, bx-r], [ySteel, ySteel], lw=2)
        ax.plot([bx-r, bx-r], [0, ySteel], lw=2)
        ax.text(bx-r + bx*0.02, ySteel/2, f"r = {fmt(r,0)} mm", va="center")
        freeW = max(0.0, bx - 2*r); spacing = freeW/(max(1, N-1)) if N > 1 else 0.0
        rad = max(3.0, min(14.0, d_mm/2.0))
        xs = [r + (i*spacing if N > 1 else freeW/2.0) for i in range(N)]
        for x in xs: ax.add_patch(plt.Circle((x, ySteel), rad, fill=True, alpha=0.4))
        ax.set_xlim(-bx*0.12, bx*1.25); ax.set_ylim(-by*0.18, by*1.08)
        ax.set_aspect("equal", adjustable="box"); ax.axis("off")
        st.pyplot(fig, use_container_width=True)

    st.markdown("---")

    # ----- CASO 1 -----
    y_s = r + d_mm/2.0; d_eff = by - y_s
    n_val = n if (not math.isnan(n)) and n > 0 else 0.0
    As_tr = (n_val - 1.0) * As; AT = Ag + As_tr
    y_bar = (Ag*(by/2.0) + As_tr*y_s) / AT if AT > 0 else float("nan")
    Ig = (bx * (by**3)) / 12.0
    I_conc = Ig + Ag * (y_bar - by/2.0)**2; I_acero = As_tr * (y_bar - y_s)**2; IT = I_conc + I_acero
    Mfis_Nmm = st.session_state.inputs["sigma_fis"] * IT / y_bar if y_bar and y_bar > 0 else float("nan"); Mfis_kNm = Mfis_Nmm / 1e6
    df_c1 = pd.DataFrame({"Cálculo":["A_T (mm²)","y (mm)","I_T (mm⁴)","M_fisurado (kN·m)"], "Valor":[AT, y_bar, IT, Mfis_kNm]})

    # ----- CASO 2 -----
    rho = As / (bx*d_eff) if bx*d_eff > 0 else float("nan")
    k   = (math.sqrt((n_val*rho)**2 + 2.0*n_val*rho) - n_val*rho) if not (math.isnan(rho) or math.isnan(n_val)) else float("nan")
    j   = 1.0 - k/3.0 if not math.isnan(k) else float("nan")
    Melast_Nmm = 0.5 * st.session_state.inputs["sigma_elast"] * bx * k * j * (d_eff**2) if not any(map(math.isnan,[k,j])) else float("nan")
    Melast_kNm = Melast_Nmm / 1e6 if Melast_Nmm is not None else float("nan")
    df_c2 = pd.DataFrame({"Cálculo":["d (mm)","ρ = As/(b·d)","k","j","M_rango elástico (kN·m)"],
                          "Valor":[d_eff, rho, k, j, Melast_kNm]})

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Caso 1 – Sin presentar fisuras en la zona a tracción")
        st.table(pretty_table(df_c1, right_cols=["Valor"], precision=6))
        st.subheader("Caso 2 – Sin superar el rango lineal a compresión")
        st.table(pretty_table(df_c2, right_cols=["Valor"], precision=6))
    with c2:
        st.subheader("Resultados de Resistencia")
        df_res = pd.DataFrame({
            "Concepto": ["Pn = 0.85 f'c Ac + As·fy", "Pn (N)", "Pn (kN)",
                         f"Le = σc_elast · {st.session_state.inputs['usar_area_limites']}", "Le (N)", "Le (kN)",
                         f"Lf = fr · {st.session_state.inputs['usar_area_limites']}", "Lf (N)", "Lf (kN)"],
            "Valor": ["", Pn, Pn/1000.0, "", Le, Le/1000.0, "", Lf, Lf/1000.0]
        })
        st.table(pretty_table(df_res, right_cols=["Valor"], precision=6))

    st.caption("Unidades: f'c, fy y Es en MPa; áreas en mm²; 1 MPa = 1 N/mm². Cálculo de áreas con alta precisión (Decimal).")

# ========================= Router =========================
if choice == "Parámetros de Acero de Refuerzo":
    page_catalogo()
else:
    page_diseno()
