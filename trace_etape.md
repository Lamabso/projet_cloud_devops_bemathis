# Trace - Étape 1 (Architecture & Repo)

## Binôme
- Benjamin E
- Mathis A

## Stratégie Git
- Trunk-based (branche principale: main)
- Branches courtes: feat/*, test/*, ci/*

## Environnement local
- OS:
- git version:
- python version:
- éditeur:



# Étape 2 - Flask local (lecture fichiers + cache TTL + UI)

## Objectif
- Lire JSON/YAML localement (simulation Blob)
- Endpoints API conformes + cache TTL + UI minimale

## Environnement
- Windows 11
- PowerShell

# Trace - Étape 3 (Tests Flask)

## Objectif
- Couvrir health checks + endpoints API (events/news/faq)
- Tests rapides, reproductibles, sans dépendance Azure

## Outil
- pytest (+ éventuellement pytest-cov)

## Résultats attendus
- Tous les tests passent en local et plus tard en CI

# Trace - Étape 4 (Docker)

## Objectif
- Dockerfile optimisé (slim, non-root)
- Conteneur stateless
- Test local obligatoire

## Environnement
- Windows 11
- Docker Desktop
- docker version:

# Trace - Étape 5 (CI GitHub Actions sans AKS)

## Objectif
- Lint + tests + build docker + push GHCR à chaque push sur main
- Pas de déploiement AKS à cette étape

## Points clés
- Authent GHCR via GITHUB_TOKEN (pas de secret à créer)
- Tags image: latest + sha

## Résultats attendus
- Workflow vert sur GitHub
- Image visible dans GHCR (Packages)

# Trace - Étape 6 (AKS)

## Objectif
- Déployer l'app Flask sur AKS via manifests Kubernetes
- Ingress NGINX, Service, Deployment, ConfigMap, Secret, probes, requests/limits

## Environnement
- Azure for Students
- Région:
- Resource Group:
- AKS cluster:

# Trace - Étape 7 (Monitoring & Sécurité)

## Objectif
- Monitoring basique AKS (CPU/Mem, disponibilité)
- Logs applicatifs INFO
- 1 alerte simple (5xx)
- Sécurité: secrets hors Git + non-root + accès Blob via Secret (minimum)

## État initial
- App OK via Ingress (IP: 20.50.164.3)