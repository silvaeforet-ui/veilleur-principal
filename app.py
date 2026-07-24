import random
import streamlit as st

st.set_page_config(page_title="Veilleur Principal", layout="wide")

if "subjects" not in st.session_state:
    st.session_state.subjects = [
        {
            "code": "AP-DES",
            "name": "Design des politiques publiques",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
Le recours au design des politiques publiques s'intègre désormais dans les processus de co-conception des services métropolitains. L'enjeu réside dans le passage d'une démarche participative cosmétique à une refonte structurelle des parcours usagers.
> « Le design public n'est pas une méthode de mise en forme, c'est un instrument critique de la décision. »
📌 **Sources :** La Gazette des Communes, Sciences Po Urba.
---
### 2. Retours d'expérience opérationnels
* **Immersion terrain :** Cartographie fine des irritants vécus par les administrés.
* **Prototypage rapide :** Test en conditions réelles avant généralisation d’un service.
---
### 3. Pistes d'action pour l'encadrement
1. Intégrer des designers au cœur des directions métiers dès la phase de cadrage.
2. Formaliser des indicateurs d'usage qualitatifs plutôt que de simples quantitatifs.
"""
        },
        {
            "code": "TEC-IAG",
            "name": "IA Générative",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
L'intégration des modèles génératifs dans les collectivités pose la question de la souveraineté des données et de l'éthique algorithmique. Les expérimentations locales se multiplient pour automatiser la rédaction de comptes-rendus ou l'analyse textuelle de grands volumes documentaires.
> « L'IA en collectivité doit être un copilote robuste et audité, jamais un substitut à la décision politique. »
📌 **Sources :** ActuIA, CNIL, DINUM.
---
### 2. Retours d'expérience opérationnels
* **Gouvernance des données :** Nécessité d'héberger les LLM sur des infrastructures sécurisées et conformes au RGPD.
* **Accompagnement des agents :** Levée des craintes liées à l'automatisation par la formation pratique.
---
### 3. Pistes d'action pour l'encadrement
1. Rédiger une charte d'usage interne clarifiant les limites de l'IA générative.
2. Lancer un cas d'usage pilote sur l'aide à la décision ou la synthèse documentaire.
"""
        },
        {
            "code": "AP-ACH",
            "name": "Achat public responsable",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
La commande publique devient un levier majeur de transition écologique et sociale avec la généralisation des clauses environnementales et l'intégration des critères d'économie circulaire dans les cahiers des charges (CCTP).
> « Acheter public, c'est façonner l'économie locale de demain par la contrainte positive du marché. »
📌 **Sources :** AEF Info, Banque des Territoires.
---
### 2. Retours d'expérience opérationnels
* **Sourcing amont :** Difficulté à mobiliser les PME locales sur des critères techniques complexes.
* **Analyse du coût global :** Intégration du bilan carbone sur toute la durée de vie du marché.
---
### 3. Pistes d'action pour l'encadrement
1. Simplifier l'accès des structures de l'économie sociale et solidaire (ESS) aux marchés.
2. Former les acheteurs aux nouvelles grilles d'analyse multicritères.
"""
        },
        {
            "code": "TER-INN",
            "name": "Innovation territoriale",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
L'innovation dans les territoires se mesure à l'aune de leur capacité à expérimenter des solutions décentralisées face aux crises climatiques et sociales, en brisant les silos traditionnels entre directions.
> « Innover en collectivité, c'est d'abord s'autoriser le droit à l'ajustement permanent. »
📌 **Sources :** La Fabrique de la Cité, IDPD.
---
### 2. Retours d'expérience opérationnels
* **Bacs à sable réglementaires :** Utilisation des dérogations pour tester de nouvelles approches.
* **Mesure d'impact :** Évaluation des communs urbains et de la résilience locale.
---
### 3. Pistes d'action pour l'encadrement
1. Créer un fonds d'amorçage interne dédié aux initiatives innovantes des agents.
2. Institutionnaliser les retours d'expérience (post-mortems) pour capitaliser sur les échecs.
"""
        },
        {
            "code": "TRA-TER",
            "name": "Transition territoriale",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
La trajectoire de transition impose de repenser l'aménagement urbain, la gestion de l'eau et l'énergie à l'échelle des bassins de vie. Les collectivités doivent composer avec la raréfaction annoncée des ressources.
> « La transition n'est plus un cap lointain, c'est la contrainte immédiate de chaque décision d'aménagement. »
📌 **Sources :** The Conversation, Cerema.
---
### 2. Retours d'expérience opérationnels
* **Artificialisation des sols :** Mise en œuvre stricte de la trajectoire ZAN (Zéro Artificialisation Nette).
* **Sobriété énergétique :** Rénovation thermique du patrimoine bâti communal.
---
### 3. Pistes d'action pour l'encadrement
1. Croiser les données géographiques et climatiques pour cartographier les vulnérabilités locales.
2. Impliquer les habitants dans les comités de suivi de la transition écologique.
"""
        },
        {
            "code": "AP-TRA",
            "name": "Politiques de transition",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
L'évaluation des politiques publiques de transition révèle un décalage persistant entre les grands plans stratégiques et la réalité des budgets opérationnels alloués sur le terrain.
> « Évaluer une politique de transition, c'est mesurer ce que l'on arrête de faire autant que ce que l'on commence. »
📌 **Sources :** France Stratégie, IDDRI.
---
### 2. Retours d'expérience opérationnels
* **Budgétisation verte :** Traçabilité des dépenses favorables à l'environnement dans le budget primitif.
* **Arbitrages budgétaires :** Conflits d'usage entre court terme et urgence climatique.
---
### 3. Pistes d'action pour l'encadrement
1. Généraliser l'analyse d'impact carbone pour chaque délibération majeure.
2. Animer des sessions de formation croisée entre élus et directions financières.
"""
        },
        {
            "code": "SHS-ESS",
            "name": "Essais SHS",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
La lecture critique des essais en sciences humaines et sociales offre des clés de décryptage indispensables pour comprendre les résistances culturelles et les dynamiques de polarisation au sein des organisations.
> « La théorie sociale n'est pas un exercice abstrait, c'est une boîte à outils pour décoder l'inacceptable quotidien. »
📌 **Sources :** OpenEdition, La Vie des Idées.
---
### 2. Retours d'expérience opérationnels
* **Sociologie des organisations :** Comprendre les dynamiques de pouvoir informelles.
* **Philosophie de l'action :** Repenser le rapport au temps long face à l'urgence administrative.
---
### 3. Pistes d'action pour l'encadrement
1. Nourrir les notes de cadrage stratégique par des apports théoriques exogènes.
2. Organiser des cercles de lecture thématiques au sein de l'équipe de management.
"""
        },
        {
            "code": "SHS-SOC",
            "name": "Sociologie des pratiques",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
L'analyse sociologique des pratiques quotidiennes montre que le changement des comportements ne passe pas par la norme juridique, mais par la transformation des environnements matériels et symboliques.
> « On ne change pas les pratiques en prêchant la vertu, mais en redessinant les configurations du milieu. »
📌 **Sources :** Revue française de sociologie, CNRS.
---
### 2. Retours d'expérience opérationnels
* **Inertie des habitudes :** Analyse des routines professionnelles et administratives.
* **Changement incrémental :** Identification des micro-basculements favorables à l'innovation.
---
### 3. Pistes d'action pour l'encadrement
1. Observer les pratiques réelles sur le terrain avant de concevoir de nouvelles procédures.
2. Valoriser les initiatives informelles qui contournent les blocages organisationnels.
"""
        },
        {
            "code": "SHS-COM",
            "name": "Psychologie sociale de la transition",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
La psychologie sociale étudie les freins cognitifs et les mécanismes de dissonance face aux annonces de rupture écologique. L'accompagnement du changement doit intégrer la dimension émotionnelle des transitions.
> « La prise de conscience de la crise génère de l'éco-anxiété qu'il s'agit de transformer en puissance d'agir collective. »
📌 **Sources :** Cairn.info, Psychologie sociale appliquée.
---
### 2. Retours d'expérience opérationnels
* **Résistance au changement :** Gestion des peurs et des sentiments d'impuissance face aux contraintes.
* **Dynamique de groupe :** Mobilisation par l'intelligence collective et le soutien par les pairs.
---
### 3. Pistes d'action pour l'encadrement
1. Instaurer des espaces de parole sécurisés pour exprimer les tensions professionnelles.
2. Privilégier les récits d'avenir positifs et désirables plutôt que les discours anxiogènes.
"""
        },
        {
            "code": "EVE-ECO",
            "name": "Événements écoresponsables",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
L'organisation d'événements publics (forums, séminaires, festivals) est scrutée sur son bilan carbone, sa gestion des déchets et son accessibilité. La charte éco-événement devient la norme incontournable.
> « Un événement écoresponsable, c'est la vitrine visible de l'exemplarité environnementale d'une collectivité. »
📌 **Sources :** ADEME, Réseau eco-événement.
---
### 2. Retours d'expérience opérationnels
* **Zero Déchet :** Élimination totale du plastique jetable et mise en place du compostage sur site.
* **Mobilité des publics :** Incitation forte aux modes actifs et aux transports en commun.
---
### 3. Pistes d'action pour l'encadrement
1. Imposer des clauses environnementales strictes aux prestataires et traiteurs.
2. Réaliser un bilan post-événement pour auditer les marges de progression.
"""
        },
        {
            "code": "TEC-TRA",
            "name": "Tech & Transitions",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
L'articulation entre technologies numériques et urgence écologique interroge le concept de « tech for good ». Le piège du techno-solutionnisme doit être évité au profit d'une sobriété numérique assumée.
> « La meilleure technologie pour la transition est souvent celle que l'on choisit de ne pas déployer. »
📌 **Sources :** The Shift Project, GreenIT.fr.
---
### 2. Retours d'expérience opérationnels
* **Allongement de la durée de vie :** Réemploi et reconditionnement du parc informatique des agents.
* **Éco-conception des services numériques :** Allègement des interfaces et des bases de données.
---
### 3. Pistes d'action pour l'encadrement
1. Réaliser un audit d'impact environnemental du système d'information de la collectivité.
2. Questionner systématiquement l'utilité réelle de tout nouvel outil numérique.
"""
        },
        {
            "code": "SAN-ALI",
            "name": "Santé & Alimentation",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
Le lien entre santé publique et alimentation locale est au cœur des politiques de prévention. La lutte contre la précarité alimentaire et l'accès à une alimentation de qualité pour tous sont des enjeux majeurs.
> « L'assiette est le premier lieu de prévention en santé publique et de reconquête de la biodiversité agricole. »
📌 **Sources :** ANSES, Ministère de la Santé.
---
### 2. Retours d'expérience opérationnels
* **Restauration collective :** Introduction de produits bruts, locaux et issus de l'agriculture biologique.
* **Sécurité sociale de l'alimentation :** Expérimentations locales de caisses alimentaires communes.
---
### 3. Pistes d'action pour l'encadrement
1. Structurer des filières d'approvisionnement direct avec les producteurs de proximité.
2. Mener des actions de sensibilisation sur la nutrition et la santé environnementale.
"""
        },
        {
            "code": "AP-ALI",
            "name": "Alimentation durable (Collectivités)",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
Dans le cadre de la loi EGALIM et des Projets Alimentaires Territoriaux (PAT), les collectivités structurent l'approvisionnement de leurs cantines scolaires et structures sociales vers des circuits courts et durables.
> « Relocaliser l'alimentation dans les cantines, c'est reconstruire l'économie agricole d'un territoire. »
📌 **Sources :** Réseau Restau'Co, Ministère de l'Agriculture.
---
### 2. Retours d'expérience opérationnels
* **Lutte contre le gaspillage :** Mise en place de pesées régulières et de tables de troc dans les cantines.
* **Diversification des menus :** Introduction progressive de protéines végétales de qualité.
---
### 3. Pistes d'action pour l'encadrement
1. Accompagner les producteurs locaux pour répondre aux contraintes de la commande publique.
2. Associer les usagers (parents, enfants) à la composition des menus.
"""
        },
        {
            "code": "TEC-OPS",
            "name": "Open source collaboratif",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
Le recours aux logiciels libres et aux communs numériques garantit aux collectivités une indépendance vis-à-vis des grands éditeurs logiciels propriétaires tout en favorisant la mutualisation inter-collectivités.
> « Le code public doit appartenir au public et être partagé comme un bien commun. »
📌 **Sources :** ADULLACT, Open Source France.
---
### 2. Retours d'expérience opérationnels
* **Mutualisation des outils :** Co-développement d'applications métiers open source entre villes.
* **Transparence algorithmique :** Publication des codes sources utilisés pour les décisions administratives.
---
### 3. Pistes d'action pour l'encadrement
1. Privilégier systématiquement les solutions open source lors des renouvellements de licences.
2. Contribuer aux communautés de partage de code entre acteurs publics.
"""
        },
        {
            "code": "TEC-VEI",
            "name": "Veille & Productivité",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
L'infobésité guette les organisations publiques. Structurer une veille efficace et automatisée permet de filtrer le bruit informationnel pour ne retenir que les signaux faibles à forte valeur stratégique.
> « La productivité intellectuelle ne vient pas de la vitesse de lecture, mais de la rigueur du filtrage. »
📌 **Sources :** INA, Documentalistes territoriaux.
---
### 2. Retours d'expérience opérationnels
* **Flux RSS et agrégateurs :** Centralisation des sources institutionnelles et de recherche.
* **Notes de synthèse éclair :** Formatage de notes courtes pour les décideurs.
---
### 3. Pistes d'action pour l'encadrement
1. Mettre en place un rituel de veille partagée au sein de l'équipe.
2. Utiliser des outils d'IA pour automatiser la structuration des revues de presse.
"""
        },
        {
            "code": "AP-ACC",
            "name": "Accompagnement au changement",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
Les réorganisations successives dans la fonction publique génèrent de la fatigue organisationnelle. L'accompagnement au changement doit être pensé comme un soutien psychologique et méthodologique de proximité.
> « On ne décrète pas l'adhésion d'une équipe, on la cultive par l'écoute et la clarté du sens. »
📌 **Sources :** Anact, La Gazette des Communes.
---
### 2. Retours d'expérience opérationnels
* **Groupes de co-développement :** Espaces d'analyse des pratiques professionnelles entre pairs.
* **Communication transparente :** Explication des attendus et co-construction des plannings.
---
### 3. Pistes d'action pour l'encadrement
1. Identifier les relais de changement informels au sein des équipes.
2. Célébrer les petites victoires intermédiaires pour maintenir la motivation.
"""
        },
        {
            "code": "IDE-ROB",
            "name": "Robustesse (O. Hamant)",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
Inspiré des travaux d'Olivier Hamant, le concept de robustesse oppose la flexibilité fragile (optimisée pour le flux tendu) à la redondance robuste (capable d'absorber les chocs par l'excès et la diversité).
> « La performance cherche l'optimisation maximale au détriment de la survie ; la robustesse cultive la redondance et la lenteur protectrice. »
📌 **Sources :** Olivier Hamant (Université de Lyon / INRAE).
---
### 2. Retours d'expérience opérationnels
* **Fin des flux tendus :** Réintroduction de marges de manœuvre et de stocks de sécurité dans l'organisation.
* **Diversité des profils :** Valorisation des expertises croisées plutôt que de l'hyper-spécialisation.
---
### 3. Pistes d'action pour l'encadrement
1. Auditer les processus fragiles de la direction face à une panne ou une crise majeure.
2. Intégrer la redondance humaine comme une assurance-vie pour le service.
"""
        },
        {
            "code": "LIT-ANT",
            "name": "Anti-lyrisme",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
L'anti-lyrisme en littérature (et dans la posture managériale) refuse les grands élans lyriques, le pathos et la grandiloquence au profit d'une écriture blanche, factuelle, attentive aux choses et aux faits précis.
> « Dire les choses sans emphase, laisser les objets et les faits raconter leur propre épaisseur. »
📌 **Sources :** Francis Ponge, Hélène Bessette, littérature contemporaine.
---
### 2. Retours d'expérience opérationnels
* **Rédaction administrative neutre :** Éviter la novlangue managériale au profit d'un style direct et précis.
* **Attention au réel :** Focus sur les objets matériels et les situations concrètes de travail.
---
### 3. Pistes d'action pour l'encadrement
1. Éurer les comptes-rendus de réunion de tout artifice rhétorique inutile.
2. Privilégier le constat factuel dans les notes d'évaluation.
"""
        },
        {
            "code": "CUL-BIB",
            "name": "Innovation en bibliothèque",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
Les bibliothèques publiques se réinventent en tiers-lieux culturels et sociaux, élargissant leurs missions bien au-delà du prêt d'ouvrages pour devenir des espaces d'inclusion numérique et de débat citoyen.
> « La bibliothèque du XXIe siècle est un espace de liens avant d'être un espace de livres. »
📌 **Sources :** Bulletin des Bibliothèques de France (BBF), Enssib.
---
### 2. Retours d'expérience opérationnels
* **Horaires élargis et automatisation :** Ouverture modulable pour s'adapter aux nouveaux modes de vie.
* **Ateliers participatifs :** Ateliers de fabrication (fablabs), repair cafés et soutien numérique.
---
### 3. Pistes d'action pour l'encadrement
1. Ouvrir l'espace physique à des acteurs associatifs locaux pour croiser les publics.
2. Former les équipes aux nouvelles médiations culturelles et numériques.
"""
        },
        {
            "code": "TER-MON",
            "name": "Mons-en-Barœul",
            "count": 0,
            "content": """
### 1. Synthèse exécutive et décryptage
Ancrage territorial de proximité, la commune de Mons-en-Barœul illustre les défis de la gestion urbaine dense en première couronne métropolitaine : rénovation
