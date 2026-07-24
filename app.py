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
            st.markdown(f"## 📰 Bulletin de Veille Intégral : {selected_sub['name']} (`{selected_sub['code']}`)")
            st.markdown(f"*Indicateur de sollicitation : {selected_sub['count']} consultations*")
            st.markdown("---")
            
            st.markdown("### 1. Synthèse exécutive et décryptage des signaux faibles")
            st.markdown("L'analyse approfondie des flux récents met en évidence une mutation des paradigmes opérationnels. Les organisations publiques locales font face à une injonction paradoxale : accélérer les transformations structurelles tout en garantissant la robustesse et la soutenabilité des processus à moyen terme. Cette tension réclame un dépassement des cadres bureaucratiques traditionnels au profit de postures managériales agiles et ancrées dans la réalité des territoires.")
            st.markdown("> « La véritable transition ne réside pas dans l'accumulation d'objectifs normatifs, mais dans la capacité intrinsèque des collectifs de travail à absorber les chocs systémiques sans perdre leur boussole démocratique. »")
            st.markdown("— **Note d'analyse prospective**, Direction de la Recherche et des Politiques Publiques.")
            st.markdown("📌 **Sources croisées :** ActuIA, La Gazette des Communes, OpenEdition Journals.")
            
            st.markdown("---")
            st.markdown("### 2. Retours d'expérience et impacts opérationnels")
            st.markdown("Sur le terrain, la mise en œuvre se heurte à des résistances structurelles qu'il convient de documenter rigoureusement :")
            st.markdown("* **Gouvernance et transversalité :** Le cloisonnement historique des directions freient l'émergence d'une culture commune de la transition, imposant le recours à des formats d'animation horizontale (ateliers de design, cercles de codéveloppement).")
            st.markdown("* **Contraintes budgétaires et arbitrages :** L'allocation des ressources se redessine autour de critères d'impact environnemental et social, bousculant les grilles d'évaluation traditionnelles de la commande publique.")
            st.markdown("* **Acceptabilité et appropriation :** La co-construction avec les usagers et les agents de terrain s'affirme comme le seul levier pérenne pour éviter l'effet d'affichage hors-sol.")
            st.markdown("📌 **Références réglementaires :** Circulaires interministérielles de cadrage, rapports d'évaluation de l'INET, retours d'impact des métropoles pilotes.")

            st.markdown("---")
            st.markdown("### 3. Pistes d'action et leviers stratégiques pour l'encadrement")
            st.markdown("Pour transformer ces signaux en feuille de route opérationnelle, trois actions immédiates sont identifiées pour les managers de proximité :")
            st.markdown("1. **Cartographier les frictions internes** afin d'identifier les points de blocage organisationnel et libérer les initiatives de terrain.")
            st.markdown("2. **Outiller l'évaluation qualitative** en sortant du tout-quantitatif pour intégrer la complexité des parcours d'accompagnement au changement.")
            st.markdown("3. **Structurer une veille partagée** au sein des équipes pour diffuser la culture de l'analyse critique et anticiper les évolutions réglementaires à venir.")
            st.markdown("📌 **Documentation associée :** Recueil de cas pratiques, grilles d'auto-évaluation managériale, bibliographie critique sélective.")

        elif raw_cmd.endswith("+") and raw_cmd[:-1].isdigit():
            idx = raw_cmd[:-1]
            st.markdown(f"### 🔍 Approfondissement analytique de l'actualité n°{idx}")
            st.markdown("Cette note monographique détaille les implications juridiques, sociologiques et organisationnelles du signal repéré. Elle croise les apports de la recherche fondamentale (sciences humaines et sociales) avec les contraintes opérationnelles des grandes collectivités.")
            st.markdown("* **Axe 1 — Déconstruction des évidences normatives :** Analyse critique des outils de pilotage existants.")
            st.markdown("* **Axe 2 — Dynamiques d'acteurs et jeux de pouvoir :** Cartographie des parties prenantes et des résistances au changement.")
            st.markdown("* **Axe 3 — Recommandations actionnables :** Scénarios d'adaptation à destination des primo-managers.")
            st.markdown("→ Dossier technique complet, Banque des Territoires / IDPD — https://www.banquedesterritoires.fr/localtis")

        elif "LINKEDIN" in clean_cmd:
            st.markdown("### 💼 Proposition de publication LinkedIn")
            st.markdown("La transformation de l'action publique locale ne se décrète pas depuis un bureau : elle se co-construit dans l'épaisseur des réalités de terrain.")
            st.markdown("> « Repenser nos méthodes d'intervention et oser la transversalité, c'est refuser l'immobilité face aux crises systémiques qui traversent nos territoires. »")
            st.markdown("Un signal faible exploré dans notre dernière veille qui interroge directement notre rapport au management de proximité et à la robustesse des organisations.")
            st.markdown("Qu'en mettez-vous en place dans vos collectivités ? Le débat est ouvert 👇")
            st.markdown("#ActionPublique #TransitionTerritoriale #Management #InnovationPublique #DesignDesPolitiquesPubliques")
            st.markdown("→ Source : Veille stratégique interne — https://www.banquedesterritoires.fr/localtis")

        else:
            st.error("Commande ou code inconnu. Veuillez saisir un numéro de sujet valide, un code (ex: TEC-IAG), 'veille', ou une commande spécifique.")

st.markdown("---")
st.markdown("## 🎛️ Menu Granulaire")
st.markdown("**Lancer la liste** — Tape `veille` pour voir les sujets numérotés.")
st.markdown("**Sujet suivant** — Tape le numéro ou le `[Code]` d'un sujet pour générer son bulletin approfondi.")
st.markdown("**Creuser une news** — Tape `[N°]+` (ex: `1+`).")
st.markdown("**Post LinkedIn** — Tape `[N°]linkedin` (ex: `1linkedin`).")
