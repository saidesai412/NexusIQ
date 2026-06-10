# NexusIQ – AI Decision Intelligence Platform

Enterprise-grade AI-powered business intelligence platform that analyzes data, predicts outcomes, detects risks, and generates strategic recommendations.

---

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend       │    │   Backend        │    │   AI Service     │
│   React.js       │◄──►│   Node.js/Express│◄──►│   Python FastAPI │
│   Tailwind CSS   │    │   JWT Auth       │    │   Prophet/XGBoost│
│   Redux Toolkit  │    │   RBAC           │    │   LangChain/RAG  │
│   Recharts       │    │   Socket.IO      │    │   Multi-Agents   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                      │                       │
         │              ┌───────┴──────┐                │
         │              │  Databases   │                 │
         │              │  PostgreSQL  │                 │
         │              │  MongoDB     │                 │
         └──────────────│  ChromaDB    │─────────────────┘
                        └─────────────┘
```

## Features

| Module | Description |
|--------|-------------|
| **Auth** | JWT, RBAC (Admin/Manager/Analyst), password reset |
| **Documents** | Upload PDF/Excel/CSV, S3 storage, auto-processing |
| **RAG Chat** | LangChain + ChromaDB semantic search + GPT-4 answers |
| **Revenue Forecast** | Prophet, XGBoost, LSTM models |
| **Churn Prediction** | Customer risk scoring + retention recommendations |
| **Demand Forecast** | Product demand + inventory optimization |
| **Risk Detection** | Revenue/Fraud/Churn/Market risk engine |
| **AI Agents** | 4-agent workflow: Analyst, Researcher, Risk, Strategy |
| **Reports** | Auto-generated PDF business intelligence reports |
| **Dashboard** | Real-time KPIs, charts, notifications |

---

## Quick Start

### Prerequisites
- Node.js 20+
- Python 3.11+
- PostgreSQL 16+
- MongoDB 7+
- Docker & Docker Compose (optional)

### 1. Clone & Setup Environment

```bash
# Backend
cd backend
cp .env.example .env
# Edit .env with your credentials
npm install
npm run dev

# AI Service
cd ai-service
cp .env.example .env
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

### 2. Docker Compose (Recommended)

```bash
docker-compose up --build
```

Access:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- AI Service: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## API Endpoints

| Service | Endpoint | Description |
|---------|----------|-------------|
| Backend | `POST /api/auth/signup` | User registration |
| Backend | `POST /api/auth/login` | Authentication |
| Backend | `POST /api/documents/upload` | Upload documents |
| Backend | `POST /api/forecast/revenue` | Revenue forecasting |
| Backend | `POST /api/churn/predict` | Churn prediction |
| Backend | `POST /api/demand/forecast` | Demand forecasting |
| Backend | `POST /api/risk/detect` | Risk detection |
| Backend | `POST /api/rag/query` | RAG chat query |
| Backend | `POST /api/agents/run` | Run AI agents |
| Backend | `POST /api/reports/generate` | Generate report |
| Backend | `GET /api/dashboard/kpis` | Dashboard KPIs |

---

## Environment Variables

### Backend (.env)
```env
PORT=5000
PG_HOST=localhost
PG_DATABASE=nexusiq
PG_USER=postgres
PG_PASSWORD=yourpassword
MONGO_URI=mongodb://localhost:27017/nexusiq
JWT_SECRET=your_jwt_secret
AWS_S3_BUCKET=nexusiq-documents
AI_SERVICE_URL=http://localhost:8000
```

### AI Service (.env)
```env
OPENAI_API_KEY=your_openai_key
MONGO_URI=mongodb://localhost:27017/nexusiq
CHROMA_PERSIST_DIR=./chroma_db
```

---

## Deployment (Kubernetes)

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/
```

---

## Tech Stack

**Frontend:** React 18, Vite, Tailwind CSS, Redux Toolkit, TanStack Query, Recharts, Socket.IO Client

**Backend:** Node.js, Express, JWT, PostgreSQL (pg), MongoDB (Mongoose), Socket.IO, AWS S3, PDFKit

**AI Service:** Python 3.11, FastAPI, Prophet, XGBoost, LangChain, ChromaDB, OpenAI GPT-4

**Infrastructure:** Docker, Kubernetes, AWS S3, PostgreSQL, MongoDB

---

## License

MIT © NexusIQ
