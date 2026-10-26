# TP2 : Inventaire 
> Dorian BORDERAN | ESGI M1 SI 2026-2027

```bash
debian@debian1 ~/api-rest-m1-1 (main)> python3 -m venv .venv
debian@debian1 ~/api-rest-m1-1 (main)> source .venv/bin/activate.fish

(.venv) debian@debian1 ~/api-rest-m1-1 (main)> pip install requests
Collecting requests
  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.5.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (46 kB)
Collecting idna<4,>=2.5 (from requests)
  Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting urllib3<3,>=1.26 (from requests)
  Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting certifi>=2023.5.7 (from requests)
  Downloading certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
Downloading requests-2.34.2-py3-none-any.whl (73 kB)
Downloading charset_normalizer-3.5.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (254 kB)
Downloading idna-3.20-py3-none-any.whl (69 kB)
Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
Downloading certifi-2026.10.23-py3-none-any.whl (135 kB)
Installing collected packages: urllib3, idna, charset_normalizer, certifi, requests
Successfully installed certifi-2026.10.23 charset_normalizer-3.5.2 idna-3.20 requests-2.34.2 urllib3-2.8.0
(.venv) debian@debian1 ~/api-rest-m1-1 (main)> echo "requests" > requirements
.txt
```

```bash
debian@debian1:~/api-rest-m1-1/adminapi$ source ../.venv/bin/activate
set -a; source .env; set +a
(.venv) debian@debian1:~/api-rest-m1-1/adminapi$ touch inventaire.py
(.venv) debian@debian1:~/api-rest-m1-1/adminapi$ python inventaire.py
-> Interrogation de l'API Docker...
-> Interrogation de l'API NetBox...

================== INVENTAIRE ==================
Date du relevé     : 2026-10-26T10:25:22.509297+00:00
NetBox version     : 4.7.3
Types d'objets     : 163 (count API = 163)
Conteneurs Docker  : 6
------------------------------------------------
 - intrus               [running]  CPU:   0.0%  RAM:    4.89 Mo  (nginx:alpine)
 - web1                 [running]  CPU:   0.0%  RAM:    4.76 Mo  (nginx:alpine)
 - apirest-netbox-1     [running]  CPU:  0.01%  RAM: 1262.75 Mo  (netboxcommunity/netbox:v4.7-5.1.1)
 - apirest-netbox-postgres-1 [running]  CPU:  3.61%  RAM:   64.67 Mo  (postgres:17-alpine)
 - apirest-docker-api-1 [running]  CPU:   0.0%  RAM:   26.97 Mo  (tecnativa/docker-socket-proxy:v0.4.2)
 - apirest-netbox-redis-1 [running]  CPU:  0.38%  RAM:   16.21 Mo  (valkey/valkey:8-alpine)
================================================
Fichier inventaire.json généré avec succès.

(.venv) debian@debian1:~/api-rest-m1-1/adminapi$ cat inventaire.json | head -n 30
{
  "date": "2026-10-26T10:25:22.509297+00:00",
  "docker": {
    "total_conteneurs": 6,
    "conteneurs": [
      {
        "id": "80dac4f0addf",
        "nom": "intrus",
        "image": "nginx:alpine",
        "etat": "running",
        "cpu_pourcent": 0.0,
        "memoire_mo": 4.89
      },
      {
        "id": "6587593e7474",
        "nom": "web1",
        "image": "nginx:alpine",
        "etat": "running",
        "cpu_pourcent": 0.0,
        "memoire_mo": 4.76
      },
      {
        "id": "cd599e4ea199",
        "nom": "apirest-netbox-1",
        "image": "netboxcommunity/netbox:v4.7-5.1.1",
        "etat": "running",
        "cpu_pourcent": 0.01,
        "memoire_mo": 1262.75
      },
      {
(.venv) debian@debian1:~/api-rest-m1-1/adminapi$ 
```