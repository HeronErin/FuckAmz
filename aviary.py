
# Launcher.Home.FR.1 apears to be all FeaturedRotatorAd

# EPG.First apears to be InlineAd
# Gordon.Live.Default.Inline is an inlineAd at the live screen?

# App.TV.Featured.Default.Rotational is tile ads

import random, string, time, json

TARGET_HOME_ROTS = 9
TARGET_HOME_TILES = 5
TARGET_GORDEN_LIVE = 1
TTL = 235

def HandleAviary(ads, flow):
    alreadyRUn = []
    canReturn = [ad["placementName"] for ad in ads]
    retAds = []
    NOW = int(time.time()) # Make sure time is always the same

    try:
        for ad in ads:

            if "Launcher.Home.FR.1" == ad["placementName"] and not ad["placementName"] in alreadyRUn:

                for _ in range(1):
                    retAds.append(featuredRotatorAd(
                        {"adRole": "mainAd", "placementName":"Launcher.Home.FR.1"},
                         main_img="https://raw.githubusercontent.com/HeronErin/FuckAmz/main/test_imgs/featured_rot_ad.jpg", 
                         url="https://www.youtube.com/watch?v=QQu1_bf1Bdo"
                        ))


            # elif "Launcher.Home.Default.Rotational" == ad["placementName"] and not ad["placementName"] in alreadyRUn:
            #     for t in range(4):
            #         retAds.append(tileAd(
            #             {"adRole": "mainAd", "placementName":"Launcher.Home.Default.Rotational"},
            #             main_img="https://raw.githubusercontent.com/HeronErin/FuckAmz/main/test_imgs/title_ad_rot.jpg",
            #             sub_img=None,
            #             head="Fuck your mother", 
            #             desc="This plays a good video", 
            #             title="Owo", 
            #             url="https://www.youtube.com/watch?v=QQu1_bf1Bdo", tile_pos=t+1
            #             ))
                # retAds.append(inlineAd(
                #     {"adRole": "mainAd", "placementName":"Launcher.Home.Default.Rotational"},
                #     head="This is my firestick now",
                #     main_img="https://raw.githubusercontent.com/HeronErin/FuckAmz/main/test_imgs/inline_ad.jpg",
                #     url="https://www.youtube.com/watch?v=QQu1_bf1Bdo",
                #     desc="This is my right as an american", 
                #     headline="Hacking is fun",
                #     img=None
                #     ))
            # elif "Gordon.Live.Default.Inline" == ad["placementName"] and not ad["placementName"] in alreadyRUn:
            #     retAds.append(inlineAd(
            #         {"adRole": "mainAd", "placementName":"Gordon.Live.Default.Inline"},
            #         head="This is my firestick now LIVE",
            #         main_img="https://raw.githubusercontent.com/HeronErin/FuckAmz/main/test_imgs/inline_ad.jpg",
            #         url="https://www.youtube.com/watch?v=QQu1_bf1Bdo",
            #         desc="This is my right as an american", 
            #         headline="Hacking is fun LIVE",
            #         img=None
            #         ))
            # elif "EPG.First" == ad["placementName"] and not ad["placementName"] in alreadyRUn:
            #     retAds.append(inlineAd(
            #         {"adRole": "mainAd", "placementName":"EPG.First"},
            #         head="This is my firestick now EPG.First",
            #         main_img="https://raw.githubusercontent.com/HeronErin/FuckAmz/main/test_imgs/inline_ad.jpg",
            #         url="https://www.youtube.com/watch?v=QQu1_bf1Bdo",
            #         desc="This is my right as an american", 
            #         headline="Hacking is fun EPG.First",
            #         img=None
            #         ))
            else:
                retAds.append(getNulledAd(ad))
            alreadyRUn.append(ad["placementName"])
            # if "App.TV.Featured.Default.Rotational" in canReturn:
            #     for t in range(TARGET_HOME_TILES):
            #         retAds.append(tileAd(
            #             {"adRole": "mainAd", "placementName":"App.TV.Featured.Default.Rotational"},
            #             main_img="https://raw.githubusercontent.com/HeronErin/FuckAmz/main/test_imgs/title_ad_rot.jpg",
            #             sub_img=None,
            #             head="Fuck your mother App.TV", 
            #             desc="This plays a good video", 
            #             title="Owo App.TV", 
            #             url="https://www.youtube.com/watch?v=QQu1_bf1Bdo", tile_pos=t
            #             ))


    finally:
        flow.response.text = json.dumps({"ads": retAds})






def generate_random_url():
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    url = f"https://aax-us-east-retail-direct.amazon.com/x/px/RC5CzggKqUeeXKk-jmZiVsQAAAGMBNHzFwEAABAHAwBvbm9fbHR0bF9iaWQxICBvbm9fdHhuX2ltcDEgICBw{random_part}/nii/{{\"ni\":true}}"
    return url

def getNulledAd(ad):
    return {
            "accessibilityText": None,
            "adId": None,
            "adRole": ad.get("adRole"),
            "adVersion": None,
            "additionalAviaryMetadataJsonString": None,
            "clickTrackingUrl": None,
            "creativeId": None,
            "imageUrl": None,
            "impressionUrl": None,
            "instrPixelUrl": generate_random_url(),
            "intentUrl": None,
            "placementName": ad.get("placementName"),
            "ttlMinutes": None,
            "type": None
        }

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Banner ad
def inlineAd(ad, acc_text=None, head=None, main_img=None, url=None, desc=None, headline=None, img=None):
    return {
        "__type": "ReturnedInlineAd:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
        "accessibilityText": acc_text if acc_text is not None else "Accessibility Text",
        "adId": str(int(random.random() * 500000000000)),
        "adRole": ad["adRole"],
        "adVersion": str(int(time.time())),
        "additionalAviaryMetadataJsonString": {
            "ThreePProviders": [],
            "adRequestId": generate_random_string(len("Tju9V2SfcTht4Q9tVF0qAQ")),
            "bidId": generate_random_string(len("r0knCIbYuU06WXFhnfHE1A")),
            "creativeVariantConfig": None,
            "eventTrackers": None,
            "firstPartyReportingJSFileURL": "",
            "instrPixelUrl": None
        },
        "clickTrackingUrl": "",
        "creativeId": str(int(random.random() * 500000000000)),
        "header": head if head is not None else "",
        "imageUrl": main_img,
        "impressionUrl": "",
        "instrPixelUrl": None,
        "intentUrl": url if url is not None else "",
        "miniDetails": {
            "__type": "ReturnedCustomAdMiniDetails:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
            "description": desc if desc is not None else "",
            "headline": headline if headline is not None else "",
            "imageUrl": img ,
            "type": "CustomAdMiniDetails",
            "videoSourceUrl": None,
            "videoStreamUrl": None
        },
        "placementName": ad["placementName"],
        "ttlMinutes": str(TTL),
        "type": "InlineAd"
    }
# Single tile
def tileAd(ad, main_img=None, sub_img=None, head=None, desc=None, title=None, url=None, acc_text=None, tile_pos=None):
    return {
        "__type": "ReturnedTileAd:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
        "accessibilityText": acc_text if acc_text is not None else "Accessibility Text",
        "adId": str(int(random.random() * 500000000000)),
        "adRole": ad["adRole"],
        "adVersion": str(int(time.time())),
        "additionalAviaryMetadataJsonString": {
            "ThreePProviders": [],
            "adRequestId": generate_random_string(len("a0xOx1iM.J-5O.P7.jj8qA")),
            "bidId": generate_random_string(len("r0knCIbYuU06WXFhnfHE1A")),
            "creativeVariantConfig": None,
            "eventTrackers": None,
            "firstPartyReportingJSFileURL": "",
            "instrPixelUrl": None
        },
        "clickTrackingUrl": "",
        "creativeId": str(int(random.random() * 500000000000)),
        "header": head if head is not None else "",
        "imageUrl": main_img,
        "impressionUrl": "",
        "instrPixelUrl": None,
        "intentUrl": url if url is not None else "",
        "isAdult": False,
        "isDefaultAd": False,
        "miniDetails": {
            "__type": "ReturnedCustomAdMiniDetails:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
            "description": desc if desc is not None else "",
            "headline": title if title is not None else "",
            "imageUrl": sub_img,
            "type": None,
            "videoSourceUrl": None,
            "videoStreamUrl": None
        },
        "placementName": ad["placementName"],
        "reviewCount": 69,
        "stars": 5.0,
        "tilePosition": tile_pos if tile_pos is not None else 1,
        "ttlMinutes": str(TTL),
        "type": "TileAd"
    }

def featuredRotatorAd(ad, acc_text=None, main_img=None, url=None, logo_img=None):
    return {
        "__type": "ReturnedFeaturedRotatorAd:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
        "accessibilityText": acc_text if acc_text is not None else "Accessibility Text",
        "adId": str(int(random.random() * 500000000000)),
        "adRole": ad["adRole"],
        "adVersion": str(int(time.time())),
        "additionalAviaryMetadataJsonString": {
            "ThreePProviders": [],
            "adRequestId": generate_random_string(len("CwwqA7CDTsesFPg6mjzHmw")),
            "bidId": generate_random_string(len("5zqhDJeVssvGzPu7F.MxNA")),
            "creativeVariantConfig": None,
            "eventTrackers": {},
            "firstPartyReportingJSFileURL": "",
            "instrPixelUrl": None
        },
        "clickTrackingUrl": "",
        "creativeId": str(int(random.random() * 500000000000)),
        "imageUrl": main_img,
        "impressionUrl": "",
        "instrPixelUrl": None,
        "intentUrl": url if url is not None else "",
        "logoUrl": logo_img,
        "placementName": ad["placementName"],
        "ttlMinutes": str(TTL),
        "type": "FeaturedRotatorAd",
        "videoUrl": "https://d24hosivsxf1sb.cloudfront.net/transcode/47883cee-c1a7-4aba-88f8-3d475d8580a2/video%2Fmp4%2Fvideo_mp4_2000.mp4"
    }
