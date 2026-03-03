# 🚦 **Data Pipeline Documentation: Alt Fuel Stations**

---

## 🥉 Step 1 – Bronze Layer *(Raw Ingestion)*

- **Source:**  
  📂 CSV files from landing zone (Blob/ADLS)

- **Actions:**  
  1. 📥 Read CSV files  
  2. 🧹 Clean column names  
  3. 💾 Write to `bronze.alt_fuel_stations_raw`

- **Frequency:**  
  ⏱️ Weekly *(or daily for higher freshness)*

---

## 🥈 Step 2 – Silver Layer *(Curated Station Table)*

- **Actions:**  
  1. 🔢 Type cast fields (e.g., `station_id`, `latitude`, `longitude`, `open_date`)  
  2. 🗂️ Deduplicate records  
  3. ✅ Apply data quality filters

- **Frequency:**  
  🔄 Same as Bronze *(immediately after Bronze ingestion)*

---

## 🥇 Step 3 – Gold Layer *(Analytics Aggregates)*

- **Actions:**  
  - ♻️ Recompute and overwrite the following derived tables:
    - `gold.stations_by_state`
    - `gold.stations_by_fuel_type`
    - `gold.stations_opened_by_year`

- **Frequency:**  
  🔄 Same as Silver *(runs downstream after Silver)*

---