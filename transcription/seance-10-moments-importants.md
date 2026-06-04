# Séance 10 - Blog automatique

## Lecture rapide

- Je pars du site WordPress construit en séance 9.
- Je choisis Codex pour une mission longue, parce que je veux une exécution plus profonde.
- Je connecte Codex à WordPress avec le Chrome MCP.
- Je lui demande d'analyser le site avant de construire le blog.
- Je crée la structure : archive `/blog/`, template Single Post, catégories, champs ACF et SEO.
- Je teste avec des articles, je vérifie le rendu, puis j'ouvre la suite vers le blog automatique avec VPS et API.

## Moments importants

- `00:00:06` Je pose le sujet : blog automatique, structure de blog et future publication SEO.
- `00:00:48` Je justifie le choix de Codex pour les tâches longues et complexes.
- `00:03:17` Je liste les 4 grandes actions : analyser le site, installer les plugins, créer ACF, construire les templates.
- `00:04:30` Je rappelle les prérequis : WordPress, accès, Codex et Chrome MCP.
- `00:05:15` Je lance Codex depuis le bon dossier de travail.
- `00:08:53` Je prépare le prompt principal au lieu de demander un blog vague.
- `00:13:10` Je force Codex à travailler en phases pour qu'il s'auto-corrige.
- `00:14:00` Je demande l'analyse des pages, du design, de la typo, des espacements et des composants.
- `00:16:37` Je passe aux prérequis : plugins, taxonomies et champs ACF.
- `00:20:59` Je détaille le template Single Post pour chaque futur article.
- `00:24:59` Je demande image principale, sommaire, FAQ, sources et structure SEO.
- `00:31:24` Je montre que cette compétence peut être vendue comme une vraie prestation.
- `00:39:23` Je résume la logique : prompt, exécution, amélioration, blog, puis automatisation.
- `00:51:56` Je vérifie l'article et je repère les points à corriger comme le TL;DR.
- `01:03:00` Je contrôle l'article SEO long : tableaux, cas d'usage, FAQ et sommaire.
- `01:06:29` J'annonce la suite : blog automatique, VPS et API.

## Prompts repris

### connect_codex

```text
connecte toi a mon site stp en mcp https://restia.fun/wp-admin/post.php?post=254&action=elementor
```
### archive

```text
Tu es un lead developer WordPress + Elementor Pro et un expert SEO/GEO.
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

GO.
```
### seo_article

```text
okay tu vas me faire un article seo assez long avec mon audit stp.
Ajoute des images, mets des tableaux, des listes a puces, des exemples et des liens internes / externes.
L'article doit faire environ 1400 mots.
Ne fais pas d'auto-correction globale.
Le but est de tester la structure que tu viens de construire.
```
### chatgpt_article

```text
Fais-moi un article sur l'intelligence artificielle pour tester mon blog.
Je veux un contenu simple, clair, avec une introduction, des H2, des exemples, une FAQ courte et une conclusion.
Garde un style naturel. Le but est de voir si mon template WordPress affiche bien un article complet.
```
### codex_article_import

```text
Prends cet article et mets-le proprement dans WordPress.
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
Publie seulement quand la preview est propre.
```
### quality

```text
Controle la page /blog/ et le single post.
Verifie desktop, tablette et mobile.
Verifie que les titres ne debordent pas, que les cards ont la meme hauteur, que la sidebar ne casse pas, que les images chargent, que le slug est propre et que l'article est bien publie.
Donne-moi une liste courte : OK, a corriger, correction faite.
```

## Fichiers de transcription

- `seance-10-transcription-brute.txt` : transcription brute complète.
- `seance-10-segments.json` : segments horodatés.