import random
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
                    "title": "Cartographie des irritants, immersion usager et refonte",
                    "summary": (
                        "La co-conception des services publics territoriaux connaît une mutation "
                        "profonde. L'objectif consiste à documenter l'activité réelle des usagers "
                        "à travers une observation directe des guichets et des démarches en ligne. "
                        "En identifiant précisément les moments de rupture ou de surcharge cognitive, "
                        "les collectivités parviennent à éliminer les règles superflues et à "
                        "reconcevoir des formulaires adaptés à la diversité des publics.\n\n"
                        "Consulter la source officielle : https://www.lagazettedescommunes.com/dossiers/design-actif-et-politiques-publiques/"
                    ),
                    "source": "La Gazette des Communes — https://www.lagazettedescommunes.com",
                    "confidence": "Élevé (Enquêtes de terrain métropolitains)",
                    "deep": (
                        "En sociologie des organisations, l'immersion usager permet de déconstruire "
                        "les impensés bureaucratiques. Lorsqu'une administration conçoit une procédure, "
                        "elle raisonne à partir de la tâche prescrite. L'immersion déplace la focale "
                        "vers la tâche réelle (la manière dont l'usager vit la démarche).\n\n"
                        "Sur le plan managérial, cela modifie le rôle des agents d'accueil. En analysant "
                        "les motifs de rejet, le design permet de traiter les dysfonctionnements en amont "
                        "plutôt que de faire porter aux agents la charge émotionnelle. C'est un levier "
                        "direct d'amélioration de la QVT."
                    ),
                    "linkedin": (
                        "Repenser l'action publique par le design, ce n'est pas de la cosmétique : "
                        "c'est adapter nos procédures au réel du terrain. Simplifier un formulaire, "
                        "c'est désamorcer les tensions ! 🎯 #DesignPublic #ActionPublique"
                    )
                },
                {
                    "id": 2,
                    "title": "Prototypage itératif et bacs à sable réglementaires",
                    "summary": (
                        "Le modèle traditionnel du grand projet déployé d'un coup ('big bang' "
                        "administratif) montre ses limites. Les collectivités recourent au prototypage "
                        "itératif : un service est testé quelques mois sur un périmètre restreint "
                        "(un quartier, une cohorte) pour confronter les hypothèses à la réalité. "
                        "Les retours sont intégrés au fil de l'eau avant l'engagement des crédits.\n\n"
                        "Consulter la source officielle : https://www.banquedesterritoires.fr/localtis"
                    ),
                    "source": "Banque des Territoires / Localtis — https://www.banquedesterritoires.fr/localtis",
                    "confidence": "Élevé (Projets d'expérimentation validés)",
                    "deep": (
                        "Le prototypage exige un changement de culture managériale. La culture "
                        "classique valorise la sécurité juridique absolue, conduisant à l'effet tunnel : "
                        "des mois d'ingénierie pour un dispositif inadapté au lancement.\n\n"
                        "L'expérimentation introduit le droit à l'ajustement. Pour le manager, "
                        "cela implique d'animer ses équipes autour d'un calendrier d'évaluation "
                        "continue. C'est une incertitude assumée, mais infiniment moins coûteuse "
                        "politiquement qu'un échec généralisé."
                    ),
                    "linkedin": (
                        "Pourquoi passer 2 ans à rédiger des cahiers des charges quand on peut "
                        "tester une solution en 3 mois sur le terrain ? Le prototypage est la meilleure "
                        "assurance contre l'inefficacité. 🛠️ #InnovationPublique #Agilité"
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
                    "title": "Souveraineté numérique et modèles de langage (SLM)",
                    "summary": (
                        "L'usage de l'IA générative dans les collectivités remet au premier plan la "
                        "souveraineté des données. Pour éviter le transfert de données sensibles, "
                        "les arbitrages se tournent vers des modèles de langage restreints (SLM) "
                        "hébergés sur des serveurs souverains (SecNumCloud). Ces modèles permettent "
                        "d'exploiter le traitement automatique tout en garantissant un cloisonnement.\n\n"
                        "Consulter la source officielle : https://www.dinum.gouv.fr/espace-presse/strategie-intelligence-artificielle-action-publique/"
                    ),
                    "source": "DINUM — https://www.dinum.gouv.fr",
                    "confidence": "Élevé (Cadre d'orientation de l'État)",
                    "deep": (
                        "L'architecture privilégiée repose sur la méthode RAG (Retrieval-Augmented "
                        "Generation). Elle permet à l'algorithme de ne répondre qu'à partir des "
                        "documents transmis par la collectivité (PLUi, délibérations), limitant "
                        "les hallucinations et assurant la traçabilité.\n\n"
                        "D'un point de vue managérial, l'IA doit être un outil de pré-traitement. "
                        "L'appréciation du contexte local et la responsabilité juridique demeurent "
                        "l'exclusivité absolue de l'agent public."
                    ),
                    "linkedin": (
                        "L'IA dans les collectivités oui, mais pas à n'importe quel prix ! "
                        "Déployer des modèles souverains est la seule voie pour moderniser nos "
                        "services sans sacrifier la confidentialité. 🤖🔒 #IAGenerative"
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
                    "title": "Robustesse organisationnelle et fin des flux tendus",
                    "summary": (
                        "Inspirée des travaux du biologiste Olivier Hamant, la robustesse remet en "
                        "cause le modèle axé sur l'optimisation maximale. Dans un monde de chocs "
                        "systémiques, une organisation poussée à son niveau de performance maximal "
                        "devient rigide et s'effondre. La robustesse préconise d'intégrer de la "
                        "redondance et des temps de respiration pour maintenir le service public.\n\n"
                        "Consulter la source officielle : https://www.inrae.fr/actualites/olivier-hamant-construire-monde-robuste"
                    ),
                    "source": "INRAE / ENS Lyon — https://www.inrae.fr",
                    "confidence": "Élevé (Recherche académique pluridisciplinaire)",
                    "deep": (
                        "La transposition de la biologie évolutive au management offre une grille "
                        "féconde. Les systèmes qui durent ne sont pas les plus 'performants' à "
                        "l'instant T, mais les plus adaptables. L'optimisation à outrance supprime "
                        "toute souplesse opérationnelle.\n\n"
                        "Créer de la robustesse consiste à réintroduire de la diversité de compétences, "
                        "à tolérer une 'lenteur protectrice' dans les vérifications, et à maintenir "
                        "des marges de manœuvre. Cela suppose de déconstruire le dogme de la "
                        "performance à court terme."
                    ),
                    "linkedin": (
                        "La recherche d'optimisation maximale rend nos organisations fragiles. "
                        "Face aux incertitudes climatiques, développons la robustesse de nos "
                        "services publics : plus de marges, moins de flux tendus ! 🌿 #Robustesse"
                    )
                }
            ]
        }
    ]

    codes_restants = [
        ("AP-TRA", "Politiques de transition", "France Stratégie", "https://www.strategie.gouv.fr/publications/evaluation-des-politiques-de-transition"), 
        ("SHS-SOC", "Sociologie des pratiques", "CNRS", "https://www.rfs-revue.fr"),
        ("AP-ACC", "Accompagnement au changement", "Anact", "https://www.anact.fr/outils-et-methodes/conduite-du-changement"), 
        ("LIT-ANT", "Anti-lyrisme", "Éditions Gallimard", "https://www.gallimard.fr"),
        ("AP-ACH", "Achat public responsable", "AEF Info", "https://www.aefinfo.fr"), 
        ("TER-INN", "Innovation territoriale", "La Fabrique de la Cité", "https://www.lafabriquedelacite.com"), 
        ("TRA-TER", "Transition territoriale", "Cerema", "https://www.cerema.fr/fr/actualites/adaptation-territoires"), 
        ("SHS-ESS", "Essais SHS", "OpenEdition", "https://www.openedition.org"), 
        ("SHS-COM", "Psychologie sociale", "Cairn Info", "https://www.cairn.info"), 
        ("EVE-ECO", "Événements écoresponsables", "ADEME", "https://www.ademe.fr/guide-eco-evenement"),
        ("TEC-TRA", "Tech & Transitions", "The Shift Project", "https://theshiftproject.org/categorie/numerique-sobre/"), 
        ("SAN-ALI", "Santé & Alimentation", "ANSES", "https://www.anses.fr/fr/content/alimentation-et-sante-publique"), 
        ("AP-ALI", "Alimentation durable", "Min. Agriculture", "https://agriculture.gouv.fr/pat-projets-alimentaires-territoriaux"), 
        ("TEC-OPS", "Open source collaboratif", "ADULLACT", "https://adullact.org"), 
        ("TEC-VEI", "Veille & Productivité", "INA", "https://www.ina.fr"), 
        ("CUL-BIB", "Innovation en bibliothèque", "Enssib", "https://bbf.enssib.fr"), 
        ("TER-MON", "Mons-en-Barœul", "Ville de Mons", "https://www.monsenbaroeul.fr"), 
        ("CUL-CIN", "Cinéma & Séries", "Cahiers du Cinéma", "https://www.cahiersducinema.com")
    ]

    for code, nom, source_nom, url_lien in codes_restants:
        data.append({
            "code": code,
            "name": nom,
            "news": [
                {
                    "id": 1,
                    "title": "Évolutions stratégiques et retours de terrain : " + nom,
                    "summary": (
                        "Les mutations politiques et réglementaires sur la thématique '" + nom + "' "
                        "connaissent une accélération marquée. Les directions doivent articuler "
                        "adaptation écologique et maintien du service. L'analyse met en évidence "
                        "l'importance d'un pilotage clair pour éviter la saturation des équipes.\n\n"
                        "Consulter la source officielle : " + url_lien
                    ),
                    "source": source_nom + " — " + url_lien,
                    "confidence": "Moyen (Rapports en cours de consolidation)",
                    "deep": (
                        "L'analyse approfondie sous l'angle des sciences humaines révèle des "
                        "tensions structurelles. La mise en œuvre se heurte aux 'injonctions "
                        "paradoxales' : les cadres doivent innover tout en respectant des carcans "
                        "stricts, ou mener la transition en réduisant les coûts.\n\n"
                        "La levée des freins passe par la reconstruction du sens du travail. "
                        "Cela suppose d'associer directement les agents aux priorités opérationnelles "
                        "et d'accepter de déprogrammer les actions secondaires."
                    ),
                    "linkedin": (
                        "Sur le sujet '" + nom + "', l'enjeu majeur est de décloisonner nos "
                        "organisations et donner du pouvoir d'agir aux équipes de terrain. 🚀 "
                        "#ActionPublique #Transitions"
                    )
                }
            ]
        })

    for d in data:
        d["count"] = 0
        
    return data


# --- GESTION DE LA SESSION ---
if "APP_VERSION_9" not in st.session_state:
    st.session_state.clear()
    st.session_state["APP_VERSION_9"] = True
    st.session_state.subjects = charger_donnees()
    st.session_state.last_subject_index = 0

# --- INTERFACE UTILISATEUR ---
st.title("🌱 Ton Veilleur Principal")
st.markdown("*Une veille analytique, documentée et conçue pour l'action.*")

cmd = st.text_input(
    "Commande",
    placeholder="Tape un N°, un [CODE], 1+, 1linkedin...",
    label_visibility="collapsed",
)

st.button("Valider")

clean_cmd = cmd.strip().upper().replace("[", "").replace("]", "")

# --- ROUTAGE DES COMMANDES (PLAT, SANS TRY/EXCEPT) ---

if not clean_cmd or clean_cmd == "VEILLE":
    sorted_subs = sorted(
        enumerate(st.session_state.subjects), 
        key=lambda x: x[1].get("count", 0)
    )
    focus = sorted_subs[:2]
    others = sorted_subs[2:]
    random.shuffle(others)

    st.markdown("🎯 **Ce que je te suggère aujourd'hui (Sujets peu explorés récents) :**")
    for idx, sub in focus:
        idx_str = str(idx + 1)
        code_str = sub.get("code", "")
        name_str = sub.get("name", "")
        count_str = str(sub.get("count", 0))
        st.markdown("* **[" + idx_str + "]** [" + code_str + "] | " + name_str + " *(Consulté : " + count_str + " fois)*")

    st.markdown("📋 **Le reste de tes thématiques actives :**")
    for idx, sub in others:
        idx_str = str(idx + 1)
        code_str = sub.get("code", "")
        name_str = sub.get("name", "")
        count_str = str(sub.get("count", 0))
        st.markdown("* **[" + idx_str + "]** [" + code_str + "] | " + name_str + " *(Consulté : " + count_str + " fois)*")

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
        
        src_str = "📌 **Source et référence d'analyse :** " + str(item.get("source", ""))
        st.markdown(src_str)
    else:
        code_str = sub.get("code", "")
        st.error("Actualité n°" + num_part + " introuvable dans le bulletin " + code_str)

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
        
        st.markdown("### 💼 Proposition de publication LinkedIn — News n°" + id_str)
        st.success(item.get("linkedin", ""))
        
        src_str = "📌 **Source à citer :** " + str(item.get("source", ""))
        st.markdown(src_str)
    else:
        st.error("Aucune actualité n°" + num_part + " disponible pour cette publication.")

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
        
        st.markdown("## 📰 Bulletin d'Actualité : " + nom_str + " (`" + code_str + "`)")
        st.markdown("*Consulté " + count_str + " fois au total.*")
        st.markdown("---")
        
        for item in selected_sub.get("news", []):
            id_str = str(item.get("id", ""))
            title_str = item.get("title", "")
            st.markdown("### **" + id_str + ". " + title_str + "**")
            st.markdown(item.get("summary", ""))
            
            src_str = str(item.get("source", ""))
            conf_str = str(item.get("confidence", ""))
            st.markdown("→ **Source :** " + src_str + " | 📊 Confiance : [" + conf_str + "]")
            st.markdown("---")
    else:
        st.warning("Commande non reconnue. Tape un numéro de sujet (ex: 1), un code (ex: AP-DES), ou un approfondissement (ex: 1+).")


st.markdown("---")
st.markdown("## 🎛️ Ta boîte à outils")
st.markdown("**Changer de sujet** — Tape un numéro de sujet ou son `[Code]`.")
st.markdown("**Creuser une news** — Tape `[N°]+` pour l'analyse stratégique (ex: `1+` ou `2+`).")
st.markdown("**Post LinkedIn** — Tape `[N°]linkedin` (ex: `1linkedin`).")
