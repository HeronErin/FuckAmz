# Fuck Amz

The amazon fire sticks come with **WAY TOO MANY ADS**, let's have some fun with that. This is an extremely early alpha of me dicking around with the amazon fire stick ad servers to display arbitrary data and play arbitrary youtube videos from said ads.
Better yet, unlike Blockada and other alternatives, it only slows down your home screen, as other apps use libraries instead of the default OS HTTP/HTTPS client.  

![Banner ad](https://raw.githubusercontent.com/HeronErin/FuckAmz/main/screenshots/banner.png)

![Home screen](https://raw.githubusercontent.com/HeronErin/FuckAmz/main/screenshots/default.png)

![Full rotation ad screen](https://raw.githubusercontent.com/HeronErin/FuckAmz/main/screenshots/fullscreen_rotator.png)

![Custom tiles](https://raw.githubusercontent.com/HeronErin/FuckAmz/main/screenshots/tiles.png)


To install you do need some techincal knowlege. It requires running a seperate device as a proxy to intercept and modify the https packets, meaning you will need to install a custom Certificate Authority. (Note the data in certs/ is no-longer used)

Summery of installation:
1. Install mitmproxy
```bash
	pip install mitmproxy
```

2. Connect to your firestick with adb (this will be usefull for debuging later)
```bash
	adb connect 192.168.1.###  Replace with your firestick's ip
```

3. Add the mitmproxy Certificate Authority to your firestick's download folder
```bash
	adb push ~/.mitmproxy/mitmproxy-ca-cert.pem /storage/emulated/0/Download
```

4. Enter the Certificate Authority installation wizzard
```bash
adb shell am start -a "android.intent.action.VIEW" -d "file:///storage/emulated/0/Download/mitmproxy-ca-cert.pem" -t "application/x-x509-ca-cert"
```

5. Access the hidden debug menu to set up the network proxy with **YOUR** PC's ip
```bash
 adb shell am start com.amazon.ssm/com.amazon.ssm.ControlPanel
```

6. Run mitmproxy with this program
```bash
mitmdump -s xprox.py
# OR
mitmproxy -s xprox.py
# OR
mitmweb -s xprox.py
```