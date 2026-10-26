# TP1 : mémo API Docker
> Dorian BORDERAN | ESGI M1 SI 2026-2027


# 1
```bash
debian@debian1 ~/a/adminapi (main)> touch notes.md
debian@debian1 ~/a/adminapi (main)> sudo apt install jq -y
[sudo] Mot de passe de debian : 
Installation de :                               
  jq

Installation de dépendances : 
  libjq1  libonig5

Sommaire :
  Mise à niveau de : 0. Installation de : 3Supprimé : 0. Non mis à jour : 95
Taille du téléchargement : 436 kB
  Espace nécessaire : 1 271 kB / 20,4 GB disponible

Réception de : 1 http://security.debian.org/debian-security trixie-security/main amd64 libjq1 amd64 1.7.1-6+deb13u4 [168 kB]
Réception de : 2 http://deb.debian.org/debian trixie/main amd64 libonig5 amd64 6.9.9-1+b1 [189 kB]
Réception de : 3 http://security.debian.org/debian-security trixie-security/main amd64 jq amd64 1.7.1-6+deb13u4 [78,9 kB]
436 ko réceptionnés en 0s (2 451 ko/s)
Sélection du paquet libonig5:amd64 précédemment désélectionné.
(Lecture de la base de données... 46073 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de .../libonig5_6.9.9-1+b1_amd64.deb ...
Dépaquetage de libonig5:amd64 (6.9.9-1+b1) ...
Sélection du paquet libjq1:amd64 précédemment désélectionné.
Préparation du dépaquetage de .../libjq1_1.7.1-6+deb13u4_amd64.deb ...
Dépaquetage de libjq1:amd64 (1.7.1-6+deb13u4) ...
Sélection du paquet jq précédemment désélectionné.
Préparation du dépaquetage de .../jq_1.7.1-6+deb13u4_amd64.deb ...
Dépaquetage de jq (1.7.1-6+deb13u4) ...
Paramétrage de libonig5:amd64 (6.9.9-1+b1) ...
Paramétrage de libjq1:amd64 (1.7.1-6+deb13u4) ...
Paramétrage de jq (1.7.1-6+deb13u4) ...
Traitement des actions différées (« triggers ») pour man-db (2.13.1-1) ...
Traitement des actions différées (« triggers ») pour libc-bin (2.41-12+deb13u4) ...
debian@debian1 ~/a/adminapi (main)> curl -s http://127.0.0.1:2375/version
{"Platform":{"Name":"Docker Engine - Community"},"Version":"29.9.0","ApiVersion":"1.56","MinAPIVersion":"1.40","Os":"linux","Arch":"amd64","Components":[{"Name":"Engine","Version":"29.9.0","Details":{"ApiVersion":"1.56","Arch":"amd64","BuildTime":"2026-10-08T20:38:33.000000000+00:00","Experimental":"false","GitCommit":"a5b58c9","GoVersion":"go1.26.9","KernelVersion":"6.12.63+deb13-amd64","MinAPIVersion":"1.40","Module":"github.com/moby/moby/v2","ModuleVersion":"v2.0.0+unknown","Os":"linux"}},{"Name":"containerd","Version":"v2.4.2","Details":{"GitCommit":"b7a25261e029d68978bbf290df0a62fc819b3c51"}},{"Name":"runc","Version":"1.5.2","Details":{"GitCommit":"v1.5.2-0-g29dd3dc2"}},{"Name":"docker-init","Version":"0.19.0","Details":{"GitCommit":"de40ad0"}}],"GitCommit":"a5b58c9","GoVersion":"go1.26.9","KernelVersion":"6.12.63+deb13-amd64","BuildTime":"2026-10-08T20:38:33.000000000+00:00"}
debian@debian1 ~/a/adminapi (main)> curl -s http://127.0.0.1:2375/version | j
q
{
  "Platform": {
    "Name": "Docker Engine - Community"
  },
  "Version": "29.9.0",
  "ApiVersion": "1.56",
  "MinAPIVersion": "1.40",
  "Os": "linux",
  "Arch": "amd64",
  "Components": [
    {
      "Name": "Engine",
      "Version": "29.9.0",
      "Details": {
        "ApiVersion": "1.56",
        "Arch": "amd64",
        "BuildTime": "2026-10-08T20:38:33.000000000+00:00",
        "Experimental": "false",
        "GitCommit": "a5b58c9",
        "GoVersion": "go1.26.9",
        "KernelVersion": "6.12.63+deb13-amd64",
        "MinAPIVersion": "1.40",
        "Module": "github.com/moby/moby/v2",
        "ModuleVersion": "v2.0.0+unknown",
        "Os": "linux"
      }
    },
    {
      "Name": "containerd",
      "Version": "v2.4.2",
      "Details": {
        "GitCommit": "b7a25261e029d68978bbf290df0a62fc819b3c51"
      }
    },
    {
      "Name": "runc",
      "Version": "1.5.2",
      "Details": {
        "GitCommit": "v1.5.2-0-g29dd3dc2"
      }
    },
    {
      "Name": "docker-init",
      "Version": "0.19.0",
      "Details": {
        "GitCommit": "de40ad0"
      }
    }
  ],
  "GitCommit": "a5b58c9",
  "GoVersion": "go1.26.9",
  "KernelVersion": "6.12.63+deb13-amd64",
  "BuildTime": "2026-10-08T20:38:33.000000000+00:00"
}

debian@debian1 ~/a/adminapi (main)> curl -s "http://127.0.0.1:2375/containers/json?all=true" | jq

[
  {
    "Id": "cd599e4ea199c130023a60f93fa39e3aa8e5cbcc072f6877bce0e8786b4558d2",
    "Names": [
      "/apirest-netbox-1"
    ],
    "Image": "netboxcommunity/netbox:v4.7-5.1.1",
    "ImageID": "sha256:6f2bedaa56e6fb1d6ef95f6fb5e08e8eb0ecf0ac590c8da723f79bc7518da6c7",
    "ImageManifestDescriptor": {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:d5fd7e8f71d7a000d1adc075e7262d1eccc7c5e35e2a7a790f838029ed3f0654",
      "size": 3708,
      "platform": {
        "architecture": "amd64",
        "os": "linux"
      }
    },
    "Command": "/usr/bin/tini -- /opt/netbox/docker-entrypoint.sh /opt/netbox/launch-netbox.sh",
    "Created": 1793003106,
    "Ports": [
      {
        "IP": "127.0.0.1",
        "PrivatePort": 8080,
        "PublicPort": 8080,
        "Type": "tcp"
      }
    ],
    "Labels": {
      "com.docker.compose.config-hash": "155461d529f31c84d80540ee42759cf76bb9f246a22fa2e44db500c7eff37447",
      "com.docker.compose.container-number": "1",
      "com.docker.compose.depends_on": "netbox-postgres:service_healthy:false,netbox-redis:service_started:false",
      "com.docker.compose.image": "sha256:d5fd7e8f71d7a000d1adc075e7262d1eccc7c5e35e2a7a790f838029ed3f0654",
      "com.docker.compose.oneoff": "False",
      "com.docker.compose.project": "apirest",
      "com.docker.compose.project.config_files": "/home/debian/api-rest-m1-1/adminapi/docker-compose.yml",
      "com.docker.compose.project.working_dir": "/home/debian/api-rest-m1-1/adminapi",
      "com.docker.compose.service": "netbox",
      "com.docker.compose.version": "5.6.0",
      "netbox.build-reason": "ubuntu",
      "netbox.git-branch": "HEAD",
      "netbox.git-ref": "3cd2c1d6469caed6c50e80eddd4cde863e0e2cf5",
      "netbox.git-url": "https://github.com/netbox-community/netbox.git",
      "netbox.last-base-image-layer": "sha256:06ad70e463aa4a17833d00d6d5d346c895ebb66fee637eefd67024dc6cdc2f1c",
      "netbox.original-tag": "v4.7.3-5.1.1",
      "org.opencontainers.image.authors": "The netbox-docker contributors.",
      "org.opencontainers.image.created": "2026-10-14T10:37:03+00:00",
      "org.opencontainers.image.description": "A container based distribution of NetBox, the free and open IPAM and DCIM solution.",
      "org.opencontainers.image.documentation": "https://github.com/netbox-community/netbox-docker/wiki",
      "org.opencontainers.image.licenses": "Apache-2.0",
      "org.opencontainers.image.revision": "7689fec7a70717f7e72feecb383e7a3f55538b5f",
      "org.opencontainers.image.source": "https://github.com/netbox-community/netbox-docker.git",
      "org.opencontainers.image.title": "NetBox Docker",
      "org.opencontainers.image.url": "https://github.com/netbox-community/netbox-docker",
      "org.opencontainers.image.vendor": "The netbox-docker contributors.",
      "org.opencontainers.image.version": "5.1.1"
    },
    "State": "running",
    "Status": "Up 22 minutes (healthy)",
    "HostConfig": {
      "NetworkMode": "apirest_default"
    },
    "Health": {
      "Status": "healthy",
      "FailingStreak": 0
    },
    "NetworkSettings": {
      "Networks": {
        "apirest_default": {
          "IPAMConfig": null,
          "Links": null,
          "Aliases": null,
          "DriverOpts": null,
          "GwPriority": 0,
          "NetworkID": "4cb231c1d4e508100bd3343db5a80a160e602643c2c756b21bc86fa80b62830c",
          "EndpointID": "2c15b7c2cffd2d57b5a05f50fc722c884f8fa89249780b2210027434598d2c1a",
          "Gateway": "172.18.0.1",
          "IPAddress": "172.18.0.2",
          "MacAddress": "ba:37:16:c8:75:9f",
          "IPPrefixLen": 16,
          "IPv6Gateway": "",
          "GlobalIPv6Address": "",
          "GlobalIPv6PrefixLen": 0,
          "DNSNames": null
        }
      }
    },
    "Mounts": []
  },
  {
    "Id": "33e68e4d8db5bb7f536e22c29b2bb9e3886765e4c6800ff6a10cada466627df4",
    "Names": [
      "/apirest-netbox-postgres-1"
    ],
    "Image": "postgres:17-alpine",
    "ImageID": "sha256:b0f9560a2de083e2cc7382e75f808c7381a32852a7ec49117deedb300e552b24",
    "ImageManifestDescriptor": {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:aa90e97ee862e558111d34cfb8b2c4bec768c2b039fb791341686928560263b3",
      "size": 2866,
      "annotations": {
        "com.docker.official-images.bashbrew.arch": "amd64",
        "org.opencontainers.image.base.digest": "sha256:d56c381f961d307a21b3ca004cf1e3910f106644aefb1f43e654c8a56c4fd395",
        "org.opencontainers.image.base.name": "alpine:3.24",
        "org.opencontainers.image.created": "2026-09-17T21:29:04Z",
        "org.opencontainers.image.revision": "2603e26e245e558218728ee14e0a42dcb020dc7f",
        "org.opencontainers.image.source": "https://github.com/docker-library/postgres.git#2603e26e245e558218728ee14e0a42dcb020dc7f:17/alpine3.24",
        "org.opencontainers.image.url": "https://hub.docker.com/_/postgres",
        "org.opencontainers.image.version": "17.11-alpine3.24"
      },
      "platform": {
        "architecture": "amd64",
        "os": "linux"
      }
    },
    "Command": "docker-entrypoint.sh postgres",
    "Created": 1793003106,
    "Ports": [
      {
        "IP": "",
        "PrivatePort": 5432,
        "Type": "tcp"
      }
    ],
    "Labels": {
      "com.docker.compose.config-hash": "034ca12bc655c8784b5559e2f952532d50a6619918e0efb336f11d0327ffa68d",
      "com.docker.compose.container-number": "1",
      "com.docker.compose.depends_on": "",
      "com.docker.compose.image": "sha256:aa90e97ee862e558111d34cfb8b2c4bec768c2b039fb791341686928560263b3",
      "com.docker.compose.oneoff": "False",
      "com.docker.compose.project": "apirest",
      "com.docker.compose.project.config_files": "/home/debian/api-rest-m1-1/adminapi/docker-compose.yml",
      "com.docker.compose.project.working_dir": "/home/debian/api-rest-m1-1/adminapi",
      "com.docker.compose.service": "netbox-postgres",
      "com.docker.compose.version": "5.6.0"
    },
    "State": "running",
    "Status": "Up 22 minutes (healthy)",
    "HostConfig": {
      "NetworkMode": "apirest_default"
    },
    "Health": {
      "Status": "healthy",
      "FailingStreak": 0
    },
    "NetworkSettings": {
      "Networks": {
        "apirest_default": {
          "IPAMConfig": null,
          "Links": null,
          "Aliases": null,
          "DriverOpts": null,
          "GwPriority": 0,
          "NetworkID": "4cb231c1d4e508100bd3343db5a80a160e602643c2c756b21bc86fa80b62830c",
          "EndpointID": "8875c4087055ac8c2c7abae37882a5515b70af1e279ade7a7f5a94ea66bcbcea",
          "Gateway": "172.18.0.1",
          "IPAddress": "172.18.0.4",
          "MacAddress": "2e:8d:07:3d:df:b5",
          "IPPrefixLen": 16,
          "IPv6Gateway": "",
          "GlobalIPv6Address": "",
          "GlobalIPv6PrefixLen": 0,
          "DNSNames": null
        }
      }
    },
    "Mounts": [
      {
        "Type": "volume",
        "Name": "apirest_netbox-donnees",
        "Source": "/var/lib/docker/volumes/apirest_netbox-donnees/_data",
        "Destination": "/var/lib/postgresql/data",
        "Driver": "local",
        "Mode": "rw",
        "RW": true,
        "Propagation": ""
      }
    ]
  },
  {
    "Id": "79c739695edb7108658406a6e0bd6cfe5d48d09e9a96005dfcc57932af10d389",
    "Names": [
      "/apirest-docker-api-1"
    ],
    "Image": "tecnativa/docker-socket-proxy:v0.4.2",
    "ImageID": "sha256:1f3a6f303320723d199d2316a3e82b2e2685d86c275d5e3deeaf182573b47476",
    "ImageManifestDescriptor": {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:bd2241b3bec83abcff25927a0a7ae518e0c5bef624b3cc247dcb31e68b53f417",
      "size": 1993,
      "platform": {
        "architecture": "amd64",
        "os": "linux"
      }
    },
    "Command": "docker-entrypoint.sh haproxy -f /tmp/haproxy.cfg",
    "Created": 1793003106,
    "Ports": [
      {
        "IP": "127.0.0.1",
        "PrivatePort": 2375,
        "PublicPort": 2375,
        "Type": "tcp"
      }
    ],
    "Labels": {
      "com.docker.compose.config-hash": "e291b4253c3d8bd3ff1129679585745eecd32d48045d81afccc637ef41d4a605",
      "com.docker.compose.container-number": "1",
      "com.docker.compose.depends_on": "",
      "com.docker.compose.image": "sha256:bd2241b3bec83abcff25927a0a7ae518e0c5bef624b3cc247dcb31e68b53f417",
      "com.docker.compose.oneoff": "False",
      "com.docker.compose.project": "apirest",
      "com.docker.compose.project.config_files": "/home/debian/api-rest-m1-1/adminapi/docker-compose.yml",
      "com.docker.compose.project.working_dir": "/home/debian/api-rest-m1-1/adminapi",
      "com.docker.compose.service": "docker-api",
      "com.docker.compose.version": "5.6.0",
      "org.opencontainers.image.created": "2025-12-16T07:26:21.623Z",
      "org.opencontainers.image.description": "Proxy over your Docker socket to restrict which requests it accepts",
      "org.opencontainers.image.licenses": "Apache-2.0",
      "org.opencontainers.image.revision": "2f04313b042c1bf4dfbd039475dfc42db79bde7a",
      "org.opencontainers.image.source": "https://github.com/Tecnativa/docker-socket-proxy",
      "org.opencontainers.image.title": "docker-socket-proxy",
      "org.opencontainers.image.url": "https://github.com/Tecnativa/docker-socket-proxy",
      "org.opencontainers.image.version": "v0.4.2"
    },
    "State": "running",
    "Status": "Up 22 minutes",
    "HostConfig": {
      "NetworkMode": "apirest_default"
    },
    "Health": {
      "Status": "none",
      "FailingStreak": 0
    },
    "NetworkSettings": {
      "Networks": {
        "apirest_default": {
          "IPAMConfig": null,
          "Links": null,
          "Aliases": null,
          "DriverOpts": null,
          "GwPriority": 0,
          "NetworkID": "4cb231c1d4e508100bd3343db5a80a160e602643c2c756b21bc86fa80b62830c",
          "EndpointID": "7d6d07394511548838569af5e03fba64c1006e84aff461afeae4440f95c431e8",
          "Gateway": "172.18.0.1",
          "IPAddress": "172.18.0.3",
          "MacAddress": "a6:15:e0:02:0d:43",
          "IPPrefixLen": 16,
          "IPv6Gateway": "",
          "GlobalIPv6Address": "",
          "GlobalIPv6PrefixLen": 0,
          "DNSNames": null
        }
      }
    },
    "Mounts": [
      {
        "Type": "bind",
        "Source": "/var/run/docker.sock",
        "Destination": "/var/run/docker.sock",
        "Mode": "ro",
        "RW": false,
        "Propagation": "rprivate"
      }
    ]
  },
  {
    "Id": "2e0d66d74514018edf360db185e1ab6074cfbed85c12257f57c20140285dea92",
    "Names": [
      "/apirest-netbox-redis-1"
    ],
    "Image": "valkey/valkey:8-alpine",
    "ImageID": "sha256:081c2f5cb575efc901aa80ff9cdbd1ec6a301682fd35e1ebb4b0990a4a4a8507",
    "ImageManifestDescriptor": {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:32627109abf6f741121096b45c732f758876803efd7b2e1018ebc0350d117119",
      "size": 1616,
      "platform": {
        "architecture": "amd64",
        "os": "linux"
      }
    },
    "Command": "tini -- docker-entrypoint.sh valkey-server",
    "Created": 1793003106,
    "Ports": [
      {
        "IP": "",
        "PrivatePort": 6379,
        "Type": "tcp"
      }
    ],
    "Labels": {
      "com.docker.compose.config-hash": "910fda7eb6249f90cab1394d675ed118b6cb0b5a55bee466b73cf9a23fb8c8f5",
      "com.docker.compose.container-number": "1",
      "com.docker.compose.depends_on": "",
      "com.docker.compose.image": "sha256:32627109abf6f741121096b45c732f758876803efd7b2e1018ebc0350d117119",
      "com.docker.compose.oneoff": "False",
      "com.docker.compose.project": "apirest",
      "com.docker.compose.project.config_files": "/home/debian/api-rest-m1-1/adminapi/docker-compose.yml",
      "com.docker.compose.project.working_dir": "/home/debian/api-rest-m1-1/adminapi",
      "com.docker.compose.service": "netbox-redis",
      "com.docker.compose.version": "5.6.0",
      "org.opencontainers.image.source": "https://github.com/valkey-io/valkey"
    },
    "State": "running",
    "Status": "Up 22 minutes",
    "HostConfig": {
      "NetworkMode": "apirest_default"
    },
    "Health": {
      "Status": "none",
      "FailingStreak": 0
    },
    "NetworkSettings": {
      "Networks": {
        "apirest_default": {
          "IPAMConfig": null,
          "Links": null,
          "Aliases": null,
          "DriverOpts": null,
          "GwPriority": 0,
          "NetworkID": "4cb231c1d4e508100bd3343db5a80a160e602643c2c756b21bc86fa80b62830c",
          "EndpointID": "9a76d99b0d6ec0897548281ae89dd6cea3ce1df1e040b202d64d550d4aee9892",
          "Gateway": "172.18.0.1",
          "IPAddress": "172.18.0.5",
          "MacAddress": "0e:27:c1:4a:58:8a",
          "IPPrefixLen": 16,
          "IPv6Gateway": "",
          "GlobalIPv6Address": "",
          "GlobalIPv6PrefixLen": 0,
          "DNSNames": null
        }
      }
    },
    "Mounts": []
  }
]
debian@debian1 ~/a/adminapi (main)> curl -s --get http://127.0.0.1:2375/containers/json --data-urlencode 'all=true' \
                                             --data-urlencode 'filters={"label":["adminapi.managed=true"]}' | jq
[]
debian@debian1 ~/a/adminapi (main)> curl -s http://127.0.0.1:2375/containers/web1/json | jq

{
  "message": "No such container: web1"
}
```

```bash
debian@debian1 ~/a/adminapi (main)> curl -i -X POST http://127.0.0.1:2375/containers/web1/stop

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    38  100    38    0     0   1773      0 --:--:-- --:--:-- --:--:--  1727

debian@debian1 ~/a/adminapi (main) [0|5]> curl -i -X POST http://127.0.0.1:2375/containers/web1/start
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    38  100    38    0     0  13858      0 --:--:-- --:--:-- --:--:-- 19000
```

# 2

```bash
debian@debian1 ~/a/adminapi (main)> curl -s -X POST http://127.0.0.1:8080/api/users/tokens/provision/ \
                                             -H "Content-Type: application/json" -H "Accept: application/json" \
                                             -d '{"username": "admin", "password": "admin"}' | jq
{
  "id": 3,
  "url": "http://127.0.0.1:8080/api/users/tokens/3/",
  "display_url": "http://127.0.0.1:8080/users/tokens/3/",
  "display": "95webGxTcW1f",
  "version": 2,
  "user": {
    "id": 1,
    "url": "http://127.0.0.1:8080/api/users/users/1/",
    "display": "admin",
    "username": "admin"
  },
  "key": "95webGxTcW1f",
  "created": "2026-10-26T09:27:46.053980Z",
  "expires": null,
  "last_used": null,
  "enabled": true,
  "write_enabled": true,
  "description": "",
  "allowed_ips": [],
  "token": "oE6VEAU74u9DRnxamRN8Rljl6CzepNjSrCvY5ScZ"
}
```

```bash
debian@debian1 ~/a/adminapi (main)> cat .env | grep -i "nbt"
# Token NetBox, obtenu au TP1. Forme : nbt_<clé>.<token>
NETBOX_TOKEN=nbt_3XkLUCJ2gaXZ.3L4cNbNTwdzv38GJA8lswV2CStZDZ0iy2QuTUfvU
```

```bash
debian@debian1 ~/a/adminapi (main)> curl -s -X POST http://127.0.0.1:8080/api/virtualization/cluster-types/ -H "Authorization
: Bearer nbt_3XkLUCJ2gaXZ.3L4cNbNTwdzv38GJA8lswV2CStZDZ0iy2QuTUfvU" \
                                             -H "Content-Type: application/json" -H "Accept: application/json" \
                                             -d '{"name": "Docker", "slug": "docker"}' | jq
{
  "name": [
    "cluster type with this name already exists."
  ],
  "slug": [
    "cluster type with this slug already exists."
  ]
}
```

```bash
debian@debian1 ~/a/adminapi (main)> curl -s -X POST http://127.0.0.1:8080/api//virtualization/clusters/ -H "Authorization: Be
arer nbt_3XkLUCJ2gaXZ.3L4cNbNTwdzv38GJA8lswV2CStZDZ0iy2QuTUfvU" \
                                             -H "Content-Type: application/json" -H "Accept: application/json" \
                                             -d '{"name": "docker-local", "type": 1}'







<!DOCTYPE html>
<html
  lang="en"
  data-netbox-url-name=""
  data-netbox-version="4.7.3-Docker-5.1.1"
  
  >
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1, maximum-scale=5, width=device-width, viewport-fit=cover" />
    <meta name="htmx-config" content='{"scrollBehavior": "auto"}'>
    <meta name="hostname" content="cd599e4ea199" />

    
    <title>Page Not Found | NetBox</title>

    
    <script
      type="text/javascript"
      src="/static/setmode.js?v=4.7.3"
      onerror="window.location='/media-failure/?filename=setmode.js'">
    </script>
    <script type="text/javascript">
      (function () {
        initMode()
      })();
      window.CSRF_TOKEN = "aoeddOx1hbOkkpmU4JW0UemsRfPJbZQnb4QX0NG8ZpVXggnRn8044yTcml1Jx5gO";
    </script>

    
    <link
      rel="stylesheet"
      href="/static/netbox-external.css?v=4.7.3"
      onerror="window.location='/media-failure/?filename=netbox-external.css'"
    />
    <link
      rel="stylesheet"
      href="/static/netbox.css?v=4.7.3"
      onerror="window.location='/media-failure/?filename=netbox.css'"
    />
    <link rel="icon" type="image/png" href="/static/netbox.ico" />
    <link rel="apple-touch-icon" type="image/png" href="/static/netbox_touch-icon-180.png" />

    
    <script
      type="text/javascript"
      src="/static/netbox.js?v=4.7.3"
      onerror="window.location='/media-failure/?filename=netbox.js'">
    </script>
    

    
    
    

  </head>
  <body>

    
    

  <div class="page">

    
    <aside class="navbar navbar-vertical navbar-expand-lg d-print-none">

      

      <div class="container-fluid">

        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#sidebar-menu" aria-controls="sidebar-menu" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        
        <h1 class="navbar-brand pb-0">
          <a href="/">
            <img src="/static/logo_netbox_dark_teal.svg" alt="NetBox Logo" class="navbar-brand-image hide-theme-dark">
            <img src="/static/logo_netbox_bright_teal.svg" alt="NetBox Logo" class="navbar-brand-image hide-theme-light">
            <div class="netbox-edition fw-semibold text-center fs-5 my-1">Community</div>
          </a>
        </h1>

        
        <div class="navbar-nav flex-row align-items-center d-lg-none">
          
          

<div class="d-flex ms-2">
  <button type="button" class="nav-link color-mode-toggle hide-theme-dark fs-2 p-0 text-secondary" title="Enable dark mode" aria-label="Enable dark mode" data-bs-toggle="tooltip" data-bs-placement="bottom">
    <i class="mdi mdi-lightbulb" aria-hidden="true"></i>
  </button>
  <button type="button" class="nav-link color-mode-toggle hide-theme-light fs-2 p-0 text-secondary" title="Enable light mode" aria-label="Enable light mode" data-bs-toggle="tooltip" data-bs-placement="bottom">
    <i class="mdi mdi-lightbulb-on" aria-hidden="true"></i>
  </button>
</div>

          





  <div class="btn-group align-items-center ps-2">
    <a class="btn btn-primary" type="button" href="/login/?next=/api//virtualization/clusters/">
      <i class="mdi mdi-login-variant" aria-hidden="true"></i> Log In
    </a>
  </div>


        </div>

        
        <div class="collapse navbar-collapse" id="sidebar-menu">
          



<ul class="navbar-nav pt-lg-2">
  <li class="nav-item d-block d-lg-none">
    <form action="/search/" method="get" autocomplete="off" novalidate>
      <div class="input-group mb-1 mt-2">
        <div class="input-group-prepend">
          <span class="input-group-text">
            <i class="mdi mdi-magnify" aria-hidden="true"></i>
          </span>
        </div>
        <input type="text" name="q" value="" class="form-control" placeholder="Search…" aria-label="Search NetBox">
        <div class="input-group-append">
          <button type="submit" class="form-control">Search</button>
        </div>
      </div>
    </form>
  </li>
  
</ul>


          
          <div class="text-muted text-center fs-5 my-3 px-3">
            NetBox Community v4.7.3-Docker-5.1.1
            
              <div>
                <a href="https://netboxlabs.com/netbox-cloud/" class="text-muted">Get Cloud</a> |
                <a href="https://netboxlabs.com/netbox-enterprise/" class="text-muted">Get Enterprise</a>
              </div>
            
          </div>

        </div>
      </div>
    </aside>

    
    <header class="navbar navbar-expand-md sticky-top d-none d-lg-flex d-print-none">
      <div class="container-fluid">

        
        <div class="navbar-nav flex-row align-items-center order-md-last">
          
          

<div class="d-flex ms-2">
  <button type="button" class="nav-link color-mode-toggle hide-theme-dark fs-2 p-0 text-secondary" title="Enable dark mode" aria-label="Enable dark mode" data-bs-toggle="tooltip" data-bs-placement="bottom">
    <i class="mdi mdi-lightbulb" aria-hidden="true"></i>
  </button>
  <button type="button" class="nav-link color-mode-toggle hide-theme-light fs-2 p-0 text-secondary" title="Enable light mode" aria-label="Enable light mode" data-bs-toggle="tooltip" data-bs-placement="bottom">
    <i class="mdi mdi-lightbulb-on" aria-hidden="true"></i>
  </button>
</div>

          





  <div class="btn-group align-items-center ps-2">
    <a class="btn btn-primary" type="button" href="/login/?next=/api//virtualization/clusters/">
      <i class="mdi mdi-login-variant" aria-hidden="true"></i> Log In
    </a>
  </div>


        </div>

        
        <div class="collapse navbar-collapse" id="navbar-menu">
          <form action="/search/" method="get" autocomplete="off" novalidate>
            <div class="input-icon">
              <span class="input-icon-addon">
                <i class="mdi mdi-magnify"></i>
              </span>
              <input type="text" name="q" value="" class="form-control" placeholder="Search…" aria-label="Search NetBox">
            </div>
          </form>
        </div>

      </div>
    </header>

    
    <div class="page-wrapper">
      <div id="page-content">

      
      

        
        
        

        
        

        
        

      
      

      
      
        <div class="page-body my-1">
          <div class="container-fluid tab-content py-3">

            
            
            

            
            
<div class="row my-5">
    <div class="col-6 offset-3">
        <div class="card">
            <h2 class="card-header text-danger">
                /api//virtualization/clusters/
            </h2>
            <div class="card-body">
                
    The requested page does not exist.

            </div>
            <div class="card-footer text-end">
                <a href="/" class="btn btn-primary">Home Page</a>
            </div>
        </div>
    </div>
</div>

            

          </div>
        </div>
      
      

      
      
      

      
      

      </div>

      
      <footer class="footer footer-transparent d-print-none py-2">
        <div class="container-fluid d-flex justify-content-between align-items-center">
          

            
            <ul class="list-inline mb-0 fs-2">
              
                
                <li class="list-inline-item">
                  <a href="/static/docs/" target="_blank" class="link-secondary" rel="noopener" aria-label="Docs">
                    <i title="Docs" class="mdi mdi-book-open-variant text-primary" data-bs-placement="top" data-bs-toggle="tooltip"></i>
                  </a>
                </li>
                
                <li class="list-inline-item">
                  <a href="/api/" target="_blank" class="link-secondary" rel="noopener" aria-label="REST API">
                    <i title="REST API" class="mdi mdi-cloud-braces text-primary" data-bs-placement="top" data-bs-toggle="tooltip"></i>
                  </a>
                </li>
                
                <li class="list-inline-item">
                  <a href="/api/schema/swagger-ui/" target="_blank" class="link-secondary" rel="noopener" aria-label="REST API documentation">
                    <i title="REST API documentation" class="mdi mdi-book text-primary" data-bs-placement="top" data-bs-toggle="tooltip"></i>
                  </a>
                </li>
                
                

                
                
                  
                  <li class="list-inline-item">
                    <a href="https://github.com/netbox-community/netbox" target="_blank" class="link-secondary" rel="noopener" aria-label="Source Code">
                      <i title="Source Code" class="mdi mdi-github text-primary" data-bs-placement="top" data-bs-toggle="tooltip"></i>
                    </a>
                  </li>
                  
                  <li class="list-inline-item">
                    <a href="https://netdev.chat" target="_blank" class="link-secondary" rel="noopener" aria-label="Community">
                      <i title="Community" class="mdi mdi-slack text-primary" data-bs-placement="top" data-bs-toggle="tooltip"></i>
                    </a>
                  </li>
                
              
            </ul>
            

            
            <ul class="list-inline list-inline-dots fs-5 mb-0" id="footer-stamp" hx-swap-oob="true">
              <li class="list-inline-item">2026-10-26 09:45:35 UTC</li>
              <li class="list-inline-item">cd599e4ea199</li>
            </ul>
            

          
        </div>
      </footer>
      

    
    </div>

  </div>


    
    
    

    
    

<div id="django-messages" class="toast-container position-fixed bottom-0 end-0 p-3" hx-swap-oob="true">

  
  

  
  

</div>


  </body>
</html>
debian@debian1 ~/a/adminapi (main)> curl -s -X POST http://127.0.0.1:8080/api//virtualization/clusters/ -H "Authorization: Be
arer nbt_3XkLUCJ2gaXZ.3L4cNbNTwdzv38GJA8lswV2CStZDZ0iy2QuTUfvU" \
                                             -H "Content-Type: application/json" -H "Accept: application/json" \
                                             -d '{"name": "docker-local", "type": 1}' | jq
jq: parse error: Invalid numeric literal at line 8, column 10
debian@debian1 ~/a/adminapi (main) [0|5]> curl -s -X POST http://127.0.0.1:8080/api/virtualization/clusters/ -H "Authorizatio
n: Bearer nbt_3XkLUCJ2gaXZ.3L4cNbNTwdzv38GJA8lswV2CStZDZ0iy2QuTUfvU" \
                                                   -H "Content-Type: application/json" -H "Accept: application/json" \
                                                   -d '{"name": "docker-local", "type": 1}' | jq
{
  "id": 1,
  "url": "http://127.0.0.1:8080/api/virtualization/clusters/1/",
  "display_url": "http://127.0.0.1:8080/virtualization/clusters/1/",
  "display": "docker-local",
  "name": "docker-local",
  "type": {
    "id": 1,
    "url": "http://127.0.0.1:8080/api/virtualization/cluster-types/1/",
    "display": "Docker",
    "name": "Docker",
    "slug": "docker",
    "description": ""
  },
  "group": null,
  "status": {
    "value": "active",
    "label": "Active"
  },
  "tenant": null,
  "scope_type": null,
  "scope_id": null,
  "scope": null,
  "description": "",
  "owner": null,
  "comments": "",
  "tags": [],
  "custom_fields": {},
  "created": "2026-10-26T09:46:01.726180Z",
  "last_updated": "2026-10-26T09:46:01.726201Z",
  "device_count": 0,
  "virtualmachine_count": 0,
  "allocated_vcpus": null,
  "allocated_memory": null,
  "allocated_disk": null
}
```

# 3

```bash
debian@debian1 ~/a/adminapi (main)> git add .
debian@debian1 ~/a/adminapi (main)> git commit -m "notes 1"
[main 0e2216c] notes 1
 1 file changed, 922 insertions(+)
 create mode 100644 adminapi/notes.md
debian@debian1 ~/a/adminapi (main)> git status
Sur la branche main
Votre branche est en avance sur 'origin/main' de 3 commits.
  (utilisez "git push" pour publier vos commits locaux)

rien à valider, la copie de travail est propre
debian@debian1 ~/a/adminapi (main)> git remote -v
origin  git@github.com:Shanskyn/api-rest-m1-1.git (fetch)
origin  git@github.com:Shanskyn/api-rest-m1-1.git (push)
```

# 4

```bash
debian@debian1 ~/api-rest-m1-1 (main)> docker run -d --name web1 --label admi
napi.managed=true nginx:alpine
6587593e7474143f0101456374d395937e95c3d241fc4fe7d0487fcdec558f0b
debian@debian1 ~/api-rest-m1-1 (main)> docker run -d --name intrus nginx:alpi
ne
80dac4f0addf555c5c433bafaa3557748ecf12911948fa466f06f64483b7fe39

debian@debian1 ~/api-rest-m1-1 (main)> curl -s http://127.0.0.1:2375/containe
rs/web1/json | jq

{
  "Id": "6587593e7474143f0101456374d395937e95c3d241fc4fe7d0487fcdec558f0b",
  "Created": "2026-10-26T09:55:03.66017326Z",
  "Path": "/docker-entrypoint.sh",
  "Args": [
    "nginx",
    "-g",
    "daemon off;"
  ],
  "State": {
    "Status": "running",
    "Running": true,
    "Paused": false,
    "Restarting": false,
    "OOMKilled": false,
    "Dead": false,
    "Pid": 3513,
    "ExitCode": 0,
    "Error": "",
    "StartedAt": "2026-10-26T09:55:03.743810308Z",
    "FinishedAt": "0001-01-01T00:00:00Z"
  },
  "Image": "sha256:df221db836e1754089190208cee7eeda94f233197056426eda74a43ab1abeac2",
  "ResolvConfPath": "/var/lib/docker/containers/6587593e7474143f0101456374d395937e95c3d241fc4fe7d0487fcdec558f0b/resolv.conf",
  "HostnamePath": "/var/lib/docker/containers/6587593e7474143f0101456374d395937e95c3d241fc4fe7d0487fcdec558f0b/hostname",
  "HostsPath": "/var/lib/docker/containers/6587593e7474143f0101456374d395937e95c3d241fc4fe7d0487fcdec558f0b/hosts",
  "LogPath": "/var/lib/docker/containers/6587593e7474143f0101456374d395937e95c3d241fc4fe7d0487fcdec558f0b/6587593e7474143f0101456374d395937e95c3d241fc4fe7d0487fcdec558f0b-json.log",
  "Name": "/web1",
  "RestartCount": 0,
  "Driver": "overlayfs",
  "Platform": "linux",
  "MountLabel": "",
  "ProcessLabel": "",
  "AppArmorProfile": "docker-default",
  "ExecIDs": null,
  "HostConfig": {
    "Binds": null,
    "ContainerIDFile": "",
    "LogConfig": {
      "Type": "json-file",
      "Config": {}
    },
    "NetworkMode": "bridge",
    "PortBindings": {},
    "RestartPolicy": {
      "Name": "no",
      "MaximumRetryCount": 0
    },
    "AutoRemove": false,
    "VolumeDriver": "",
    "VolumesFrom": null,
    "ConsoleSize": [
      26,
      77
    ],
    "CapAdd": null,
    "CapDrop": null,
    "CgroupnsMode": "private",
    "Dns": null,
    "DnsOptions": [],
    "DnsSearch": [],
    "ExtraHosts": null,
    "GroupAdd": null,
    "IpcMode": "private",
    "Cgroup": "",
    "Links": null,
    "OomScoreAdj": 0,
    "PidMode": "",
    "Privileged": false,
    "PublishAllPorts": false,
    "ReadonlyRootfs": false,
    "SecurityOpt": null,
    "UTSMode": "",
    "UsernsMode": "",
    "ShmSize": 67108864,
    "Runtime": "runc",
    "Isolation": "",
    "CpuShares": 0,
    "Memory": 0,
    "NanoCpus": 0,
    "CgroupParent": "",
    "BlkioWeight": 0,
    "BlkioWeightDevice": [],
    "BlkioDeviceReadBps": [],
    "BlkioDeviceWriteBps": [],
    "BlkioDeviceReadIOps": [],
    "BlkioDeviceWriteIOps": [],
    "CpuPeriod": 0,
    "CpuQuota": 0,
    "CpuRealtimePeriod": 0,
    "CpuRealtimeRuntime": 0,
    "CpusetCpus": "",
    "CpusetMems": "",
    "Devices": [],
    "DeviceCgroupRules": null,
    "DeviceRequests": null,
    "MemoryReservation": 0,
    "MemorySwap": 0,
    "MemorySwappiness": null,
    "OomKillDisable": null,
    "PidsLimit": null,
    "Ulimits": null,
    "CpuCount": 0,
    "CpuPercent": 0,
    "IOMaximumIOps": 0,
    "IOMaximumBandwidth": 0,
    "MaskedPaths": [
      "/proc/acpi",
      "/proc/asound",
      "/proc/interrupts",
      "/proc/kcore",
      "/proc/keys",
      "/proc/latency_stats",
      "/proc/sched_debug",
      "/proc/scsi",
      "/proc/timer_list",
      "/proc/timer_stats",
      "/sys/devices/virtual/powercap",
      "/sys/firmware"
    ],
    "ReadonlyPaths": [
      "/proc/bus",
      "/proc/fs",
      "/proc/irq",
      "/proc/sys",
      "/proc/sysrq-trigger"
    ]
  },
  "Storage": {
    "RootFS": {
      "Snapshot": {
        "Name": "overlayfs"
      }
    }
  },
  "Mounts": [],
  "Config": {
    "Hostname": "6587593e7474",
    "Domainname": "",
    "User": "",
    "AttachStdin": false,
    "AttachStdout": false,
    "AttachStderr": false,
    "ExposedPorts": {
      "80/tcp": {}
    },
    "Tty": false,
    "OpenStdin": false,
    "StdinOnce": false,
    "Env": [
      "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
      "NGINX_VERSION=1.31.6",
      "PKG_RELEASE=1",
      "DYNPKG_RELEASE=1",
      "NJS_VERSION=1.0.1",
      "NJS_RELEASE=1",
      "ACME_VERSION=0.4.1"
    ],
    "Cmd": [
      "nginx",
      "-g",
      "daemon off;"
    ],
    "Image": "nginx:alpine",
    "Volumes": null,
    "WorkingDir": "/",
    "Entrypoint": [
      "/docker-entrypoint.sh"
    ],
    "Labels": {
      "adminapi.managed": "true",
      "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
    },
    "StopSignal": "SIGQUIT"
  },
  "NetworkSettings": {
    "SandboxID": "9f8d26e21189cf8142f01d84db32440da7be92d8f7e9d6270c9c77cc914df371",
    "SandboxKey": "/var/run/docker/netns/9f8d26e21189",
    "Ports": {
      "80/tcp": null
    },
    "Networks": {
      "bridge": {
        "IPAMConfig": null,
        "Links": null,
        "Aliases": null,
        "DriverOpts": null,
        "GwPriority": 0,
        "NetworkID": "5db6df3bb1ca53b8e8e309523e950da6011f91fc298f4f0704bee643a8f6ea7a",
        "EndpointID": "7511b823b46d9e94fd3c5806aa253935a1dc8fdd749cd9daeb9515371db9e7cb",
        "Gateway": "172.17.0.1",
        "IPAddress": "172.17.0.2",
        "MacAddress": "3a:89:3f:be:7a:2c",
        "IPPrefixLen": 16,
        "IPv6Gateway": "",
        "GlobalIPv6Address": "",
        "GlobalIPv6PrefixLen": 0,
        "DNSNames": null
      }
    }
  },
  "ImageManifestDescriptor": {
    "mediaType": "application/vnd.oci.image.manifest.v1+json",
    "digest": "sha256:0530961ff0592b58c10f767535cc0abdfccf9e389ff7cc90f87320c1bc7e8506",
    "size": 2495,
    "annotations": {
      "com.docker.official-images.bashbrew.arch": "amd64",
      "org.opencontainers.image.base.digest": "sha256:9b58c1e8e776c8f79fca3e56d969b9ee1474ddfcf70d50a617dc85e9882a7bdb",
      "org.opencontainers.image.base.name": "nginx:1.31.6-alpine-slim",
      "org.opencontainers.image.created": "2026-09-22T22:09:49Z",
      "org.opencontainers.image.revision": "a16f1329e13e7273c4103f75d863ca625b75109e",
      "org.opencontainers.image.source": "https://github.com/nginx/docker-nginx.git#a16f1329e13e7273c4103f75d863ca625b75109e:mainline/alpine",
      "org.opencontainers.image.url": "https://hub.docker.com/_/nginx",
      "org.opencontainers.image.version": "1.31.6-alpine"
    },
    "platform": {
      "architecture": "amd64",
      "os": "linux"
    }
  }
}
debian@debian1 ~/api-rest-m1-1 (main)> curl -i -X POST http://127.0.0.1:2375/
containers/web1/stop |jq

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--       0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--       0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
jq: parse error: Invalid numeric literal at line 1, column 9
debian@debian1 ~/api-rest-m1-1 (main) [0|5]> curl -i -X POST http://127.0.0.1
:2375/containers/web1/start | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--       0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
jq: parse error: Invalid numeric literal at line 1, column 9
```