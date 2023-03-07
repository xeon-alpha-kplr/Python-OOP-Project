import json
from unidecode import unidecode
from treelib import Tree
import os

def json_dict_from_file():
    json_data = json.load(open('/workspaces/Python-OOP-Project/exercices/03.class_tree/json_data.json', "rb"))
    json_str = json.dumps(json_data)
    json_data = (unidecode(json_str))
    json_dict = json.loads(json_data)

    return json_dict

def create_tree_from_dict(tree, parent_node_id, parent_dict):
    for key, value in parent_dict.items():
        if isinstance(value, dict):
            # Créer un nouveau noeud pour la clé courante du dictionnaire
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            create_tree_from_dict(tree, new_node_id, value)
        else:
            # Créer un nouveau noeud pour la feuille courante du dictionnaire
            leaf_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)

def recursive_tree_from_json(tree, json_dict, parent_node_id):
    for key, value in json_dict.items():
        if (key == "subclasses"):
            recursive_tree_from_json(tree, json_dict, parent_node_id)
        elif (isinstance(value, dict)):
            new_node_id = f"(parent_node_id).{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            recursive_tree_from_json(tree, json_dict, parent_node_id)
        elif not (isinstance(value,dict)):
            pass


def main():
    
    my_tree = Tree()
    # Créer le noeud racine pour l'arbre
    my_tree.create_node(tag="Racine", identifier="racine")

    # Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    json_dict = json_dict_from_file()
    create_tree_from_dict(my_tree, "racine", json_dict)
    recursive_tree_from_json(my_tree, json_dict, "racine")
    # Afficher l'arbre
    my_tree.show()

if __name__ == '__main__':
    # Appeler la fonction principale
    main()