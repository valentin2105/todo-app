"""Gestionnaire de tâches en ligne de commande."""
import json
import sys
from pathlib import Path

FICHIER = Path("taches.json")


def charger():
    if FICHIER.exists():
        return json.loads(FICHIER.read_text(encoding="utf-8"))
    return []


def sauvegarder(taches):
    FICHIER.write_text(json.dumps(taches, indent=2, ensure_ascii=False), encoding="utf-8")


def ajouter(texte):
    taches = charger()
    taches.append({"texte": texte, "faite": False})
    sauvegarder(taches)
    print(f"Tâche ajoutée : {texte}")


def lister():
    taches = charger()
    if not taches:
        print("Aucune tâche.")
    for numero, tache in enumerate(taches, start=1):
        case = "x" if tache["faite"] else " "
        print(f"{numero}. [{case}] {tache['texte']}")
    print(f"Total : {len(taches)} tâche(s)")


def afficher_aide():
    print("Usage : python todo.py <commande> [arguments]")
    print("Commandes : ajouter <texte>, lister, aide")


def main():
    if len(sys.argv) < 2:
        afficher_aide()
        return
    commande = sys.argv[1]
    if commande == "ajouter":
        ajouter(" ".join(sys.argv[2:]))
    elif commande == "lister":
        lister()
    elif commande == "aide":
        afficher_aide()
    else:
        print(f"Commande inconnue : {commande}")

if __name__ == "__main__":
    main()
