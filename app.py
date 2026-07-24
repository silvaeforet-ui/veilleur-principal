import random
import streamlit as st

st.set_page_config(page_title="Veilleur Principal", layout="wide")

# Initialisation des sujets
if "subjects" not in st.session_state:
    st.session_state.subjects = {
        "AP-DES": {"name": "Design des politiques publiques", "count": 0},
        "TEC-IAG": {"name": "IA Générative", "count": 0},
        "AP-ACH": {"name": "Achat public responsable", "count": 0},
        "TER-INN": {"name": "Innovation territoriale", "count": 0},
        "TRA-TER": {"name": "Transition territoriale", "count": 0},
        "AP-TRA": {"name": "Politiques de transition", "count": 0},
        "SHS-ESS": {"name": "Essais SHS", "count": 0},
        "SHS-SOC": {"name": "Sociologie des pratiques", "count": 0},
        "SHS-COM": {"name": "Psychologie sociale de la transition", "count": 0},
        "EVE-ECO": {"name": "Événements écoresponsables", "count": 0},
        "TEC-TRA": {"name": "Tech & Transitions", "count": 0},
        "SAN-ALI": {"name": "Santé & Alimentation", "count": 0},
        "AP-ALI": {"name": "Alimentation durable (Collectivités)", "count": 0},
        "TEC-OPS": {"name": "Open source collaboratif", "count": 0},
        "TEC-VEI": {"name": "Veille & Productivité", "count": 0},
        "AP-ACC": {"name": "Accompagnement au changement", "count": 0},
        "IDE-ROB": {"name": "Robustesse (O. Hamant)", "count": 0},
        "LIT-ANT": {"name": "Anti-lyrisme", "count": 0},
        "CUL-BIB": {"name": "Innovation en bibliothèque", "count": 0},
        "TER-MON": {"name": "Mons-en-Barœul", "count": 0},
        "CUL-CIN": {"name": "Cinéma & Séries exigeants", "count": 0},
    }

st.title("🛡️ Ton Veilleur Principal")

# Entrée de commande
cmd = st.text_input(
    "Commande",
    placeholder="Tape veille, un [CODE], 1+, etc.",
    label_visibility="collapsed",
)

if cmd.strip().lower() == "veille":
    sorted_subs = sorted(
        st.session_state.subjects.items(), key=lambda x: x[1]["count"]
    )
    focus = sorted_subs[:2]
    others = sorted_subs[2:]
    random.shuffle(others)

    st.markdown("🎯 **Focus suggéré (Sujets peu explorés récemment) :**")
    for code, data in focus:
        st.markdown(f"* [{code}] | {data['name']} [Sollicité : {data['count']} fois]")

    st.markdown("📋 **Autres sujets actifs :**")
    for code, data in others:
        st.markdown(f"* [{code}] | {data['name']} [Sollicité : {data['count']} fois]")

elif cmd.strip().upper() in st.session_state.subjects:
    code = cmd.strip().upper()
    st.session_state.subjects[code]["count"] += 1
    st.success(
        f"Bulletin généré pour {st.session_state.subjects[code]['name']} "
        f"(Compteur : {st.session_state.subjects[code]['count']} fois)."
    )

# Menu Granulaire
st.markdown("---")
st.markdown("## 🎛️ Menu Granulaire")
st.markdown("**Lancer la liste** — Tape `veille` pour voir les sujets.")
st.markdown(
    "**Sujet suivant** — Tape le `[Code]` d'un sujet pour générer son bulletin."
)
st.markdown("**Creuser une news** — Tape `[N°]+` (ex: `1+`).")
st.markdown("**Post LinkedIn** — Tape `[N°]linkedin` (ex: `1linkedin`).")

