# Medallion Architecture: EPA Data Pipeline

# ──────────────────────────────
# 1️⃣ Bronze Layer (Raw Ingestion)
# ──────────────────────────────
# Tables:
#   - bronze.epa_vehicles_raw
#   - bronze.epa_emissions_raw
#
# Frequency: Monthly
# Rationale:
#   - EPA datasets change less frequently than event-based sources (e.g., complaints).
#   - Monthly refresh balances data freshness and compute/API cost.
#   - Schedule can be increased to weekly if business requires faster updates.

# ──────────────────────────────────────────────
# 2️⃣ Silver Layer (Curated & Relational Model)
# ──────────────────────────────────────────────
# Tables:
#   - silver.epa_vehicles         (1 row per vehicle_id)
#   - silver.epa_emissions        (multiple rows per vehicle_id, keyed by sales area + standard)
#
# Frequency: Same run as Bronze (immediately downstream)
# Loading Strategy:
#   - MERGE / upsert into Silver tables for idempotency and to avoid duplicates.
#   - Type casting and minimal cleaning (numeric fields, standard text, scores).

# ──────────────────────────────────────────────
# 3️⃣ Gold Layer (Analytics / Reporting)
# ──────────────────────────────────────────────
# Tables (examples):
#   - gold.epa_smartway_by_make_year
#
# Frequency: Same run as Silver (downstream dependency)
# Loading Strategy:
#   - Gold tables are fully derived from Silver and recomputed using overwrite for consistency.

# ──────────────────────────────
# Execution Order & Dependencies
# ──────────────────────────────
# 1. Bronze: Ingest Vehicles + Emissions CSV
# 2. Silver: Curate + merge into relational tables
# 3. Gold: Join-based aggregations for reporting
#
# Dependencies are enforced in ADF so Gold runs only after Silver succeeds.