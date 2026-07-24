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
                    "title": "Cartographie des irritants, immersion usager et refonte des parcours d'accueil",
                    "summary": """La co-conception des services publics territoriaux connaît une mutation profonde. Les démarches actuelles abandonnent les simples boîtes à idées ou les consultations citoyennes de surface pour s'imposer comme un outil rigoureux d'ingénierie publique. L'objectif consiste à documenter l'activité réelle des usagers à travers une observation directe et participante des guichets, des démarches en ligne et de la gestion des réclamations. En identifiant précisément les moments de rupture, de confusion ou de surcharge cognitive dans la constitution des dossiers, les collectivités parviennent à éliminer les règles administratives superflues et à reconcevoir des formulaires véritablement adaptés à la diversité des publics, notamment les plus éloignés du numérique.

Consulter la source officielle : https://www.lagazettedescommunes.com/dossiers/design-actif-et-politiques-publiques/""",
                    "source": "La Gazette des Communes — https://www.lagazettedescommunes.com",
                    "confidence": "Élevé (Enquêtes de terrain et retours d'expériences métropolitains)",
                    "deep": """L'analyse en sociologie des organisations démontre que l'immersion usager permet de déconstruire les impensés bureaucratiques ancrés dans les habitudes de service. Lorsqu'une administration conçoit une procédure, elle raisonne presque toujours à partir de la *tâche prescrite* (les textes juridiques et les contraintes logicielles). L'immersion déplace la focale vers la *tâche réelle* (la manière dont l'usager, confronté à sa précarité, sa maîtrise de la langue ou sa maîtrise technique, vit la démarche). 

Sur le plan du management d'équipe, cette méthode modifie radicalement le rôle des agents d'accueil. En analysant conjointement les motifs de rejet de dossiers et la récurrence des incivilités aux guichets, la démarche de design permet de traiter les dysfonctionnements organisationnels amont plutôt que de faire porter aux seuls agents de première ligne la charge émotionnelle de la frustration des usagers. Simplifier le parcours administratif constitue ainsi un levier direct d'amélioration des conditions de travail (QVT) et de prévention des risques psychosociaux (RPS).""",
                    "linkedin": """Repenser l'action publique par le design, ce n'est pas faire de la cosmétique : c'est refuser la complexité bureaucratique pour adapter nos procédures au réel du terrain. Simplifier un formulaire ou repenser un accueil, c'est désamorcer les tensions et redonner du sens au service public ! 🎯 #DesignPublic #InnovationTerritoriale #ActionPublique"""
                },
                {
                    "id": 2,
                    "title": "Prototypage itératif, expérimentation locale et bacs à sable réglementaires",
                    "summary": """Face à la multiplicité des crises territoriales, le modèle traditionnel du grand projet pluriannuel déployé d'un coup (le 'big bang' administratif) montre ses limites. Les collectivités territoriales recourent désormais au prototypage itératif : un service public ou un dispositif nouveau est testé pendant quelques mois sur un périmètre restreint (un quartier, une mairie annexe, une cohorte ciblée) afin de confronter les hypothèses de travail à la réalité du terrain. Les retours d'expérience sont intégrés au fil de l'eau pour corriger les bugs d'usage avant tout déploiement à grande échelle et avant l'engagement définitif des crédits budgétaires.

Consulter la source officielle : https://www.banquedesterritoires.fr/localtis""",
                    "source": "Banque des Territoires / Localtis — https://www.banquedesterritoires.fr/localtis",
                    "confidence": "Élevé (Projets d'expérimentation validés)",
                    "deep": """Le passage au prototypage itératif exige un changement de culture managériale profond au sein des directions métiers. La culture administrative classique valorise la sécurité juridique absolue et l'exhaustivité préalable, ce qui conduit fréquemment à l'effet tunnel : des mois d'ingénierie en chambre pour concevoir un dispositif qui s'avère partiellement inadapté lors de son lancement.

L'expérimentation par bacs à sable réglementaires introduit le *droit à l'ajustement*. Pour le primo-manager ou le directeur, cela implique d'animer ses équipes non plus autour d'un livrable figé, mais autour d'un calendrier d'évaluation continue. Cette posture requiert une grande clarté vis-à-vis des élus : tester à petite échelle comporte une part d'incertitude assumeé, mais cette incertitude est infiniment moins coûteuse politiquement et financièrement qu'un échec de déploiement généralisé.""",
                    "linkedin": """Pourquoi passer deux ans à rédiger des cahiers des charges complexes en chambre quand on peut tester une solution en trois mois sur le terrain ? Le prototypage à petite échelle est la meilleure assurance contre l'inefficacité publique. 🛠️ #InnovationPublique #Agilité #Territoires"""
                }
            ]
        },
        {
            "code": "TEC-IAG",
            "name": "IA Générative",
            "news": [
                {
                    "id": 1,
                    "title": "Souveraineté numérique, modèles de langage souverains et conformité RGPD",
                    "summary": """L'accélération de l'usage de l'intelligence artificielle générative dans les grandes collectivités locales remet au premier plan la question de la souveraineté des données. Pour éviter le transfert de données administratives, foncières ou nominatives vers des infrastructures soumises à des législations extraterritoriales, les arbitrages se tournent vers le déploiement de modèles de langage restreints (SLM - Small Language Models) hébergés sur des serveurs souverains ou des clouds qualifiés SecNumCloud. Ces modèles, entraînés ou affinés spécifiquement sur les corpus réglementaires français et territoriaux, permettent aux agents d'exploiter la puissance du traitement automatique du langage tout en garantissant un cloisonnement hermétique.

Consulter la source officielle : https://www.dinum.gouv.fr/espace-presse/strategie-intelligence-artificielle-action-publique/""",
                    "source": "DINUM (Direction Interministérielle du Numérique) — https://www.dinum.gouv.fr",
                    "confidence": "Élevé (Cadre d'orientation de l'État)",
                    "deep": """L'architecture technique privilégiée repose sur le couplage entre un modèle de langage et une base de connaissances métier via la méthode RAG (*Retrieval-Augmented Generation*). Cette technique permet à l'algorithme de ne répondre qu'à partir des documents transmis par la collectivité (PLUi, délibérations, synthèses budgétaires, arrêtés), limitant drastiquement les risques d'hallucination et assurant la traçabilité de chaque affirmation par la citation explicite du paragraphe source.

D'un point de vue managérial et sociologique, la gouvernance de ces outils impose une clarification des responsabilités. L'IA générative doit être strictement positionnée comme un outil de pré-traitement ou de pré-rédaction. La validation finale, l'appréciation du contexte politique local et la responsabilité juridique de tout document produit demeurent l'exclusivité absolue de l'agent public assermenté.""",
                    "linkedin": "L'IA dans les collectivités oui, mais pas à n'importe quel prix ! Déployer des modèles souverains et sécurisés est la seule voie pour moderniser nos services sans sacrifier la confidentialité de nos données publiques. 🤖🔒 #IAGenerative #DataResponsable #ServicePublic"
                }
            ]
        },
        {
            "code": "IDE-ROB",
            "name": "Robustesse (O. Hamant)",
            "news": [
                {
                    "id": 1,
                    "title": "Robustesse organisationnelle, fin des flux tendus et écologie des services",
                    "summary": """Inspirée directement des travaux du biologiste Olivier Hamant, la notion de robustesse remet en cause le modèle managérial dominant axé sur l'optimisation maximale, l'efficience à tout prix et la gestion en flux tendus. Dans un monde caractérisé par des chocs systémiques répétés (dérèglement climatique, crises sanitaires, tensions sur les ressources, incertitudes financières), une organisation publique poussée à son niveau de performance maximal devient rigide et s'effondre à la moindre perturbation. La robustesse préconise au contraire d'intégrer de la redondance, des stocks stratégiques et des temps de respiration pour maintenir le service public en mode dégradé ou fluctuant.

Consulter la source officielle : https://www.inrae.fr/actualites/olivier-hamant-construire-monde-robuste""",
                    "source": "INRAE / École Normale Supérieure de Lyon — https://www.inrae.fr",
                    "confidence": "Élevé (Travaux de recherche académique pluridisciplinaires)",
                    "deep": """La transposition des principes de la biologie évolutive au management public offre une grille d'analyse d'une grande fécondité. Les systèmes biologiques qui traversent les âges ne sont pas ceux qui sont le plus 'performants' à un instant T dans un environnement stable, mais ceux qui sont les plus *adaptables* dans un environnement instable. L'optimisation à outrance (diminution des effectifs au strict minimum, suppression de toutes les étapes de vérification jugées 'non rentables', mutualisation poussée à l'extrême) supprime toute la souplesse opérationnelle d'une direction.

Créer de la robustesse dans un service municipal de 5 000 agents consiste à réintroduire de la diversité de compétences (éviter les monopoles de savoir sur un poste unique), à tolérer une part de 'lenteur protectrice' dans la vérification des projets d'aménagement, et à maintenir des marges de manœuvre physiques ou budgétaires non affectées. Cela suppose de déconstruire le dogme de la performance budgétaire à court terme pour valoriser la continuité du service sur le long terme.""",
                    "linkedin": "La recherche d'optimisation maximale et le culte de la performance à court terme rendent nos organisations fragiles. Pour faire face aux incertitudes climatiques et sociales, nous devons développer la robustesse de nos services publics : plus de diversité, plus de marges de manœuvre, moins de flux tendus ! 🌿 #Robustesse #ManagementPublic #Transitions"
                }
            ]
        }
    ]

    codes_restants = [
        ("AP-TRA", "Politiques de transition", "France Stratégie", "https://www.strategie.gouv.fr/publications/evaluation-des-politiques-de-transition"), 
        ("SHS-SOC", "Sociologie des pratiques", "CNRS / Revue Française de Sociologie", "https://www.rfs-revue.fr"),
        ("AP-ACC", "Accompagnement au changement", "Anact", "https://www.anact.fr/outils-et-methodes/conduite-du-changement"), 
        ("LIT-ANT", "Anti-lyrisme", "Éditions Gallimard / Études stylistiques", "https://www.gallimard.fr"),
        ("AP-ACH", "Achat public responsable", "AEF Info / Commande publique", "https://www.aefinfo.fr"), 
        ("TER-INN", "Innovation territoriale", "La Fabrique de la Cité", "https://www.lafabriquedelacite.com"), 
        ("TRA-TER", "Transition territoriale", "Cerema", "https://www.cerema.fr/fr/actualites/adaptation-territoires"), 
        ("SHS-ESS", "Essais SHS", "OpenEdition Journals", "https://www.openedition.org"), 
        ("SHS-COM", "Psychologie sociale", "Cairn Info", "https://www.cairn.info"), 
        ("EVE-ECO", "Événements écoresponsables", "ADEME", "https://www.ademe.fr/guide-eco-evenement"),
        ("TEC-TRA", "Tech & Transitions", "The Shift Project", "https://theshiftproject.org/categorie/numerique-sobre/"), 
        ("SAN-ALI", "Santé & Alimentation", "ANSES", "https://www.anses.fr/fr/content/alimentation-et-sante-publique"), 
        ("AP-ALI", "Alimentation durable", "Ministère de l'Agriculture", "https://agriculture.gouv.fr/pat-projets-alimentaires-territoriaux"), 
        ("TEC-OPS", "Open source collaboratif", "ADULLACT", "https://adullact.org"), 
        ("TEC-VEI", "Veille & Productivité", "INA", "https://www.ina.fr"), 
        ("CUL-BIB", "Innovation en bibliothèque", "Enssib / BBF", "https://bbf.enssib.fr"), 
        ("TER-MON", "Mons-en-Barœul", "Ville de Mons-en-Barœul", "https://www.monsenbaroeul.fr"), 
        ("CUL-CIN", "Cinéma & Séries", "Cahiers du Cinéma", "https://www.cahiersducinema.com")
    ]

    for code, nom, source_nom, url_lien in codes_restants:
        data.append({
            "code": code,
            "name": nom,
            "news": [
                {
                    "id": 1,
                    "title": "Évolutions stratégiques, cadres opérationnels et retours de terrain : " + nom,
                    "summary": f"""Les mutations politiques, réglementaires et environnementales relatives à la thématique '{nom}' connaissent une accélération marquée dans la gestion des grandes collectivités territoriales. Les directions opérationnelles doivent articuler des impératifs d'adaptation écologique, de maîtrise des ressources budgétaires et de maintien de la qualité du service rendu. L'analyse des retours d'expérience locaux met en évidence l'importance d'un pilotage clair pour éviter la saturation des équipes face à l'empilement des procédures.

Consulter la source officielle : {url_lien}""",
                    "source": f"{source_nom} — {url_lien}",
                    "confidence": "Moyen (Rapports thématiques en cours de consolidation)",
                    "deep": f"""L'analyse approfondie de cette thématique sous l'angle des sciences humaines et de la sociologie des organisations révèle des tensions structurelles récurrentes. La mise en œuvre des directives sur le terrain se heurte souvent à ce que la recherche nomme les 'injonctions paradoxales' : les cadres de proximité sont sommés d'innover tout en respectant des carcans réglementaires stricts, ou de mener la transition tout en réduisant leurs coûts de fonctionnement.

Pour débloquer ces situations d'inertie, la levée des freins ne passe pas par l'injonction managériale descendante, mais par la reconstruction du sens du travail. Cela suppose d'animer des espaces de régulation au sein des services, d'associer directement les agents de terrain à la définition des priorités opérationnelles et d'accepter de déprogrammer les actions secondaires pour concentrer les moyens sur l'essentiel.""",
                    "linkedin": f"""Sur le sujet '{nom}', l'enjeu majeur ne réside pas dans les grands discours, mais dans la capacité à décloisonner nos organisations et à donner du pouvoir d'agir aux équipes de terrain. L'action publique gagne en efficacité quand elle s'ancre dans la réalité quotidienne ! 🚀 #ActionPublique #Transitions #Management"""
                }
            ]
        })

    for d in data:
        d["count"] = 0
        
    return data

if "APP_VERSION_8" not in st.session_state:
    st.session_state.clear()
    st.session_state["APP_VERSION_8"] = True
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
            
            fo
