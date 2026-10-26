import os
import sys
import json
from datetime import datetime, timezone
import requests

# 1. Variables d'environnement
DOCKER = os.environ.get("DOCKER_API_URL", "http://127.0.0.1:2375")
NETBOX = os.environ.get("NETBOX_URL", "http://127.0.0.1:8080")

try:
    JETON = os.environ["NETBOX_TOKEN"]
except KeyError:
    sys.exit("Erreur : La variable d'environnement NETBOX_TOKEN n'est pas définie.")

TIMEOUT = 5  # Timeout en secondes pour éviter de bloquer indéfiniment

def main():
    session = requests.Session()

    # --- PARTIE 1 : DOCKER ---
    print("-> Interrogation de l'API Docker...")
    try:
        # Lister tous les conteneurs (all=true)
        res = session.get(f"{DOCKER}/containers/json?all=true", timeout=TIMEOUT)
        res.raise_for_status()
        containers_raw = res.json()
    except requests.RequestException as e:
        sys.exit(f"Erreur critique lors de la connexion à l'API Docker ({DOCKER}) : {e}")

    conteneurs = []

    for c in containers_raw:
        c_id = c["Id"]
        nom = c["Names"][0].lstrip("/") if c.get("Names") else c_id[:12]
        image = c.get("Image", "")
        etat = c.get("State", "")

        cpu_pct = 0.0
        mem_mo = 0.0

        # Mesure stats uniquement si le conteneur est en cours d'exécution
        if etat == "running":
            try:
                stats_res = session.get(f"{DOCKER}/containers/{c_id}/stats?stream=false", timeout=TIMEOUT)
                if stats_res.status_code == 200:
                    stats = stats_res.json()
                    
                    # Calcul CPU selon la formule du cours
                    cpu = stats.get("cpu_stats", {})
                    avant = stats.get("precpu_stats", {})
                    delta_cpu = cpu.get("cpu_usage", {}).get("total_usage", 0) - avant.get("cpu_usage", {}).get("total_usage", 0)
                    delta_systeme = cpu.get("system_cpu_usage", 0) - avant.get("system_cpu_usage", 0)
                    online_cpus = cpu.get("online_cpus", 1)
                    
                    if delta_systeme and delta_systeme > 0:
                        cpu_pct = round((delta_cpu / delta_systeme) * online_cpus * 100, 2)
                    
                    # Calcul Mémoire en Mo
                    mem_usage = stats.get("memory_stats", {}).get("usage", 0)
                    mem_mo = round(mem_usage / 1024 / 1024, 2)
            except requests.RequestException:
                pass  # Si le conteneur s'arrête entre temps

        conteneurs.append({
            "id": c_id[:12],
            "nom": nom,
            "image": image,
            "etat": etat,
            "cpu_pourcent": cpu_pct,
            "memoire_mo": mem_mo
        })

    # --- PARTIE 2 : NETBOX ---
    print("-> Interrogation de l'API NetBox...")
    headers = {"Authorization": f"Bearer {JETON}"}

    # 1. Version de NetBox
    try:
        status_res = session.get(f"{NETBOX}/api/status/", headers=headers, timeout=TIMEOUT)
        status_res.raise_for_status()
        netbox_version = status_res.json().get("netbox-version", "inconnue")
    except requests.RequestException as e:
        sys.exit(f"Erreur critique lors de la récupération du statut NetBox : {e}")

    # 2. Pagination des types d'objets (/api/core/object-types/?limit=50)
    url_types = f"{NETBOX}/api/core/object-types/?limit=50"
    nb_types = 0
    total_attendu = None

    try:
        while url_types:
            r = session.get(url_types, headers=headers, timeout=TIMEOUT)
            r.raise_for_status()
            data = r.json()
            if total_attendu is None:
                total_attendu = data.get("count", 0)
            
            nb_types += len(data.get("results", []))
            url_types = data.get("next")  # Suit le lien 'next' tant qu'il n'est pas None
    except requests.RequestException as e:
        sys.exit(f"Erreur critique lors de la pagination des types d'objets NetBox : {e}")

    # --- PARTIE 3 : ÉCRITURE DANS INVENTAIRE.JSON ---
    inventaire = {
        "date": datetime.now(timezone.utc).isoformat(),
        "docker": {
            "total_conteneurs": len(conteneurs),
            "conteneurs": conteneurs
        },
        "netbox": {
            "version": netbox_version,
            "object_types_count": nb_types
        }
    }

    with open("inventaire.json", "w", encoding="utf-8") as f:
        json.dump(inventaire, f, indent=2, ensure_ascii=False)

    # --- RÉSUMÉ LISIBLE DANS LE TERMINAL ---
    print("\n================== INVENTAIRE ==================")
    print(f"Date du relevé     : {inventaire['date']}")
    print(f"NetBox version     : {netbox_version}")
    print(f"Types d'objets     : {nb_types} (count API = {total_attendu})")
    print(f"Conteneurs Docker  : {len(conteneurs)}")
    print("------------------------------------------------")
    for c in conteneurs:
        print(f" - {c['nom']:<20} [{c['etat']:<7}]  CPU: {c['cpu_pourcent']:>5}%  RAM: {c['memoire_mo']:>7} Mo  ({c['image']})")
    print("================================================")
    print("Fichier inventaire.json généré avec succès.\n")

if __name__ == "__main__":
    main()
