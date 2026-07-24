import random
import streamlit as st

st.set_page_config(page_title="Veilleur Principal", layout="wide")

if "subjects" not in st.session_state:
    st.session_state.subjects = [
        {
            "code": "AP-DES",
            "name": "Design des politiques publiques",
            "count": 0,
            "ideas": [
                "**Cartographie sensible des irritants** : co-concevoir les parcours usagers en partant directement des frictions vécues sur le terrain plutôt que des organigrammes.",
                "**Prototypage itératif** : tester des services à petite échelle (bacs à sable) avant toute généralisation administrative.",
                "**Design critique** : utiliser les ateliers de design comme un instrument de remise en question des dispositifs existants."
            ],
            "deep": "Méthodologie détaillée d'immersion usager et de design de services publics locaux.",
            "linkedin": "Repenser l'action publique par le design, c'est refuser la complexité bureaucratique pour remettre l'usager au centre. #DesignPublic"
        },
        {
            "code": "TEC-IAG",
            "name": "IA Générative",
            "count": 0,
            "ideas": [
                "**Souveraineté des modèles** : privilégier l'hébergement de LLM sur des infrastructures locales sécurisées et conformes au RGPD.",
                "**Copilote documentaire** : automatiser l'analyse croisée et la synthèse de grands volumes de rapports administratifs.",
                "**Charte d'usage éthique** : fixer des limites claires distinguant l'aide à la rédaction de la décision politique."
            ],
            "deep": "Architecture technique souveraine des LLM et audit des biais algorithmiques en collectivité.",
            "linkedin": "L'IA générative en collectivité doit être un copilote rigoureux et audité, jamais un substitut à la décision. #IA #ActionPublique"
        },
        {
            "code": "AP-ACH",
            "name": "Achat public responsable",
            "count": 0,
            "ideas": [
                "**Allotissement stratégique** : découper les marchés pour faciliter l'accès des structures de l'ESS et des PME locales.",
                "**Coût global et carbone** : intégrer l'empreinte environnementale sur toute la durée de vie du marché dans les critères d'attribution.",
                "**Sourcing amont actif** : aller chercher les acteurs alternatifs avant la rédaction définitive des cahiers des charges."
            ],
            "deep": "Sécurisation juridique des clauses environnementales et sociales dans les CCTP.",
            "linkedin": "Acheter public, c'est façonner l'économie locale de demain par la contrainte positive du marché. #AchatResponsable"
        },
        {
            "code": "TER-INN",
            "name": "Innovation territoriale",
            "count": 0,
            "ideas": [
                "**Bacs à sable réglementaires** : utiliser les dérogations juridiques pour tester des solutions locales inédites.",
                "**Post-mortems institutionnels** : formaliser et partager les échecs d'innovation pour capitaliser sur les apprentissages.",
                "**Fonds d'amorçage interne** : libérer des micro-budgets directement accessibles aux agents porteurs d'initiatives."
            ],
            "deep": "Utilisation des dérogations et création de laboratoires d'innovation territoriale.",
            "linkedin": "Innover en collectivité, c'est s'autoriser à tester, ajuster et partager nos réussites comme nos échecs. #Innovation"
        },
        {
            "code": "TRA-TER",
            "name": "Transition territoriale",
            "count": 0,
            "content": "",
            "ideas": [
                "**Trajectoire ZAN stricte** : croiser données géographiques et climatiques pour cartographier les vulnérabilités foncières.",
                "**Sobriété spatiale** : sanctuariser les espaces naturels et repenser les mobilités à l'échelle des bassins de vie.",
                "**Comités de suivi citoyens** : associer les habitants aux arbitrages d'aménagement pour éviter les oppositions locales."
            ],
            "deep": "Application de la loi ZAN et arbitrages fonciers en première couronne métropolitaine.",
            "linkedin": "La transition n'est plus un cap lointain, c'est la contrainte immédiate de chaque décision d'aménagement. #Transition"
        },
        {
            "code": "AP-TRA",
            "name": "Politiques de transition",
            "count": 0,
            "ideas": [
                "**Budgétisation verte** : tracer ligne par ligne les dépenses favorables et défavorables à l'environnement dans le budget primitif.",
                "**Analyse d'impact ex-ante** : systématiser l'évaluation carbone de chaque délibération majeure soumise au vote.",
                "**Stratégie de renoncement** : identifier explicitement ce que la collectivité arrête de financer pour financer la transition."
            ],
            "deep": "Méthodologie de la budgétisation verte et arbitrages budgétaires locaux.",
            "linkedin": "Évaluer une politique de transition, c'est mesurer ce que l'on arrête de faire autant que ce que l'on commence. #PolitiquesPubliques"
        },
        {
            "code": "SHS-ESS",
            "name": "Essais SHS",
            "count": 0,
            "ideas": [
                "**Sociologie des institutions** : décoder les jeux de pouvoir informels et les résistances hiérarchiques.",
                "**Temps long institutionnel** : réinjecter de la profondeur critique face à l'injonction permanente à l'urgence.",
                "**Apports théoriques exogènes** : nourrir la réflexion stratégique des directions par des concepts issus de la recherche."
            ],
            "deep": "Notes de lecture croisées sur la sociologie du travail et l'anthropologie des institutions.",
            "linkedin": "La théorie sociale n'est pas un exercice abstrait, c'est une boîte à outils indispensable pour décoder le quotidien. #SHS"
        },
        {
            "code": "SHS-SOC",
            "name": "Sociologie des pratiques",
            "count": 0,
            "ideas": [
                "**Écart prescrit / réel** : observer l'activité effective des agents avant de concevoir de nouvelles procédures.",
                "**Micro-basculements** : identifier les petites habitudes informelles qui permettent de contourner les blocages.",
                "**Transformation des milieux** : modifier les environnements matériels plutôt que de prêcher la bonne conduite."
            ],
            "deep": "Étude sociologique sur l'ajustement entre règles administratives et pratiques de terrain.",
            "linkedin": "On ne change pas les pratiques en prêchant la vertu, mais en redessinant les configurations du milieu de travail. #Sociologie"
        },
        {
            "code": "SHS-COM",
            "name": "Psychologie sociale de la transition",
            "count": 0,
            "ideas": [
                "**Espaces de parole sécurisés** : structurer des temps d'échange pour exprimer les tensions et l'éco-anxiété.",
                "**Puissance d'agir collective** : transformer l'angoisse climatique en projets opérationnels partagés.",
                "**Récits d'avenir désirables** : fuir les discours strictement anxiogènes au profit de visions mobilisatrices."
            ],
            "deep": "Analyse des biais cognitifs et des stratégies de défense face aux crises systémiques.",
            "linkedin": "L'accompagnement au changement doit intégrer la dimension émotionnelle pour éviter l'épuisement des équipes. #Psychologie"
        },
        {
            "code": "EVE-ECO",
            "name": "Événements écoresponsables",
            "count": 0,
            "ideas": [
                "**Politique Zéro Plastique** : éliminer totalement le jetable de la chaîne logistique des manifestations.",
                "**Compostage in situ** : installer des dispositifs de traitement des biodéchets directement sur les sites événementiels.",
                "**Mobilités actives** : conditionner l'accès aux grands rassemblements aux transports en commun et modes doux."
            ],
            "deep": "Cahier des charges et audit logistique pour des événements publics à empreinte minimale.",
            "linkedin": "L'exemplarité environnementale d'une collectivité se lit aussi dans la façon dont elle conçoit ses événements. #Ecoresponsable"
        },
        {
            "code": "TEC-TRA",
            "name": "Tech & Transitions",
            "count": 0,
            "ideas": [
                "**Réemploi informatique** : prolonger la durée de vie du parc matériel par le reconditionnement intensif.",
                "**Sobriété logicielle** : alléger les interfaces et supprimer les fonctionnalités superflues pour réduire la charge serveur.",
                "**Droit de refus technologique** : questionner systématiquement l'utilité réelle de tout nouvel outil numérique."
            ],
            "deep": "Étude critique du techno-solutionnisme et audit de l'empreinte matérielle des SI publics.",
            "linkedin": "La meilleure technologie pour la transition est souvent celle que l'on choisit de ne pas déployer. #SobrieteNumerique"
        },
        {
            "code": "SAN-ALI",
            "name": "Santé & Alimentation",
            "count": 0,
            "ideas": [
                "**Sécurité sociale de l'alimentation** : expérimenter des caisses communes pour garantir l'accès à tous à des produits de qualité.",
                "**Approvisionnement brut** : privilégier les produits non transformés issus de l'agriculture locale dans la prévention santé.",
                "**Éducation nutritionnelle** : lier santé environnementale et sensibilisation au goût dès le plus jeune âge."
            ],
            "deep": "Analyse des déterminants de santé publique liés aux modèles alimentaires territoriaux.",
            "linkedin": "L'assiette est le premier lieu de prévention en santé publique et de reconquête de la biodiversité. #AlimentationDurable"
        },
        {
            "code": "AP-ALI",
            "name": "Alimentation durable (Collectivités)",
            "count": 0,
            "ideas": [
                "**Pesées et anti-gaspillage** : suivre finement les flux de déchets en restauration collective avec des tables de troc.",
                "**Diversification végétale** : introduire progressivement des protéines végétales de qualité dans les menus scolaires.",
                "**Partenariats producteurs** : sécuriser les volumes des fermes locales via des contrats pluriannuels."
            ],
            "deep": "Mise en œuvre opérationnelle de la loi EGALIM et structuration des PAT.",
            "linkedin": "Relocaliser l'alimentation dans les cantines publiques, c'est reconstruire l'économie agricole locale. #PAT #Egalim"
        },
        {
            "code": "TEC-OPS",
            "name": "Open source collaboratif",
            "count": 0,
            "content": "",
            "ideas": [
                "**Mutualisation inter-villes** : co-développer des logiciels métiers open source pour partager les coûts et les savoirs.",
                "**Transparence des algorithmes** : publier en open source les codes régissant l'attribution des aides ou des services.",
                "**Indépendance logicielle** : s'affranchir progressivement des grands éditeurs propriétaires."
            ],
            "deep": "Modèles économiques et de gouvernance des communs numériques publics.",
            "linkedin": "Le code produit par la puissance publique doit être partagé comme un bien commun. #OpenSource"
        },
        {
            "code": "TEC-VEI",
            "name": "Veille & Productivité",
            "count": 0,
            "ideas": [
                "**Filtrage par les flux RSS** : centraliser les sources institutionnelles et de recherche pour éliminer le bruit.",
                "**Notes de synthèse éclair** : formater l'information en points clés directement actionnables par les décideurs.",
                "**Veille collaborative** : croiser les regards au sein de l'équipe pour mutualiser la veille."
            ],
            "deep": "Méthodologie de filtrage d'information et structuration de revues stratégiques.",
            "linkedin": "La productivité intellectuelle ne vient pas de la vitesse de lecture, mais de la rigueur du filtrage. #Veille"
        },
        {
            "code": "AP-ACC",
            "name": "Accompagnement au changement",
            "count": 0,
            "ideas": [
                "**Co-développement managérial** : animer des espaces d'analyse des pratiques entre pairs pour libérer la parole.",
                "**Repérage des ambassadeurs** : identifier les relais informels de terrain pour porter les transformations.",
                "**Célébration des micro-victoires** : jalonner les projets de réussites intermédiaires visibles."
            ],
            "deep": "Dispositifs d'animation de groupes de co-développement et réduction de la fatigue organisationnelle.",
            "linkedin": "On ne décrète pas l'adhésion d'une équipe, on la cultive par la clarté du sens et le dialogue. #Management"
        },
        {
            "code": "IDE-ROB",
            "name": "Robustesse (O. Hamant)",
            "count": 0,
            "ideas": [
                "**Fin des flux tendus** : réintroduire volontairement des marges de manœuvre et des stocks de sécurité.",
                "**Redondance organisationnelle** : cultiver la diversité des compétences plutôt que l'hyper-spécialisation fragile.",
                "**Lenteur protectrice** : ralentir les processus pour garantir leur solidité face aux chocs systémiques."
            ],
            "deep": "Application des concepts de biologie évolutive (Olivier Hamant) aux organisations publiques.",
            "linkedin": "La performance cherche l'optimisation maximale ; la robustesse cultive la redondance et la protection. #Robustesse"
        },
        {
            "code": "LIT-ANT",
            "name": "Anti-lyrisme",
            "count": 0,
            "ideas": [
                "**Écriture blanche** : proscrire la novlangue managériale au profit d'un style neutre et factuel.",
                "**Focus sur les objets** : laisser les situations concrètes et matérielles primer sur les grands concepts abstraits.",
                "**Comptes-rendus épurés** : retirer tout artifice rhétorique des documents de travail."
            ],
            "deep": "Style factuel et poétique des objets (Francis Ponge) appliqué à la rédaction administrative.",
            "linkedin": "Dire les choses sans emphase pour laisser les faits raconter leur propre épaisseur. #AntiLyrisme"
        },
        {
            "code": "CUL-BIB",
            "name": "Innovation en bibliothèque",
            "count": 0,
            "ideas": [
                "**Tiers-lieux hybrides** : transformer les bibliothèques en espaces d'inclusion numérique et de débat citoyen.",
                "**Horaires modulables** : adapter l'ouverture des équipements aux nouveaux rythmes de vie.",
                "**Fablabs et repair cafés** : ouvrir les lieux à des activités contributives et de réparation partagée."
            ],
            "deep": "Mutation des bibliothèques municipales en plateformes d'innovation sociale.",
            "linkedin": "La bibliothèque du XXIe siècle est un espace de liens avant d'être un espace de livres. #TiersLieu"
        },
        {
            "code": "TER-MON",
            "name": "Mons-en-Barœul",
            "count": 0,
            "ideas": [
                "**Urbanisme de proximité** : décliner les politiques métropolitaines à hauteur d'habitant dans les quartiers.",
                "**Conseils de quartier actifs** : impliquer directement les citoyens dans la coconception des aménagements locaux.",
                "**Cohésion sociale dense** : articuler rénovation urbaine et animation de proximité."
            ],
            "deep": "Monographie territoriale de première couronne et dynamiques d'animation locale.",
            "linkedin": "Penser la ville à hauteur d'habitant dans un tissu urbain dense et vivant. #MonsEnBaroeul"
        },
        {
            "code": "CUL-CIN",
            "name": "Cinéma & Séries exigeants",
            "count": 0,
            "ideas": [
                "**Narrations complexes** : utiliser l'analyse des structures filmiques pour décrypter les récits institutionnels.",
                "**Laboratoire anthropologique** : observer les mutations politiques et sociales à travers les fictions contemporaines.",
                "**Études de cas fictionnelles** : croiser regards artistiques et sociologiques pour penser la gestion de crise."
            ],
            "deep": "Analyse critique des fictions audiovisuelles comme analyseurs du contemporain.",
            "linkedin": "La fiction n'est pas un divertissement, c'est le laboratoire critique où s'expérimentent nos futurs collectifs. #Cinema"
        },
    ]

if "last_index" not in st.session_state:
    st.session_state.last_index = 0

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

    elif raw_cmd.endswith("+") and raw_cmd[:-1].isdigit():
        idx = int(raw_cmd[:-1]) - 1
        if 0 <= idx < len(st.session_state.subjects):
            st.session_state.last_index = idx
            sub = st.session_state.subjects[idx]
            st.markdown(f"### 🔍 Approfondissement : {sub['name']} (`{sub['code']}`)")
            st.markdown(sub["deep"])
        else:
            st.error("Numéro d'actualité inconnu.")

    elif "LINKEDIN" in clean_cmd:
        num_str = "".join([c for c in clean_cmd if c.isdigit()])
        if num_str:
            idx = int(num_str) - 1
            if 0 <= idx < len(st.session_state.subjects):
                st.session_state.last_index = idx
        
        sub = st.session_state.subjects[st.session_state.last_index]
        sub["count"] += 1
        st.markdown(f"### 💼 Proposition de publication LinkedIn ({sub['code']})")
        st.markdown(sub["linkedin"])

    else:
        selected_sub = None
        if clean_cmd.isdigit():
            idx = int(clean_cmd) - 1
            if 0 <= idx < len(st.session_state.subjects):
                selected_sub = st.session_state.subjects[idx]
                st.session_state.last_index = idx
        else:
            for i, sub in enumerate(st.session_state.subjects):
                if sub["code"] == clean_cmd:
                    selected_sub = sub
                    st.session_state.last_index = i
                    break

        if selected_sub:
            selected_sub["count"] += 1
            st.markdown(f"## 💡 Idées clés : {selected_sub['name']} (`{selected_sub['code']}`)")
            st.markdown(f"*Indicateur de sollicitation : {selected_sub['count']} consultations*")
            st.markdown("---")
       
