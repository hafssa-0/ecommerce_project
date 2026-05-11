E-commerce Project avec django 

Ce projet est une application de gestion de produits développée avec Django. Il permet de gérer un catalogue de produits organisés par catégories, incluant des images et des détails techniques. 

Architecture et MécanismesDjango repose sur le pattern MVT (Model-View-Template). Voici comment les fichiers interagissent entre eux dans ce projet :
1. Le Modèle (models.py)C'est le cœur de l'application. Il définit la structure de la base de données via l'ORM (Object-Relational Mapping).
2. Category : Représente les catégories de produits.Product : Représente les articles en vente.Relation : Une relation ForeignKey (plusieurs-à-un) lie les produits aux catégories : une catégorie peut avoir plusieurs produits, mais un produit n'appartient qu'à une seule catégorie.
3.Les Vues (views.py)Les vues contiennent la logique métier. Elles récupèrent les données depuis les modèles et les envoient aux templates.
product_list : Récupère tous les produits via Product.objects.all().
category_detail : Utilise related_name='products' pour lister tous les produits liés à une catégorie spécifique.
4. Les Templates (templates/products/)Ce sont les fichiers HTML qui définissent l'affichage. Ils utilisent le langage de template Django (ex: {% for product in products %}) pour afficher dynamiquement les données envoyées par les vues.
5. Le Routage (urls.py)Il fait le lien entre l'URL tapée par l'utilisateur dans le navigateur et la fonction correspondante dans views.py 

Installation et ConfigurationPrérequisPython installéEnvironnement virtuel activé (myenv) Librairie Pillow pour la gestion des images : pip install pillow 
