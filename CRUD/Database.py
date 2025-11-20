from . import Input

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "date_created": "YYYY-MM-DD",
    "nama": 255*" ",
    "tanggal_lahir": "YYYY-MM-DD",
    "umur": "XX",
    "jenis_kelamin": "X",
    "posisi": 255*" ",
    "skor_psikotest": "XX.XXXXXXXXXXXXXXXXXXXX",
    "skor_teknikal": "XX.XXXXXXXXXXXXXXXXXXXX",
    "skor_wawancara": "XX.XXXXXXXXXXXXXXXXXXXX",
    "kecocokan": "XX.XXXXXXXXXXXXXXXXXXXX",    
}

def init_console():
                
    try:
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init done")

    except:
        print("Database tidak ditemukan, membuat database baru...\n")
        Input.create_data()
        print("Database berhasil dibuat dengan data pertama.\n")