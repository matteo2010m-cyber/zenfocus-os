import streamlit as st
import pandas as pd
from datetime import datetime
import time

# -------------------------------------------------
# 1. DESIGN SYSTEM: ULTRA-BLACK & EYE-CARE
# -------------------------------------------------
st.set_page_config(page_title="ZenFocus OS", page_icon="🍏", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
    
    /* Sfondo Natural Linen per riposo visivo */
    [data-testid="stAppViewContainer"] {
        background-color: #f2f0e9;
        background-image: url("https://www.transparenttextures.com/patterns/natural-paper.png");
        font-family: 'Inter', sans-serif;
    }

    /* Testo Antracite per contrasto morbido */
    h1, h2, h3, p, label, .stMarkdown { 
        color: #3a3a3c !important; 
    }

    /* Card Luxury con vetro opaco */
    .eye-care-card {
        background: rgba(255, 255, 252, 0.7);
        border: 1px solid #d1d1d6;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }

    /* FORZATURA PULSANTI: ULTRA-BLACK EDITION */
    div.stButton > button {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 16px 20px !important;
        font-weight: 600 !important;
        letter-spacing: 1.2px !important; /* Testo più arioso */
        width: 100% !important;
        text-transform: uppercase !important;
        font-size: 0.85rem !important;
        transition: all 0.3s ease !important;
        display: block !important;
    }

    div.stButton > button:hover {
        background-color: #333333 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.25) !important;
    }
    
    /* Forza il colore bianco del testo (sovrascrive i default di Streamlit) */
    div.stButton > button p {
        color: #ffffff !important;
    }

    /* Ottimizzazione Mobile */
    @media (max-width: 640px) {
        .eye-care-card { padding: 15px; }
        h1 { font-size: 1.6rem !important; }
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# 2. LOGICA DI SISTEMA: ZEN ENGINE
# -------------------------------------------------
class ZenEngine:
    @staticmethod
    def evaluate(tipo, stress, ora):
        # Regola 1: Spam notturno
        if tipo == "Spam" and (ora >= 20 or ora < 7):
            return False, "Protocollo Silenzio", "Spam intercettato. La tua serata è protetta."
        
        # Regola 2: Riposo assoluto
        if ora < 7 or ora > 23:
            return False, "Fase Rigenerativa", "Notifica soppressa per favorire il riposo."
        
        # Regola 3: Scudo cognitivo per stress elevato
        if stress == "Elevato" and tipo != "Famiglia":
            return False, "Scudo Cognitivo", "Stress alto: ammesse solo urgenze familiari."
        
        return True, "Accesso Consentito", "La notifica è in armonia con il tuo stato."

# -------------------------------------------------
# 3. INTERFACCIA UTENTE
# -------------------------------------------------
def main():
    if "profile" not in st.session_state:
        st.session_state.profile = None
    if "stats" not in st.session_state:
        st.session_state.stats = {"Passate": 0, "Bloccate": 0}

    # --- SCHERMATA DI BENVENUTO ---
    if st.session_state.profile is None:
        st.write("<br><br>", unsafe_allow_html=True)
        _, col_center, _ = st.columns([1, 1.5, 1])
        with col_center:
            st.markdown("""
                <div class='eye-care-card' style='text-align:center;'>
                    <h1 style='letter-spacing:-1.5px; margin-bottom:0;'>ZenFocus OS</h1>
                    <p style='opacity:0.6;'>Ambiente Operativo Protetto</p>
                </div>
            """, unsafe_allow_html=True)
            
            prof = st.selectbox("Qual è il tuo cluster operativo?", [
                "Executive Manager", "Creative Designer", "Chirurgo", 
                "Pilota", "Social Media Manager", "Sviluppatore", "Chef", "Studente"
            ])
            
            st.write("<br>", unsafe_allow_html=True)
            if st.button("Attiva Ecosistema"):
                with st.spinner("Calibrazione parametri..."):
                    time.sleep(1)
                st.session_state.profile = prof
                st.rerun()
        return

    # --- DASHBOARD PRINCIPALE ---
    st.markdown(f"<h1>ZenFocus <span style='font-weight:200; color:#86868b'>| {st.session_state.profile}</span></h1>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1.6, 1])

    with col_l:
        st.markdown("<div class='eye-care-card'>", unsafe_allow_html=True)
        st.markdown("### Analisi Flusso Notifiche")
        tipo = st.selectbox("Sorgente Notifica", ["Lavoro", "Famiglia", "Social", "Spam"])
        stress = st.select_slider("Carico Mentale Attuale", options=["Assente", "Moderato", "Elevato"])
        ora = st.slider("Asse Orario (24h)", 0, 23, datetime.now().hour)
        
        st.write("<br>", unsafe_allow_html=True)
        if st.button("Verifica Impatto"):
            allowed, titolo, desc = ZenEngine.evaluate(tipo, stress, ora)
            if allowed:
                st.session_state.stats["Passate"] += 1
                st.success(f"**{titolo}**: {desc}")
            else:
                st.session_state.stats["Bloccate"] += 1
                st.warning(f"**{titolo}**: {desc}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_r:
        # Widget Tempo - Design Minimalista
        st.markdown(f"""
            <div class='eye-care-card' style='text-align: center;'>
                <div style='font-size: 0.7rem; opacity: 0.5; text-transform: uppercase; letter-spacing:2px;'>Focus Clock</div>
                <div style='font-size: 3rem; font-weight: 300; color: #1a1a1a;'>{datetime.now().strftime('%H:%M')}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Report delle Stats
        st.markdown("<div class='eye-care-card'>", unsafe_allow_html=True)
        st.markdown("### Focus Report")
        m1, m2 = st.columns(2)
        m1.metric("Bloccate", st.session_state.stats["Bloccate"])
        m2.metric("Passate", st.session_state.stats["Passate"])
        
        st.write("<br>", unsafe_allow_html=True)
        if st.button("Scollega Profilo"):
            st.session_state.profile = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()