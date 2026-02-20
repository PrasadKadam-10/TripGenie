import os
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_page(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)

        if r.status_code != 200:
            print(f"  ❌ Failed ({r.status_code}):", url)
            return ""

        soup = BeautifulSoup(r.text, "html.parser")

        # grab all readable text blocks
        sections = soup.find_all(["p", "li", "h2", "h3"])

        cleaned = []
        for s in sections:
            txt = s.get_text(" ", strip=True)
            if len(txt) > 40:   # filter menu junk
                cleaned.append(txt)

        return "\n".join(cleaned)

    except Exception as e:
        print(f"  ❌ Error scraping {url}: {e}")
        return ""


# =====================================================================
#  ALL DESTINATIONS  (Karnataka + Pan-India)
# =====================================================================
destinations = {

    # ── Karnataka ─────────────────────────────────────────────────────
    "bagalkot":            "https://karnatakatourism.org/en/destinations/bagalkote",
    "bengaluru_urban":     "https://karnatakatourism.org/en/destinations/bengaluru",
    "bengaluru_rural":     "https://karnatakatourism.org/en/destinations/bengaluru-rural",
    "belagavi":            "https://karnatakatourism.org/en/destinations/belagavi",
    "ballari":             "https://karnatakatourism.org/en/destinations/ballari",
    "bidar":               "https://karnatakatourism.org/en/destinations/bidar",
    "vijayapura":          "https://karnatakatourism.org/en/destinations/vijayapura",
    "chamarajanagar":      "https://karnatakatourism.org/en/destinations/chamarajanagar",
    "chikkaballapura":     "https://karnatakatourism.org/en/destinations/chikkaballapur",
    "chikkamagaluru":      "https://karnatakatourism.org/en/destinations/chikkamagalur",
    "chitradurga":         "https://karnatakatourism.org/en/destinations/chitradurga",
    "dakshina_kannada":    "https://karnatakatourism.org/en/destinations/dakshina-kannada",
    "davanagere":          "https://karnatakatourism.org/en/destinations/davanagere",
    "dharwad":             "https://karnatakatourism.org/en/destinations/dharwad",
    "gadag":               "https://karnatakatourism.org/en/destinations/gadag",
    "kalaburagi":          "https://karnatakatourism.org/en/destinations/kalaburagi",
    "hassan":              "https://karnatakatourism.org/en/destinations/hassan",
    "haveri":              "https://karnatakatourism.org/en/destinations/haveri",
    "kodagu":              "https://karnatakatourism.org/en/destinations/coorg",
    "kolar":               "https://karnatakatourism.org/en/destinations/kolar",
    "koppal":              "https://karnatakatourism.org/en/destinations/koppal",
    "hubballi":            "https://karnatakatourism.org/en/destinations/hubballi",
    "mandya":              "https://karnatakatourism.org/en/destinations/mandya",
    "mysuru":              "https://karnatakatourism.org/en/destinations/mysuru",
    "mangaluru":           "https://karnatakatourism.org/en/destinations/mangaluru",
    "hampi":               "https://karnatakatourism.org/en/destinations/hampi",
    "raichur":             "https://karnatakatourism.org/en/destinations/raichur",
    "ramanagara":          "https://karnatakatourism.org/en/destinations/ramanagara",
    "shivamogga":          "https://karnatakatourism.org/en/destinations/shivamogga",
    "tumakuru":            "https://karnatakatourism.org/en/destinations/tumakuru",
    "udupi":               "https://karnatakatourism.org/en/destinations/udupi",
    "uttara_kannada":      "https://karnatakatourism.org/en/destinations/uttara-kannada",
    "yadgir":              "https://karnatakatourism.org/en/destinations/yadgiri",
    "vijayanagara":        "https://karnatakatourism.org/en/destinations/vijayanagara",
    "Devarayanadurga":     "https://karnatakatourism.org/en/destinations/devarayanadurga",
    "pattadakal":          "https://karnatakatourism.org/en/destinations/pattadakal",
    "halebeedu":           "https://karnatakatourism.org/en/destinations/halebeedu",
    "badami":              "https://karnatakatourism.org/en/destinations/badami",
    "gudibande":           "https://karnatakatourism.org/en/destinations/gudibande",
    "magadi":              "https://karnatakatourism.org/en/destinations/magadi",
    "kasargod":            "https://karnatakatourism.org/en/destinations/kasarkod-beach-karnataka-indias-first-blue-flag-beach-you-must-visit",
    "gokharna":            "https://karnatakatourism.org/en/destinations/gokarna",

    # ── Pan-India ─────────────────────────────────────────────────────
    "ANDAMAN_AND_NICOBAR": "https://www.andamantourism.gov.in/tourist-places",
    "Auli":                "https://uttarakhandtourism.gov.in/destination/auli",
    "Badrinath":           "https://uttarakhandtourism.gov.in/destination/badrinath",
    "Bir":                 "https://himachaltourism.gov.in/destination/bir-billing/",
    "Bodh_Gaya":           "https://bihartourism.gov.in/destinations/bodh-gaya",
    "Chennai":             "https://www.tamilnadutourism.tn.gov.in/destinations/chennai",
    "Cherrapunji":         "https://www.meghalayatourism.in/destination/cherrapunji",
    "Darjeeling":          "https://www.westbengaltourism.gov.in/darjeeling",
    "Goa":                 "https://www.goatourism.gov.in/destinations",
    "Harike_wetland":      "https://punjab.gov.in/harike-wetland",
    "Kasol":               "https://himachaltourism.gov.in/destination/kasol/",
    "kerala":              "https://www.keralatourism.org/destinations/",
    "ladhakh":             "https://ladakhtourism.in/destinations",
    "manali":              "https://himachaltourism.gov.in/destination/manali/",
    "mumbai":              "https://www.maharashtratourism.gov.in/destination/mumbai",
    "Periyar_sanctuary":   "https://www.keralatourism.org/destination/periyar-wildlife-sanctuary/142",
    "Pondicherry":         "https://www.tourism.pondicherry.gov.in/places-of-interest",
    "shimala":             "https://himachaltourism.gov.in/destination/shimla/",
    "ujjain":              "https://www.mptourism.com/destination-ujjain.html",
    "varkala":             "https://www.keralatourism.org/destination/varkala/36",
    "india_travel_datasets": "https://incredibleindia.org/destinations",
}


# =====================================================================
os.makedirs("data", exist_ok=True)

success = 0
failed  = []

for name, url in destinations.items():
    print(f"Scraping: {name}")
    text = scrape_page(url)

    if text:
        with open(f"data/{name}.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  ✅ Saved: {name}")
        success += 1
    else:
        print(f"  ⚠️  Empty — skipped: {name}")
        failed.append(name)

print(f"\n{'='*50}")
print(f"✅ Scraped successfully : {success}")
print(f"❌ Failed / Empty       : {len(failed)}")
if failed:
    print("   Failed list:", failed)
print("DONE ✅")