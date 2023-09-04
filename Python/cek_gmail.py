import requests

def search_email(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Email {email} terlibat dalam kebocoran data.")
        print("Layanan yang terkena dampak:")
        data = response.json()
        for entry in data:
            print(entry["Name"])
    elif response.status_code == 404:
        print(f"Email {email} tidak terlibat dalam kebocoran data.")
    else:
        print("Terjadi kesalahan saat mencari kebocoran data.")

email = "numannasyarmz11@gmail.com"  # Ganti dengan email Anda
search_email(email)
