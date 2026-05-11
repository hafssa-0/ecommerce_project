AuraLand - Plateforme E-Commerce

AuraLand est une application de commerce électronique moderne développée avec le framework Django. Ce projet permet de gérer un catalogue complet de produits organisés par catégories, avec une gestion précise des stocks, des images et un système d'authentification sécurisé.

Fonctionnalités principales

Gestion du Catalogue : Affichage dynamique des produits et des catégories avec une interface fluide.

Système d'Authentification : Gestion complète des comptes (Inscription personnalisée, Connexion et Déconnexion).

Espace Client Sécurisé : Page de profil protégée affichant les informations de l'utilisateur et accès réservé au panier.

Infrastructure Docker : Utilisation d'un conteneur MySQL pour une base de données robuste et portable.

Interface d'Administration : Tableau de bord centralisé pour la gestion des articles, des catégories et des droits d'accès.

Architecture et Mécanismes (MVT)

Le projet repose sur l'architecture Model-View-Template de Django :

1. Le Modèle (models.py)

Définit la structure des données via l'ORM :

Category : Classe permettant de classer les produits (nom unique).

Product : Gère les informations techniques (prix, stock, description) et les images via la bibliothèque Pillow.

Relation : Une ForeignKey lie chaque produit à une catégorie (liaison plusieurs-à-un).

2. Les Vues (views.py)

Elles traitent la logique métier et les restrictions d'accès :

product_list & product_detail : Récupération des données pour l'affichage boutique.

signup : Gestion de la création de nouveaux comptes via RegisterForm.

profile & cart : Vues sécurisées accessibles uniquement aux membres connectés.

3. Les Templates (templates/)

Interface utilisateur utilisant le langage de template Django :

Héritage : Utilisation de layout.html pour garantir une barre de navigation (Navbar) et un pied de page (Footer) cohérents sur tout le site.

Aperçu du Projet

Voici les différentes interfaces et étapes de réalisation :

1. Architecture du Projet

L'application est divisée en deux modules principaux : products (catalogue) et accounts (comptes utilisateurs).
<img width="1915" height="997" alt="image" src="https://github.com/user-attachments/assets/06f147de-944a-46d8-b1bc-e86afefad138" />


2. Boutique AuraLand

Liste des produits : Présentation des articles disponibles avec images.

Détails du produit : Fiche technique affichant le prix, la description et le stock.
[Image de la liste des produits]
[Image de détails d'un produit]

3. Espace Utilisateur

Inscription & Connexion : Formulaires de sécurité pour accéder à l'espace client.

Profil après connexion : Page dédiée affichant les informations du compte (Nom d'utilisateur, Email, Statut).
[Image de la page d'inscription]
[Image de la page de connexion]
[Image de la page de profil après connexion]

4. Sécurité

Déconnexion : Bouton permettant de fermer la session de manière sécurisée.
[Image montrant la déconnexion]

5. Administration

Interface Django pour la gestion totale du contenu (Produits, Catégories, Groupes).
[Image de l'interface d'administration Django]

🔒 Concepts de Sécurité implémentés

Le décorateur @login_required

Dans AuraLand, la sécurité des pages sensibles (comme le Profil ou le Panier) est assurée par ce décorateur.

Son rôle : Il intercepte la requête pour vérifier si l'utilisateur est authentifié avant d'autoriser l'accès à la vue.

Fonctionnement : Si l'utilisateur n'est pas connecté, il est automatiquement redirigé vers la page de connexion. Cela garantit la protection des données privées.

Le tag {% csrf_token %}

Présent dans tous nos formulaires (inscription, connexion, ajout au panier), ce tag est une mesure de sécurité obligatoire.

Son rôle : Il protège l'application contre les attaques CSRF (Cross-Site Request Forgery).

Fonctionnement : Django génère un jeton unique et secret pour chaque session, prouvant que la requête provient bien de notre application et non d'un site tiers malveillant.

🚀 Installation et Configuration

Prérequis

Python 3.x

Docker & Docker Compose

Environnement virtuel (myenv) activé.

Lancement rapide

Installation des dépendances :
pip install pillow mysqlclient

Démarrage de la base de données (Docker) :
docker-compose up -d

Synchronisation de la base :
python manage.py migrate

Lancement du serveur :
python manage.py runserver

Accéder à l'application : http://127.0.0.1:8000/
