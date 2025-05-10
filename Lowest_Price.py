import requests
import urllib.parse
import re
from urllib.parse import quote

# ==========================
# SETUP
# ==========================
# Vraag aan de gebruiker wat er gekocht moet worden
user_input = input("Wat wil je allemaal kopen? (scheid met komma):\n")
mode = input("Kies modus: cheap of lazy: ").strip().lower()
# Verdeel de input in een lijst
grocery_list = [item.strip() for item in user_input.split(",") if item.strip()]

# Maak een dictionary met de originele term en de URL-gecodeerde variant
searches = [{"term": term, "encoded": quote(term)} for term in grocery_list]
for search_data in searches:
    search = search_data["term"]
    search_url = search_data["encoded"]

# Default weights for items sold per piece
default_weights = [
    ("mini magnum", 55),
    ("magnum", 100),
    ("cornets", 40),
    ("raket", 67),
    ("karamel", 51),
    ("waterijs", 67),
    ("ijsjes", 67),
    ("pirulo", 67),
    ("mars", 51),
    ("brood", 800),
    ("stokbrood", 400),
    ("vochtig toiletpapier", 4.5),
    ("toiletpapier", 136),
    ("croissant", 60),
]

unit_aliases = {
    "kilogram": "kg", "kg": "kg", "kilo": "kg",
    "gram": "g", "g": "g", "ml": "g", "milliliter": "g",
    "mg": "mg", "milligram": "mg", "l": "l", "liter": "l",
    "stk": "stk", "stuk": "stk", "st": "stk", "stuks": "stk",
    "doekjes": "stk", "velletjes": "stk", "vellen": "stk"
}

def resolve_default_mass(name, subtitle, unit, amount):
    if unit != "stk":
        return amount, unit
    name_lower = name.lower()
    subtitle_lower = subtitle.lower()
    for keyword, default_weight in default_weights:
        if keyword in name_lower:
            count_match = re.search(r"(\d+)", subtitle_lower)
            count = int(count_match.group(1)) if count_match else int(amount) if amount else 1
            return default_weight * count, "g"
    return amount, unit


def calculate_price_per_kg(name, subtitle, unit, amount, price):
    unit = unit_aliases.get(unit.lower(), unit)
    if unit == "stk":
        amount, unit = resolve_default_mass(name, subtitle, unit, amount)
    if amount is None:
        return None
    if unit == "mg":
        amount_kg = amount / 1_000_000
    elif unit in ["g"]:
        amount_kg = amount / 1_000
    elif unit in ["kg", "l"]:
        amount_kg = amount
    else:
        return None
    if amount_kg == 0:
        return None
    return price / amount_kg
# ==========================
# DATA PLUS
# ==========================
url = "https://www.plus.nl/screenservices/ECP_Composition_CW/ProductLists/PLP_Content/DataActionGetProductListAndCategoryInfo"

payload = {
    "versionInfo": {
        "moduleVersion": "EH1b7hCuPiTJcG_ibLRhIQ",
        "apiVersion": "bYh0SIb+kuEKWPesnQKP1A"
    },
    "viewName": "MainFlow.SearchPage",
    "screenData": {"variables": {
            "AppliedFiltersList": {
                "List": [],
                "EmptyListItem": {
                    "Name": "",
                    "Quantity": "0",
                    "IsSelected": False,
                    "URL": ""
                }
            },
            "LocalCategoryID": 0,
            "LocalCategoryName": "",
            "LocalCategoryParentId": 0,
            "LocalCategoryTitle": "",
            "IsLoadingMore": False,
            "IsFirstDataFetched": False,
            "ShowFilters": False,
            "IsShowData": False,
            "StoreNumber": 0,
            "StoreChannel": "",
            "CheckoutId": "9b00374b-6b11-4a64-b7b8-a640d98fccd8",
            "IsOrderEditMode": False,
            "ProductList_All": {
                "List": [],
                "EmptyListItem": {
                    "SKU": "",
                    "Brand": "",
                    "Name": "",
                    "Product_Subtitle": "",
                    "Slug": "",
                    "ImageURL": "",
                    "ImageLabel": "",
                    "MetaTitle": "",
                    "MetaDescription": "",
                    "OriginalPrice": "0",
                    "NewPrice": "0",
                    "Quantity": 0,
                    "LineItemId": "",
                    "IsProductOverMajorityAge": False,
                    "Logos": {
                        "PLPInUpperLeft": {
                            "List": [],
                            "EmptyListItem": {
                                "Name": "",
                                "LongDescription": "",
                                "URL": "",
                                "Order": 0
                            }
                        },
                        "PLPAboveTitle": {
                            "List": [],
                            "EmptyListItem": {
                                "Name": "",
                                "LongDescription": "",
                                "URL": "",
                                "Order": 0
                            }
                        },
                        "PLPBehindSizeUnit": {
                            "List": [],
                            "EmptyListItem": {
                                "Name": "",
                                "LongDescription": "",
                                "URL": "",
                                "Order": 0
                            }
                        }
                    },
                    "EAN": "",
                    "Packging": "",
                    "Categories": {
                        "List": [],
                        "EmptyListItem": {"Name": ""}
                    },
                    "IsAvailable": False,
                    "PromotionLabel": "",
                    "PromotionBasedLabel": "",
                    "PromotionStartDate": "1900-01-01",
                    "PromotionEndDate": "1900-01-01",
                    "IsFreeDeliveryOffer": False,
                    "IsOfflineSaleOnly": False,
                    "MaxOrderLimit": 0,
                    "CitrusAdId": ""
                }
            },
            "PageNumber": 1,
            "SelectedSort": "",
            "OrderEditId": "",
            "IsListRendered": False,
            "IsAlreadyFetch": False,
            "IsPromotionBannersFetched": False,
            "Period": {
                "FromDate": "2025-05-07",
                "ToDate": "2025-05-13"
            },
            "UserStoreId": "0",
            "FilterExpandedList": {
                "List": [],
                "EmptyListItem": False
            },
            "ItemsInCart": {
                "List": [],
                "EmptyListItem": {
                    "LineItemId": "",
                    "SKU": "",
                    "MainCategory": {
                        "Name": "",
                        "Webkey": "",
                        "OrderHint": "0"
                    },
                    "Quantity": 0,
                    "Name": "",
                    "Subtitle": "",
                    "Brand": "",
                    "Image": {
                        "Label": "",
                        "URL": ""
                    },
                    "ItemTypeAttributeId": "",
                    "DepositFee": "0",
                    "Slug": "",
                    "ChannelId": "",
                    "Promotion": {
                        "BasedLabel": "",
                        "Label": "",
                        "StampURL": "",
                        "NewPrice": "0",
                        "IsFreeDelivery": False
                    },
                    "IsNIX18": False,
                    "Price": "0",
                    "MaxOrderLimit": 0,
                    "QuantityOfFreeProducts": 0
                }
            },
            "HideDummy": False,
            "OneWelcomeUserId": "",
            "_oneWelcomeUserIdInDataFetchStatus": 1,
            "CategorySlug": "",
            "_categorySlugInDataFetchStatus": 1,
            "SearchKeyword": search,             
            "_searchKeywordInDataFetchStatus": 1,
            "IsDesktop": True,
            "_isDesktopInDataFetchStatus": 1,
            "IsSearch": True,
            "_isSearchInDataFetchStatus": 1,
            "URLPageNumber": 1,
            "_uRLPageNumberInDataFetchStatus": 1,
            "FilterQueryURL": "",
            "_filterQueryURLInDataFetchStatus": 1,
            "IsMobile": False,
            "_isMobileInDataFetchStatus": 1,
            "IsTablet": False,
            "_isTabletInDataFetchStatus": 1,
            "Monitoring_FlowTypeId": 2,
            "_monitoring_FlowTypeIdInDataFetchStatus": 1,
            "IsCustomerUnderAge": False,
            "_isCustomerUnderAgeInDataFetchStatus": 1
        }}
}
headers = {
    "cookie": "SSLB=1; nr1Users=lid%253dAnonymous%253btuu%253d0%253bexp%253d0%253brhs%253dXBC1ss1nOgYW1SmqUjSxLucVOAg%253d%253bhmc%253d4DwFYjtQmhXgYB3zdBmXn5G3zBA%253d; nr2Users=crf%253dT6C%252b9iB49TLra4jEsMeSckDMNhQ%253d%253buid%253d0%253bunm%253d; nlbi_1876175=eZeEb8HSulxhzeQP%2BvsR5gAAAAB86gezruY3avz34vu1a3Vu; incap_ses_1185_1876175=RowPTNK7%2BgEMIrOjcPdxEAZEG2gAAAAAu3CaUpOK1eel%2FjazmVrb0A%3D%3D; SSID_WA9S=CQDT0x0OAAAAAAA4wBhoCDvDDDjAGGgJAAAAAABkKNtrrEQbaAD0DJBOAQNuJCkAOMAYaAkA; SSSC_WA9S=1036.G7500956526350383880.9%7C85648.2696302; SSRT_WA9S=rEQbaAADAA",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "nl,en-US;q=0.7,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=UTF-8",
    "Cookie": "SSLB=1; SSID_WA9S=CQCjIB0OAAAAAAA4wBhoCDvDDDjAGGgOAAAAAABkKNtrjXccaAD0DJBOAQNuJCkAOMAYaA4A; SSRT_WA9S=6HwcaAADAA; visid_incap_1876175=LZOG4nvMTr2f593jEOy+MjfAGGgAAAAAQUIPAAAAAAAPSV2gpxcpmdaa4BDOyTKf; osVisitor=cb6c241c-4db9-4be2-b852-09ea61ff2651; nr1Users=lid%3dAnonymous%3btuu%3d0%3bexp%3d0%3brhs%3dXBC1ss1nOgYW1SmqUjSxLucVOAg%3d%3bhmc%3d4DwFYjtQmhXgYB3zdBmXn5G3zBA%3d; nr2Users=crf%3dT6C%2b9iB49TLra4jEsMeSckDMNhQ%3d%3buid%3d0%3bunm%3d; plus_cookie_level=3; baked=2023-05-12 10:20:05; SSSC_WA9S=1036.G7500956526350383880.14|85648.2696302; nlbi_1876175=nbolHyY4vCGmpbLL+vsR5gAAAACxVR6Lb0JIK03Vtpz6KBdc; incap_ses_1185_1876175=ejQAae/rxnAiJ7CkcPdxEOd8HGgAAAAAdRbrOrgCfQpZtwO0oGmnbQ==; osVisit=4b458cbb-2e72-4f09-8e65-fad60c75f1da",
    "Origin": "https://www.plus.nl",
    "OutSystems-locale": "nl-NL",
    "Referer": f"https://www.plus.nl/zoekresultaten?SearchTerm={search_url}",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "traceparent": "00-621cbf1060c2471aa4f25234e76dd634-ab6b733579ab0aaa-01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0",
    "X-CSRFToken": "T6C+9iB49TLra4jEsMeSckDMNhQ="
}

all_results = {"PLUS": [], "ALDI": []}

# ==========================
# SCRAPE PLUS
# ==========================
def scrape_plus(search):
    print(f"[DEBUG] Searching PLUS for: {search}")
    payload["screenData"]["variables"]["SearchKeyword"] = search
    response = requests.post(url, json=payload, headers=headers)
    items = response.json().get("data", {}).get("ProductList", {}).get("List", [])
    results = []
    for item in items:
        plp = item.get("PLP_Str", {})
        name = plp.get("Name", "")
        subtitle = plp.get("Product_Subtitle", "")
        original_price = float(plp.get("OriginalPrice", "0") or 0)
        new_price = float(plp.get("NewPrice", "0") or 0)
        final_price = new_price if new_price != 0 else original_price

        match = re.search(r"(\d[\d\.,]*)\s*(\w+)", subtitle)
        if not match:
            continue
        amount = float(match.group(1).replace(",", "."))
        unit = match.group(2)

        price_per_kg = calculate_price_per_kg(name, subtitle, unit, amount, final_price)
        if price_per_kg is None:
            continue

        results.append({
            "Name": name,
            "Subtitle": subtitle,
            "Price": final_price,
            "PricePerKg": price_per_kg,
            "Source": "PLUS"
        })
    return results


# ==========================
# SCRAPE ALDI
# ==========================
def scrape_aldi(search):
    url = "https://2hu29pf6bh-dsn.algolia.net/1/indexes/*/queries"
    querystring = {
        "x-algolia-agent": "Algolia for JavaScript (4.24.0); Browser (lite)",
        "x-algolia-api-key": "686cf0c8ddcf740223d420d1115c94c1",
        "x-algolia-application-id": "2HU29PF6BH"
    }
    payload = {"requests": [{
        "indexName": "an_prd_nl_nl_products",
        "params": f"query={search}&hitsPerPage=1000"
    }]}
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://www.aldi.nl",
        "Referer": "https://www.aldi.nl/",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    results = []
    for item in response.json()["results"][0]["hits"]:
        brand = item.get("brandName", "")
        product = item.get("variantName", "")
        subtitle = item.get("salesUnit", "")
        price_data = item.get("currentPrice", {})
        price = price_data.get("priceValue", None)
        keywords = search.lower().split()
        name = f"{brand} {product}".strip()

        relevant_fields = [
            (brand or "").lower(),
            (product or "").lower(),
        ]

        if not all(keyword in " ".join(relevant_fields) for keyword in keywords):
            continue
        if price is None:
            continue

        match = re.search(r"(\d[\d\.,]*)\s*(\w+)", subtitle)
        if not match:
            continue
        amount = float(match.group(1).replace(",", "."))
        unit = match.group(2)

        price_per_kg = calculate_price_per_kg(name, subtitle, unit, amount, price)
        if price_per_kg is None:
            continue

        print(name, f" - €{price}", subtitle, f" - €{round(price_per_kg, 2)} per kg!")

        results.append({
            "Name": name,
            "Subtitle": subtitle,
            "Price": price,
            "PricePerKg": price_per_kg,
            "Source": "ALDI"
        })
    return results

# ==========================
# MAIN
# ==========================
cheapest_per_store = {"PLUS":[], "ALDI":[]}
totals = {"PLUS": 0, "ALDI": 0}

for item in grocery_list:
    for store, func in [("PLUS", scrape_plus), ("ALDI", scrape_aldi)]:
        matches = func(item)
        all_results[store].extend(matches)

for store in ["PLUS", "ALDI"]:
    print(f"\n==== Resultaten van {store} ====")
    for result in all_results[store]:
        print(f"{result['Name']} - €{result['Price']} - {result['Subtitle']} - €{round(result['PricePerKg'], 2)} per kg")


# ==========================
# CHEAP MODE
# ==========================
if mode.lower() == "cheap":

    for item in grocery_list:
        keywords = item.lower().split()
        combined = all_results["PLUS"] + all_results["ALDI"]
        matches = [r for r in combined if any(k in r["Name"].lower() for k in keywords)]
        if matches:
            cheapest = min(matches, key=lambda x: x["PricePerKg"])
            store = cheapest["Source"]
            cheapest_per_store[store].append(cheapest)
            totals[store] += cheapest["Price"]
        else:
            print(f"{item} → niet gevonden bij PLUS of ALDI.")

    # Goedkoopste per winkel
    for store, items in cheapest_per_store.items():
        print(f"\n---- Goedkoopste opties bij {store} ----")
        for item in items:
            print(f"Product: {item['Name']}")
            print(f"Verpakking: {item['Subtitle']}")
            print(f"Prijs: €{item['Price']}")
            print(f"Prijs per kg: €{round(item['PricePerKg'], 2)}")
            print("-" * 30)
        print(f"Totaal bij {store}: €{round(totals[store], 2)}")
    
    total_all = sum(totals.values())
    print(f"\nTotale som over alle winkels: €{round(total_all, 2)}")

    

# ==========================
# LAZY MODE
# ==========================
if mode.lower() == "lazy":
    store_totals = {
        "PLUS": {"total": 0, "items": [], "missing": []},
        "ALDI": {"total": 0, "items": [], "missing": []},
    }

    for item in grocery_list:
        keywords = item.lower().split()
        for store in ["PLUS", "ALDI"]:
            matches = [r for r in all_results[store] if all(k in r["Name"].lower() for k in keywords)]
            if matches:
                cheapest = min(matches, key=lambda x: x["PricePerKg"])
                store_totals[store]["total"] += cheapest["Price"]
                store_totals[store]["items"].append(cheapest)
            else:
                store_totals[store]["missing"].append(item)

    best_store = None
    if any(not store_totals[s]["missing"] for s in store_totals):
        best_store = min(
            (s for s in store_totals if not store_totals[s]["missing"]),
            key=lambda s: store_totals[s]["total"]
        )
    else:
        best_store = min(
            store_totals,
            key=lambda s: (len(store_totals[s]["missing"]), store_totals[s]["total"])
        )

    print(f"\n---- LAZY MODE: Koop alles bij {best_store} ----")
    for product in store_totals[best_store]["items"]:
        print(f"{product['Name']} - €{product['Price']} - {product['Subtitle']} - €{round(product['PricePerKg'], 2)} per kg")
    print(f"Totaal bij {best_store}: €{round(store_totals[best_store]['total'], 2)}")

    if store_totals[best_store]["missing"]:
        print("\n---- Niet gevonden bij gekozen winkel ----")
        other_store = "ALDI" if best_store == "PLUS" else "PLUS"
        for missing in store_totals[best_store]["missing"]:
            keywords = missing.lower().split()
            other_matches = [r for r in all_results[other_store] if all(k in r["Name"].lower() for k in keywords)]
            if other_matches:
                cheapest = min(other_matches, key=lambda x: x["PricePerKg"])
                print(f"{missing} → {cheapest['Name']} - €{cheapest['Price']} bij {other_store}")
            else:
                print(f"{missing} → ook niet gevonden bij {other_store}.")
