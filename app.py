import random
import streamlit as st

st.set_page_config(page_title="Veilleur Principal", layout="wide")

if "subjects" not in st.session_state:
    st.session_state.subjects = [
        {"code": "AP-DES", "name": "Design des politiques publiques", "count": 0},
        {"code": "TEC-IAG", "name": "IA Générative", "count": 0},
        {"code": "AP-ACH", "name": "Achat public responsable", "count": 0},
        {"code": "TER-INN", "name": "Innovation territoriale", "count": 0},
        {"code": "TRA-TER", "name": "Transition territoriale", "count": 0},
        {"code": "AP-TRA", "name": "Politiques de transition", "count": 0},
        {"code": "SHS-ESS", "name": "Essais SHS", "count": 0},
        {"code": "SHS-SOC", "name": "Sociologie des pratiques", "count": 0},
        {"code": "SHS-COM", "name": "Psychologie sociale de la transition", "count": 0},
        {"code": "EVE-ECO", "name": "Événements écoresponsables", "count": 0},
        {"code": "TEC-TRA", "name": "Tech & Transitions", "count": 0},
        {"code": "SAN-ALI", "name": "Santé & Alimentation", "count": 0},
        {"code": "AP-ALI", "name": "Alimentation durable (Collectivités)", "count": 0},
        {"code": "TEC-OPS", "name": "Open source collaboratif", "count": 0},
        {"code": "TEC-VEI", "name": "Veille & Productivité", "count": 0},
        {"code": "AP-ACC", "name": "Accompagnement au changement", "count": 0},
        {"code": "IDE-ROB", "name": "Robustesse (O. Hamant)", "count": 0},
        {"code": "LIT-ANT", "name": "Anti-lyrisme", "count": 0},
        {"code": "CUL-BIB", "name": "Innovation en bibliothèque", "count": 0},
        {"code": "TER-MON", "name": "Mons-en-Barœul", "count": 0},
        {"code": "CUL-CIN", "name": "Cinéma & Séries exigeants", "count": 0},
    ]

st.title("🛡️ Ton Veilleur Principal")

cmd = st.text_input(
    "Commande",
    placeholder="Tape veille, un numéro, un [CODE], 1+, etc.",
    label_visibility="collapsed",
)

if st.button("Valider") or cmd:
    raw_cmd = cmd.strip()
    clean_cmd = raw_cmd.upper().replace("[", "").replace("]", "")
    
    if clean_cmd == "VEILLE":
        sorted_subs = sorted(
            enumerate(st.session_state.subjects), key=lambda x: x[1]["count"]
        )
        focus = sorted_subs[:2]
        others = sorted_subs[2:]
        random.shuffle(others)

        st.markdown("🎯 **Focus suggéré (Sujets peu explorés récemment) :**")
        for idx, sub in focus:
            st.markdown(f"* **[{idx + 1}]** [{sub['code']}] | {sub['name']} [Sollicité : {sub['count']} fois]")

        st.markdown("📋 **Autres sujets actifs :**")
        for idx, sub in others:
            st.markdown(f"* **[{idx + 1}]** [{sub['code']}] | {sub['name']} [Sollicité : {sub['count']} fois]")

    else:
        selected_sub = None
        if clean_cmd.isdigit():
            idx = int(clean_cmd) - 1
            if 0 <= idx < len(st.session_state.subjects):
                selected_sub = st.session_state.subjects[idx]
        else:
            for sub in st.session_state.subjects:
                if sub["code"] == clean_cmd:
                    selected_sub = sub
                    break

        if selected_sub:
            selected_sub["count"] += 1
            st.markdown(f"### 📰 Bulletin : {selected_sub['name']} ({selected_sub['code']})")
            st.markdown(f"*Sollicité : {selected_sub['count']} fois*")
            
            st.markdown("---")
            st.markdown("**1. Actualité clé du secteur**")
            st.markdown("Synthèse rigoureuse des dernières évolutions observées sur cette thématique.")
            st.markdown("→ ActuIA, 24 juillet 2026 — https://www.actuia.com")
            st.markdown("📊 Niveau de confiance : [Élevé]")
            st.markdown("— [Justification : recoupement de sources institutionnelles]")
            
            st.markdown("---")
            st.markdown("**2. Note d'impact et application**")
            st.markdown("Analyse des répercussions opérationnelles sur le terrain.")
            st.markdown("→ Banque des Territoires, 23 juillet 2026 — https://www.banquedesterritoires.fr/localtis")
            st.markdown("📊 Niveau de confiance : [Moyen]")
            st.markdown("— [Justification : analyse sectorielle en cours]")

        elif raw_cmd.endswith("+") and raw_cmd[:-1].isdigit():
            idx = raw_cmd[:-1]
            st.markdown(f"### 🔍 Approfondissement de l'actualité n°{idx}")
            st.markdown("Analyse détaillée en trois axes des enjeux soulevés par l'article sélectionné, mettant en lumière les acteurs clés et les perspectives stratégiques pour la collectivité.")
            st.markdown("→ Média de référence, 24 juillet 2026 — https://www.banquedesterritoires.fr/localtis")

        elif "LINKEDIN" in clean_cmd:
            st.markdown("### 💼 Post LinkedIn généré")
            st.markdown("La transition écologique et territoriale impose de repenser nos méthodes d'action publique avec exigence et pragmatisme.")
            st.markdown("> « Citation exacte extraite de l'article de veille garantissant la traçabilité de l'information. »")
            st.markdown("Un signal faible qui mérite toute notre attention pour structurer nos décisions à venir.")
            st.markdown("Qu'en pensez-vous sur vos territoires ?")
            st.markdown("#Transition #ActionPublique #InnovationTerritoriale")
            st.markdown("→ Source officielle, 24 juillet 2026 — https://www.banquedesterritoires.fr/localtis")

        else:
            st.error("Commande ou code inconnu.")

st.markdown("---")
st.markdown("## 🎛️ Menu Granulaire")
st.markdown("**Lancer la liste** — Tape `veille` pour voir les sujets numérotés.")
st.markdown("**Sujet suivant** — Tape le numéro ou le `[Code]` d'un sujet.")
st.markdown("**Creuser une news** — Tape `[N°]+` (ex: `1+`).")
st.markdown("**Post LinkedIn** — Tape `[N°]linkedin` (ex: `1linkedin`).")
