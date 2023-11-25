import json, os,time
BASE = "research/bodys"

f = open("KnownBods.log", "r")
readNext = False
lstrat = ""
for line in f.read().split("\n"):
	if readNext:
		for ad in json.loads(line)["ads"]:
			if ad.get("intentUrl") is not None:

				_dir = os.path.join(BASE, ad["placementName"])
				print(_dir, ad["placementName"], ad.get("adId", "NO_ID"), "_", ad.get("adVersion", ""),".json")
				if not os.path.exists(_dir):
					os.mkdir(_dir)

				f = open(os.path.join(_dir, ad.get("adId", "NO_ID") + "_" + (ad.get("adVersion", "") or "")+".json"), "a")
				f.write(f"\n{lstrat}:\n\n")
				f.write(json.dumps(ad))
				f.close()

	if line == "+++++++++++++++++++++++++++++++++++++++":
		readNext = True
	else:
		readNext = False
	if line.startswith("Strat["):
		lstrat = line



f.close()
