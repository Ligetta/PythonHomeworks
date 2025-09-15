

def vardnicuFormatetajs(vardnica):
    for atslēga, vērtība in vardnica.items():
        print(f"{atslēga}: {vērtība}")

parbaude = {"Vārds": "Adīna",
           "Vecums": 21}

vardnicuFormatetajs(parbaude)