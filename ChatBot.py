# Daftar ucapan yang bisa dimengerti chatbot
ucapan_pengguna = ["halo", "apa kabar", "siapa kamu", "terima kasih", "sampai jumpa"]
jawaban_chatbot = ["Halo! Ada yang bisa saya bantu?", "Saya baik-baik saja, terima kasih. Kamu sendiri bagaimana?", "Saya Bard, chatbot yang dibuat dengan Python.", "Sama-sama. Senang bisa membantu!", "Sampai jumpa lagi!"]

# Menjalankan loop percakapan
while True:
  # Mendapatkan input dari pengguna
  input_pengguna = input("Masukkan pesan: ").lower()

  # Menemukan jawaban yang sesuai
  for i in range(len(ucapan_pengguna)):
    if ucapan_pengguna[i] in input_pengguna:
      jawaban = jawaban_chatbot[i]
      break
  else:
    jawaban = "Maaf, saya tidak mengerti maksud kamu."

  # Menampilkan jawaban chatbot
  print(f"Chatbot: {jawaban}")

  # Memeriksa apakah pengguna ingin mengakhiri percakapan
  if input_pengguna == "bye":
    print(f"Chatbot: Sampai jumpa lagi!")
    exit(0)
  elif input_pengguna == "exit":
    print(f"Chatbot: Sampai jumpa lagi!")
    exit(0)
