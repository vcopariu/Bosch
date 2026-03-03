# 🛠️ Bosch Assignment – Databricks Execution Order Guide

Welcome! Follow this guide to set up and run your Bosch data pipeline in Databricks.  
Let’s make your data journey smooth and organized! 🚦✨

---

## 📋 Prerequisites

**Before running any dataset notebooks:**

### 1️⃣ Create Schemas

- **Run:** `CreateSchema` notebook

  This will create the following schemas:
  - 🟫 `bronze`
  - 🥈 `silver`
  - 🥇 `gold`

  > _**Note:** This step must be executed **once** before any other notebook!_

---

## ⚙️ Configuration

In the **Utils / configuration** section, ensure these paths are set:

python
bronze_schema = "bronze"
silver_schema = "silver"
gold_schema = "gold"

dataset2_file_path = "/Volumes/bosch/bronze/dataset2/alt_fuel_stations (Mar 2 2026).csv"
dataset3_file_path_emissions = "/Volumes/bosch/bronze/dataset3/emissions.csv"
dataset3_file_path_vehicles = "/Volumes/bosch/bronze/dataset3/vehicles.csv"


---

## 📦 DATASET 1 – NHTSA (API)

### 🟫 Bronze Layer  
_Run in this order:_
1. `Bronze_ModelYears`
2. `Bronze_VehicleMakes`
3. `Bronze_VehicleModels`

### 🥈 Silver Layer  
- `Silver_Complaints`  
  _Creates:_
  - `silver.complaints`
  - `silver.complaint_products`
  - `silver.complaint_components`

### 🥇 Gold Layer  
- `Gold_Complaints`

---

## 📦 DATASET 2 – DOE (Alternative Fuel Stations)

### 🟫 Bronze Layer  
- `Bronze_DOE_Stations`

### 🥈 Silver Layer  
- `Silver_DOE_Stations`

### 🥇 Gold Layer  
- `Gold_DOE_Analytics`

---

## 📦 DATASET 3 – EPA (Vehicles + Emissions)

### 🟫 Bronze Layer  
- `Bronze_EPA_Vehicles`
- `Bronze_EPA_Emissions`

### 🥈 Silver Layer  
- `Silver_EPA_Vehicles`
- `Silver_EPA_Emissions`

### 🥇 Gold Layer  
- `Gold_EPA_Analytics`

---

