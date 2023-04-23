# FilesMirror *version threads*

<!-- membres ici -->
> ### **Membres :** 
> - POTEZ Alexandre
> - RASCLE Jérôme
> - GARCIA Matéo

## Comment utiliser le projet

Pour utiliser notre projet, il faut lancer le fichier `main.py` comme pour la version séquentielle. Avec comme paramètre:
- Les informations de connexion au serveur FTP.
- Le fichier local à synchroniser.
- La profondeur de recherche.
- La fréquence de synchronisation.
- **Le nombre de threads à utiliser.**
- Les extensions à exclure (option).

```bash
python3 main.py ftbUrl,user,password,,port local_path depth frequency threads [extensions]
```
