"""
This script is an example of how to manipulate cookies both outgoing (requests)
and ingoing (responses). In particular, this script inserts a cookie (specified
in a json file) into every request (overwriting any existing cookie of the same
name), and removes cookies from every response that have a certain set of names
specified in the variable (set) FILTER_COOKIES.

Usage:

    mitmproxy -s examples/contrib/http_manipulate_cookies.py

Note:
    this was created as a response to SO post:
    https://stackoverflow.com/questions/55358072/cookie-manipulation-in-mitmproxy-requests-and-responses

"""
import json

from mitmproxy import http
import random, string, time
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
def inline(ad, acc_text = None, head=None, main_img = None, url=None, desc=None, headline=None, img=None):
    return {
        "__type": "ReturnedInlineAd:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
        "accessibilityText": "Accessibility Text" if acc_text is None else acc_text,
        "adId": str(int(random.random()*500000000000)),
        "adRole": ad["adRole"],
        "adVersion": str(int(time.time())),
        "additionalAviaryMetadataJsonString": {
            "ThreePProviders": [],
            "adRequestId": generate_random_string(len("Tju9V2SfcTht4Q9tVF0qAQ")),
            "bidId": generate_random_string(len("r0knCIbYuU06WXFhnfHE1A")),
            "creativeVariantConfig": None,
            "eventTrackers": {
                "miniDetailsHover": [
                    {
                        "params": {
                            "name": "miniDetailsHover",
                            "variations": "[[\"pfm\",\"placementName\"]]"
                        },
                        "type": "pmet"
                    }
                ],
                "selectionEnter": [
                    {
                        "params": {
                            "name": "selectionEnter",
                            "variations": "[[\"pfm\",\"placementName\"]]"
                        },
                        "type": "pmet"
                    }
                ],
                "selectionExit": [
                    {
                        "params": {
                            "name": "selectionExit",
                            "variations": "[[\"pfm\",\"placementName\"]]"
                        },
                        "type": "pmet"
                    }
                ]
            },
            "firstPartyReportingJSFileURL": "",
            "instrPixelUrl": None
        },
        "clickTrackingUrl": "",
        "creativeId": str(int(random.random()*500000000000)),
        "header": "" if head is None else head,
        "imageUrl": "invalid.jpg" if main_img is None else main_img,
        "impressionUrl": "",
        "instrPixelUrl": None,
        "intentUrl": url,
        "miniDetails": {
            "__type": "ReturnedCustomAdMiniDetails:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
            "description": desc,
            "headline": headline,
            "imageUrl": "invalid.jpg" if img is None else img,
            "type": "CustomAdMiniDetails",
            "videoSourceUrl": None,
            "videoStreamUrl": None
        },
        "placementName": ad["placementName"],
        "ttlMinutes": "1",
        "type": "InlineAd"
    }

def titleAd(ad, main_img=None, sub_img=None, head=None, desc=None, title=None, url=None, acc_text=None):
    return {
          "__type": "ReturnedTileAd:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
          "accessibilityText": "Accessibility Text" if acc_text is None else acc_text,
          "adId": str(int(random.random()*500000000000)),
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
          "creativeId": str(int(random.random()*500000000000)),
          "header": "" if head is None else head,
          "imageUrl": "invalid.jpg" if main_img is None else main_img,
          "impressionUrl": "",
          "instrPixelUrl": None,
          "intentUrl": "" if url is None else url,
          "isAdult": False,
          "isDefaultAd": False,
          "miniDetails": {
            "__type": "ReturnedCustomAdMiniDetails:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
            "description": "" if desc is None else desc,
            "headline": "" if title is None else title,
            "imageUrl": "invalid.jpg" if sub_img is None else sub_img,
            "type": None,
            "videoSourceUrl": None,
            "videoStreamUrl": None
          },
          "placementName": ad["placementName"],
          "reviewCount": 69,
          "stars": 5.0,
          "tilePosition": 5,
          "ttlMinutes": "1",
          "type": "TileAd"
        }

def featureRot(ad, main_img=None):
    return {
      "__type": "ReturnedFeaturedRotatorAd:http://internal.amazon.com/coral/com.amazon.dadetaviary/",
      "accessibilityText": "Accessibility Text",
      "adId": str(int(random.random()*500000000000)),
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
      "creativeId": str(int(random.random()*500000000000)),
      "imageUrl": "https://m.media-amazon.com/images/I/81bXhP91J1L.jpg",
      "impressionUrl": "",
      "instrPixelUrl": None,
      "intentUrl": "amzn://com.amazon.tv.subscription/offer?refMarker=ktb_3p_nog_c&benefitTypeId=hbomaxus&sourceTag=LAUNCHER_MOVIES_FR_3",
      "logoUrl": "https://m.media-amazon.com/images/I/31PcgTO-P1L.png",
      "placementName": ad["placementName"],
      "ttlMinutes": "1",
      "type": "FeaturedRotatorAd",
      "videoUrl": "https://d24hosivsxf1sb.cloudfront.net/transcode/47883cee-c1a7-4aba-88f8-3d475d8580a2/video%2Fmp4%2Fvideo_mp4_2000.mp4"
    }


def response(flow: http.HTTPFlow) -> None:
    if flow.response and flow.response.content:

        if "aviary.amazon.com" == flow.request.headers.get("host"):
            strat = flow.request.headers.get("x-amzn-blackbird-refresh-strategy")
            if strat is None:
                f = open("errors.log", "a")
                f.write("Found a request without strat\n")
                f.close()
                return
            f = open("KnownBods.log", "a")
            f.write(f"\n\nStrat[{strat}]:\n")
            f.write(flow.request.text)
            f.write(f"\n+++++++++++++++++++++++++++++++++++++++\n")
            f.write(flow.response.text)
            f.close()
            flow.response.text=""

            jso = json.loads(flow.request.text)
            ads = []
            print("INTERCEPTED")
            if strat == "PreloadRefreshStrategy":
                for ad in jso["ads"]:
                    ads.append(   getNulledAd(ad)     )
            else:
                for ad in jso["ads"]:
                    if ad["placementName"] in ["Launcher.Home.Default.Rotational", "Gordon.Live.Default.Inline"]:
                        data = None
                        if ad["placementName"] == "Launcher.Home.Default.Rotational":
                            data = titleAd(ad,
                                head="Rarararaar", 
                                headline = "It is happening",
                                desc = "The Revolution has begun!!!!",
                                url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                                main_img="https://raw.githubusercontent.com/HeronErin/FuckAmz/main/test_imgs/title_ad_rot.jpg")
                        else:
                            data = inline(ad, 
                                head="Owo", 
                                headline = "Things are happening",
                                desc = "The Revolution has begun!!!!",
                                url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                                main_img="https://raw.githubusercontent.com/HeronErin/FuckAmz/main/test_imgs/inline_ad.jpg", 
                                img="https://raw.githubusercontent.com/HeronErin/FuckAmz/main/test_imgs/inine_background.jpg")
                        ads.append(data)
                    else:
                        ads.append(getNulledAd(ad))

            flow.response.text = json.dumps({"ads": ads})

        elif "ktpx.amazon.com/mb/data" in flow.request.url:
            flow.response.text = ""

        #     data = {
        #         "type": "com.amazon.mediabrowse.movie@1",
        #         "text": "Saw 5 is for loosers",
        #         "ref": "[reftype=mb/item,refid=aiv_us|B00P03BPMY|PFXojNLpiZxvD1UM2hvso2FkdwImy4dkHAuoPXigiAk=]",
        #         "ttl": 1229,
        #         "csIdSource": "ASIN",
        #         "csId": "B00P03BPMY",
        #         "image": None,
        #         "qualifiedImage": {
        #             "baseUrl": "https://m.media-amazon.com/images/S/pv-target-images/98789f41405313fd78e2f7d81e05cbec765912d2c74ce552e689ed0d0ed1895e._QL100_.jpg",
        #             "badgeString": None,
        #             "width": 1920,
        #             "height": 2560,
        #             "isMsa": True
        #         },
        #         "widescreenImage": {
        #             "baseUrl": "https://m.media-amazon.com/images/S/pv-target-images/a7d34718a12e533af1254b06e64d25ad30f14436b3b71e647b8e469106e4aeca._QL100_.jpg",
        #             "badgeString": None,
        #             "width": 1920,
        #             "height": 1080,
        #             "isMsa": True
        #         },
        #         "backgroundImage": "https://m.media-amazon.com/images/S/pv-target-images/494ec7ba35783b27862dddd09d73e7dbe6174fb9a664b30884ea0a776503b287._QL100_.jpg",
        #         "titleImage": None,
        #         "treatments": None,
        #         "headerText": None,
        #         "description": "In the fifth (lol) installment of the SAW franchise, Detective Hoffman is seemingly the last person alive to carry on the Jigsaw legacy.",
        #         "vORef": "[reftype=mb/item/viewingoptions,refid=aiv_us|B00P03BPMY|PFXojNLpiZxvD1UM2hvso2FkdwImy4dkHAuoPXigiAk=]",
        #         "runtime": 128,
        #         "runtimeSecs": 7680,
        #         "availableOn": [
        #             {
        #                 "provider": "aiv",
        #                 "quality": []
        #             }
        #         ],
        #         "rvwRef": None,
        #         "simRef": "[reftype=related/video,refid=aiv_us|B00P03BPMY|PFXojNLpiZxvD1UM2hvso2FkdwImy4dkHAuoPXigiAk=]",
        #         "subtitle": None,
        #         "studio": "currentTime=1700896946070",
        #         "genreList": [
        #             "Thriller",
        #             "Horror"
        #         ],
        #         "additionalContent": None,
        #         "longDescription": "BONUS FEATURES INCLUDED WITH PURCHASE. In the fifth installment of the SAW franchise, Detective Hoffman is seemingly the last person alive to carry on the Jigsaw legacy. But when his secret is threatened, Hoffman must go on the hunt to eliminate all loose ends.",
        #         "releaseDate": "2008-10-24T00:00:00.000+0000",
        #         "contentRating": "G",
        #         "enforcementRating": "8+",
        #         "releaseYear": 2008,
        #         "metacriticScore": None,
        #         "metacriticScoreCount": None,
        #         "nURef": None,
        #         "smartlistItemId": "smart",
        #         "amazonRating": 9,
        #         "amazonRatingCount": 2011,
        #         "imdbRating": "5.8",
        #         "imdbRatingCount": 135009,
        #         "contributors": "[reftype=mb/item/contrib,refid=aiv_us|B00P03BPMY|PFXojNLpiZxvD1UM2hvso2FkdwImy4dkHAuoPXigiAk=]",
        #         "aivSdkId": "B00P1FJ4FG",
        #         "aivGti": "amzn1.dv.gti.60a9f758-eeb5-59e5-65e5-f3cedcd90040",
        #         "topActors": [
        #             "Scott Patterson",
        #             "Costas Mandylor",
        #             "Tobin Bell",
        #             "Betsy Russell",
        #             "Julie Benz"
        #         ],
        #         "topDirectors": [
        #             "David Hackl"
        #         ],
        #         "hasXrayData": False,
        #         "descriptionHeader": None,
        #         "attributes": None,
        #         "previewVideoUrl": None,
        #         "previewVideoId": None,
        #         "previewVideoProvider": None,
        #         "displayAspectRatio": None,
        #         "badges": None,
        #         "adaptivePreviewVideoUrl": None,
        #         "metaData": None,
        #         "tags": None
        #     }



        #     flow.response.text = json.dumps(
        #         {"type":"com.amazon.mediabrowse.response@1","response":[
        #             data
        #         ]}
        #         )

    # print(flow.request.headers.get("host"))