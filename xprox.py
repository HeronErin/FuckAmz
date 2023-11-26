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
from aviary import HandleAviary, getNulledAd


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
                HandleAviary(jso["ads"], flow)

        # elif "ktpx.amazon.com/mb/data" in flow.request.url:
        #     f = open(f"research/data/{time.ctime()}.json", "w")
        #     f.write(flow.request.headers.get("x-amzn-accept-type", ""))
        #     f.write("\n\n\n")
        #     f.write(flow.request.text)
        #     f.write("\n\n\n")
        #     f.write(flow.response.text)
        #     f.close()

        #     flow.response.status_code = 404
        #     flow.response.text = ""


    # print(flow.request.headers.get("host"))