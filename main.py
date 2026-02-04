from google import genai
from google.genai import Client
from google.genai import types
from IPython.display import Markdown

client = genai.Client(api_key='AIzaSyA7pRWGhUvfbwJ9DRq-gbXiu7W8q1x4x5s')

mapel = input('Masukan Mata Pelajaran yang diinginkan: ')
topik = input('Masukan topik yang ingin dijadikan bahas: ')
jumlah = int(input('Masukan jumlah soal yang diinginkan: '))
lvl = input('Masukan tingkat kesulitan soal yang diinginkan(Mudah/Sedang/Sulit/HOTS): ')
content = f"Saya akan menghadapi ujian {mapel} dengan bab {topik}. Bisakah kamu membuat soal latihan untuk saya berjumlah {jumlah}. dengan tingkat kesuiltan {lvl}. buat tanpa kunci jawaban"
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=content,
    config=types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
    ),
)

def tampilkan_isi_respons(response):
    if hasattr(response, 'text') and response.text:
        hasil = response.text.strip()
    elif hasattr(response, 'candidates') and response.candidates:
        hasil = response.candidates[0].content.strip()
    else:
        hasil = str(response).strip()
    print("\n===== SOAL LATIHAN =====\n")
    print(hasil)
    print("\n=======================\n")
    return hasil

tampilkan_isi_respons(response)
soal = tampilkan_isi_respons(response)


p = input("apakah ingin menampilkan kunci jawaban? (y/n): ")
if p.lower() == 'y':
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"buatkan kunci jawaban dari soal sebelumnya: {soal}",
        config=types.GenerateContentConfig(
            temperature=0,
            top_p=0.95,
            top_k=20,
        ),
    )
    def tampilkan_isi_respons(response):
        if hasattr(response, 'text') and response.text:
            hasil = response.text.strip()
        elif hasattr(response, 'candidates') and response.candidates:
            hasil = response.candidates[0].content.strip()
        else:
            hasil = str(response).strip()
        print("\n===== KUNCI JAWABAN =====\n")
        print(hasil)
        print("\n=========================\n")
    tampilkan_isi_respons(response)
else:
    print("terima kasih telah menggunakan layanan ini.")



