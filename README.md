# ForgeAI Monorepo (Turborepo MVP)

A production-ready MVP monorepo for a high-converting marketing content generator wrapper.

## Stack
- Monorepo: Turborepo + pnpm
- Web: Next.js 14 App Router, TypeScript, TailwindCSS, Framer Motion, React Hook Form + Zod, shared `@forgeai/ui`
- API: FastAPI, SQLModel, Alembic
- DB: PostgreSQL
- Auth: JWT access + refresh with bcrypt password hashing
- Infra: Docker Compose (dev-first)

## Quick start
```bash
pnpm install
cp .env.example .env
pnpm dev
```

This starts Postgres and runs `web` + `api` in parallel.

## Migrations
```bash
cd apps/api
alembic upgrade head
```

## Seed demo data
```bash
cd apps/api
python -m app.seed
```
Demo login: `demo@forgeai.dev` / `password123`

## API provider switching
Set in `.env`:
- `AI_PROVIDER=mock` (default deterministic local output)
- `AI_PROVIDER=openai` (fallbacks to mock if missing key/errors)
- `AI_PROVIDER=anthropic` (fallbacks to mock if missing key/errors)

## Docker only
```bash
docker compose -f infra/docker/docker-compose.yml up --build
```

## Repo structure
- `apps/web`: frontend routes and auth guard middleware
- `apps/api`: backend routers, auth, models, ai providers
- `packages/ui`: reusable components and app shell layout
- `packages/config`: shared tailwind and tsconfig presets
- `packages/types`: shared frontend type contracts
- `infra/docker`: Dockerfiles and Compose
