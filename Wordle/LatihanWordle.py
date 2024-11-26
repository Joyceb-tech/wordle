import random

def load_words():
    # Daftar kata-kata lima huruf, bisa diperluas
    return ["tebak", "santai", "nyala", "pohon", "kunci", "lampu", "murah"]

def check_guess(word, guess):
    result = []
    for w, g in zip(word, guess):
        if g == w:
            result.append("🟩")  # Huruf benar dan posisi benar
        elif g in word:
            result.append("🟨")  # Huruf benar tapi posisi salah
        else:
            result.append("⬜")  # Huruf salah
    return "".join(result)

def play_wordle():
    words = load_words()
    word_to_guess = random.choice(words)
    attempts = 6  # Jumlah maksimum tebakan
    print("Selamat datang di Wordle!")
    print(f"Tebak kata lima huruf dalam {attempts} percobaan.\n")

    for attempt in range(1, attempts + 1):
        guess = input(f"Percobaan {attempt}/{attempts}: ").lower()
        
        if len(guess) != 5:
            print("Masukkan kata lima huruf!")
            continue

        if guess not in words:
            print("Kata tidak ditemukan dalam daftar! Coba lagi.")
            continue

        result = check_guess(word_to_guess, guess)
        print("Hasil:", result)

        if guess == word_to_guess:
            print(f"Selamat! Anda berhasil menebak kata dalam {attempt} percobaan!")
            break
    else:
        print(f"Sayang sekali! Kata yang benar adalah '{word_to_guess}'.")

if _name_ == "_main_":
    play_wordle()