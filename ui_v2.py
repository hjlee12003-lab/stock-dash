from __future__ import annotations

import html
import streamlit as st


NAV_ITEMS = [
    ("홈", "⌂"),
    ("시장 현황", "▥"),
    ("종목 분석", "◫"),
    ("공시 분석", "▤"),
    ("테마 & 섹터", "◇"),
    ("포트폴리오", "▣"),
    ("관심 종목", "☆"),
    ("AI 인사이트", "✦"),
    ("데이터 연결 관리", "⚙"),
]


def apply_theme():
    st.markdown(
        """
<style>
:root {
  --bg:#061526; --bg-deep:#04101d; --panel:#0a2035; --panel-2:#0d2943;
  --line:#1b4262; --text:#f4f8ff; --muted:#9eb6cf; --blue:#2186f6;
  --blue-soft:#123b64; --green:#29d68b; --cyan:#35c9ff; --red:#ff5360; --amber:#ffb53d;
}
html, body, [class*="css"] {
  font-family:Pretendard,"Noto Sans KR","Apple SD Gothic Neo",sans-serif;
  color:var(--text);
}
.stApp {
  background:
    radial-gradient(circle at 62% -10%, rgba(26,92,148,.18), transparent 38%),
    linear-gradient(145deg,var(--bg-deep),var(--bg));
  color:var(--text);
}
.block-container { max-width:1540px; padding:1.05rem 1.25rem 3rem; }
header[data-testid="stHeader"] { background:rgba(4,16,29,.82); backdrop-filter:blur(14px); }
section[data-testid="stSidebar"] {
  background:linear-gradient(180deg,#071a2e 0%,#061526 72%,#08243c 100%);
  border-right:1px solid var(--line);
  min-width:240px !important;
}
section[data-testid="stSidebar"] > div { padding-top:.7rem; }
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] { color:var(--muted); }
[data-testid="stSidebar"] .stRadio > label { display:none; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] { gap:.35rem; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
  padding:.72rem .78rem; border-radius:8px; border-left:3px solid transparent;
  transition:background .16s ease,border-color .16s ease,transform .16s ease;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
  background:#0c2944; transform:translateX(2px);
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
  color:#fff; background:linear-gradient(90deg,#105aa4,#123a64);
  border-left-color:#42a5ff; font-weight:800; box-shadow:0 8px 22px rgba(0,102,204,.22);
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) p { color:#fff; }
h1,h2,h3,h4 { color:var(--text); letter-spacing:-.035em; }
h1 { font-weight:850; } h2,h3 { font-weight:780; }
p,li { line-height:1.58; }
[data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p { color:var(--muted); }
[data-testid="stVerticalBlockBorderWrapper"] {
  border:1px solid var(--line) !important; border-radius:10px !important;
  background:linear-gradient(150deg,rgba(12,39,64,.96),rgba(6,24,42,.97));
  box-shadow:0 12px 32px rgba(0,0,0,.18);
}
[data-testid="stMetric"] {
  background:linear-gradient(150deg,#0d2a45,#081c30); border:1px solid var(--line);
  border-radius:10px; padding:16px 18px; box-shadow:0 10px 26px rgba(0,0,0,.16);
}
[data-testid="stMetricLabel"] { color:var(--muted); }
[data-testid="stMetricValue"] { color:var(--text); font-weight:800; font-variant-numeric:tabular-nums; }
[data-testid="stMetricDelta"] svg { display:none; }
.stButton>button,.stFormSubmitButton>button {
  border-radius:7px; min-height:2.65rem; font-weight:750;
  background:#0d2943; border-color:#245377; color:var(--text);
}
.stButton>button:hover,.stFormSubmitButton>button:hover { border-color:#42a5ff; color:#fff; }
.stButton>button[kind="primary"],.stFormSubmitButton>button[kind="primary"] {
  background:linear-gradient(135deg,#1672d4,#2186f6); border-color:#3398ff; color:white;
}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"]>div {
  background:#071a2e !important; color:var(--text) !important; border-color:var(--line) !important;
  border-radius:8px !important;
}
.stTabs [data-baseweb="tab-list"] { gap:6px; border-bottom-color:var(--line); }
.stTabs [data-baseweb="tab"] { border-radius:7px 7px 0 0; padding:8px 13px; color:var(--muted); }
.stTabs [aria-selected="true"] { background:#123b64; color:#fff !important; }
.stDataFrame { border:1px solid var(--line); border-radius:9px; overflow:hidden; }
[data-testid="stDataFrame"] { color:var(--text); }
[data-testid="stExpander"] { background:#081d31; border-color:var(--line); border-radius:8px; }
hr { border-color:var(--line) !important; }
a { color:#63b8ff; }
.planx-brand { display:flex; align-items:center; gap:11px; margin:4px 0 22px; }
.planx-brand-mark {
  width:39px; height:39px; border-radius:8px; display:flex; align-items:center; justify-content:center;
  background:linear-gradient(145deg,#1672d4,#42a5ff); color:#fff; font-size:24px; font-weight:900;
  box-shadow:0 8px 22px rgba(30,132,245,.3);
}
.planx-brand-title { color:#fff; font-size:21px; line-height:1.05; font-weight:850; letter-spacing:-.04em; }
.planx-brand-sub { font-size:11px; color:#8faccc; margin-top:5px; }
.planx-hero {
  position:relative; overflow:hidden;
  background:linear-gradient(135deg,#0d2943 0%,#081c30 58%,#0c3659 100%);
  border:1px solid var(--line); border-radius:12px; padding:24px 27px; margin-bottom:16px;
  box-shadow:0 14px 36px rgba(0,0,0,.2);
}
.planx-hero:after {
  content:""; position:absolute; right:-40px; top:-75px; width:240px; height:190px;
  background:radial-gradient(circle,rgba(38,143,244,.2),transparent 68%);
}
.planx-eyebrow { color:#55adff; font-size:11px; font-weight:850; letter-spacing:.13em; margin-bottom:7px; }
.planx-hero h1 { margin:0; font-size:32px; line-height:1.17; }
.planx-hero p { margin:8px 0 0; color:#a9bfd5; font-size:14px; max-width:780px; }
.planx-card {
  position:relative; overflow:hidden; background:linear-gradient(145deg,#0d2943,#081c30);
  border:1px solid var(--line); border-radius:10px; padding:16px 17px; min-height:112px;
  box-shadow:0 10px 26px rgba(0,0,0,.16);
}
.planx-card:after {
  content:""; position:absolute; left:0; bottom:0; width:100%; height:3px;
  background:linear-gradient(90deg,#2186f6,#2dd4bf);
}
.planx-card-title { font-size:13px; color:#b1c8de; margin-bottom:7px; font-weight:750; }
.planx-card-value { font-size:24px; color:#fff; font-weight:850; letter-spacing:-.03em; font-variant-numeric:tabular-nums; }
.planx-card-note { margin-top:7px; font-size:11px; color:#7f9bb7; }
.planx-empty {
  background:#081d31; border:1px dashed #285477; border-radius:9px; padding:21px; color:#8faac4;
}
.planx-empty strong { color:#dbeafe !important; }
.planx-source {
  display:inline-flex; align-items:center; gap:5px; color:#a9bfd5; background:#0a2238;
  border:1px solid var(--line); padding:4px 9px; border-radius:999px; font-size:10px;
}
.planx-status-ok { color:#4ee4a4; background:#073226; border-color:#176044; }
.planx-status-wait { color:#ffc766; background:#342a0c; border-color:#665321; }
.planx-status-bad { color:#ff7a83; background:#3b1720; border-color:#6d2937; }
@media(max-width:900px) {
  .block-container{padding-left:1rem;padding-right:1rem}.planx-hero{padding:21px 19px}.planx-hero h1{font-size:27px}
  section[data-testid="stSidebar"]{min-width:unset !important}
}
@media(max-width:640px) {
  .block-container{padding-top:1rem}.planx-card{min-height:96px;padding:14px}.planx-card-value{font-size:21px}
}
</style>
""",
        unsafe_allow_html=True,
    )


def brand():
    st.markdown(
        """
<div class="planx-brand">
  <div class="planx-brand-mark">↗</div>
  <div>
    <div class="planx-brand-title">주식 대시보드</div>
    <div class="planx-brand-sub">시장을 읽고, 더 나은 내일을 준비합니다.</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, eyebrow: str = "PLANX INVESTMENT OS"):
    st.markdown(
        f"""
<div class="planx-hero">
  <div class="planx-eyebrow">{html.escape(eyebrow)}</div>
  <h1>{html.escape(title)}</h1>
  <p>{html.escape(subtitle)}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def card(title: str, value: str, note: str = "", status: str = ""):
    status_html = f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ""
    st.markdown(
        f"""
<div class="planx-card">
  <div class="planx-card-title">{html.escape(title)}</div>
  <div class="planx-card-value">{html.escape(value)}</div>
  <div class="planx-card-note">{html.escape(note)}</div>
  {status_html}
</div>
""",
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str):
    st.markdown(
        f"""
<div class="planx-empty">
  <strong style="color:#334155">{html.escape(title)}</strong><br>
  <span>{html.escape(message)}</span>
</div>
""",
        unsafe_allow_html=True,
    )


def source_badge(label: str, state: str = "wait"):
    cls = {"ok": "planx-status-ok", "bad": "planx-status-bad"}.get(state, "planx-status-wait")
    st.markdown(
        f'<span class="planx-source {cls}">{html.escape(label)}</span>',
        unsafe_allow_html=True,
    )
