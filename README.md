# World Bank Data360: Demographic & Economic Dashboard
### 專題示範：未富先老（Getting Old Before Getting Rich）

[![GitHub Pages](https://img.shields.io/badge/Deployment-GitHub%20Pages-brightgreen)](https://nutcelvischen-jpg.github.io/worldbank-demographic-economic-dashboard/)
[![Data Source](https://img.shields.io/badge/Data-World%20Bank%20Data360-blue)](https://data360.worldbank.org/en/api)
[![Language](https://img.shields.io/badge/Language-Bilingual%20(ZH%20%2F%20EN)-orange)](#)

本專案為大專院校與高中經濟學/社會學課程的實證研究示範專案，展示如何串接 **世界銀行新一代 Data360 API**（`WB_WDI` 資料庫），進行跨國總體數據分析、資料視覺化儀表板開發，並深入論證**「未富先老」**的制度性與結構性挑戰。

---

## 🌐 線上部署展示 (Live Demo)

* 🇹🇼 **中文版儀表板 (Live Demo)：** [點此造訪 GitHub Pages (中文)](https://nutcelvischen-jpg.github.io/worldbank-demographic-economic-dashboard/)
* 🇺🇸 **English Dashboard (Live Demo)：** [Click here for English Version](https://nutcelvischen-jpg.github.io/worldbank-demographic-economic-dashboard/en.html)
* 🐙 **GitHub 原始碼庫 (Repository)：** [https://github.com/nutcelvischen-jpg/worldbank-demographic-economic-dashboard](https://github.com/nutcelvischen-jpg/worldbank-demographic-economic-dashboard)

---

## 📌 核心研究問題 (Core Research Question)

> **Hint 3: "Getting Old Before Getting Rich" (未富先老的難題)**
>
> * **數據事實 (Empirical Fact)：** 中國總人口開始出現歷史性負成長（-0.10%），生育率跌至 1.03，65歲以上佔比突破 14.32%；然而其人均 GDP 僅約 **$12,951 美元**（相較於美國的 **$82,587 美元**，差距逾 6 倍）。
> * **學生核心思考題 (For Students)：** 為什麼人口高齡化對人均所得僅約 1.3 萬美元的中等所得國家而言，其經濟承受度與轉型難度會遠遠高於高所得國家？

---

## 📊 專案架構 (Project Structure)

```text
├── index.html                  # 中文版視覺化分析儀表板 (HTML + Tailwind + SVG + JS)
├── en.html                     # 英文版視覺化分析儀表板 (Bilingual English Dashboard)
├── fetch_wb_data.py            # 透過 Python 串接 World Bank Data360 API 的自動化腳本
├── wb_population_economy_data.json # 從 API 抓取的各國總人口、GDP、生育率完整資料庫
└── README.md                   # 專案說明與學生作業規範指南
```

---

## 🚀 如何本地執行與重新獲取最新數據 (How to Run Locally)

### 1. 複製專案
```bash
git clone https://github.com/nutcelvischen-jpg/worldbank-demographic-economic-dashboard.git
cd worldbank-demographic-economic-dashboard
```

### 2. 透過 Python 自動調取 World Bank Data360 API
```bash
python fetch_wb_data.py
```
> 此腳本將自動向 `https://data360api.worldbank.org/data360/data` 發起 REST 請求，批次獲取多國 2000~2023 年之總人口、生育率、扶養比、人均 GDP 及實質成長率。

### 3. 開啟儀表板
直接在瀏覽器中雙擊開啟 `index.html` 或 `en.html`，即可使用互動試算模擬器與圖表。

---

## 🎯 深度分析結論（作業範例解析）

本專案歸納出四大關鍵維度，解釋中所得國家面臨人口老化的脆弱性：

1. **年金與社福財政儲備不足（Fiscal Buffer Deficit）：** 成熟高所得國在跨入 14% 高齡化門檻時，人均所得已達 3.5 萬～5.5 萬美元，累積了可觀的國民海外資產與主權退休金基金；中所得國家則面臨「未富先提領」的財政赤字風險。
2. **產業價值鏈升級夾心層（Value Chain Squeeze）：** 失去廉價勞動力紅利後面臨產業外移，但高附加價值高科技產業仍面臨先進國技術壁壘，容易卡在「中等收入陷阱」。
3. **醫療與長照的城鄉撕裂（Rural-Urban Divide）：** 數十年青壯年人口向都會流動，導致農村地區出現巨量失能失智與空巢長者，造成嚴峻的非正式家庭照護負擔。
4. **國際移民吸納彈性匱乏（Immigration Inelasticity）：** 缺乏歐美的高薪購買力與開放簽證制度，難以透過全球勞動移民來撫平人口金字塔崩塌。

---

## 📝 學生作業評分與撰寫指引 (Rubric & Student Guidelines)

學生在撰寫總體經濟數據分析作業時，可參考本專案之標準規範：
* **[30%] 數據嚴謹性：** 必須指明數據出處與指標代碼（如世銀 `WB_WDI_SP_POP_TOTL`、`WB_WDI_NY_GDP_PCAP_CD`），且時間區間一致。
* **[25%] 對照組設計：** 須設定明確基準國（如中所得 vs. 高所得、東亞 vs. 歐美），避免孤立羅列單一國家。
* **[25%] 機制性推論：** 不可僅停留在「勞工變少所以 GDP 下降」，須深入總體生產函數（TFP、資本深化）與財政社保收支。
* **[20%] 呈現與視覺化：** 善用對比圖表、互動模擬器或乾淨的 Dashboard，提高政策建議的可讀性與溝通效率。
