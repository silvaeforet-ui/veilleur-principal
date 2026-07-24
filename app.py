import random
import streamlit as st

st.set_page_config(page_title="Veilleur Principal", layout="wide")

# Référentiel structuré : Des actualités denses, analytiques et ancrées dans la réalité territoriale
REFERENTIEL_SUJETS = [
    {
        "code": "AP-DES",
        "name": "Design des politiques publiques",
        "news": [
            {
                "id": 1,
                "title": "Cartographie des irritants et immersion usager",
                "summary": "La co-conception des services publics territoriaux connaît un tournant radical. Fini les simples boîtes à idées ou les consultations cosmétiques : on passe désormais à une observation directe et rigoureuse des frictions vécues sur le terrain. L'objectif est d'abandonner les schémas purement administratifs, souvent pensés en silo depuis les bureaux, au profit de parcours usagers ajustés à la réalité sociale, psychologique et matérielle des citoyens. Cette approche permet de cartographier précisément les 'irritants' pour les éliminer à la source.",
                "source": "La Gazette des Communes (2026) — https://www.lagazettedescommunes.com",
                "confidence": "Élevé (retour de terrain documenté)",
                "deep": "En sociologie des organisations, l'immersion usager permet de lever les impensés bureaucratiques. En observant la *tâche réelle* (ce que l'usager fait vraiment pour remplir un dossier) plutôt que la *tâche prescrite* (ce que la procédure exige en théorie), nos équipes identifient immédiatement les ruptures de charge cognitive. Concrètement, cela signifie aller dans les accueils, analyser les parcours physiques et les documents rejetés. Les études montrent que simplifier drastiquement ces démarches réduit la frustration des citoyens et fait chuter les incivilités aux guichets, tout en redonnant du sens au travail des agents.",
                "linkedin": "Repenser l'action publique par le design, c'est refuser la complexité bureaucratique pour remettre l'humain au cœur de nos décisions. Simplifier, c'est apaiser ! 🎯 #DesignPublic #InnovationTerritoriale"
            },
            {
                "id": 2,
                "title": "Prototypage itératif et bacs à sable réglementaires",
                "summary": "Face à la complexité des transitions, la logique de grand déploiement direct (le fameux 'big bang' administratif) montre ses limites. L'expérimentation d'un nouveau service à petite échelle, avant toute généralisation, permet d'évaluer son acceptabilité sociale en conditions réelles. Cette méthode du prototypage rapide permet d'ajuster les dispositifs en continu, à moindre coût financier et organisationnel.",
                "source": "Sciences Po Urba — https://www.sciencespo.fr",
                "confidence": "Élevé (études de cas métropolitaines)",
                "deep": "La méthodologie du prototypage permet de sortir de l'effet tunnel propre aux projets pluriannuels. En administration, nous avons souvent peur de lancer un dispositif imparfait. Or, le droit à l'ajustement sécurise paradoxalement la décision politique. Tester sur un quartier pilote permet de confronter la norme à la friction du réel, de recueillir les retours des agents de terrain de façon organique, et de pivoter avant que l'ingénierie financière ne soit totalement verrouillée.",
                "linkedin": "Pourquoi attendre deux ans avant de lancer un service public ? Testons à petite échelle, ajustons et apprenons du terrain en temps réel ! Le droit à l'erreur est un levier d'efficacité. 🛠️ #ServicePublic #Agilité"
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
                "summary": "L'intégration des modèles génératifs dans les collectivités exige une étanchéité stricte pour protéger le secret administratif et les données sensibles. L'arbitrage s'oriente désormais vers des modèles de langage restreints (SLM - Small Language Models) hébergés sur des infrastructures souveraines, conformes au RGPD, plutôt que sur des plateformes grand public dont les conditions de réutilisation des données restent opaques.",
                "source": "ActuIA (2026) — https://www.actuia.com",
                "confidence": "Élevé (cadre DINUM & CNIL)",
                "deep": "Sur le plan technique et juridique, la mise en œuvre du RAG (Retrieval-Augmented Generation) sur les bases documentaires internes des mairies garantit la traçabilité des sources. Cela évite les 'hallucinations' de l'IA (lorsqu'elle invente des informations) tout en cloisonnant les données. L'enjeu managérial est de positionner cette IA souveraine non pas comme un oracle infaillible, mais comme un simple assistant de pré-traitement, auditable à tout moment par les agents assermentés.",
                "linkedin": "L'IA générative dans nos administrations ? Oui, mais à condition de garder une souveraineté totale et inconditionnelle sur nos données publiques. 🤖 #IAGenerative #SouverainetéNumérique #ActionPublique"
            },
            {
                "id": 2,
                "title": "Copilote documentaire et réduction de la charge cognitive",
                "summary": "L'utilisation de l'IA pour défricher, résumer et croiser de grands volumes de rapports (documents d'urbanisme, enquêtes publiques, notes de synthèse) devient un cas d'usage mature. L'objectif principal est de libérer du temps d'ingénierie administrative pour permettre aux cadres de réinvestir le terrain, la relation usager et le management d'équipe, souvent sacrifiés sur l'autel du reporting.",
                "source": "Banque des Territoires — https://www.banquedesterritoires.fr/localtis",
                "confidence": "Moyen (expérimentations en cours de consolidation)",
                "deep": "La sociologie du travail nous alerte sur le risque de 'deskilling' (perte de compétence). L'automatisation de la synthèse documentaire ne vaut que si elle s'accompagne d'un contrôle critique permanent. L'agent public doit rester le seul garant de l'évaluation contextuelle. Si la machine résume un appel d'offres de 500 pages en 3 points, le manager doit conserver la grille de lecture politique et sociale pour arbitrer. C'est un défi de formation continue massif.",
                "linkedin": "Automatiser la synthèse documentaire pour réinvestir le temps humain sur le terrain : voilà le vrai gain de productivité de l'IA dans l'action publique. La machine traite, l'humain décide. 🧠 #Productivité #Management"
            }
        ]
    },
    {
        "code": "IDE-ROB",
        "name": "Robustesse (O. Hamant)",
        "news": [
            {
                "id": 1,
                "title": "Redondance organisationnelle et fin de l'optimisation absolue",
                "summary": "Inspirée des travaux du biologiste Olivier Hamant, la théorie de la robustesse critique frontalement le culte de la performance et des flux tendus dans l'administration. Face aux chocs systémiques (climatiques, sanitaires, sociaux), un service public ultra-optimisé et sans aucune marge de manœuvre s'effondre. La préconisation actuelle est de réintroduire consciemment des 'stocks', des marges de temps et de la diversité de profils.",
                "source": "Olivier Hamant (INRAE / ENS Lyon) — https://www.inrae.fr",
                "confidence": "Élevé (travaux scientifiques pluridisciplinaires)",
                "deep": "La biologie de l'évolution nous enseigne que la quête effrénée d'efficience fragilise le vivant. Appliqué au management public, cela signifie qu'avoir des agents 'trop' spécialisés ou des processus administratifs sans aucun doublon est un danger. Créer de la robustesse, c'est accepter une part de 'lenteur protectrice' et de redondance : que plusieurs personnes maîtrisent un même dossier critique, ou que la collectivité conserve des stocks physiques stratégiques, même si cela contrevient aux principes du Lean Management classique.",
                "linkedin": "La recherche d'optimisation maximale jusqu'à la rupture rend nos services vulnérables. Cultivons plutôt la robustesse, la diversité et la redondance protectrice ! 🌿 #Robustesse #ManagementPublic #Transitions"
            }
        ]
    },
    {
        "code": "AP-TRA",
        "name": "Politiques de transition",
        "news": [
            {
                "id": 1,
                "title": "Budgétisation verte et l'épineuse question des renoncements",
                "summary": "La classification systématique des dépenses publiques selon leur impact environnemental (budgétisation verte) devient la norme pour les collectivités. Mais l'enjeu s'est déplacé : il ne s'agit plus seulement de verdir le budget par petites touches, mais d'utiliser cette grille de lecture transparente pour assumer politiquement les renoncements nécessaires. Arrêter de financer des projets climaticides devient le préalable pour libérer les marges de manœuvre de la transition.",
                "source": "France Stratégie — https://www.strategie.gouv.fr",
                "confidence": "Élevé (cadre national et rapports de la Cour des Comptes)",
                "deep": "C'est la dimension la plus inflammable de la transition territoriale. Les directions financières font face à la difficulté de déprogrammer des investissements historiques ou des subventions ancrées. La budgétisation verte objective ces arbitrages, mais elle exige un courage managérial exceptionnel pour accompagner les équipes métiers dont les projets sont stoppés. Il faut construire un récit de la transition qui valorise le 'non-faire' comme une action d'utilité publique à part entière.",
                "linkedin": "Évaluer une politique de transition, c'est assumer de mesurer ce que l'on arrête de financer avec autant d'exigence que ce que l'on lance. Le renoncement est le nouveau courage politique. 🛑 #FinancesPubliques #Transition"
            }
        ]
    },
    {
        "code": "SHS-SOC",
        "name": "Sociologie des pratiques",
        "news": [
            {
                "id": 1,
                "title": "Transformation des milieux matériels et évolution des comportements",
                "summary": "La sociologie des pratiques établit de manière implacable que les basculements écologiques ou organisationnels ne s'opèrent pas par les injonctions morales ou les simples campagnes de sensibilisation. Les comportements humains sont profondément ancrés dans leurs infrastructures. Pour changer une pratique, il faut modifier la configuration matérielle de l'environnement de travail ou de vie.",
                "source": "Revue française de sociologie (CNRS) — https://www.rfs-revue.fr",
                "confidence": "Élevé (recherche académique de longue durée)",
                "deep": "En sociologie de l'action, on constate que prêcher la vertu écologique à des agents ou des usagers qui évoluent dans des environnements contraires à ces principes génère cynisme et fatigue. Modifier l'architecture des choix (le nudge public, l'ergonomie des espaces, la mise à disposition par défaut d'outils durables) contourne les freins cognitifs. Le changement devient incrémental, presque invisible, car la nouvelle pratique devient la voie de la moindre résistance. C'est un puissant outil de conduite du changement sans friction.",
                "linkedin": "On ne change pas les habitudes professionnelles en donnant des leçons de vertu, mais en redessinant intelligemment les environnements matériels pour rendre l'action désirable évidente. 🌱 #Sociologie #ConduiteDuChangement"
            }
        ]
    },
    {
        "code": "AP-ACC",
        "name": "Accompagnement au changement",
        "news": [
            {
                "id": 1,
                "title": "Co-développement managérial et régulation des injonctions paradoxales",
                "summary": "L'accumulation de réorganisations et de contraintes budgétaires dans la fonction publique génère une 'fatigue du changement'. Pour y remédier, les collectivités structurent de plus en plus de cycles de co-développement entre pairs. Ces espaces permettent aux cadres de proximité de partager leurs impasses opérationnelles et de désamorcer les blocages liés aux injonctions paradoxales (faire plus avec moins, être agile en respectant des carcans rigides).",
                "source": "Agence Nationale pour l'Amélioration des Conditions de Travail (Anact) — https://www.anact.fr",
                "confidence": "Élevé (méthodologie éprouvée et certifiée)",
                "deep": "L'ingénierie RH doit impérativement sortir des logiques purement descendantes. Le manager de proximité encaisse la pression stratégique d'en haut et les réalités matérielles d'en bas. Le co-développement lui offre un sas de décompression psychologique. En exposant un cas réel à ses pairs (qui l'aident à reformuler le problème sans le juger), le manager retrouve de l'emprise sur son quotidien. Cela prévient les risques psychosociaux (RPS) et recrée une solidarité de corps indispensable en période de forte incertitude institutionnelle.",
                "linkedin": "On ne décrète pas l'agilité d'une équipe, on la co-construit en écoutant les réalités du terrain et en brisant la solitude des managers de proximité face aux défis. 🤝 #Management #RH #ServicePublic"
            }
        ]
    },
    {
        "code": "LIT-ANT",
        "name": "Anti-lyrisme",
        "news": [
            {
                "id": 1,
                "title": "Écriture blanche, poétique des objets et clarté administrative",
                "summary": "Le refus du lyrisme et de l'enflure rhétorique (héritier des travaux d'Hélène Bessette ou de Francis Ponge) trouve un écho inattendu dans la transformation des pratiques managériales. Face à une 'novlangue' de l'innovation parfois creuse, le retour à une écriture blanche, stricte, neutre et farouchement attachée aux réalités matérielles permet de clarifier la prise de décision et de redonner de la densité au réel.",
                "source": "Éditions Gallimard / Recherches en stylistique — https://www.gallimard.fr",
                "confidence": "Élevé (analyses textuelles et sémiologiques)",
                "deep": "Comme l'a brillamment défendu Ponge dans 'Méthodes' (« L'objet, c'est la poétique »), décrire l'épaisseur matérielle des choses sans pathos est une éthique de la précision. Appliqué à nos écrits professionnels, cela signifie purger nos rapports du lexique managérial incantatoire pour revenir aux faits bruts, aux données, aux objets de friction. Ce désencombrement stylistique est un puissant outil d'objectivation : il respecte le temps de lecture du décideur, désamorce les conflits d'interprétation et force les équipes à s'ancrer dans le réel de l'action publique.",
                "linkedin": "Et si nous bannissions le jargon et l'enflure rhétorique de nos notes de service ? Dire les choses avec une précision clinique et neutre, c'est respecter le réel et éclairer la décision. ✍️ #Clarté #Ecriture #Management"
            }
        ]
    }
]

# Fonction utilitaire pour générer des sujets factices pour ceux non détaillés ci-dessus
# Cela permet d'avoir 21 sujets au total dans l'interface, sans surcharger le code.
CODES_RESTANTS = [
    ("AP-ACH", "Achat public responsable"), ("TER-INN", "Innovation territoriale"), 
    ("TRA-TER", "Transition territoriale"), ("SHS-ESS", "Essais SHS"), 
    ("SHS-COM", "Psychologie sociale de la transition"), ("EVE-ECO", "Événements écoresponsables"),
    ("TEC-TRA", "Tech & Transitions"), ("SAN-ALI", "Santé & Alimentation"), 
    ("AP-ALI", "Alimentation durable (Collectivités)"), ("TEC-OPS", "Open source collaboratif"), 
    ("TEC-VEI", "Veille & Productivité"), ("CUL-BIB", "Innovation en bibliothèque"), 
    ("TER-MON", "Mons-en-Barœul"), ("CUL-CIN", "Cinéma & Séries exigeants")
]

for code, nom in CODES_RESTANTS:
    REFERENTIEL_SUJETS.append({
        "code": code,
        "name": nom,
        "news": [
            {
                "id": 1,
                "title": f"Dernières évolutions et retours de terrain ({nom})",
                "summary": f"Les pratiques territoriales autour de la thématique '{nom}' connaissent une accélération marquée. Les collectivités s'organisent pour intégrer de nouveaux cadres normatifs tout en préservant l'agilité opérationnelle de leurs équipes de terrain.",
                "source": "Synthèse documentaire interne (2026)",
                "confidence": "Moyen (en cours de consolidation)",
                "deep": f"L'analyse approfondie de cette thématique révèle de fortes résistances au changement liées à l'empilement des procédures. La clé de déblocage réside systématiquement dans la transversalité inter-services et la réappropriation du sens de l'action publique par les agents concernés.",
                "linkedin": f"Le traitement de cette thématique ({nom}) nous oblige à repenser nos silos administratifs pour plus d'efficacité sur nos territoires ! 🚀 #Transition #ActionPublique"
            }
        ]
    })

# Initialisation et synchronisation
if "subjects" not in st.session_state:
    for s in REFERENTIEL_SUJETS:
        s["count"] = 0
    st.session_state.subjects = REFERENTIEL_SUJETS
else:
    for i, ref_sub in enumerate(REFERENTIEL_SUJETS):
        if i < len(st.session_state.subjects):
            ref_sub["count"] = st.session_state.subjects[i].get("count", 0)
        else:
            ref_sub["count"] = 0
    st.session_state.subjects = REFERENTIEL_SUJETS

if "last_subject_index" not in st.session_state:
    st.session_state.last_subject_index = 0

st.title("🌱 Ton Veilleur Principal")
st.markdown("*Une veille analytique, documentée et conçue pour l'action.*")

cmd = st.text_input(
    "Commande",
    placeholder="Tape un N°, un [CODE], 1+, 1linkedin...",
    label_visibility="collapsed",
)

st.button("Valider")

raw_cmd = cmd.strip()
clean_cmd = raw_cmd.upper().replace("[", "").replace("]", "")

# 1. SI REQUÊTE VIDE OU "VEILLE" -> LISTE DES SUJETS
if not clean_cmd or clean_cmd == "VEILLE":
    sorted_subs = sorted(
        enumerate(st.session_state.subjects), key=lambda x: x[1]["count"]
    )
    focus = sorted_subs[:2]
    others = sorted_subs[2:]
    random.shuffle(others)

    st.markdown("🎯 **Ce que je te suggère aujourd'hui (Sujets peu explorés récemment) :**")
    for idx, sub in focus:
        st.markdown(f"* **[{idx + 1}]** [{sub['code']}] | {sub['name']} *(Vu : {sub['count']} fois)*")

    st.markdown("📋 **Le reste de tes thématiques actives :**")
    for idx, sub in others:
        st.markdown(f"* **[{idx + 1}]** [{sub['code']}] | {sub['name']} *(Vu : {sub['count']} fois)*")

# 2. SI COMMANDE D'APPROFONDISSEMENT (ex: 1+, 2+)
elif "+" in clean_cmd:
    num_part = clean_cmd.replace("+", "").strip()
    sub = st.session_state.subjects[st.session_state.last_subject_index]
    
    news_idx = 0
    if num_part.isdigit():
        news_idx = int(num_part) - 1

    if 0 <= news_idx < len(sub["news"]):
        item = sub["news"][news_idx]
        st.markdown(f"### 🔍 Approfondissement analytique — News n°{item['id']}")
        st.markdown(f"**Sujet associé :** {sub['name']} (`{sub['code']}`)")
        st.info(item["deep"])
        st.markdown(f"📌 **Fondé sur l'analyse critique de :** {item['source']}")
    else:
        st.error(f"Oups, je ne trouve pas l'actualité n°{num_part} dans le bulletin {sub['code']}. On réessaie ?")

# 3. SI COMMANDE LINKEDIN (ex: 1linkedin, 2linkedin)
elif "LINKEDIN" in clean_cmd:
    num_part = clean_cmd.replace("LINKEDIN", "").strip()
    sub = st.session_state.subjects[st.session_state.last_subject_index]
    
    news_idx = 0
    if num_part.isdigit():
        news_idx = int(num_part) - 1

    if 0 <= news_idx < len(sub["news"]):
        item = sub["news"][news_idx]
        sub["count"] += 1
        st.markdown(f"### 💼 Piste de réflexion pour ton r
