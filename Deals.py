import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from collections import defaultdict
from datetime import datetime
from tqdm import tqdm

#Plus Scraper
url = "https://www.plus.nl/screenservices/ECP_Composition_CW/Promotions/Promotion_LP_Content_TF/DataActionGetPromotionList"

payload = {
    "versionInfo": {
        "moduleVersion": "6uc+XDsRynmQ7JQS4jOSaQ",
        "apiVersion": "eynwGehUh7DY1+Mg0udXDw"
    },
    "viewName": "MainFlow.Promotions",
    "screenData": {"variables": {
            "IsShowData": False,
            "StoreNumber": 0,
            "StoreChannel": "",
            "CheckoutId": "9b00374b-6b11-4a64-b7b8-a640d98fccd8",
            "IsOrderEditMode": False,
            "Promotions_All": {
                "List": [],
                "EmptyListItem": {
                    "ProductPromotionBanner": {
                        "InternalTitle": "",
                        "Subtitle": "",
                        "Title": "",
                        "AnchorLinkTitle": "",
                        "Cta": {
                            "InternalTitle": "",
                            "Link": {
                                "Title": "",
                                "Url": "",
                                "AltText": "",
                                "IsPdf": False
                            }
                        },
                        "BackgroundColorClassName": "",
                        "BannerImageNoProducts": {
                            "Url": "",
                            "AltText": ""
                        },
                        "BannerImageWithProducts": {
                            "Url": "",
                            "AltText": ""
                        },
                        "Productspromotions": {
                            "List": [],
                            "EmptyListItem": ""
                        },
                        "ProductPromotionTiles": {
                            "List": [],
                            "EmptyListItem": {
                                "PromotionId": "",
                                "OfferId": "",
                                "ProductName": "",
                                "PromotionLabel": "",
                                "PromotionBasedLabel": "",
                                "Subtitle": "",
                                "Brand": "",
                                "Slug": "",
                                "DisplayInfo_Label": "",
                                "DisplayInfo_PromotionBasedLabel": "",
                                "NewPrice": "0",
                                "PriceOriginal": "0",
                                "PriceOriginal_Highest": "0",
                                "PriceOriginal_Lowest": "0",
                                "StartDate": "1900-01-01",
                                "EndDate": "1900-01-01",
                                "ImageURL": "",
                                "ImageLabel": "",
                                "Position": 0,
                                "IsProduct": False,
                                "IsFreeDeliveryOffer": False,
                                "IsSingleProductPromotion": False,
                                "BadgeQuantity": 0,
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
                                "IsProductOverMajorityAge": False,
                                "Categories": {
                                    "List": [],
                                    "EmptyListItem": {"Name": ""}
                                },
                                "PromotionVariant": "",
                                "PromotionPackage": "",
                                "PromotionExplanation": "",
                                "ProductSKU": "",
                                "ProductLineItemId": "",
                                "StampURL": "",
                                "MaxOrderLimit": 0
                            }
                        },
                        "IsUnderAge": False,
                        "ClickDelayValue": 0,
                        "ProductCategories": "",
                        "PromotionCategories": "",
                        "Priority": 0,
                        "UpdatedAt": "1900-01-01T00:00:00",
                        "ProductCategoriesList": {
                            "List": [],
                            "EmptyListItem": ""
                        },
                        "PromotionCategoriesList": {
                            "List": [],
                            "EmptyListItem": ""
                        }
                    },
                    "Category": {
                        "CategoryId": "",
                        "CategoryLabel": "",
                        "CategorySortOrder": "0",
                        "Offers": {
                            "List": [],
                            "EmptyListItem": {
                                "PromotionID": "",
                                "Offer_Id": "",
                                "PromotionSortOrder": "0",
                                "Brand": "",
                                "Name": "",
                                "Example": "",
                                "Variant": "",
                                "Explanation": "",
                                "Package": "",
                                "Slug": "",
                                "ImageURL": "",
                                "ImageLabel": "",
                                "MetaTitle": "",
                                "MetaDescription": "",
                                "NewPrice": "0",
                                "PriceOriginal_Product": "0",
                                "PriceOriginal_Highest": "0",
                                "PriceOriginal_Lowest": "0",
                                "IsOfflineSaleOnly": False,
                                "IsProductOverMajorityAge": False,
                                "DisplayInfo_Label": "",
                                "DisplayInfo_PromotionBasedLabel": "",
                                "StartDate": "1900-01-01",
                                "EndDate": "1900-01-01",
                                "IsFreeDeliveryOffer": False,
                                "IsSingleProduct": False,
                                "Product_SKU": "",
                                "Product_LineItemId": "",
                                "Product_Quantity": 0,
                                "ProductLoyaltyInfoID": 0,
                                "Product_IsNIX18": False,
                                "Product_MaxOrderLimit": 0,
                                "StampURL": "",
                                "StoreNumberList": {
                                    "List": [],
                                    "EmptyListItem": ""
                                }
                            }
                        },
                        "SKUsAvailable": {
                            "List": [],
                            "EmptyListItem": ""
                        },
                        "NumberOfProducts": 0
                    }
                }
            },
            "OrderEditId": "",
            "PromotionPeriodId": 1,
            "ItemExistsInCart": {
                "List": [],
                "EmptyListItem": {
                    "LineItemId": "",
                    "SKU": "",
                    "Quantity": 0
                }
            },
            "HideDummy": True,
            "IsDesktop": True,
            "_isDesktopInDataFetchStatus": 1,
            "IsTablet": False,
            "_isTabletInDataFetchStatus": 1,
            "IsPhone": False,
            "_isPhoneInDataFetchStatus": 1,
            "OneWelcomeUserId": "",
            "_oneWelcomeUserIdInDataFetchStatus": 1,
            "IsCustomerUnderAge": False,
            "_isCustomerUnderAgeInDataFetchStatus": 1,
            "UserStoreId": "0",
            "_userStoreIdInDataFetchStatus": 1,
            "ItemsInCartJSON": "[]",
            "_itemsInCartJSONInDataFetchStatus": 1,
            "IsTimetraveler": False,
            "_isTimetravelerInDataFetchStatus": 1
        }}
}
headers = {
    "cookie": "SSLB=1; nr1Users=lid%253dAnonymous%253btuu%253d0%253bexp%253d0%253brhs%253dXBC1ss1nOgYW1SmqUjSxLucVOAg%253d%253bhmc%253d4DwFYjtQmhXgYB3zdBmXn5G3zBA%253d; nr2Users=crf%253dT6C%252b9iB49TLra4jEsMeSckDMNhQ%253d%253buid%253d0%253bunm%253d; nlbi_1876175=eZeEb8HSulxhzeQP%2BvsR5gAAAAB86gezruY3avz34vu1a3Vu; incap_ses_1185_1876175=RowPTNK7%2BgEMIrOjcPdxEAZEG2gAAAAAu3CaUpOK1eel%2FjazmVrb0A%3D%3D; SSID_WA9S=CQDT0x0OAAAAAAA4wBhoCDvDDDjAGGgJAAAAAABkKNtrrEQbaAD0DJBOAQNuJCkAOMAYaAkA; SSSC_WA9S=1036.G7500956526350383880.9%7C85648.2696302; SSRT_WA9S=rEQbaAADAA",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "nl,en-US;q=0.7,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=UTF-8",
    "Cookie": "SSLB=1; SSID_WA9S=CQBzxR0OAAAAAAA4wBhoCDvDDDjAGGgIAAAAAABkKNtrtf0aaAD0DJBOAQNuJCkAOMAYaAgA; SSRT_WA9S=P_4aaAADAA; visid_incap_1876175=LZOG4nvMTr2f593jEOy+MjfAGGgAAAAAQUIPAAAAAAAPSV2gpxcpmdaa4BDOyTKf; osVisitor=cb6c241c-4db9-4be2-b852-09ea61ff2651; nr1Users=lid%3dAnonymous%3btuu%3d0%3bexp%3d0%3brhs%3dXBC1ss1nOgYW1SmqUjSxLucVOAg%3d%3bhmc%3d4DwFYjtQmhXgYB3zdBmXn5G3zBA%3d; nr2Users=crf%3dT6C%2b9iB49TLra4jEsMeSckDMNhQ%3d%3buid%3d0%3bunm%3d; plus_cookie_level=3; baked=2023-05-12 10:20:05; SSSC_WA9S=1036.G7500956526350383880.8|85648.2696302; nlbi_1876175=CvcUJ+i2+Gq0MfcC+vsR5gAAAADKU12J2E4a9/in1Wl+A3D0; incap_ses_1686_1876175=1YVCDrwkgy5Ca5rcTeBlF7X9GmgAAAAAxWPWhmtussw2F+v6ZBGXCQ==; osVisit=c6fd940b-50c5-4fca-b7ef-d84ca78b9541",
    "Origin": "https://www.plus.nl",
    "OutSystems-locale": "nl-NL",
    "Referer": "https://www.plus.nl/aanbiedingen",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "traceparent": "00-9cfd45519e0be55f8f0f2e9877ca08a2-bd566d68e0333ebc-01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0",
    "X-CSRFToken": "T6C+9iB49TLra4jEsMeSckDMNhQ="
}

response_plus_deals = requests.request("POST", url, json=payload, headers=headers)

all_promos = []
grouped_promos = defaultdict(list)

for item in response_plus_deals.json()["data"]["PromotionOfferList"]["List"]:
    category = item.get("Category", {})
    category_label = category.get("CategoryLabel", "")
    
    if category_label.lower() == "gratis bezorging":
        continue  # Skip "Gratis Bezorging" category

    offers = category.get("Offers", {}).get("List", [])

    for promo in offers:
        name = promo.get("Name", "").strip()
        new_price = promo.get("NewPrice", "").strip()
        old_price = promo.get("PriceOriginal_Lowest", "").strip()
        
                        # Date handling
        start_date = promo.get("StartDate", "").strip()
        end_date = promo.get("EndDate", "").strip()

        # Check if the promo starts in the future
        future_flag = ""
        if start_date:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
            if start_dt > datetime.today().date():
                future_flag = f" [NOT YET ACTIVE - Starts {start_date}]"

        # Handle the "1+1 Free" deal or similar deals
        display_info = promo.get("DisplayInfo_Label", "").strip()
        if "1+1" in display_info or "gratis" in display_info.lower():
            discount = 50.0  # 50% discount for "1+1 Free" deals or similar
        else:
            # Calculate discount for regular promotions
            new_price_float = float(new_price.replace('€', '').replace(',', '.'))
            old_price_float = float(old_price.replace('€', '').replace(',', '.')) if old_price else new_price_float
            discount = ((old_price_float - new_price_float) / old_price_float) * 100 if old_price_float > new_price_float else 0

        full_name = name + future_flag
        
        # Append deal with calculated discount
        deal = {
            "Name": full_name,
            "NewPrice": new_price,
            "OldPrice": old_price,
            "Discount": round(discount, 2),
            "Category": category_label
        }

        all_promos.append(deal)

# Group promos by category
for deal in all_promos:
    category = deal["Category"]
    grouped_promos[category].append(deal)

# Print out the categorized and generalized deals with discounts
ingredient_categories = [
    "Aardappelen, groente, fruit",
    "Vlees, kip, vis, vega",
    "Pasta, rijst, internationale keuken"
]

ingredient_names = []

# Store and display deals with their discount
for category in ingredient_categories:
    print(f"--- {category} ---")  # Print the category name, nice and bold

    for promo in grouped_promos[category]:
        print(f"{promo['Name']} - €{promo['NewPrice']} - {promo['Discount']}% OFF")
        ingredient_names.append(promo)

    print()  # New line after each category

