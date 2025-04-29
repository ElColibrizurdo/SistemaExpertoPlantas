import requests

name = "Capnodium coffeae"
url_match = f"https://api.gbif.org/v1/species/match?name={name.replace(' ', '%20')}"
res = requests.get(url_match)
taxon_key = res.json().get("usageKey")

if taxon_key:
    url_occ = f"https://api.gbif.org/v1/occurrence/search?taxon_key={taxon_key}"
    print(url_occ)
    occ_res = requests.get(url_occ)
    data = occ_res.json()
    print("Registros encontrados:", len(data.get("results", [])))
    for r in data.get("results", []):
        print(r["scientificName"], "-", r.get("country"), "-", r.get("eventDate"))
else:
    print("Taxon no encontrada")
