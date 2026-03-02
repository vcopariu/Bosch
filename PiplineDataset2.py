# # Data Pipeline Documentation: Alt Fuel Stations

# ## Step 1 – Bronze Layer (Raw Ingestion)
# - **Source:** CSV files from landing zone (Blob/ADLS)
# - **Actions:**
#   - Read CSV files
#   - Clean column names
#   - Write to `bronze.alt_fuel_stations_raw`
# - **Frequency:** Weekly (or daily for higher freshness)

# ---

# ## Step 2 – Silver Layer (Curated Station Table)
# - **Actions:**
#   - Type cast fields (e.g., `station_id`, `latitude`, `longitude`, `open_date`)
#   - Deduplicate records
#   - Apply data quality filters
# - **Frequency:** Same as Bronze (immediately after Bronze ingestion)

# ---

# ## Step 3 – Gold Layer (Analytics Aggregates)
# - **Actions:**
#   - Recompute and overwrite the following derived tables:
#     - `gold.stations_by_state`
#     - `gold.stations_by_fuel_type`
#     - `gold.stations_opened_by_year`
# - **Frequency:** Same as Silver (runs downstream after Silver)

# ---