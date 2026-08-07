# testing-repo

Minimal FastAPI app with a `/health` route. The API prefix is configured via the
`API_PREFIX` environment variable (see `.env`, default `/api`).

## Run locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/uvicorn app.main:app --reload
```

Then hit `http://127.0.0.1:8000/api/health` (or whatever prefix `API_PREFIX` is set to).

## Run with Docker

```bash
docker build -t testing-repo .
docker run -p 8999:8999 -e API_PREFIX=/api testing-repo
```
