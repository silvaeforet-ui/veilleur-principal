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
                    "title": "Cartographie des irritants et immersion usager",
                    "summary": """La co-conception des services publics territoriaux connaît un tournant radical. Fini les simples boîtes à idées ou les consultations cosmétiques : on passe désormais à une observation directe et rigoureuse des frictions vécues sur le terrain. L'objectif est d'abandonner les schémas purement administratifs, souvent pensés en silo depuis les bureaux, au profit de parcours usagers ajustés à la réalité sociale, psychologique et matérielle des citoyens. Cette approche permet de cartographier précisément les 'irritants' pour les éliminer à la source.""",
                    "source": "La Gazette des Communes",
                    "confidence": "Élevé (retour de terrain documenté)",
                    "deep": """En sociologie des organisations, l'immersion usager permet de lever les impensés bureaucratiques. En observant la tâche réelle (ce que l'usager fait vraiment pour remplir un dossier) plutôt que la tâche prescrite (ce que la procédure exige en théorie), nos équipes identifient immédiatement les ruptures de charge cognitive. Concrètement, cela signifie aller dans les accueils, analyser les parcours physiques et les documents rejetés. Les études montrent que simplifier drastiquement ces démarches réduit la frustration des citoyens et fait chuter les incivilités aux guichets, tout en redonnant du sens au travail des agents.""",
                    "linkedin": """Repenser l'action publique par le design, c'est refuser la complexité bureaucratique pour remettre l'humain au cœur de nos décisions. Simplifier, c'est apaiser ! 🎯 #DesignPublic #InnovationTerritoriale"""
                },
                {
                    "id": 2,
                    "title": "Prototypage itératif et bacs à sable réglementaires",
                    "summary": """Face à la complexité des transitions, la logique de grand déploiement direct (le fameux 'big bang' administratif) montre ses limites. L'expérimentation d'un nouveau service à petite échelle, avant toute généralisation, permet d'évaluer son acceptabilité sociale en conditions réelles. Cette méthode du prototypage rapide permet d'ajuster les dispositifs en continu, à moindre coût financier et organisationnel.""",
                    "source": "Sciences Po Urba",
                    "confidence": "Élevé (études de cas métropolitaines)",
                    "deep": """La méthodologie du prototypage permet de sortir de l'effet tunnel propre aux projets pluriannuels. En administration, nous avons souvent peur de lancer un dispositif imparfait. Or, le droit à l'ajustement sécurise paradoxalement la décision politique. Tester sur un quartier pilote permet de confronter la norme à la friction du réel, de recueillir les retours des agents de terrain de façon organique, et de pivoter avant que l'ingénierie financière ne soit totalement verrouillée.""",
                    "linkedin": """Pourquoi attendre deux ans avant de lancer un service public ? Testons à petite échelle, ajustons et apprenons du terrain en temps réel ! Le droit à l'erreur est un levier d'efficacité. 🛠️ #ServicePublic #Agilité"""
                }
            ]
        },
        {
            "code": "TEC-IAG",
            "name": "IA Générative",
            "news": [
                {
                    "id": 1,
                    "title": "Souveraineté des données et déploiement de LLM locaux",
                    "summary": """L'intégration des modèles génératifs dans les collectivités exige une étanchéité stricte pour protéger le secret administratif et les données sensibles. L'arbitrage s'oriente désormais vers des modèles de langage restreints (SLM - Small Language Models) hébergés sur des infrastructures souveraines, conformes au RGPD, plutôt que sur des plateformes grand public dont les conditions de réutilisation des données restent opaques.""",
                    "source": "ActuIA",
                    "confidence": "Élevé (cadre DINUM & CNIL)",
                    "deep": """Sur le plan technique et juridique, la mise en œuvre du RAG (Retrieval-Augmented Generation) sur les bases documentaires internes des mairies garantit la traçabilité des sources. Cela évite les 'hallucinations' de l'IA (lorsqu'elle invente des informations) tout en cloisonnant les données. L'enjeu managérial est de positionner cette IA souveraine non pas comme un oracle infaillible, mais comme un simple assistant de pré-traitement, auditable à tout moment par les agents assermentés.""",
                    "linkedin": """L'IA générative dans nos administrations ? Oui, mais à condition de garder une souveraineté totale et inconditionnelle sur nos données publiques. 🤖 #IAGenerative #SouverainetéNumérique"""
                },
                {
                    "id": 2,
                    "title": "Copilote documentaire et réduction de la charge cognitive",
                    "summary": """L'utilisation de l'IA pour défricher, résumer et croiser de grands volumes de rapports (documents d'urbanisme, enquêtes publiques, notes de synthèse) devient un cas d'usage mature. L'objectif principal est de libérer du temps d'ingénierie administrative pour permettre aux cadres de réinvestir le terrain.""",
                    "source": "Banque des Territoires",
                    "confidence": "Moyen (en consolidation)",
                    "deep": """La sociologie du travail nous alerte sur le risque de perte de compétence (deskilling). L'automatisation de la synthèse documentaire ne vaut que si elle s'accompagne d'un contrôle critique permanent. L'agent public doit rester le seul garant de l'évaluation contextuelle. Si la machine résume un appel d'offres de 500 pages en 3 points, le manager doit conserver la grille de lecture politique et sociale pour arbitrer. C'est un défi de formation continue massif.""",
                    "linkedin": """Automatiser la synthèse documentaire pour réinvestir le temps humain sur le terrain : voilà le vrai gain de productivité de l'IA dans l'action publique. La machine traite, l'humain décide. 🧠 #Productivité"""
                }
            ]
        },
        {
            "code": "IDE-ROB",
            "name": "Robustesse (O. Hamant)",
            "news": [
                {
                    "id": 1,
                    "title": "Redondance organisationnelle et fin de l'optimisation",
                    "summary": """Inspirée des travaux du biologiste Olivier Hamant, la théorie de la robustesse critique frontalement le culte de la performance et des flux tendus dans l'administration. Face aux chocs systémiques (climatiques, sanitaires, sociaux), un service public ultra-optimisé et sans aucune marge de manœuvre s'effondre.""",
                    "source": "Olivier Hamant (INRAE)",
                    "confidence": "Élevé (recherche)",
                    "deep": """La biologie de l'évolution nous enseigne que la quête effrénée d'efficience fragilise le vivant. Appliqué au management public, cela signifie qu'avoir des agents 'trop' spécialisés ou des processus sans aucun doublon est un danger. Créer de la robustesse, c'est accepter une part de 'lenteur protectrice' et de redondance : que plusieurs personnes maîtrisent un même dossier critique, ou que la collectivité conserve des marges de temps, même si cela contrevient aux principes du Lean Management.""",
                    "linkedin": """La recherche d'optimisation maximale jusqu'à la rupture rend nos services vulnérables. Cultivons plutôt la robustesse, la diversité et la redondance protectrice ! 🌿 #Robustesse #ManagementPublic"""
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
                    "title": "Évolutions et enjeux : " + nom,
                    "summary": """Les pratiques territoriales autour de cette thématique connaissent une accélération marquée. Les collectivités s'organisent pour intégrer de nouveaux cadres normatifs tout en préservant l'agilité opérationnelle de leurs équipes de terrain face à des injonctions parfois contradictoires.""",
                    "source": "Synthèse interne",
                    "confidence": "Moyen",
                    "deep": """L'analyse approfondie de cette thématique révèle de fortes résistances au changement liées à l'empilement des procédures et à la fatigue organisationnelle. La clé de déblocage réside systématiquement dans la transversalité inter-services et la réappropriation du sens concret de l'action publique par les agents sur le terrain, loin des injonctions purement descendantes.""",
                    "linkedin": """Repenser nos silos administratifs pour plus d'efficacité sur nos territoires reste le défi majeur. L'action publique doit se décloisonner ! 🚀 #Transition #ActionPublique"""
                }
            ]
        })

    for d in data:
        d["count"] = 0
        
    return data

if "APP_VERSION_7" not in st.session_state:
    st.session_state.clear()
    st.session_state["APP_VERSION_7"] = True
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
            st.markdown("* **[" + idx_str + "]** [" + code_str + "] | " + name_str + " *(Vu : " + count_str + " fois)*")

        st.markdown("📋 **Le reste des thématiques actives :**")
        for idx, sub in others:
            idx_str = str(idx + 1)
            code_str = sub.get("code", "")
            name_str = sub.get("name", "")
            count_str = str(sub.get("count", 0))
            st.markdown("* **[" + idx_str + "]** [" + code_str + "] | " + name_str + " *(Vu : " + count_str + " fois)*")

    elif "+" in clean_cmd:
        num_part = clean_cmd.replace("+", "").strip()
        last_idx = st.session_state.last_subject_index
        sub = st.session_state.subjects[last_idx]
        
        news_idx = int(num_part) - 1 if num_part.isdigit() else 0
        news_list = sub.get("news", [])
        
        if 0 <= news_idx < len(news_list):
            item = news_list[news_idx]
            id_str = str(item.get("id", ""))
            
            st.markdown("### 🔍 Approfondissement analytique — News n°" + id_str)
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
