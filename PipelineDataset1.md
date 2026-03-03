# 🚗 Data Ingestion & Processing Schedule

## 1️⃣ Model Years Ingestion (`bosch.bronze.model_years`)
- **Frequency:** 🗓️ Once per year (beginning of year)
- **Rationale:** New vehicle model years are introduced annually. No value in more frequent runs. Annual execution = minimal cost & overhead.

## 2️⃣ Vehicle Catalog (Makes & Models) – Bronze Layer
- **Tables:** `bronze.vehicle_makes`, `bronze.vehicle_models`
- **Frequency:** 🔁 Weekly
- **Rationale:** Catalog evolves over time for current model year. Weekly refresh = catalog consistency, low API load. Data volume is small.

## 3️⃣ Complaints Ingestion – Silver Layer
- **Tables:** `silver.complaints`, `silver.complaint_products`, `silver.complaint_components`
- **Frequency:** 🌙 Daily (nightly)
- **Rationale:** Complaints are submitted continuously. Daily ingestion = up-to-date analytics. Merge logic ensures idempotency (no duplicates).

## 4️⃣ Gold Layer (Aggregations)
- **Tables:** `gold.model_complaint_stats`, `gold.component_stats`, `gold.yearly_trend`
- **Frequency:** 🌅 Daily (post-Silver)
- **Rationale:** Gold tables are derived from Silver. Overwrite mode ensures consistency. Designed for reporting & dashboards.

---

### 🏁 Execution Order:
1. Bronze – Model Years (annual)
2. Bronze – Makes & Models (weekly)
3. Silver – Complaints (daily)
4. Gold – Aggregations (daily, after Silver)

### 🔗 Dependencies managed via ADF pipelines for sequencing & fault tolerance.