from __future__ import annotations

import json
import shutil
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEANCES = ROOT.parent


VISUALS = [
    ("01-intro-blog-site.jpg", "img/session-10/01-intro-blog-site.jpg", "Je pose le sujet : le blog devient la base de publication du site."),
    ("02-wordpress-site-reference.jpg", "img/session-10/02-wordpress-site-reference.jpg", "Je pars du site RestIA existant, pas d'un écran vide."),
    ("03-prompt-analyse-contexte.jpg", "img/session-10/03-prompt-analyse-contexte.jpg", "Je prépare un prompt long pour que Codex analyse le contexte."),
    ("04-prompt-phases-blog.jpg", "img/session-10/04-prompt-phases-blog.jpg", "Je découpe la mission en phases pour forcer la réflexion."),
    ("05-structure-template-article.jpg", "img/session-10/05-structure-template-article.jpg", "Je détaille le template d'article avant de demander l'exécution."),
    ("06-homepage-restia-preview.jpg", "img/session-10/06-homepage-restia-preview.jpg", "Je garde la cohérence avec le design déjà créé sur le site."),
    ("07-pagespeed-check.jpg", "img/session-10/07-pagespeed-check.jpg", "Je pense aux performances et au SEO dès la structure."),
    ("08-codex-terminal-action.jpg", "img/session-10/08-codex-terminal-action.jpg", "Codex travaille dans le terminal sur une mission longue."),
    ("09-codex-wordpress-working.jpg", "img/session-10/09-codex-wordpress-working.jpg", "Codex pilote WordPress et continue les vérifications."),
    ("10-single-post-test.jpg", "img/session-10/10-single-post-test.jpg", "Le premier article test valide le template Single Post."),
    ("11-acf-fields-wordpress.jpg", "img/session-10/11-acf-fields-wordpress.jpg", "Les champs ACF rendent l'article plus professionnel."),
    ("12-gutenberg-article-published.jpg", "img/session-10/12-gutenberg-article-published.jpg", "Je vérifie le statut, le slug et l'image mise en avant."),
    ("13-single-post-content-table.jpg", "img/session-10/13-single-post-content-table.jpg", "Le contenu long doit rester lisible avec sommaire et tableaux."),
    ("14-blog-archive-empty.jpg", "img/session-10/14-blog-archive-empty.jpg", "L'archive /blog/ montre la structure de cartes et de sidebar."),
    ("15-wordpress-admin-pages.jpg", "img/session-10/15-wordpress-admin-pages.jpg", "Je contrôle l'admin WordPress pour vérifier les pages et contenus."),
    ("16-prompt-copy-full.jpg", "img/session-10/16-prompt-copy-full.jpg", "Le prompt complet précise les livrables et les variables."),
    ("17-codex-connected-mcp.jpg", "img/session-10/17-codex-connected-mcp.jpg", "La connexion MCP permet à Codex d'ouvrir et lire WordPress."),
    ("18-elementor-context.jpg", "img/session-10/18-elementor-context.jpg", "Elementor sert de contexte visuel pour reproduire le style."),
    ("19-template-hero-notes.jpg", "img/session-10/19-template-hero-notes.jpg", "Je précise le hero article, la catégorie et la méta row."),
    ("20-template-sidebar-notes.jpg", "img/session-10/20-template-sidebar-notes.jpg", "Je précise sommaire, FAQ, sources et partage social."),
    ("21-report-terminal.jpg", "img/session-10/21-report-terminal.jpg", "Le rapport terminal donne la trace de ce qui a été fait."),
    ("22-seo-article-request.jpg", "img/session-10/22-seo-article-request.jpg", "Je teste ensuite avec un vrai sujet SEO plus long."),
    ("23-final-article-check.jpg", "img/session-10/23-final-article-check.jpg", "Je finis par une vérification visuelle de l'article publié."),
]


PROMPTS = {
    "connect_codex": """connecte toi a mon site stp en mcp https://restia.fun/wp-admin/post.php?post=254&action=elementor""",
    "archive": """Tu es un lead developer WordPress + Elementor Pro et un expert SEO/GEO.
Tu as acces au Chrome MCP. Utilise-le pour regarder mon site et verifier le rendu.

Contexte :
J'ai deja construit mon site RestIA en Elementor : accueil, solutions, contact, header et footer.
Maintenant je veux monter la partie blog.
Attention : je ne veux pas encore produire des dizaines d'articles.
Je veux preparer la structure propre qui va recevoir les articles ensuite.

Mission :
1. Creer la page archive /blog/.
2. Creer le template Single Post pour tous les articles.
3. Installer ou verifier les bons plugins.
4. Creer les categories et les champs ACF.
5. Tester avec des articles factices, puis remettre les tests en brouillon.

Travaille en 5 phases.
Avant chaque phase, ecris ce que tu vas faire.
Apres chaque phase, ecris ce que tu as produit et ce que tu as appris.

PHASE 1 - Discovery
- Crawle la home, les pages principales, le header et le footer.
- Extrais la palette, les typos, les espacements, les bordures, les radius, les ombres, les animations et le ton.
- Note les composants Elementor deja presents.
- Cree discovery.md, design-tokens.json et seo-stack.md.

PHASE 2 - Prerequis WordPress
- Verifie ou installe Rank Math Free.
- Verifie ou installe ACF Free.
- Verifie ou installe ACF to REST API.
- Verifie ou installe Smush ou un plugin de compression image.
- Cree des categories propres selon le secteur. Ne cree pas categorie-1, categorie-2, etc.
- Cree des tags utiles : Agent IA, Automatisation, News IA.
- Cree les champs article :
  - en_resume
  - temps_lecture
  - niveau
  - faq
  - sources
  - mise_a_jour_manuelle

PHASE 3 - Template Single Post
Construis dans Elementor Theme Builder -> Single Post.
Condition : tous les posts.
Structure :
1. Breadcrumb.
2. Hero post avec tag categorie, H1, extrait, avatar, auteur, date, temps de lecture, niveau.
3. Image mise en avant en 16:9.
4. Bloc en_resume si le champ est rempli.
5. Sommaire sticky sur desktop.
6. Contenu article avec H2, H3, callouts, tableaux responsive, images et captions.
7. FAQ si le champ est rempli.
8. Sources si le champ est rempli.
9. Bloc auteur.
10. CTA contextualise.
11. Articles lies.
12. Partage LinkedIn, X et copier le lien.
13. Pas de commentaires.

PHASE 4 - Archive /blog/
Construis dans Elementor Theme Builder -> Archive.
Condition : Posts Archive.
Structure :
1. Hero archive compact avec H1, baseline et recherche.
2. Article epingle optionnel.
3. Filtres categories en pills.
4. Grid articles : 3 colonnes desktop, 2 tablette, 1 mobile.
5. Card avec image 4:3, categorie, titre 2 lignes max, extrait 2 lignes max, date et temps de lecture.
6. Pagination numerotee, pas de load more.
7. Sidebar : newsletter, articles recents, tags.
8. Etat vide propre si aucun article n'est publie.

PHASE 5 - Verification
- Cree 2 posts factices avec image, categorie et champs remplis.
- Verifie /blog/.
- Clique sur un article et verifie le template.
- Verifie mobile 375px.
- Verifie Lighthouse sur archive et single post.
- Verifie le schema si possible.
- Remets les posts factices en brouillon.

Rapport final :
Cree RAPPORT.md avec les plugins, les champs, les categories, les captures, les scores, les corrections et la prochaine etape.

GO.""",
    "seo_article": """okay tu vas me faire un article seo assez long avec mon audit stp.
Ajoute des images, mets des tableaux, des listes a puces, des exemples et des liens internes / externes.
L'article doit faire environ 1400 mots.
Ne fais pas d'auto-correction globale.
Le but est de tester la structure que tu viens de construire.""",
    "chatgpt_article": """Fais-moi un article sur l'intelligence artificielle pour tester mon blog.
Je veux un contenu simple, clair, avec une introduction, des H2, des exemples, une FAQ courte et une conclusion.
Garde un style naturel. Le but est de voir si mon template WordPress affiche bien un article complet.""",
    "codex_article_import": """Prends cet article et mets-le proprement dans WordPress.
Titre : [TITRE_ARTICLE]
Categorie : [CATEGORIE]
Tags : [TAGS]
Remplis les champs :
- TL;DR
- Temps de lecture
- Niveau
- FAQ
- Sources
- Date de mise a jour
Ajoute une image mise en avant depuis la mediathèque.
Publie seulement quand la preview est propre.""",
    "quality": """Controle la page /blog/ et le single post.
Verifie desktop, tablette et mobile.
Verifie que les titres ne debordent pas, que les cards ont la meme hauteur, que la sidebar ne casse pas, que les images chargent, que le slug est propre et que l'article est bien publie.
Donne-moi une liste courte : OK, a corriger, correction faite.""",
}


SECTIONS = [
    ("Le blog n'est pas un bonus", "Je ne crée pas un blog pour remplir un menu. Je crée un endroit où mon système peut publier des contenus utiles, tester des sujets, pousser mes offres et construire de l'autorité. Si mon site RestIA explique ce que je vends, le blog explique pourquoi mes solutions ont du sens.", "hero", 7),
    ("Le point de départ : mon-business", "Je garde le même dossier de travail que dans les séances précédentes. Le dossier mon-business évite de mélanger les fichiers de marque, de marché, de site, de blog, de prospection et de clients. Pour cette séance je pars de 02-site, parce que le blog se construit dans le WordPress déjà en place.", "image", 1),
    ("Pourquoi je travaille dans 02-site", "Le blog n'est pas séparé du site. Il doit reprendre la charte, la navbar, le footer, les couleurs et les boutons déjà créés. Si je lançais Codex dans un autre dossier, il perdrait une partie du contexte et il pourrait produire un blog qui ne ressemble pas au reste.", "method", None),
    ("Ce que je veux à la fin", "Je veux trois choses simples : une page /blog/ qui liste les articles, un template d'article qui affiche chaque contenu proprement, et une méthode pour publier sans refaire le design à chaque fois. Une fois le système prêt, chaque nouvel article doit tomber dans la bonne structure tout seul.", "cards", None),
    ("La logique IA derrière la séance", "Ce n'est pas une séance WordPress classique. La vraie compétence, c'est de savoir donner une mission complète à un agent : contexte, accès, structure attendue, preuves de réussite, pièges à éviter. Codex ne doit pas deviner. Je le guide comme un exécutant technique.", "quote", 2),
    ("Je ne cherche pas à tout automatiser tout de suite", "Avant de publier 100 articles automatiquement, je vérifie que le blog peut recevoir un seul article correctement. C'est le bon ordre. D'abord la coquille. Ensuite le contenu. Ensuite l'automatisation.", "before", None),
    ("Le fil rouge RestIA", "Je garde le même exemple : RestIA, un site pour aider les restaurants avec l'IA. Le blog doit servir ce business. Les articles ne doivent pas être génériques. Ils doivent parler d'appels manqués, de réservations, d'avis clients, de menus, de service, de visibilité et d'automatisations utiles.", "story", None),
    ("Ce que tu vas refaire", "Tu vas ouvrir ton projet, lancer Codex dans le bon dossier, le connecter à WordPress, lui donner un prompt précis, vérifier les pages créées, tester un article, régler les catégories, puis publier proprement. Chaque étape a une preuve observable.", "check", None),
    ("Préparer le dossier avant Codex", "Avant de demander quoi que ce soit, je vérifie que je suis dans le dossier du site. Si je travaille dans le mauvais dossier, Codex peut créer des rapports, des fichiers ou des notes au mauvais endroit. Ce n'est pas grave, mais ça rend la suite confuse.", "terminal", 2),
    ("Lancer Codex dans le bon contexte", "Dans la séance, je lance Codex en mode terminal depuis le dossier 02-site. Le but est qu'il comprenne l'environnement local et qu'il puisse écrire ses fichiers de rapport au même endroit que le projet.", "prompt", None, "connect_codex"),
    ("Ce que Codex voit au lancement", "Codex affiche le modèle, le dossier courant et les permissions. Je vérifie ces trois lignes. Si le dossier n'est pas le bon, je coupe et je relance. C'est plus propre que de corriger après.", "image", 3),
    ("Le mode YOLO demande de la responsabilité", "Quand j'autorise Codex à travailler sans me demander chaque permission, je gagne du temps. Mais je dois être sûr du dossier et de la mission. Ce mode est utile dans un projet de confiance, pas dans un dossier rempli de fichiers sensibles.", "warning", None),
    ("La connexion MCP vers WordPress", "Je donne l'URL WordPress à Codex pour qu'il puisse ouvrir le site via le navigateur. Le MCP sert à piloter Chrome : ouvrir une page, cliquer, lire l'interface, récupérer un snapshot et vérifier visuellement.", "method", 4),
    ("Pourquoi je donne une URL précise", "Je ne dis pas seulement : connecte-toi à mon site. Je donne une URL exacte. Dans la capture, l'URL pointe vers l'éditeur Elementor d'une page. Codex gagne du temps parce qu'il arrive directement au bon endroit.", "diagnostic", None),
    ("Première preuve : WordPress répond", "La première preuve n'est pas que Codex écrit beaucoup de texte. La preuve, c'est que WordPress s'ouvre, que la session est active, et que la page ou l'admin est visible.", "image", 4),
    ("Je garde mes accès sous contrôle", "Si une connexion est nécessaire, je peux la faire moi-même. Codex n'a pas besoin de voir mes mots de passe. Une fois connecté, il peut travailler dans la session active.", "warning", None),
    ("Le prompt de construction doit être concret", "Je ne demande pas : fais-moi un blog. Je décris exactement l'archive, les filtres, les cartes, la pagination, la sidebar et l'état vide. Plus le prompt est précis, moins Codex invente.", "prompt", 5, "archive"),
    ("L'archive /blog/ sert de hub", "La page /blog/ est la porte d'entrée du contenu. Elle doit être simple : un titre, une recherche, des catégories, une grille d'articles, une pagination. L'utilisateur doit comprendre où cliquer en moins de cinq secondes.", "story", None),
    ("Le rôle de l'article épinglé", "L'article épinglé n'est pas obligatoire. Il sert à mettre en avant un contenu fort : un guide, une étude, un audit, une offre de lead magnet. Si tu n'as rien d'important, tu laisses l'état vide propre.", "cards", None),
    ("Les filtres catégories", "Les catégories doivent aider à naviguer. Sur RestIA, je peux avoir Guides, Cas d'usage, Actualités IA, Automatisation, Restaurant. Ce ne sont pas des catégories décoratives : elles aident le lecteur à trouver ce qui l'intéresse.", "table", None),
    ("Pourquoi pas categorie-1", "Une catégorie nommée categorie-1 ne parle à personne. Si Codex crée ce genre de nom, je corrige. Un blog professionnel utilise des catégories lisibles, même si le contenu est encore vide.", "warning", 21),
    ("La grille d'articles", "La grille doit être régulière. Une card trop haute casse le rythme. Je demande donc une image en ratio fixe, un titre limité à deux lignes, un extrait limité, et un footer stable avec date et temps de lecture.", "image", 18),
    ("Le mobile compte dès maintenant", "Le blog peut être joli sur desktop et cassé sur mobile. Je vérifie vite : 375px, une colonne, aucun texte qui déborde, pas de sidebar trop large, pas de bouton coupé.", "check", None),
    ("L'état vide est important", "Au début il n'y a pas forcément d'article publié. Une page vide peut faire amateur. Je veux un message propre : Bientôt - premiers articles en préparation. C'est mieux qu'une grille cassée ou une page blanche.", "quote", None),
    ("Le template Single Post", "Un article WordPress ne doit pas dépendre d'une mise en page faite à la main à chaque fois. Le Single Post template donne une structure automatique : titre, image, contenu, sommaire, FAQ, sources, CTA.", "image", 9),
    ("Le titre doit porter le sujet", "Sur un article, le H1 est central. Il sert au lecteur, au SEO et au modèle IA qui analysera la page. Je veux un titre clair, pas un titre vague comme Article test.", "method", 14),
    ("Le breadcrumb donne le contexte", "Le fil d'Ariane aide le lecteur à comprendre où il est : Accueil > Blog > Catégorie > Article. Il aide aussi Google à comprendre la structure du site.", "cards", None),
    ("L'extrait n'est pas optionnel", "L'extrait donne une phrase d'intention sous le titre. Il sert aussi aux cards d'archive. Si l'extrait est vide, WordPress peut prendre un bout de texte au hasard.", "diagnostic", None),
    ("L'image mise en avant", "L'image mise en avant doit être choisie, pas laissée vide. Elle apparaît dans l'article, dans la card, parfois dans le partage social. Elle donne le premier signal visuel.", "image", 22),
    ("La médiathèque", "Je range les visuels dans la médiathèque WordPress. L'objectif n'est pas d'avoir une belle galerie. L'objectif est de pouvoir réutiliser les images au bon endroit, avec un alt propre.", "image", 23),
    ("Le contenu de l'article", "Le corps de l'article doit avoir des H2, des paragraphes courts, des exemples, des tableaux si utile, et des callouts. Le template doit rendre tout ça lisible sans retoucher le design.", "image", 10),
    ("Le sommaire", "Le sommaire permet de naviguer dans un article long. Sur desktop, il peut rester à droite. Sur mobile, il doit se placer au-dessus ou disparaître proprement.", "cards", None),
    ("Les callouts", "Je veux trois types de blocs : info, attention, conseil. Ils rendent l'article plus lisible et évitent les murs de texte. Codex peut les prévoir dans le CSS du template.", "table", None),
    ("La fin de l'article doit vendre sans forcer", "Un article doit finir par une action logique : réserver un audit, lire une page service, télécharger un guide, demander un devis. Le CTA doit être lié au sujet, pas collé au hasard.", "image", 11),
    ("Le partage social", "Je garde LinkedIn, X et copier le lien. Sur un blog B2B, c'est souvent plus utile que de mettre dix réseaux sociaux qui ne seront jamais utilisés.", "method", None),
    ("Le bloc auteur", "Le bloc auteur rassure. Il montre qui écrit, quel est le rôle, et pourquoi la personne est crédible. C'est utile pour l'E-E-A-T et pour la lecture humaine.", "cards", None),
    ("Les articles liés", "Les articles liés créent du maillage interne. Ils gardent le lecteur sur le site et aident Google à comprendre les groupes de sujets.", "story", None),
    ("La FAQ", "La FAQ répond aux questions simples que le lecteur se pose. Elle peut aussi nourrir le schema FAQPage si le site le gère proprement.", "table", None),
    ("Les sources", "Les sources externes évitent de faire croire que tout sort de nulle part. Pour un article sérieux, je veux au moins quelques liens utiles, vérifiés, et pas seulement du texte généré.", "warning", None),
    ("Les champs ACF", "Les champs ACF permettent de structurer l'article sans écrire du code à chaque fois. TL;DR, temps de lecture, niveau, date de mise à jour, FAQ, sources : tout devient plus propre.", "image", 15),
    ("Le TL;DR", "Le TL;DR doit résumer l'article en deux ou trois lignes. C'est très utile pour le lecteur pressé. Je le place en haut de l'article pour qu'il comprenne vite l'intérêt.", "method", None),
    ("Le temps de lecture", "Le temps de lecture donne une attente. Si l'article est long, le lecteur sait dans quoi il s'engage. C'est simple, mais ça rend le blog plus professionnel.", "cards", None),
    ("Le niveau", "Le champ niveau évite de mélanger les contenus débutants et avancés. Sur RestIA, un restaurateur doit savoir si l'article est accessible ou technique.", "table", None),
    ("La date de mise à jour", "Un article IA vieillit vite. Je veux pouvoir montrer qu'un contenu a été revu. C'est utile pour la confiance et pour éviter les guides obsolètes.", "warning", None),
    ("Les permaliens", "Je règle les permaliens sur Titre de la publication. Une URL comme /intelligence-artificielle-restaurant/ est plus claire que /?p=123.", "image", 19),
    ("Le slug", "Le slug doit être court, lisible, sans accents, sans mots inutiles. Je ne laisse pas WordPress créer un slug trop long si le titre est long.", "diagnostic", 22),
    ("Rank Math", "Rank Math sert à gérer le SEO de base : title, meta description, sitemap, breadcrumbs, schema. Je ne l'utilise pas comme décoration. Il sert à contrôler le signal envoyé.", "cards", None),
    ("Smush ou compression image", "Un blog peut devenir lourd si chaque image fait plusieurs Mo. Je compresse les images et je vérifie qu'elles chargent correctement.", "method", None),
    ("ACF to REST API", "Ce plugin peut aider si Codex doit lire ou remplir des champs personnalisés via l'API. Il rend les champs plus accessibles aux automatisations.", "table", None),
    ("Créer des articles factices", "Avant de publier de vrais articles, je crée des brouillons ou des articles de test. Ils servent à vérifier les cards, les catégories, le single template et les champs.", "image", 13),
    ("Pourquoi je repasse les tests en brouillon", "Un article factice ne doit pas rester public. Une fois la vérification terminée, je le remets en brouillon ou je le supprime. Le site public doit rester propre.", "warning", None),
    ("Créer un premier article réel", "Une fois la structure prête, je peux créer un article réel. Dans la capture, le titre AGENT IA VISIO montre l'étape de démarrage : je pose le sujet, puis je remplis le contenu et les champs.", "image", 14),
    ("Utiliser ChatGPT pour un test simple", "Je peux demander à ChatGPT un article de test pour voir si le template fonctionne. Ce n'est pas encore une stratégie éditoriale complète. C'est juste un test d'affichage.", "prompt", 16, "chatgpt_article"),
    ("Demander un article SEO plus long", "Quand le template est prêt, je peux demander un article plus long avec des tableaux, des listes, des liens et des images. Le but est de tester la structure complète, pas de publier n'importe quoi.", "prompt", 12, "seo_article"),
    ("Importer proprement dans WordPress", "Je ne colle pas juste un texte brut. Je demande à Codex de remplir le titre, la catégorie, les tags, les champs ACF, l'image mise en avant et la preview.", "prompt", None, "codex_article_import"),
    ("La preview avant publication", "Je vérifie la preview. Je regarde le titre, les espacements, l'image, le sommaire, la FAQ, le CTA et la sidebar. Si un élément casse, je corrige avant de publier.", "image", 17),
    ("La publication", "Publier ne veut pas dire que le travail est fini. Après publication je rouvre la page publique, sans être dans l'admin, et je vérifie ce qu'un visiteur voit vraiment.", "method", 20),
    ("La liste des articles", "La liste WordPress permet de contrôler les statuts : publié, brouillon, Elementor, auteur, catégorie, date. C'est mon tableau de bord éditorial.", "image", 20),
    ("Les catégories dans l'admin", "Je vérifie que les catégories sont propres. Si je vois Uncategorized ou categorie-1 partout, je corrige. Les catégories doivent parler au business.", "image", 21),
    ("Les images d'article", "Une image trop générique ne sert pas. Pour RestIA, l'image doit évoquer l'IA, le restaurant, l'automatisation ou le sujet exact de l'article.", "diagnostic", 23),
    ("Les liens internes", "Chaque article doit pointer vers au moins une page utile du site : solution, contact, audit, offre, autre article. Le blog doit soutenir le tunnel commercial.", "table", None),
    ("Les liens externes", "Un lien externe doit apporter une preuve ou une ressource. Je ne mets pas des liens pour remplir. Je choisis des sources fiables et je les ouvre avant de les ajouter.", "warning", None),
    ("La sidebar", "La sidebar doit rester utile : newsletter, articles récents, tags. Si elle alourdit la page, je la simplifie. Sur mobile elle doit passer sous le contenu.", "cards", None),
    ("Le design ne doit pas casser le contenu", "Le style RestIA est marqué : bordures, gros titres, vert, contraste. Mais un article reste un article. La lisibilité passe avant l'effet visuel.", "quote", 7),
    ("Le test desktop", "Je vérifie en grand écran : largeur du contenu, alignement du sommaire, cards de l'archive, header, footer, CTA. Rien ne doit flotter bizarrement.", "check", None),
    ("Le test mobile", "Je vérifie en 375px : titre, image, boutons, card, sidebar, tableau, prompt, CTA. Le texte ne doit pas sortir de l'écran.", "check", None),
    ("Le test WordPress admin", "Je vérifie aussi l'admin : les champs sont simples, les catégories existent, la médiathèque charge, l'image mise en avant se sélectionne, le bouton publier reste accessible.", "image", 4),
    ("Le rapport final", "Je demande à Codex de me dire ce qu'il a créé, ce qu'il a vérifié, les fichiers, les plugins, les scores et les points à surveiller. Un rapport évite de perdre la trace du travail.", "prompt", 6, "quality"),
    ("Ce que je garde dans mon QG", "Je garde les prompts, les URLs utiles, les décisions, les catégories, les champs ACF et les corrections. Ce support sert à refaire la séance sans repartir de zéro.", "story", None),
    ("Ce qu'il ne faut pas déléguer aveuglément", "Je ne délègue pas le jugement éditorial. Codex peut construire, importer, tester. Mais je dois valider si le sujet est utile, si le ton est bon, si l'article sert vraiment mon business.", "warning", None),
    ("La différence entre contenu test et contenu stratégie", "Un article de test sert à vérifier l'affichage. Un article stratégique sert à capter des leads. Ne mélange pas les deux. Tant que la structure n'est pas validée, le contenu n'est qu'un test.", "before", None),
    ("La suite logique", "Après cette séance, tu peux automatiser la création d'articles : plan éditorial, sources, rédaction, images, publication, contrôle qualité. Mais cette automatisation vaut seulement si le blog est propre.", "timeline", None),
    ("Mini checklist avant de passer à l'automatisation", "Je valide : /blog/ charge, un article s'affiche, les catégories sont propres, les champs se remplissent, l'image apparaît, le slug est bon, le mobile passe, les articles test ne polluent pas le site.", "check", None),
    ("Ce que tu dois retenir", "Le blog automatique commence par une structure propre. Si la structure est bonne, l'IA peut publier à grande échelle. Si la structure est mauvaise, l'IA publie vite un mauvais système.", "recap", None),
    ("Plan de répétition", "Refais la séance une fois sur un site de test. Puis refais-la sur ton vrai projet. Plus tu répètes cette méthode, plus tu sais guider Codex sans sur-expliquer.", "method", None),
    ("La compétence business", "Tu peux vendre cette compétence : créer un blog WordPress prêt pour la publication IA, avec template, champs, SEO, catégories, système d'article et contrôle qualité.", "cards", None),
    ("Le dernier contrôle", "Avant de dire que c'est terminé, j'ouvre le site public, je clique sur Blog, je clique sur un article, je reviens à l'archive, je teste mobile, puis je note les corrections.", "image", 18),
    ("Pourquoi je parle déjà de VPS", "À la fin je prépare la suite : pour automatiser vraiment la publication, il faudra un endroit qui tourne tout seul. C'est le rôle du VPS. Le site WordPress reçoit les articles, mais le système qui les fabrique peut vivre ailleurs.", "method", None),
    ("Pourquoi les API arrivent après", "Les API servent à brancher les modèles, récupérer des données, générer du contenu, créer des images, pousser dans WordPress et contrôler le résultat. Je n'attaque pas ça tant que le blog n'est pas propre, parce que l'automatisation amplifierait les défauts.", "timeline", None),
    ("Fin de séance", "À la fin, je n'ai pas seulement un blog. J'ai une base réutilisable. Chaque futur article aura une structure, des champs, un slug, une image, une catégorie et une logique business.", "final", None),
]


def copy_visuals() -> list[dict[str, str]]:
    out = ROOT / "img" / "session-10"
    out.mkdir(parents=True, exist_ok=True)
    copied = []
    for idx, (name, rel, caption) in enumerate(VISUALS, 1):
        src = (ROOT / rel).resolve()
        dst = out / name
        if not src.exists():
            raise FileNotFoundError(src)
        if src != dst.resolve():
            shutil.copyfile(src, dst)
        copied.append({"id": idx, "file": f"img/session-10/{name}", "caption": caption})
    return copied


def render_prompt(key: str) -> str:
    text = escape(PROMPTS[key])
    return f"""
      <div class="prompt-card">
        <div class="prompt-head"><span>Prompt à copier</span><button class="copy-btn" type="button">Copier</button></div>
        <pre><code>{text}</code></pre>
      </div>
    """


def figure(visuals: list[dict[str, str]], idx: int | None) -> str:
    if not idx:
        return ""
    v = visuals[idx - 1]
    return f"""
      <figure class="shot">
        <img src="{v['file']}" alt="{escape(v['caption'])}" loading="lazy">
        <figcaption><span>Capture {idx:02d}</span>{escape(v['caption'])}</figcaption>
      </figure>
    """


def section_html(n: int, data: tuple, visuals: list[dict[str, str]]) -> str:
    title, body, kind, img, *rest = data
    prompt = rest[0] if rest else None
    tag = f"{n:02d}"
    base_meta = f"""
      <div class="meta-row">
        <span class="num">{tag}</span>
        <span>{escape(kind)}</span>
        <span>{'pratique' if n % 3 == 0 else 'méthode' if n % 3 == 1 else 'vérification'}</span>
      </div>
    """
    body_p = f"<p class=\"lead\">{escape(body)}</p>"
    fig = figure(visuals, img)
    prompt_html = render_prompt(prompt) if prompt else ""

    if kind in {"hero", "final"}:
        return f"""
    <section id="section-{tag}" class="section {kind}" data-section="{n}">
      <div class="hero-grid">
        <div>{base_meta}<h2>{escape(title)}</h2>{body_p}
          <div class="hero-actions"><a href="#section-09">Commencer</a><a href="#prompts">Prompts</a><a href="#section-80">Checklist finale</a></div>
        </div>
        {fig}
      </div>
    </section>"""
    if kind == "image":
        return f"""
    <section id="section-{tag}" class="section" data-section="{n}">
      {base_meta}<h2>{escape(title)}</h2>{body_p}{fig}
      <div class="note-row"><div><b>Action</b><p>Je vérifie l'écran réel avant de passer à la suite.</p></div><div><b>Preuve</b><p>Je peux expliquer ce que je vois et pourquoi je l'utilise.</p></div></div>
    </section>"""
    if kind == "prompt":
        return f"""
    <section id="section-{tag}" class="section split" data-section="{n}">
      <div>{base_meta}<h2>{escape(title)}</h2>{body_p}<div class="tip"><b>Pourquoi ce prompt sert</b><p>Il transforme une intention vague en tâche contrôlable. Tu peux le copier, remplacer les variables, puis vérifier le résultat.</p></div></div>
      <div>{fig}{prompt_html}</div>
    </section>"""
    if kind == "check":
        return f"""
    <section id="section-{tag}" class="section" data-section="{n}">
      {base_meta}<h2>{escape(title)}</h2>{body_p}
      <div class="check-grid">
        <label><input type="checkbox"> Je sais quoi ouvrir</label>
        <label><input type="checkbox"> Je sais quoi demander</label>
        <label><input type="checkbox"> Je sais quelle preuve regarder</label>
        <label><input type="checkbox"> Je sais quoi corriger si ça bloque</label>
      </div>{fig}
    </section>"""
    if kind == "table":
        return f"""
    <section id="section-{tag}" class="section" data-section="{n}">
      {base_meta}<h2>{escape(title)}</h2>{body_p}
      <div class="table-wrap"><table><thead><tr><th>Élément</th><th>Pourquoi je le garde</th><th>Comment tu vérifies</th></tr></thead><tbody>
      <tr><td>Structure</td><td>Elle évite que l'IA parte dans tous les sens.</td><td>Le résultat suit l'ordre prévu.</td></tr>
      <tr><td>Business</td><td>Le blog doit servir le site, pas faire joli.</td><td>Chaque bloc mène vers une action utile.</td></tr>
      <tr><td>Contrôle</td><td>Sans preuve, je ne valide pas.</td><td>Je regarde le site public et l'admin.</td></tr>
      </tbody></table></div>{fig}
    </section>"""
    if kind == "warning":
        return f"""
    <section id="section-{tag}" class="section split warning-layout" data-section="{n}">
      <div>{base_meta}<h2>{escape(title)}</h2>{body_p}</div>
      <div class="warning"><b>Piège terrain</b><p>Si tu vas trop vite ici, tu gagnes dix minutes maintenant et tu en perds une heure plus tard. Reviens toujours à une preuve simple.</p></div>{fig}
    </section>"""
    if kind == "before":
        return f"""
    <section id="section-{tag}" class="section" data-section="{n}">
      {base_meta}<h2>{escape(title)}</h2>{body_p}
      <div class="before-after"><div><b>Avant</b><p>Une demande floue, un site qui peut casser, et un agent qui improvise.</p></div><div><b>Après</b><p>Un chemin clair : contexte, prompt, exécution, contrôle, correction.</p></div></div>{fig}
    </section>"""
    if kind == "timeline":
        return f"""
    <section id="section-{tag}" class="section" data-section="{n}">
      {base_meta}<h2>{escape(title)}</h2>{body_p}
      <div class="timeline"><div><span>1</span>Préparer</div><div><span>2</span>Construire</div><div><span>3</span>Tester</div><div><span>4</span>Publier</div></div>{fig}
    </section>"""
    if kind == "cards":
        return f"""
    <section id="section-{tag}" class="section" data-section="{n}">
      {base_meta}<h2>{escape(title)}</h2>{body_p}
      <div class="card-grid"><div><b>Ce que je prépare</b><p>Je clarifie l'entrée de travail.</p></div><div><b>Ce que je crée</b><p>Je transforme l'idée en bloc exploitable.</p></div><div><b>Ce que je vérifie</b><p>Je regarde le résultat dans l'outil réel.</p></div></div>{fig}
    </section>"""
    if kind == "diagnostic":
        return f"""
    <section id="section-{tag}" class="section diagnostic-layout" data-section="{n}">
      {base_meta}<h2>{escape(title)}</h2>{body_p}
      <div class="diagnostic"><b>Diagnostic rapide</b><p>Si cette étape bloque, demande-toi : suis-je dans le bon dossier ? la bonne page ? le bon statut WordPress ? le bon écran public ?</p></div>{fig}
    </section>"""
    if kind == "quote":
        return f"""
    <section id="section-{tag}" class="section quote-layout" data-section="{n}">
      {base_meta}<blockquote>{escape(body)}</blockquote><h2>{escape(title)}</h2>
      <p class="lead">Je garde cette idée en tête pendant toute la séance : un blog utile se construit avec une méthode, pas avec une succession de clics.</p>{fig}
    </section>"""
    if kind == "recap":
        return f"""
    <section id="section-{tag}" class="section recap" data-section="{n}">
      {base_meta}<h2>{escape(title)}</h2>{body_p}
      <div class="recap-grid"><div>/blog/ propre</div><div>Article lisible</div><div>Champs remplis</div><div>Mobile validé</div><div>Catégories utiles</div><div>Prompts gardés</div></div>
    </section>"""

    return f"""
    <section id="section-{tag}" class="section split" data-section="{n}">
      <div>{base_meta}<h2>{escape(title)}</h2>{body_p}</div>
      <div class="method-box"><b>Méthode</b><ol><li>Je prépare le contexte.</li><li>Je lance une action courte.</li><li>Je vérifie dans l'interface réelle.</li><li>Je corrige uniquement ce qui bloque.</li></ol></div>{fig}
    </section>"""


def build_html(visuals: list[dict[str, str]]) -> str:
    sections = "\n".join(section_html(i, s, visuals) for i, s in enumerate(SECTIONS, 1))
    nav = "".join(f'<a href="#section-{i:02d}">{i:02d}</a>' for i in range(1, 81))
    visual_list = "".join(f'<li><a href="{v["file"]}" target="_blank">Capture {v["id"]:02d}</a> — {escape(v["caption"])}</li>' for v in visuals)
    return f"""<!doctype html>
<html lang="fr" id="top">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Séance 10 — Blog automatique | DENEM Academy</title>
  <meta name="description" content="Support complet : créer une structure de blog WordPress avec Codex, Elementor, ACF, Rank Math et une méthode de vérification simple.">
  <link rel="icon" href="logo-denem.jpeg">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    :root{{--ink:#0f172a;--muted:#475569;--paper:#fff;--blue:#2563eb;--violet:#7c3aed;--green:#32d397;--soft:#f8fafc;--line:#0f172a;--shadow:7px 7px 0 var(--ink);--shadow-sm:4px 4px 0 var(--ink)}}
    *{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:#fff;color:var(--ink);font-family:Inter,system-ui,sans-serif;letter-spacing:0;overflow-x:hidden}}::selection{{background:#dbeafe;color:#0f172a}}a{{color:inherit}}.progress{{position:fixed;top:0;left:0;height:6px;background:linear-gradient(90deg,var(--blue),var(--violet),var(--green));z-index:100;width:0}}.topbar{{position:sticky;top:0;z-index:90;background:rgba(255,255,255,.94);backdrop-filter:blur(14px);border-bottom:2px solid var(--ink)}}.topbar-inner{{max-width:1320px;margin:auto;padding:12px 18px;display:flex;align-items:center;justify-content:space-between;gap:18px}}.brand{{display:flex;align-items:center;gap:12px;text-decoration:none;font-weight:900}}.brand img{{width:40px;height:40px;object-fit:cover;border:2px solid var(--ink);box-shadow:var(--shadow-sm)}}.brand span{{font-family:JetBrains Mono,monospace;font-size:12px;text-transform:uppercase}}.nav{{display:flex;gap:7px;overflow-x:auto;padding-bottom:4px;max-width:760px}}.nav a{{text-decoration:none;border:2px solid var(--ink);box-shadow:var(--shadow-sm);padding:6px 8px;background:#fff;font-family:JetBrains Mono,monospace;font-size:11px;font-weight:900}}.nav a.active{{background:var(--ink);color:#fff}}.hero-main{{position:relative;overflow:hidden;border-bottom:2px solid var(--ink);background:linear-gradient(135deg,#fff 0%,#eff6ff 45%,#f5f3ff 100%)}}.hero-main:before{{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(37,99,235,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(15,23,42,.06) 1px,transparent 1px);background-size:34px 34px}}.hero-inner{{position:relative;max-width:1320px;margin:auto;padding:72px 18px 56px}}.eyebrow{{display:inline-flex;background:var(--blue);color:#fff;border:2px solid var(--ink);box-shadow:var(--shadow-sm);padding:8px 12px;font-family:JetBrains Mono,monospace;font-size:12px;font-weight:900;text-transform:uppercase}}.hero-main h1{{max-width:1000px;font-size:clamp(42px,7vw,86px);line-height:.92;margin:24px 0 20px;font-weight:950}}.hero-main p{{font-size:20px;line-height:1.75;color:#334155;max-width:900px}}.hero-actions{{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}}.hero-actions a{{text-decoration:none;border:2px solid var(--ink);box-shadow:var(--shadow-sm);background:#fff;padding:12px 16px;font-weight:900}}.hero-actions a:first-child{{background:var(--ink);color:#fff}}.summary{{max-width:1320px;margin:auto;padding:34px 18px;border-bottom:2px solid var(--ink)}}.summary-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}.summary-card{{border:2px solid var(--ink);box-shadow:var(--shadow-sm);background:#fff;padding:18px;text-decoration:none;transition:transform .18s ease}}.summary-card:hover{{transform:translate(-2px,-2px)}}.summary-card b{{font-family:JetBrains Mono,monospace;color:var(--blue)}}.summary-card p{{font-size:14px;line-height:1.6;color:var(--muted)}}main{{background:#fff}}.section{{scroll-margin-top:86px;max-width:1320px;margin:auto;padding:74px 18px;border-bottom:2px solid var(--ink)}}.section:nth-child(odd){{background-image:linear-gradient(90deg,rgba(37,99,235,.045) 0 1px,transparent 1px),linear-gradient(rgba(124,58,237,.04) 0 1px,transparent 1px);background-size:36px 36px}}.split,.hero-grid{{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:start}}.meta-row{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px}}.meta-row span{{border:2px solid var(--ink);box-shadow:var(--shadow-sm);background:#fff;padding:6px 9px;font-family:JetBrains Mono,monospace;font-size:11px;font-weight:900;text-transform:uppercase}}.meta-row .num{{background:var(--blue);color:#fff}}.section h2{{font-size:clamp(32px,4vw,54px);line-height:1.02;margin:0 0 18px;font-weight:950}}.lead{{font-size:18px;line-height:1.8;color:#334155;margin:0 0 20px}}.shot{{border:2px solid var(--ink);box-shadow:var(--shadow);background:#fff;margin:0 0 24px;overflow:hidden}}.shot img{{display:block;width:100%;height:auto;background:#fff}}.shot figcaption{{display:flex;gap:10px;align-items:flex-start;border-top:2px solid var(--ink);padding:12px 14px;font-size:13px;line-height:1.5;color:#334155;font-weight:800}}.shot figcaption span{{font-family:JetBrains Mono,monospace;color:var(--blue)}}.note-row,.before-after,.card-grid,.check-grid,.recap-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:22px}}.note-row div,.before-after div,.card-grid div,.method-box,.tip,.warning,.diagnostic,.recap-grid div{{border:2px solid var(--ink);box-shadow:var(--shadow-sm);background:#fff;padding:18px}}.note-row b,.tip b,.warning b,.diagnostic b,.method-box b{{font-family:JetBrains Mono,monospace;text-transform:uppercase;font-size:12px}}.note-row p,.card-grid p,.before-after p,.tip p,.warning p,.diagnostic p{{line-height:1.65;color:#334155;margin:8px 0 0}}.warning{{background:#fff7ed}}.tip{{background:#eff6ff}}.diagnostic{{background:#111827;color:#fff}}.diagnostic p{{color:#e5e7eb}}.check-grid{{grid-template-columns:repeat(4,1fr)}}.check-grid label{{border:2px solid var(--ink);box-shadow:var(--shadow-sm);background:#fff;padding:16px;font-weight:850;line-height:1.35}}.check-grid input{{width:18px;height:18px;margin-right:8px;accent-color:var(--blue)}}.prompt-card{{border:2px solid var(--ink);box-shadow:var(--shadow);background:#0b1020;color:#fff;margin:18px 0;overflow:hidden}}.prompt-head{{display:flex;justify-content:space-between;align-items:center;gap:12px;border-bottom:2px solid rgba(255,255,255,.25);padding:10px 12px;background:#111827}}.prompt-head span{{font-family:JetBrains Mono,monospace;text-transform:uppercase;font-size:12px;font-weight:900;color:#bfdbfe}}.copy-btn{{border:2px solid #fff;background:#fff;color:#0f172a;padding:7px 10px;font-weight:900;cursor:pointer}}.copy-btn.copied{{background:#bbf7d0}}.prompt-card pre{{margin:0;padding:20px;white-space:pre-wrap;overflow-x:auto;font-family:JetBrains Mono,monospace;font-size:13px;line-height:1.75}}.table-wrap{{overflow:auto;border:2px solid var(--ink);box-shadow:var(--shadow-sm);margin-top:22px}}table{{border-collapse:collapse;width:100%;min-width:720px;background:#fff}}th,td{{border:2px solid var(--ink);padding:14px;text-align:left;vertical-align:top;line-height:1.55}}th{{background:var(--ink);color:#fff}}.timeline{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:22px}}.timeline div{{border:2px solid var(--ink);box-shadow:var(--shadow-sm);background:#fff;padding:18px;font-weight:900}}.timeline span{{display:inline-grid;place-items:center;width:30px;height:30px;background:var(--violet);color:#fff;border:2px solid var(--ink);margin-right:8px;font-family:JetBrains Mono,monospace}}blockquote{{font-size:clamp(28px,4vw,48px);line-height:1.15;font-weight:950;margin:0 0 22px;padding:24px;border-left:10px solid var(--violet);background:#f5f3ff}}.method-box ol{{margin:12px 0 0;padding-left:20px;line-height:1.85;color:#334155;font-weight:750}}.recap{{background:#0f172a;color:#fff;max-width:none}}.recap .lead{{color:#e2e8f0}}.recap-grid{{grid-template-columns:repeat(3,1fr);max-width:1100px}}.recap-grid div{{background:#fff;color:#0f172a;font-weight:900;text-align:center}}.assets-list{{max-width:1320px;margin:auto;padding:56px 18px;border-bottom:2px solid var(--ink)}}.assets-list ol{{columns:2;line-height:1.8;color:#334155}}.assets-list a{{color:var(--blue);font-weight:800}}.footer{{border-top:2px solid var(--ink);padding:26px 18px;font-family:JetBrains Mono,monospace;font-size:12px;font-weight:900;text-transform:uppercase}}.footer-inner{{max-width:1320px;margin:auto;display:flex;justify-content:space-between;gap:16px;align-items:center}}.reveal{{opacity:0;transform:translateY(18px);transition:.45s ease}}.reveal.visible{{opacity:1;transform:none}}@media(max-width:1050px){{.summary-grid{{grid-template-columns:repeat(2,1fr)}}.split,.hero-grid{{grid-template-columns:1fr}}.check-grid,.timeline,.recap-grid{{grid-template-columns:repeat(2,1fr)}}.nav{{max-width:100%}}.topbar-inner{{align-items:flex-start;flex-direction:column}}}}@media(max-width:700px){{.hero-inner{{padding:46px 16px}}.summary-grid,.note-row,.before-after,.card-grid,.check-grid,.timeline,.recap-grid{{grid-template-columns:1fr}}.section{{padding:54px 16px}}.shot{{box-shadow:var(--shadow-sm)}}.prompt-card pre{{font-size:12px}}.assets-list ol{{columns:1}}.footer-inner{{flex-direction:column;align-items:flex-start}}}}
  </style>
</head>
<body>
  <div class="progress" id="progress"></div>
  <header class="topbar">
    <div class="topbar-inner">
      <a class="brand" href="#top"><img src="logo-denem.jpeg" alt="Logo DENEM Academy"><span>DENEM Academy · Séance 10</span></a>
      <nav class="nav" aria-label="Navigation sections">{nav}</nav>
    </div>
  </header>
  <section class="hero-main">
    <div class="hero-inner">
      <span class="eyebrow">Acte 2 · Lancer · Blog automatique</span>
      <h1>Créer la structure de blog WordPress avec Codex.</h1>
      <p>Je pars du site RestIA créé avant. Je garde le même système, le même dossier, le même design. Cette fois, je prépare le blog : archive, articles, champs, catégories, SEO, images, vérifications. Le but est simple : tu dois pouvoir refaire la séance sans te perdre.</p>
      <div class="hero-actions"><a href="#section-01">Commencer</a><a href="#prompts">Prompts à copier</a><a href="#assets">Captures utilisées</a></div>
    </div>
  </section>
  <aside class="summary">
    <div class="summary-grid">
      <a class="summary-card" href="#section-01"><b>01</b><h3>Comprendre le but</h3><p>Je ne crée pas un blog pour remplir le menu. Je crée une base de publication IA.</p></a>
      <a class="summary-card" href="#section-09"><b>02</b><h3>Préparer Codex</h3><p>Je lance Codex au bon endroit et je le connecte à WordPress.</p></a>
      <a class="summary-card" href="#section-17"><b>03</b><h3>Construire /blog/</h3><p>Je donne une structure d'archive claire : hero, filtres, grid, sidebar.</p></a>
      <a class="summary-card" href="#section-25"><b>04</b><h3>Construire l'article</h3><p>Je crée le template Single Post avec les blocs utiles.</p></a>
      <a class="summary-card" href="#section-40"><b>05</b><h3>Structurer les champs</h3><p>ACF, Rank Math, catégories, slug, image mise en avant.</p></a>
      <a class="summary-card" href="#section-50"><b>06</b><h3>Tester le contenu</h3><p>Je publie seulement après preview et contrôle.</p></a>
      <a class="summary-card" href="#section-64"><b>07</b><h3>Vérifier</h3><p>Desktop, mobile, admin, liens, statuts et rapport.</p></a>
      <a class="summary-card" href="#section-74"><b>08</b><h3>Industrialiser</h3><p>Je transforme la séance en méthode réutilisable.</p></a>
    </div>
  </aside>
  <main>
{sections}
  </main>
  <section id="assets" class="assets-list">
    <div class="meta-row"><span class="num">IMG</span><span>23 captures</span><span>aucune image externe</span></div>
    <h2>Captures utilisées dans le support</h2>
    <p class="lead">Les visuels servent à expliquer les étapes réelles : dossier, Codex, WordPress, article, catégories, image mise en avant, médiathèque et contrôle.</p>
    <ol>{visual_list}</ol>
  </section>
  <section id="prompts" class="assets-list">
    <div class="meta-row"><span class="num">PROMPTS</span><span>copiables</span><span>à garder</span></div>
    <h2>Index des prompts</h2>
    {''.join(render_prompt(k) for k in PROMPTS)}
  </section>
  <footer class="footer"><div class="footer-inner"><span>DENEM Academy · Séance 10</span><span>Blog automatique avec Codex</span></div></footer>
  <script>
    const progress = document.getElementById('progress');
    const navLinks = [...document.querySelectorAll('.nav a')];
    const sections = [...document.querySelectorAll('[data-section]')];
    const update = () => {{
      const max = document.documentElement.scrollHeight - innerHeight;
      progress.style.width = Math.max(0, Math.min(100, scrollY / max * 100)) + '%';
      let active = 0;
      sections.forEach((s, i) => {{ if (s.getBoundingClientRect().top < innerHeight * .35) active = i; }});
      navLinks.forEach((a, i) => a.classList.toggle('active', i === active));
    }};
    addEventListener('scroll', update, {{passive:true}}); update();
    document.querySelectorAll('.copy-btn').forEach(btn => {{
      btn.addEventListener('click', async () => {{
        const code = btn.closest('.prompt-card').querySelector('code').innerText;
        await navigator.clipboard.writeText(code);
        btn.classList.add('copied'); btn.innerText = 'Copié';
        setTimeout(() => {{ btn.classList.remove('copied'); btn.innerText = 'Copier'; }}, 1200);
      }});
    }});
    const obs = new IntersectionObserver(entries => entries.forEach(e => e.target.classList.toggle('visible', e.isIntersecting)), {{threshold:.12}});
    document.querySelectorAll('.section,.summary-card,.shot').forEach(el => {{ el.classList.add('reveal'); obs.observe(el); }});
    addEventListener('keydown', e => {{
      if (e.key.toLowerCase() === 'b') document.body.classList.toggle('show-blog-path');
    }});
  </script>
</body>
</html>
"""


def build_transcription() -> None:
    out = ROOT / "transcription"
    out.mkdir(exist_ok=True)
    raw_path = out / "seance-10-transcription-brute.txt"
    segments_path = out / "seance-10-segments.json"
    md = [
        "# Séance 10 - Blog automatique",
        "",
        "## Lecture rapide",
        "",
        "- Je pars du site WordPress construit en séance 9.",
        "- Je choisis Codex pour une mission longue, parce que je veux une exécution plus profonde.",
        "- Je connecte Codex à WordPress avec le Chrome MCP.",
        "- Je lui demande d'analyser le site avant de construire le blog.",
        "- Je crée la structure : archive `/blog/`, template Single Post, catégories, champs ACF et SEO.",
        "- Je teste avec des articles, je vérifie le rendu, puis j'ouvre la suite vers le blog automatique avec VPS et API.",
        "",
        "## Moments importants",
        "",
    ]
    moments = [
        ("00:00:06", "Je pose le sujet : blog automatique, structure de blog et future publication SEO."),
        ("00:00:48", "Je justifie le choix de Codex pour les tâches longues et complexes."),
        ("00:03:17", "Je liste les 4 grandes actions : analyser le site, installer les plugins, créer ACF, construire les templates."),
        ("00:04:30", "Je rappelle les prérequis : WordPress, accès, Codex et Chrome MCP."),
        ("00:05:15", "Je lance Codex depuis le bon dossier de travail."),
        ("00:08:53", "Je prépare le prompt principal au lieu de demander un blog vague."),
        ("00:13:10", "Je force Codex à travailler en phases pour qu'il s'auto-corrige."),
        ("00:14:00", "Je demande l'analyse des pages, du design, de la typo, des espacements et des composants."),
        ("00:16:37", "Je passe aux prérequis : plugins, taxonomies et champs ACF."),
        ("00:20:59", "Je détaille le template Single Post pour chaque futur article."),
        ("00:24:59", "Je demande image principale, sommaire, FAQ, sources et structure SEO."),
        ("00:31:24", "Je montre que cette compétence peut être vendue comme une vraie prestation."),
        ("00:39:23", "Je résume la logique : prompt, exécution, amélioration, blog, puis automatisation."),
        ("00:51:56", "Je vérifie l'article et je repère les points à corriger comme le TL;DR."),
        ("01:03:00", "Je contrôle l'article SEO long : tableaux, cas d'usage, FAQ et sommaire."),
        ("01:06:29", "J'annonce la suite : blog automatique, VPS et API."),
    ]
    for t, text in moments:
        md.append(f"- `{t}` {text}")
    md.extend(["", "## Prompts repris", ""])
    for k, v in PROMPTS.items():
        md.append(f"### {k}\n\n```text\n{v}\n```")
    md.extend(["", "## Fichiers de transcription", ""])
    if raw_path.exists():
        md.append("- `seance-10-transcription-brute.txt` : transcription brute complète.")
    if segments_path.exists():
        md.append("- `seance-10-segments.json` : segments horodatés.")
    (out / "seance-10-moments-importants.md").write_text("\n".join(md), encoding="utf-8")


def main() -> None:
    visuals = copy_visuals()
    (ROOT / "index.html").write_text(build_html(visuals), encoding="utf-8")
    build_transcription()
    (ROOT / ".gitignore").write_text(".DS_Store\n*.mp4\n*.mov\n*.m4v\n*.m4a\nnode_modules/\n.playwright-mcp/\ndraft_frames/\ntools/__pycache__/\n10-*/\n", encoding="utf-8")


if __name__ == "__main__":
    main()
