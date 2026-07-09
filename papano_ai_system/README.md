# papano_ai_system (Professional multi-agent skeleton)

Projet: PAPANO AI — Architecture multi-agents orchestrée (CEO Orchestrator + Agents).

But
- Fournir une base professionnelle, sécurisée et extensible pour un système multi-agents.
- Intégrations prévues : LangGraph (stubs), OpenAI, ChromaDB, Postgres, Redis.
- API : FastAPI, exécution orchestrée via `CEOAgent`.

Sécurité
- Ne commitez jamais de clés dans le repo.
- Utilisez GitHub Secrets (OPENAI_API_KEY, CHROMA_API_KEY, DATABASE_URL, REDIS_URL).
- Fichiers fournis : `.env.template` à remplir localement.

Structure
- orchestrator/: CEO orchestration
- agents/: agents métiers (marketing, ecommerce, finance, ai, realestate, legal)
- memory/: templates de mémoire (user_profile, company_context)
- prompts/: prompts par agent
- tools/: adaptateurs API (stubs sécurisés)
- main.py: FastAPI app pour exécuter l'orchestrateur
- .github/workflows/ci.yml: tests + lint

Démarrage local
1. Copier `.env.template` en `.env` et remplir les valeurs.
2. python -m venv .venv && source .venv/bin/activate
3. pip install -r requirements.txt
4. uvicorn main:app --reload

Déploiement Docker (exemple)
- docker build -t papano_ai_system .
- docker run -e OPENAI_API_KEY=... -p 8000:8000 papano_ai_system

CI / qualité
- Black, isort, flake8 + pytest sont inclus dans requirements.
- Workflow GitHub Actions déjà fourni.

Licence
- MIT (fichier LICENSE).

Contact
- Papanopato
