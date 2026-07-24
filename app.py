import random
import streamlit as st

st.set_page_config(page_title="Veilleur Principal", layout="wide")

# Référentiel des données avec un ton plus chaleureux et complice ("Gemini Pro style")
REFERENTIEL_SUJETS = [
    {
        "code": "AP-DES",
        "name": "Design des politiques publiques",
        "ideas": [
            "**👋 Partir du terrain, toujours** : Et si on allait directement voir où ça coince pour nos usagers ? C'est souvent là que se cachent les meilleures solutions.",
            "**🛠️ Le droit de tester (et de se tromper)** : Avant de déployer une usine à gaz, lançons de petits prototypes. Ça rassure tout le monde et ça coûte moins cher !",
            "**🧐 Un regard critique** : Utilisons nos ateliers pour oser remettre en question ce qu'on fait « depuis toujours »."
        ],
        "deep": "En plongeant dans le quotidien des usagers, on réalise vite que simplifier un formulaire a parfois plus d'impact qu'une grande réforme. Prenons le temps de concevoir avec eux, pas juste pour eux.",
        "linkedin": "Repenser l'action publique, c'est parfois juste avoir le courage de refuser la complexité bureaucratique pour remettre l'humain au centre de la table. Qu'en pensez-vous ? 👇 #DesignPublic #ActionPublique"
    },
    {
        "code": "TEC-IAG",
        "name": "IA Générative",
        "ideas": [
            "**🔐 Garder la main sur nos données** : L'IA c'est génial, mais hébergeons nos modèles en local pour protéger nos informations sensibles.",
            "**🤖 Un super assistant de lecture** : Utilisons l'IA pour digérer les pavés administratifs, ça nous dégagera du temps pour l'essentiel : l'humain.",
            "**⚖️ Fixer les règles du jeu** : Rédigeons une charte bienveillante pour rassurer les équipes sur ce qu'elles peuvent (et ne doivent pas) faire avec l'IA."
        ],
        "deep": "L'enjeu n'est pas de remplacer nos agents, mais de leur redonner du souffle. Une architecture IA souveraine permet de gagner un temps précieux sur la synthèse documentaire, tout en garantissant que la décision finale reste toujours humaine.",
        "linkedin": "L'IA générative dans nos services ? Oui, mais comme un copilote rigoureux. La décision, elle, doit rester profondément humaine et politique. 🤖✨ #IAGenerative #ServicePublic"
    },
    {
        "code": "AP-ACH",
        "name": "Achat public responsable",
        "ideas": [
            "**🧩 Découper pour mieux régner** : Allotissons nos marchés de manière astucieuse pour donner une vraie chance à nos PME locales et aux structures de l'ESS.",
            "**🌍 Penser plus loin que le prix** : Intégrons enfin l'empreinte carbone et le coût global sur toute la durée de vie de ce qu'on achète.",
            "**🤝 Aller au contact** : N'attendons pas la publication du marché. Faisons du sourcing en amont pour découvrir les pépites de notre territoire."
        ],
        "deep": "Le cahier des charges est notre meilleur levier de transformation. Sécurisons nos clauses environnementales, non pas pour contraindre, mais pour encourager tout un écosystème à évoluer avec nous.",
        "linkedin": "Et si la commande publique n'était pas qu'une affaire de procédures, mais notre meilleur levier pour façonner l'économie locale de demain ? 🌱 #AchatResponsable #Transition"
    },
    {
        "code": "TER-INN",
        "name": "Innovation territoriale",
        "ideas": [
            "**🏖️ Oser les bacs à sable** : Profitons des dérogations juridiques pour tester des solutions un peu folles à petite échelle.",
            "** autopsy 🩹 Apprendre de nos loupés** : Partageons sereinement ce qui n'a pas marché. Un échec analysé, c'est une victoire pour la suite.",
            "**🌱 Faire confiance au terrain** : Libérons de petits budgets d'amorçage pour laisser les agents tester leurs propres idées."
        ],
        "deep": "L'innovation n'est pas qu'une affaire de technologie. C'est surtout créer un climat de confiance où l'on s'autorise à essayer de nouvelles choses en cassant les silos habituels.",
        "linkedin": "Innover dans nos collectivités, c'est d'abord créer un climat de confiance où l'on s'autorise à tester, à ajuster, et surtout à partager nos loupés ! 💡 #InnovationPublique"
    },
    {
        "code": "TRA-TER",
        "name": "Transition territoriale",
        "ideas": [
            "**🗺️ Objectiver avec la data** : Croisons nos données climatiques avec la réalité du terrain pour cibler nos actions là où ça chauffe vraiment.",
            "**🌳 Protéger notre espace** : Sanctuarisons nos espaces naturels. Le ZAN n'est pas qu'une contrainte, c'est une opportunité de repenser la ville.",
            "**🗣️ Embarquer les citoyens** : Faisons de la place aux habitants dans nos comités de suivi. C'est le meilleur moyen d'éviter les blocages."
        ],
        "deep": "Face à la raréfaction des ressources, l'aménagement de nos quartiers doit pivoter. Prendre en compte concrètement les trajectoires de zéro artificialisation demande de la pédagogie, mais c'est vital pour nos bassins de vie.",
        "linkedin": "La transition n'est plus un grand discours abstrait, c'est la contrainte immédiate (et passionnante !) de chaque décision d'aménagement que nous prenons aujourd'hui. 🌍 #TransitionTerritoriale"
    },
    {
        "code": "AP-TRA",
        "name": "Politiques de transition",
        "ideas": [
            "**🟢 Parler vrai avec le budget** : Mettons en place une vraie budgétisation verte pour voir clairement où va notre argent.",
            "**⚖️ Évaluer avant de voter** : Prenons le réflexe d'estimer l'impact carbone de nos grosses délibérations en amont.",
            "**🛑 Le courage d'arrêter** : Transitionner, c'est aussi assumer de dire « stop » à certains projets pour pouvoir en financer de nouveaux."
        ],
        "deep": "C'est dans l'ingénierie financière que se gagne la transition. Le vrai courage managérial et politique consiste à arbitrer et à renoncer consciemment à certaines dépenses pour rester alignés avec nos ambitions climatiques.",
        "linkedin": "On parle souvent de ce qu'il faut créer pour la transition écologique... mais si le vrai courage politique, c'était d'assumer publiquement ce que l'on décide d'arrêter de faire ? 🛑 #PolitiquesPubliques #Climat"
    },
    {
        "code": "SHS-ESS",
        "name": "Essais SHS",
        "ideas": [
            "**🔎 Décoder les jeux de pouvoir** : Un peu de sociologie aide énormément à comprendre pourquoi certains dossiers bloquent en interne.",
            "**⏳ Protéger notre temps long** : La philo nous rappelle l'importance de lever le nez du guidon face à la dictature de l'urgence administrative.",
            "**📚 Respirer intellectuellement** : Nourrissons nos réunions stratégiques avec des concepts qui viennent d'ailleurs. Ça fait un bien fou !"
        ],
        "deep": "Prendre le temps de lire et de croiser la sociologie du travail avec notre quotidien administratif nous redonne du pouvoir d'agir. C'est une vraie boîte à outils pour manager de manière plus éclairée.",
        "linkedin": "La théorie sociale n'est pas qu'un exercice universitaire lointain. C'est une boîte à outils incroyablement puissante pour décoder notre quotidien administratif ! 🧠 #Management #SHS"
    },
    {
        "code": "SHS-SOC",
        "name": "Sociologie des pratiques",
        "ideas": [
            "**👀 Regarder ce qui se fait vraiment** : Avant de pondre une nouvelle procédure, allons voir comment les agents se débrouillent concrètement sur le terrain.",
            "**🦋 Guetter les petits basculements** : C'est souvent par de toutes petites habitudes que le vrai changement s'installe.",
            "**🛋️ Agir sur l'environnement** : On ne change pas les gens avec des discours, on les aide en modifiant leurs outils et leur cadre de travail."
        ],
        "deep": "Il y a toujours un écart entre la règle qu'on imagine au bureau et la réalité du terrain. Plutôt que de forcer le trait, adaptons nos environnements de travail pour rendre les nouvelles pratiques naturelles et fluides.",
        "linkedin": "On ne change pas les pratiques professionnelles en prêchant la vertu, mais en redessinant intelligemment et avec empathie les environnements de travail. #Sociologie #ConduiteDuChangement"
    },
    {
        "code": "SHS-COM",
        "name": "Psychologie sociale de la transition",
        "ideas": [
            "**💬 Vider son sac** : Créons des moments sûrs où nos équipes peuvent exprimer leur fatigue ou leur anxiété face aux injonctions paradoxales.",
            "**💪 Retrouver le pouvoir d'agir** : Transformons cette angoisse climatique en actions concrètes et collectives, même petites.",
            "**🌅 Raconter de belles histoires** : Les discours catastrophes épuisent. Mettons plutôt en lumière ce qui marche et ce qui donne envie."
        ],
        "deep": "Nos équipes sont parfois tiraillées. Les accompagner dans cette transition écologique, c'est aussi accueillir leurs émotions, comprendre leurs résistances et transformer l'éco-anxiété en énergie collective positive.",
        "linkedin": "Si l'on veut embarquer nos équipes dans les transitions, il faut écouter la fatigue et l'éco-anxiété. L'accompagnement doit devenir émotionnel autant qu'opérationnel. ❤️‍🩹 #PsychologieSociale #Management"
    },
    {
        "code": "EVE-ECO",
        "name": "Événements écoresponsables",
        "ideas": [
            "**🚫 Fini le plastique** : Supprimons totalement le jetable de nos événements. C'est symbolique et tellement impactant.",
            "**🍎 Retour à la terre** : Installons des composteurs temporaires directement sur les lieux de nos manifestations.",
            "**🚲 Venir autrement** : Facilitons vraiment la vie de ceux qui viennent à vélo ou en transports en commun."
        ],
        "deep": "Un événement public, c'est la vitrine de nos engagements. En posant un cahier des charges strict sur les déchets et la mobilité, on prouve que la sobriété peut être festive et joyeuse !",
        "linkedin": "L'exemplarité environnementale de nos structures se jauge aussi dans la façon dont nous organisons nos temps forts et nos événements publics. Faisons de la sobriété une fête ! 🎉♻️ #Ecoresponsable"
    },
    {
        "code": "TEC-TRA",
        "name": "Tech & Transitions",
        "ideas": [
            "**💻 Chouchouter notre matériel** : Faisons durer nos ordinateurs au maximum en privilégiant la réparation et le reconditionné.",
            "**🪶 Alléger nos outils** : Choisissons des logiciels sobres, qui ne demandent pas des serveurs surdimensionnés pour fonctionner.",
            "**✋ Savoir dire non** : Avons-nous vraiment besoin d'une énième application ? Le courage, c'est aussi de refuser la sur-numérisation."
        ],
        "deep": "La technologie n'est pas une baguette magique. Assumer une vraie sobriété numérique, c'est questionner nos usages réels et limiter le renouvellement compulsif de notre matériel informatique.",
        "linkedin": "Dans nos administrations, la meilleure technologie pour réussir la transition est souvent celle que l'on choisit... de ne pas déployer. Sobriété avant tout ! 📵 #SobrieteNumerique #TechForGood"
    },
    {
        "code": "SAN-ALI",
        "name": "Santé & Alimentation",
        "ideas": [
            "**💳 L'alimentation pour tous** : Soutenons les projets locaux de sécurité sociale de l'alimentation. Bien manger ne doit pas être un luxe.",
            "**🥕 Moins d'ultra-transformé** : Mettons le paquet sur les produits bruts et locaux dans nos actions de prévention santé.",
            "**👅 Rééduquer le goût** : Dès le plus jeune âge, montrons que la santé de la planète et celle de notre corps sont intimement liées."
        ],
        "deep": "La santé de nos concitoyens se joue en grande partie dans l'assiette. Agir sur la précarité alimentaire et promouvoir des filières locales et brutes, c'est faire de la médecine préventive très concrète.",
        "linkedin": "Ne l'oublions jamais : l'assiette de nos usagers est le premier lieu de prévention en santé publique et de reconquête de notre biodiversité. 🍅 #AlimentationDurable #SantePublique"
    },
    {
        "code": "AP-ALI",
        "name": "Alimentation durable (Collectivités)",
        "ideas": [
            "**🗑️ Stop au gaspillage** : Suivons de près ce qui part à la poubelle dans nos cantines et installons des tables de troc entre les enfants.",
            "**🌱 Explorer le végétal** : Introduisons en douceur des repas végétariens gourmands et équilibrés.",
            "**🧑‍🌾 Chouchouter nos producteurs** : Sécurisons les paysans du coin avec des contrats de confiance sur le long terme."
        ],
        "deep": "La restauration collective est un levier magique. En appliquant la loi EGALIM avec intelligence, on nourrit mieux nos enfants tout en structurant l'économie agricole juste autour de chez nous.",
        "linkedin": "Relocaliser l'alimentation dans nos cantines publiques, ce n'est pas qu'une question de menus. C'est reconstruire activement l'économie agricole de nos territoires. 🧑‍🌾 #PAT #Egalim #Cantines"
    },
    {
        "code": "TEC-OPS",
        "name": "Open source collaboratif",
        "ideas": [
            "**🤝 Développer à plusieurs** : Mutualisons nos budgets avec d'autres villes pour co-créer les logiciels dont nous avons toutes besoin.",
            "**🔍 Jouer la transparence** : Publions les codes de nos algorithmes publics. Ça crée de la confiance avec les citoyens.",
            "**🕊️ Gagner en liberté** : Libérons-nous progressivement de notre dépendance aux grands éditeurs logiciels commerciaux."
        ],
        "deep": "L'open source, ce n'est pas qu'un truc de geeks. C'est un modèle politique et économique puissant pour mutualiser l'argent public et garder la maîtrise de nos propres outils numériques.",
        "linkedin": "L'argent public doit financer du code public. C'est en partageant nos outils open source entre collectivités que nous regagnerons notre souveraineté numérique ! 💻🔓 #OpenSource #ServicePublic"
    },
    {
        "code": "TEC-VEI",
        "name": "Veille & Productivité",
        "ideas": [
            "**🧹 Faire le tri** : Centralisons nos sources d'info via des flux RSS propres pour arrêter de se noyer dans le bruit ambiant.",
            "**⚡ Aller à l'essentiel** : Rédigeons de petites notes de synthèse ultra-courtes, pensées pour être directement utiles.",
            "**🗣️ Veiller à plusieurs** : Partageons nos trouvailles en équipe pour que tout le monde monte en compétence sans effort."
        ],
        "deep": "Face à la masse d'informations, la vraie compétence devient la curation. Structurer une veille collaborative nous permet de capter les bons signaux faibles sans épuiser notre charge mentale.",
        "linkedin": "Aujourd'hui, la productivité intellectuelle ne vient plus de notre vitesse de lecture, mais bien de la rigueur et de l'intelligence de notre filtrage. 🧠 #VeilleStratégique #Productivité"
    },
    {
        "code": "AP-ACC",
        "name": "Accompagnement au changement",
        "ideas": [
            "**☕ Prendre le temps d'en parler** : Les groupes de co-développement sont formidables pour que nos managers puissent échanger sur leurs galères entre pairs.",
            "**🌟 S'appuyer sur les bonnes volontés** : Identifions les collègues qui ont naturellement envie de faire avancer les choses et faisons-en nos relais.",
            "**🥳 Fêter les petits pas** : Ne minimisons pas les petites victoires du quotidien. Les célébrer fait un bien fou au moral de l'équipe !"
        ],
        "deep": "Gérer de grosses équipes et des réorganisations à répétition, c'est usant. L'accompagnement ne doit pas être un process froid, mais un vrai soutien de proximité pour libérer la parole et désamorcer les blocages.",
        "linkedin": "On ne décrète pas l'adhésion d'une équipe à la nouveauté. On la cultive patiemment par la clarté du sens, l'écoute, et le dialogue de proximité. 🤝 #Management #ConduiteDuChangement"
    },
    {
        "code": "IDE-ROB",
        "name": "Robustesse (O. Hamant)",
        "ideas": [
            "**🛑 Relâcher la pression** : Le flux tendu nous fragilise. Ayons le courage de recréer de vraies marges de manœuvre et des temps de respiration.",
            "**🌈 Miser sur nos différences** : Une équipe aux parcours variés sera toujours plus solide en temps de crise qu'un groupe d'hyper-spécialistes.",
            "**🐢 L'éloge de la lenteur** : Ralentir certains de nos processus n'est pas une perte de temps, c'est une sécurité pour encaisser les chocs."
        ],
        "deep": "Inspirons-nous du vivant ! Olivier Hamant nous montre brillamment que chercher l'optimisation à tout prix nous rend vulnérables. Cultivons la diversité et la redondance dans nos services pour être enfin robustes.",
        "linkedin": "La performance cherche l'optimisation maximale jusqu'à la rupture. La robustesse, elle, cultive la marge de manœuvre et la protection. Lequel de ces deux modèles voulons-nous pour nos services publics ? 🌿 #Robustesse #Management"
    },
    {
        "code": "LIT-ANT",
        "name": "Anti-lyrisme",
        "ideas": [
            "**🧊 Aller droit au but** : Traquons la « novlangue » managériale dans nos notes pour retrouver un style clair, neutre et facile à lire.",
            "**🪑 Regarder les objets** : Raccrochons nos projets à des réalités matérielles et concrètes. C'est toujours plus parlant !",
            "**✂️ Couper le gras** : Épurons nos comptes-rendus. Moins de fioritures, plus de décisions claires."
        ],
        "deep": "Comme l'a merveilleusement théorisé Francis Ponge avec *Méthodes* (et pas dans le parti pris, soyons précis !), ou Hélène Bessette avec *La Tour*, revenir à la description factuelle des choses, sans fioriture, donne une force et une efficacité redoutable à nos écrits professionnels.",
        "linkedin": "Et si on arrêtait d'utiliser des grands mots pour ne rien dire ? Dire les choses simplement, sans emphase, pour laisser la réalité raconter sa propre épaisseur. ✍️ #EcritureProfessionnelle #AntiLyrisme"
    },
    {
        "code": "CUL-BIB",
        "name": "Innovation en bibliothèque",
        "ideas": [
            "**🛋️ Un vrai lieu de vie** : Transformons nos bibliothèques en espaces accueillants où l'on a juste envie de se poser et d'échanger.",
            "**🕒 S'adapter aux vraies vies** : Faisons évoluer nos horaires pour être ouverts quand les gens ont vraiment du temps libre.",
            "**🛠️ Faire ensemble** : Accueillons des repair cafés ou des fablabs. La bibliothèque est le lieu idéal pour l'inclusion numérique."
        ],
        "deep": "Les bibliothèques sont les cœurs battants de nos villes. En devenant de véritables tiers-lieux d'innovation sociale, elles renouvellent le lien de proximité de manière incroyable.",
        "linkedin": "La bibliothèque publique du XXIe siècle est devenue un espace formidable pour tisser des liens sociaux, bien avant d'être un simple espace de stockage pour nos livres. 📚✨ #TiersLieux #Culture"
    },
    {
        "code": "TER-MON",
        "name": "Mons-en-Barœul",
        "ideas": [
            "**🏘️ Proche des gens** : C'est en déclinant nos ambitions métropolitaines à la fine échelle du quartier qu'on a le plus d'impact.",
            "**👂 Écouter les conseils** : Appuyons-nous vraiment sur les conseils de quartier pour co-construire notre espace public.",
            "**🧶 Tisser du lien** : Articulons intelligemment nos chantiers de rénovation urbaine avec une vraie chaleur dans l'animation locale."
        ],
        "deep": "La gestion de proximité dans un tissu urbain dense exige beaucoup d'agilité. C'est un formidable terrain de jeu pour prouver que la transition écologique peut améliorer concrètement la vie quotidienne.",
        "linkedin": "Le grand défi des 
