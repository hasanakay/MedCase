# MedCase Agent — Google Cloud Run Deployment Guide

This guide describes how to deploy the MedCase Agent application (FastAPI backend + Next.js frontend) to **Google Cloud Run**, which is the recommended deployment strategy for the Google for Startups AI Agents Challenge.

---

## Prerequisites

1. A [Google Cloud Console](https://console.cloud.google.com/) account with an active billing project.
2. [Google Cloud SDK (gcloud CLI)](https://cloud.google.com/sdk/docs/install) installed locally.
3. Docker installed (optional, since we use Cloud Build to build remote container images).
4. A Google Gemini API Key (get one from [Google AI Studio](https://aistudio.google.com/)).

---

## Step 1: Configure gcloud CLI

Log in and set your Google Cloud project:

```bash
# Log in to Google Cloud
gcloud auth login

# Set your active project ID
gcloud config set project YOUR_PROJECT_ID

# Enable the necessary Google Cloud APIs
gcloud services enable run.googleapis.com \
                       containerregistry.googleapis.com \
                       cloudbuild.googleapis.com
```

---

## Step 2: Deploy the FastAPI Backend

We will build the container using **Cloud Build** and deploy it to **Cloud Run**.

1. Navigate to the `backend/` directory.
2. Ensure you have a `.gcloudignore` file to exclude `venv/` and `medcase.db` from being uploaded.
3. Verify that `Dockerfile` uses dynamic port binding: `CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]`
4. Run the build and deploy commands:

```bash
# Build the container image using Cloud Build
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/medcase-backend

# Deploy the image to Google Cloud Run
gcloud run deploy medcase-backend \
    --image gcr.io/YOUR_PROJECT_ID/medcase-backend \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars="GEMINI_API_KEY=your_gemini_api_key_here"
```

Once deployment completes, note down the **Service URL** outputted by the CLI (e.g., `https://medcase-backend-xxxxx-uc.a.run.app`). This will be your `NEXT_PUBLIC_API_URL` for the frontend.

---

## Step 3: Deploy the Next.js Frontend

1. Navigate to the `frontend/` directory.
2. Create a `.gcloudignore` file to ignore local `node_modules/`, `.next/` cache, and other temporary files to speed up uploading files to Google Cloud.
3. Update the API connection configuration. Create a production `.env` or set it dynamically:
   
   Create/update `.env.production` inside the `frontend/` directory:
   ```env
   NEXT_PUBLIC_API_URL=https://medcase-backend-xxxxx-uc.a.run.app
   ```

4. Build and deploy the frontend:

```bash
# Build the frontend container image
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/medcase-frontend

# Deploy the frontend to Google Cloud Run
gcloud run deploy medcase-frontend \
    --image gcr.io/YOUR_PROJECT_ID/medcase-frontend \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --port=3000
```

Once the deploy command finishes, you will receive the public **Service URL** of your frontend (e.g., `https://medcase-frontend-xxxxx-uc.a.run.app`). This is the URL you will submit to the hackathon judges!

---

## Step 4: Security and Production Hardening

For production usage:
- **Secrets Management**: Instead of passing the API Key as clear text `--set-env-vars`, use **Google Secret Manager** to securely bind the key:
  ```bash
  # Create a secret for Gemini API Key
  gcloud secrets create gemini-api-key --replication-policy="automatic"

  # Add value to the secret version
  echo -n "your_gemini_api_key" | gcloud secrets versions add gemini-api-key --data-file=-

  # Grant Cloud Run service account access to the secret
  gcloud secrets add-iam-policy-binding gemini-api-key \
      --member="serviceAccount:YOUR_PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
      --role="roles/secretmanager.secretAccessor"
  ```
  Then deploy referencing the secret:
  ```bash
  gcloud run deploy medcase-backend \
      --image gcr.io/YOUR_PROJECT_ID/medcase-backend \
      --platform managed \
      --region us-central1 \
      --allow-unauthenticated \
      --set-secrets="GEMINI_API_KEY=gemini-api-key:latest"
  ```

- **Database Persistence**: Switch from SQLite to a production-grade **Google Cloud SQL (PostgreSQL)** database. Set the `DATABASE_URL` env variable pointing to your Cloud SQL instance connection:
  ```bash
  # Deploy Cloud Run backend with Cloud SQL connection
  gcloud run deploy medcase-backend \
      --image gcr.io/YOUR_PROJECT_ID/medcase-backend \
      --platform managed \
      --region us-central1 \
      --allow-unauthenticated \
      --set-env-vars="DATABASE_URL=postgresql://user:password@/medcase_db?host=/cloudsql/YOUR_PROJECT_ID:us-central1:medcase-db" \
      --add-cloudsql-instances="YOUR_PROJECT_ID:us-central1:medcase-db"
  ```

- **MCP Sidecar Deployment**:
  To deploy the FastMCP server alongside the backend, you can launch `mcp_server.py` as an independent subprocess inside the FastAPI Docker container or run it as a separate container sidecar within the same Cloud Run service.

