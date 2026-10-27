import urllib.request
import json
import os

countries = {
    'WLD': '全球 (World)',
    'EAS': '東亞與太平洋 (East Asia & Pacific)',
    'JPN': '日本 (Japan)',
    'KOR': '南韓 (South Korea)',
    'CHN': '中國 (China)',
    'IND': '印度 (India)',
    'DEU': '德國 (Germany)',
    'USA': '美國 (USA)',
    'NGA': '奈及利亞 (Nigeria)'
}

indicators = {
    'WB_WDI_SP_POP_TOTL': '總人口',
    'WB_WDI_SP_POP_GROW': '人口年增率(%)',
    'WB_WDI_SP_DYN_TFRT_IN': '生育率(每位婦女)',
    'WB_WDI_SP_POP_65UP_TO_ZS': '65歲以上人口佔比(%)',
    'WB_WDI_NY_GDP_PCAP_CD': '人均GDP(現價美元)',
    'WB_WDI_NY_GDP_MKTP_KD_ZG': 'GDP實質成長率(%)'
}

results = {}

for c_code, c_name in countries.items():
    results[c_code] = {'name': c_name, 'indicators': {}}
    for ind_code, ind_label in indicators.items():
        url = f"https://data360api.worldbank.org/data360/data?DATABASE_ID=WB_WDI&INDICATOR={ind_code}&REF_AREA={c_code}&timePeriodFrom=2000&timePeriodTo=2023"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                val_map = {}
                for r in data.get('value', []):
                    period = r.get('TIME_PERIOD')
                    val = r.get('OBS_VALUE')
                    if val is not None:
                        try:
                            val_map[period] = round(float(val), 2)
                        except:
                            val_map[period] = val
                results[c_code]['indicators'][ind_code] = {
                    'label': ind_label,
                    'series': val_map
                }
        except Exception as e:
            print(f"Error {c_code} {ind_code}: {e}")

with open('wb_population_economy_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Done! Data written to wb_population_economy_data.json")
