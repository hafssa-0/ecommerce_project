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

Lancement du serveur :
python manage.py runserver

Accéder à l'application : http://127.0.0.1:8000/

Aperçu du Projet

Voici les différentes interfaces et étapes de réalisation :

2. Architecture du Projet

L'application est divisée en deux modules principaux : products (catalogue) et accounts (comptes utilisateurs).
<img width="1915" height="997" alt="image" src="https://github.com/user-attachments/assets/06f147de-944a-46d8-b1bc-e86afefad138" />


3. capture de la liste des produits :

Présentation des articles disponibles avec images.
<img width="1920" height="889" alt="image" src="https://github.com/user-attachments/assets/12dece24-c761-4015-a5d2-da384f6c23f8" />
4. capture du détail d’un produit : 
<img width="1912" height="675" alt="image" src="https://github.com/user-attachments/assets/f8680e3d-0a2c-4cbd-9be3-a7a1526278ce" />
5. capture de la page d’inscription
<img width="1897" height="568" alt="image" src="https://github.com/user-attachments/assets/c44fdd9d-1e0c-4d70-95c2-e9b625b8a6f4" />

6. capture de la page de connexion 



<img width="1890" height="380" alt="image" src="https://github.com/user-attachments/assets/0e97a5b9-dde7-450c-8fda-2637634f3b61" />

7. capture de la page profil après connexion

  <img width="1894" height="462" alt="image" src="https://github.com/user-attachments/assets/a506c4db-7d1f-41e8-9a95-9ebc46b0b933" />

8. capture montrant la déconnexion

Déconnexion : Bouton permettant de fermer la session de manière sécurisée.
<img width="1899" height="529" alt="image" src="https://github.com/user-attachments/assets/ac9638f6-74d0-416c-9028-83e2c2b9fbcb" />

9. capture de l’interface d’administration Django

Interface Django pour la gestion totale du contenu (produits, catégories).
<img width="1882" height="539" alt="image" src="https://github.com/user-attachments/assets/e6de5ffc-eb28-4153-935f-de1ba7e5668e" />


10. @login_required

Dans AuraLand, la sécurité des pages sensibles (comme le profil ou le panier) est assurée par @login_required qui est un décorateur. Il intercepte la requête pour vérifier si l'utilisateur est authentifié avant d'autoriser l'accès à la vue. Si l'utilisateur n'est pas connecté, il est automatiquement redirigé vers la page de connexion. Cela garantit la protection des données privées.

11. {% csrf_token %}

C'est un tag. Il est présent dans tous nos formulaires (inscription, connexion, ajout au panier), il est une mesure de sécurité obligatoire. Il protège l'application contre les attaques CSRF (Cross-Site Request Forgery). Django génère un jeton unique et secret pour chaque session, prouvant que la requête provient bien de notre application et non d'un site tiers malveillant.

12. une démonstration que la page profil est inaccessible sans connexion:
<img width="1888" height="425" alt="image" src="https://github.com/user-attachments/assets/3b973e16-d3fd-4468-a7f1-aa1fe9b6b4d7" />
