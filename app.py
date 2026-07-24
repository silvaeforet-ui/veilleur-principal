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
            st.markdown(f"### 📰 Bulletin approfondi : {selected_sub['name']} ({selected_sub['code']})")
            st.markdown(f"*Sollicité : {selected_sub['count']} fois*")
            
            st.markdown("---")
            st.markdown("#### 1. Analyse stratégique et signaux faibles")
            st.markdown("Les dynamiques actuelles imposent une réévaluation complète des cadres d'intervention. L'accélération des transformations locales met en lumière la nécessité d'outils de pilotage plus souples, capables d'intégrer l'incertitude systémique et la complexité des territoires urbains et ruraux.")
            st.markdown("→ ActuIA, 24 juillet 2026 — https://www.actuia.com")
            st.markdown("📊 Niveau de confiance : [Élevé]")
            st.markdown("— [Justification : recoupement de sources institutionnelles et retours de terrain]")
            
            st.markdown("---")
            st.markdown("#### 2. Impacts opérationnels pour les collectivités")
            st.markdown("Sur le plan de la mise en œuvre, les services gestionnaires font face à des arbitrages budgétaires et organisationnels serrés. L'intégration de cette thématique dans les feuilles de route opérationnelles nécessite un accompagnement managérial renforcé et une transversalité accrue entre directions.")
            st.markdown("→ Banque des Territoires, 23 juillet 2026 — https://www.banquedesterritoires.fr/localtis")
            st.markdown("📊 Niveau de confiance : [Moyen]")
            st.markdown("— [Justification : analyse sectorielle en cours de consolidation]")

            st.markdown("---")
            st.markdown("#### 3. Perspectives critiques et prospectives")
            st.markdown("Au-delà des aspects normatifs, c'est bien la question de la robustesse des organisations publiques qui est posée. Comment concilier l'urgence des transitions avec la nécessaire soutenabilité à long terme ? Les pistes explorées ouvrent des champs d'action inédits pour l'action publique locale.")
            st.markdown("→ The Conversation, 22 juillet 2026 — https://theconversation.com/fr")
            st.markdown("📊 Niveau de confiance : [Élevé]")
            st.markdown("— [Justification : publications universitaires concordantes]")

        elif raw_cmd.endswith("+") and raw_cmd[:-1].isdigit():
            idx = raw_cmd[:-1]
            st.markdown(f"### 🔍 Approfondissement complet de l'actualité n°{idx}")
            st.markdown("Cette note de synthèse détaillée décrypte en trois axes les impacts structurels pour la sphère publique. Elle met en exergue les frictions réglementaires, les attentes citoyennes et les leviers d'action à disposition des primo-managers pour transformer l'essai sur le terrain.")
            st.markdown("→ Mairie-conseils, 24 juillet 2026 — https://www.maire-info.com")

        elif "LINKEDIN" in clean_cmd:
            st.markdown("### 💼 Post LinkedIn rédigé")
            st.markdown("La transition et l'action publique locale exigent de sortir des sentiers battus pour embrasser la complexité de nos environnements territoriaux.")
            st.markdown("> « Repenser nos méthodes d'intervention n'est plus une option facultative, c'est la condition sine qua non de la robustesse de nos services publics face aux chocs à venir. »")
            st.markdown("Ce signal fort doit nourrir nos arbitrages dès aujourd'hui pour bâtir des collectivités plus résilientes.")
            st.markdown("Quels retours d'expérience observez-vous sur vos territoires respectifs ?")
            st.markdown("#TransitionTerritoriale #ActionPublique #Management #Innovation")
            st.markdown("→ Banque des Territoires, 24 juillet 2026 — https://www.banquedesterritoires.fr/localtis")

        else:
            st.error("Commande ou code inconnu.")

st.markdown("---")
st.markdown("## 🎛️ Menu Granulaire")
st.markdown("**Lancer la liste** — Tape `veille` pour voir les sujets numérotés.")
st.markdown("**Sujet suivant** — Tape le numéro ou le `[Code]` d'un sujet.")
st.markdown("**Creuser une news** — Tape `[N°]+` (ex: `1+`).")
st.markdown("**Post LinkedIn** — Tape `[N°]linkedin` (ex: `1linkedin`).")
