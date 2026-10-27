# World Bank Data360: Demographic Dynamics & Economic Dashboard
### Academic Case Study: Getting Old Before Getting Rich

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen)](https://nutcelvischen-jpg.github.io/worldbank-demographic-economic-dashboard/)
[![Data Source](https://img.shields.io/badge/Data-World%20Bank%20Data360-blue)](https://data360.worldbank.org/en/api)
[![Language](https://img.shields.io/badge/Language-English%20%7C%20%E4%B8%AD%E6%96%87-orange)](#)

> **Languages:** [English](README.md) | [繁體中文 (Traditional Chinese)](README.zh-TW.md)

This project serves as a comprehensive educational benchmark and assignment demonstration for collegiate and high school economics/sociology courses. It showcases how to programmatically interface with the **World Bank Data360 REST API** (`WB_WDI` database), extract cross-national macroeconomic indicators, build interactive data visualization dashboards, and rigorously analyze the structural phenomenon of **"Getting Old Before Getting Rich"**.

---

## 🌐 Live Deployments

* 🇺🇸 **English Interactive Dashboard:**  
  [https://nutcelvischen-jpg.github.io/worldbank-demographic-economic-dashboard/en.html](https://nutcelvischen-jpg.github.io/worldbank-demographic-economic-dashboard/en.html)
* 🇹🇼 **Traditional Chinese Dashboard (中文版):**  
  [https://nutcelvischen-jpg.github.io/worldbank-demographic-economic-dashboard/](https://nutcelvischen-jpg.github.io/worldbank-demographic-economic-dashboard/)
* 🐙 **GitHub Repository:**  
  [https://github.com/nutcelvischen-jpg/worldbank-demographic-economic-dashboard](https://github.com/nutcelvischen-jpg/worldbank-demographic-economic-dashboard)

---

## 📌 Core Research Question (Student Prompt)

> ### **Hint 3: "Getting Old Before Getting Rich"**
>
> * **Empirical Fact:** China's total population has begun shrinking (-0.10%), with its total fertility rate dropping to 1.03 and the population aged 65+ reaching 14.32%. However, its GDP per capita stands around **$12,951** (compared to over **$82,587** in the United States—a gap of more than 6x).
> * **Guiding Question for Students:** *Why is population aging significantly more dangerous and difficult to manage for middle-income economies than for advanced high-income economies?*

---

## 📊 Empirical Data Comparison (World Bank Data360)

| Economy / Region | Total Population (2023) | Pop. Growth | Fertility Rate (TFR) | Aged 65+ (%) | GDP per Capita (USD) | Real GDP Growth |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **World (WLD)** | 8.06 B | +0.93% | 2.22 | 9.98% | $13,314 | 2.86% |
| **United States (USA)** | 336.8 M | +0.82% | 1.66 | 17.43% | $82,587 | 2.93% |
| **Germany (DEU)** | 83.3 M | +0.13% | 1.46 | 22.79% | $54,777 | -0.87% |
| **Japan (JPN)** | 124.5 M | -0.49% | 1.26 | 29.56% | $35,215 | 0.72% |
| **South Korea (KOR)** | 51.7 M | +0.08% | 0.78 | 18.34% | $35,674 | 1.58% |
| **China (CHN)** | 1.41 B | -0.10% | 1.03 | 14.32% | $12,951 | 5.42% |
| **India (IND)** | 1.44 B | +0.88% | 1.99 | 6.92% | $2,434 | 7.21% |
| **Nigeria (NGA)** | 227.9 M | +2.10% | 4.55 | 3.03% | $2,139 | 3.32% |

---

## 🎯 Four Structural Pillars Answering the Question

1. **Fiscal & Pension Buffer Deficit:**  
   Western economies and Japan achieved high-income status before their populations aged ("Rich Before Old"). They built up decades of household financial wealth and multi-trillion-dollar sovereign/private retirement trusts. Middle-income nations face a massive retirement wave with underfunded social safety nets.

2. **The Industrial Value Chain Squeeze (Middle-Income Trap):**  
   Disappearing demographic dividends push wages up, driving labor-intensive manufacturing out to Southeast Asia and India. Meanwhile, climbing into capital- and tech-intensive frontier sectors (semiconductors, AI, biotech) faces formidable technological and geopolitical barriers.

3. **Rural-Urban Healthcare & Caregiving Divide:**  
   Decades of internal migrant labor drained working-age youths toward metropolitan coastal cities, leaving countryside regions filled with isolated senior citizens. Fragile rural medical infrastructure creates acute non-market caregiving burdens on younger workers.

4. **Immigration Inelasticity:**  
   The US, Canada, and Western Europe use high wages and open immigration pathways to absorb working-age global talent and blunt domestic aging. Middle-income economies lack the wage premium and institutional mechanisms to offset workforce declines via foreign immigration.

---

## 📂 Repository Layout

```text
├── index.html                      # Traditional Chinese Interactive Dashboard
├── en.html                         # English Interactive Dashboard
├── fetch_wb_data.py                # Automated Python ETL script for World Bank Data360 API
├── wb_population_economy_data.json # Serialized empirical data fetched via API
├── README.md                       # English documentation and student guide
└── README.zh-TW.md                 # Traditional Chinese documentation
```

---

## 🚀 How to Run Locally & Query the API

### 1. Clone the Repository
```bash
git clone https://github.com/nutcelvischen-jpg/worldbank-demographic-economic-dashboard.git
cd worldbank-demographic-economic-dashboard
```

### 2. Fetch Fresh Data via World Bank Data360 API
```bash
python fetch_wb_data.py
```
> The script issues REST requests to `https://data360api.worldbank.org/data360/data` across indicators:
> * `WB_WDI_SP_POP_TOTL` (Total Population)
> * `WB_WDI_SP_POP_GROW` (Population Growth Rate %)
> * `WB_WDI_SP_DYN_TFRT_IN` (Fertility Rate)
> * `WB_WDI_SP_POP_65UP_TO_ZS` (Population Aged 65+ %)
> * `WB_WDI_NY_GDP_PCAP_CD` (GDP per Capita, current US$)
> * `WB_WDI_NY_GDP_MKTP_KD_ZG` (Real GDP Growth Rate %)

### 3. Open the Dashboards
Simply double-click `index.html` or `en.html` in your browser. No local web server or build tool is required.

---

## 📝 Student Assignment Rubric & Submission Guidelines

When preparing economic research assignments, students should adhere to these core standards demonstrated in this repository:

* **[30%] Data Provenance & Reproducibility:** Explicitly cite API endpoint specifications, database names, and standardized indicator codes.
* **[25%] Comparative Methodology:** Establish counterfactual or control groups (e.g., middle-income vs. high-income benchmarks) rather than analyzing one nation in isolation.
* **[25%] Mechanistic Reasoning:** Connect demographic shifts to macroeconomic production theory (e.g., Cobb-Douglas production function, TFP compensation, fiscal dependency ratios).
* **[20%] Visual & Interactive Presentation:** Use intuitive visual comparisons and interactive simulators to effectively communicate empirical findings.
