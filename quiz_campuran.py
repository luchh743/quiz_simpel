def quiz_pilihan_ganda():
    print("=== BAGIAN 1: PILIHAN GANDA ===")
    score = 0

    soal_pg = [
        {
            "pertanyaan": "1. Siapa penemu bahasa Python?",
            "pilihan": ["A. James Gosling", "B. Guido van Rossum", "C. Elon Musk", "D. Bill Gates"],
            "jawaban": "b"
        },
        {
            "pertanyaan": "2. Tahun berapa Python pertama kali dirilis?",
            "pilihan": ["A. 2001", "B. 1989", "C. 1991", "D. 2000"],
            "jawaban": "c"
        },
        {
            "pertanyaan": "3. Apa ekstensi file Python?",
            "pilihan": ["A. .py", "B. .pt", "C. .js", "D. .exe"],
            "jawaban": "a"
        },
        {
            "pertanyaan": "4. Perintah untuk menampilkan teks di Python adalah?",
            "pilihan": ["A. echo", "B. say", "C. print", "D. output"],
            "jawaban": "c"
        },
        {
            "pertanyaan": "5. Tipe data untuk bilangan desimal adalah?",
            "pilihan": ["A. int", "B. str", "C. bool", "D. float"],
            "jawaban": "d"
        },
    ]

    for s in soal_pg:
        print("\n" + s["pertanyaan"])
        for pilihan in s["pilihan"]:
            print(pilihan)
        jawab = input("Jawaban kamu (a/b/c/d): ").lower()

        if jawab == s["jawaban"]:
            print("✅ Benar!")
            score += 1
        else:
            print(f"❌ Salah! Jawaban yang benar adalah '{s['jawaban'].upper()}'")

    print(f"\nSkor pilihan ganda kamu: {score}/5")
    return score


def quiz_essai():
    print("\n=== BAGIAN 2: ESSAI ===")
    score = 0

    soal_essai = [
        {
            "pertanyaan": "1. Jelaskan secara singkat apa itu Python!",
            "kunci": ["bahasa pemrograman", "mudah dibaca"]
        },
        {
            "pertanyaan": "2. Sebutkan satu kegunaan Python dalam dunia nyata!",
            "kunci": ["data", "web", "ai", "otomasi"]
        },
        {
            "pertanyaan": "3. Apa kelebihan Python dibanding bahasa lain?",
            "kunci": ["mudah", "banyak library", "populer"]
        },
    ]

    for s in soal_essai:
        print("\n" + s["pertanyaan"])
        jawab = input("Jawaban kamu: ").lower()

        benar = False
        for kata in s["kunci"]:
            if kata in jawab:
                benar = True
                break

        if benar:
            print("✅ Bagus! Jawaban kamu sesuai.")
            score += 1
        else:
            print("❌ Belum tepat, tetap semangat!")

    print(f"\nSkor essai kamu: {score}/3")
    return score


def main():
    while True:
        print("\n=== QUIZ SIMPEL PY ===")
        print("Ketik 'exit' kapan aja buat keluar.\n")

        skor_pg = quiz_pilihan_ganda()
        skor_essai = quiz_essai()

        total_skor = skor_pg + skor_essai
        print("\n=== HASIL AKHIR ===")
        print(f"Total skor kamu: {total_skor}/8")

        nilai = (total_skor / 8) * 100
        print(f"Nilai kamu: {nilai:.0f}")

        if nilai == 100:
            print(" gacorr🔥🔥, nilai : A+.")
        elif nilai >= 75:
            print(" sigmaa😎😎,nilai kamu : B+.")
        elif nilai >= 50:
            print(" mid🙂🙂,nilai kamu : C+.")
        else:
            print(" losser😅😅,nilai kamu : D.")

        ulang = input("\nMau main lagi? (y/n): ").lower()
        if ulang != "y":
            print("Terima kasih udah main! 👋")
            break


if __name__ == "__main__":
     main()