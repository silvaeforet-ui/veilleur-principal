import random
import traceback
import streamlit as st

st.set_page_config(page_title="Veilleur Principal", layout="wide")

def charger_donnees():
    data = [
        {
            "code": "AP-DES",
            "name": "Design des politiques publiques",
            "news": [
                {
                    "id": 1,
                    "title": "Cartographie des irritants",
                    "summary": (
                        "La co-conception connaît un tournant radical. "
                        "On passe à une observation directe des frictions. "
                        "L'objectif : abandonner les schémas en silo au profit "
                        "de parcours usagers ajustés à la réalité matérielle."
                    ),
                    "source": "La Gazette des Communes",
                    "confidence": "Élevé",
                    "deep": (
                        "L'immersion permet de lever les impensés "
                        "bureaucratiques en observant la tâche réelle "
                        "plutôt que la tâche prescrite."
                    ),
                    "linkedin": (
                        "Refuser la complexité bureaucratique pour remettre "
                        "l'humain au cœur des décisions. 🎯 #DesignPublic"
                    )
                },
                {
                    "id": 2,
                    "title": "Prototypage itératif",
                    "summary": (
                        "La logique de 'big bang' administratif montre "
                        "ses limites. L'expérimentation à petite échelle "
                        "permet d'évaluer l'acceptabilité sociale en "
                        "conditions réelles et d'ajuster en continu."
                    ),
                    "source": "Sciences Po Urba",
                    "confidence": "Élevé",
                    "deep": (
                        "Le prototypage permet de sortir de l'effet tunnel "
                        "propre aux projets pluriannuels. Le droit à l'erreur "
                        "sécurise paradoxalement la décision politique."
                    ),
                    "linkedin": (
                        "Pourquoi attendre 2 ans avant de lancer un service ? "
                        "Testons à petite échelle ! 🛠️ #Agilité"
                    )
                }
            ]
        },
        {
            "code": "TEC-IAG",
            "name": "IA Générative",
            "news": [
                {
                    "id": 1,
                    "title": "Souveraineté des données",
                    "summary": (
                        "L'intégration des modèles génératifs exige une "
                        "étanchéité stricte. L'arbitrage s'oriente vers des "
                        "modèles restreints (SLM) hébergés en local."
                    ),
                    "source": "ActuIA",
                    "confidence": "Élevé",
                    "deep": (
                        "La mise en œuvre du RAG garantit la traçabilité "
                        "des sources et évite les hallucinations de l'IA, "
                        "tout en cloisonnant les données sensibles."
                    ),
                    "linkedin": (
                        "L'IA oui, mais avec une souveraineté totale sur "
                        "nos données publiques ! 🤖 #IAGenerative"
                    )
                }
            ]
        },
        {
            "code": "IDE-ROB",
            "name": "Robustesse (O. Hamant)",
            "news": [
                {
                    "id": 1,
                    "title": "Redondance organisationnelle",
                    "summary": (
                        "La théorie de la robustesse critique le culte de "
                        "la performance. Un service public ultra-optimisé "
                        "sans marge de manœuvre s'effondre face aux chocs."
                    ),
                    "source": "Olivier Hamant (INRAE)",
                    "confidence": "Élevé",
                    "deep": (
                        "Créer de la robustesse, c'est accepter une part de "
                        "lenteur protectrice et de redondance pour sécuriser "
                        "les processus critiques."
                    ),
                    "linkedin": (
                        "L'optimisation maximale rend nos services "
                        "vulnérables. Cultivons la robustesse ! 🌿 #Management"
                    )
                }
            ]
        }
    ]

    codes_restants = [
        ("AP-TRA", "Politiques de transition"), 
        ("SHS-SOC", "Sociologie des pratiques"),
        ("AP-ACC", "Accompagnement au changement"), 
        ("LIT-ANT", "Anti-lyrisme"),
        ("AP-ACH", "Achat public responsable"), 
        ("TER-INN", "Innovation territoriale"), 
        ("TRA-TER", "Transition territoriale"), 
        ("SHS-ESS", "Essais SHS"), 
        ("SHS-COM", "Psychologie sociale"), 
        ("EVE-ECO", "Événements écoresponsables"),
        ("TEC-TRA", "Tech & Transitions"), 
        ("SAN-ALI", "Santé & Alimentation"), 
        ("AP-ALI", "Alimentation durable"), 
        ("TEC-OPS", "Open source collaboratif"), 
        ("TEC-VEI", "Veille & Productivité"), 
        ("CUL-BIB", "Innovation en bibliothèque"), 
        ("TER-MON", "Mons-en-Barœul"), 
        ("CUL-CIN", "Cinéma & Séries")
    ]

    for code, nom in codes_restants:
        data.append({
            "code": code,
            "name": nom,
            "news": [
                {
                    "id": 1,
                    "title": "Évolutions : " + nom,
                    "summary": (
                        "Les pratiques territoriales sur cette thématique "
                        "connaissent une forte accélération."
                    ),
                    "source": "Synthèse interne",
                    "confidence": "Moyen",
                    "deep": (
                        "La clé de déblocage réside dans la transversalité "
                        "inter-services et le sens de l'action publique."
                    ),
                    "linkedin": (
                        "Repenser nos silos administratifs pour plus "
                        "d'efficacité ! 🚀 #ActionPublique"
                    )
                }
            ]
        })

    for d in data:
        d["count"] = 0
        
    return data

if "APP_VERSION_6" not in st.session_state:
    st.session_state.clear()
    st.session_state["APP_VERSION_6"] = True
    st.session_state.subjects = charger_donnees()
    st.session_state.last_subject_index = 0

st.title("🌱 Ton Veilleur Principal")
st.markdown("*Une veille analytique, documentée et conçue pour l'action.*")

cmd = st.text_input(
    "Commande",
    placeholder="Tape un N°, un [CODE], 1+, 1linkedin...",
    label_visibility="collapsed",
)

st.button("Valider")

clean_cmd = cmd.strip().upper().replace("[", "").replace("]", "")

try:
    if not clean_cmd or clean_cmd == "VEILLE":
        sorted_subs = sorted(
            enumerate(st.session_state.subjects), 
            key=lambda x: x[1].get("count", 0)
        )
        focus = sorted_subs[:2]
        others = sorted_subs[2:]
        random.shuffle(others)

        st.markdown("🎯 **Ce que je suggère (Sujets peu explorés) :**")
        for idx, sub in focus:
            idx_str = str(idx + 1)
            code_str = sub.get("code", "")
            name_str = sub.get("name", "")
            count_str = str(sub.get("count", 0))
            st.markdown(
                "* **[" + idx_str + "]** [" + code_str + "] | " + 
                name_str + " *(Vu : " + count_str + " fois)*"
            )

        st.markdown("📋 **Le reste des thématiques actives :**")
        for idx, sub in others:
            idx_str = str(idx + 1)
            code_str = sub.get("code", "")
            name_str = sub.get("name", "")
            count_str = str(sub.get("count", 0))
            st.markdown(
                "* **[" + idx_str + "]** [" + code_str + "] | " + 
                name_str + " *(Vu : " + count_str + " fois)*"
            )

    elif "+" in clean_cmd:
        num_part = clean_cmd.replace("+", "").strip()
        last_idx = st.session_state.last_subject_index
        sub = st.session_state.subjects[last_idx]
        
        news_idx = int(num_part) - 1 if num_part.isdigit() else 0
        news_list = sub.get("news", [])
        
        if 0 <= news_idx < len(news_list):
            item = news_list[news_idx]
            id_str = str(item.get("id", ""))
            
            st.markdown("### 🔍 Approfondissement — News n°" + id_str)
            
            sujet_str = sub.get("name", "") + " (`" + sub.get("code", "") + "`)"
            st.markdown("**Sujet associé :** " + sujet_str)
            
            st.info(item.get("deep", ""))
            
            src_str = "📌 **Source critique :** " + str(item.get("source", ""))
            st.markdown(src_str)
        else:
            code_str = sub.get("code", "")
            st.error("Actualité introuvable dans le bulletin " + code_str)

    elif "LINKEDIN" in clean_cmd:
        num_part = clean_cmd.replace("LINKEDIN", "").strip()
        last_idx = st.session_state.last_subject_index
        sub = st.session_state.subjects[last_idx]
        
        news_idx = int(num_part) - 1 if num_part.isdigit() else 0
        news_list = sub.get("news", [])
        
        if 0 <= news_idx < len(news_list):
            item = news_list[news_idx]
            sub["count"] = sub.get("count", 0) + 1
            id_str = str(item.get("id", ""))
            
            st.markdown("### 💼 Piste de réflexion — News n°" + id_str)
            st.success(item.get("linkedin", ""))
            
            src_str = "📌 **Source :** " + str(item.get("source", ""))
            st.markdown(src_str)
        else:
            st.error("Aucune actualité disponible pour ce post.")

    else:
        selected_sub = None
        if clean_cmd.isdigit():
            idx = int(clean_cmd) - 1
            if 0 <= idx < len(st.session_state.subjects):
                selected_sub = st.session_state.subjects[idx]
                st.session_state.last_subject_index = idx
        else:
            for i, sub in enumerate(st.session_state.subjects):
                if sub.get("code") == clean_cmd:
                    selected_sub = sub
                    st.session_state.last_subject_index = i
                    break

        if selected_sub:
            selected_sub["count"] = selected_sub.get("count", 0) + 1
            nom_str = selected_sub.get("name", "")
            code_str = selected_sub.get("code", "")
            count_str = str(selected_sub.get("count", 0))
            
            st.markdown("## 📰 Bulletin : " + nom_str + " (`" + code_str + "`)")
            st.markdown("*Indicateur de suivi : " + count_str + " fois.*")
            st.markdown("---")
            
            for item in selected_sub.get("news", []):
                id_str = str(item.get("id", ""))
                title_str = item.get("title", "")
                st.markdown("### **" + id_str + ". " + title_str + "**")
                st.markdown(item.get("summary", ""))
                
                src_str = str(item.get("source", ""))
                conf_str = str(item.get("confidence", ""))
                st.markdown("→ **Source :** " + src_str + " | 📊 [" + conf_str + "]")
                st.markdown("---")
        else:
            st.warning("Commande non reconnue. Essayez un chiffre ou 1+.")

except Exception as e:
    st.error("🚨 Erreur critique interceptée :")
    st.code(traceback.format_exc(), language="python")

st.markdown("---")
st.markdown("## 🎛️ Ta boîte à outils")
st.markdown("**Changer de sujet** — Tape un numéro ou un `[Code]`.")
st.markdown("**Creuser une news** — Tape `[N°]+` (ex: `1+` ou `2+`).")
st.markdown("**Post LinkedIn** — Tape `[N°]linkedin` (ex: `1linkedin`).")
