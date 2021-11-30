kody = {"Kielce": 25-900,
        "Warszawa": 00-900,
        "Lublin": 34-200,
        }

print(kody["Kielce"])
print("Lublin" in kody)
print(-875 in kody.values())
print(kody.keys())
print(kody.values())
kody["Gdynia"] = 87-800
kody[123] = "0000"
kody.pop("Kielce")
print(kody)

