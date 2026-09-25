# 🗄️ Multi-Tenant Postgres Schema Provisioner
> Enterprise-grade database isolation and Row-Level Security (RLS) automation for SaaS and ERP architectures. Built by **Arjumand Labs**.

---

### 📖 What It Is
A lightweight, high-performance Python migration runner that automatically provisions completely isolated PostgreSQL schemas for new clients, organizations, or tenants with a single terminal command. 

### 🛑 Why We Built It (The Problem)
Most early-stage SaaS platforms and ERPs use a **"Shared Schema"** architecture—dumping all client data into the exact same tables (e.g., `invoices`, `users`) and separating them by a `tenant_id` column. 

This creates massive technical debt:
1. **Security Risks:** A single bug in a backend query can accidentally leak Client A's financial data to Client B.
2. **Backup Nightmares:** If Client C accidentally deletes their data, you cannot restore just their data without rolling back the entire database for everyone else.
3. **Compliance Blockers:** Enterprise clients often require strict data isolation to meet legal compliance.

### 💡 The Solution (Isolated Schemas + RLS)
This tool implements a **"Schema-per-Tenant"** architecture. When you onboard a new client, the script automatically:
* Generates a dedicated, sandboxed PostgreSQL schema named after the client.
* Replicates all core tables specifically for that schema.
* Enforces **Row-Level Security (RLS)** at the database level so data cannot be queried across tenants.
* Executes idempotently (can be run multiple times safely without crashing or duplicating data).

---

### ⚙️ Features
- **Dynamic SQL Injection:** Safely formats raw `.sql` templates with the target tenant's naming conventions.
- **Sequential Execution:** Automatically scans the `sql/templates/` directory and executes scripts in alphabetical order (`01_...`, `02_...`).
- **Idempotent by Default:** Uses `IF NOT EXISTS` and policy dropping to ensure safe re-runs.

---

### 🛠️ Quickstart

**1. Clone & Install**
```bash
git clone [https://github.com/FakhareArjumand/pg-tenant-provisioner.git](https://github.com/FakhareArjumand/pg-tenant-provisioner.git)
cd pg-tenant-provisioner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt