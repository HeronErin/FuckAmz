# import json, os,time
# BASE = "research/bodys"

# f = open("KnownBods.log", "r")
# readNext = False
# lstrat = ""
# for line in f.read().split("\n"):
# 	if readNext:
# 		for ad in json.loads(line)["ads"]:
# 			if ad.get("intentUrl") is not None:

# 				_dir = os.path.join(BASE, ad["placementName"])
# 				print(_dir, ad["placementName"], ad.get("adId", "NO_ID"), "_", ad.get("adVersion", ""),".json")
# 				if not os.path.exists(_dir):
# 					os.mkdir(_dir)

# 				f = open(os.path.join(_dir, ad.get("adId", "NO_ID") + "_" + (ad.get("adVersion", "") or "")+".json"), "a")
# 				f.write(f"\n{lstrat}:\n\n")
# 				f.write(json.dumps(ad))
# 				f.close()

# 	if line == "+++++++++++++++++++++++++++++++++++++++":
# 		readNext = True
# 	else:
# 		readNext = False
# 	if line.startswith("Strat["):
# 		lstrat = line



# f.close()

import json, os,time
BASE = "research/ad_packets"
i = 0
f = open("KnownBods.log", "r")
while True:
	line1 = f.readline()
	if line1 == "": break
	if not line1.startswith("Strat["): continue

	l2l = len(l2:=json.loads(f.readline())["ads"])
	f.readline()
	l3l = len(l3:=json.loads(f.readline())["ads"])
	if l2l < l3l:
		print(l3)
	dir = os.path.join(BASE, str(i).zfill(4)+f"_{l2l}_{l3l}_{line1}" )
	os.mkdir(dir)
	f2 = open(os.path.join(dir, "req"), "w")
	f2.write(json.dumps(l2, sort_keys=True, indent=4))
	f2.close()

	f2 = open(os.path.join(dir, "res"), "w")
	f2.write(json.dumps(l3, sort_keys=True, indent=4))
	f2.close()

	for i2, ad in enumerate(l3):
		if ad['type'] is None: continue
		dir2 = os.path.join(dir, ad["placementName"])
		if not os.path.exists(dir2):
			os.mkdir(dir2)
		f2 = open(os.path.join(dir2, str(i2)+f"_{ad['type']}_{len(json.dumps(ad))}"), "w")
		f2.write(json.dumps(ad, sort_keys=True, indent=4))
		f2.close()


	i+=1


f.close()

