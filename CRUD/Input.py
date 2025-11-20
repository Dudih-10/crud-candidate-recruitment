import datetime as dt
from . import Database as db
import random
import os

# ----------------------
# Utility I/O & helpers
# ----------------------

def read(index: int = None):
    """
    Jika index diberikan (int), mengembalikan baris ke-index (1-based).
    Jika tidak, mengembalikan list semua baris (tanpa newline), atau [] jika file tidak ada.
    """
    try:
        with open(db.DB_NAME, "r", encoding="utf-8") as file:
            lines = [line.rstrip("\n") for line in file.readlines()]
    except FileNotFoundError:
        return []

    if index is None:
        return lines

    # index diberikan sebagai nomor baris (1-based)
    if isinstance(index, int):
        idx0 = index - 1
        if 0 <= idx0 < len(lines):
            return lines[idx0]
        else:
            return None
    else:
        # fallback: jika index bukan int, kembalikan None
        return None


def write_all(data_list):
    """Overwrite seluruh file dengan list of lines (tanpa newline)."""
    with open(db.DB_NAME, "w", encoding="utf-8") as file:
        for line in data_list:
            file.write(line + "\n")


# ----------------------
# Input helpers
# ----------------------

def input_angka(prompt, min_val, max_val):
    while True:
        try:
            angka = int(input(prompt))
            if min_val <= angka <= max_val:
                return angka
            else:
                print(f"Input harus antara {min_val} - {max_val}. Coba lagi.\n")
        except ValueError:
            print("Input harus berupa angka. Silahkan coba lagi.\n")


def input_tanggal_lahir():
    """
    Mengembalikan string tanggal (ISO) 'YYYY-MM-DD'.
    Validasi tanggal termasuk tidak boleh >= hari ini.
    """
    print("Masukkan Tanggal Lahir")
    tgl = input_angka("Tanggal\t\t\t: ", 1, 31)
    bln = input_angka("Bulan\t\t\t: ", 1, 12)
    thn = input_angka("Tahun\t\t\t: ", 1900, dt.date.today().year)

    try:
        tanggal_lahir = dt.date(thn, bln, tgl)
    except ValueError:
        print("\nTanggal tidak valid (contoh: 30 Februari). Coba lagi!\n")
        return input_tanggal_lahir()

    if tanggal_lahir >= dt.date.today():
        print("\nTanggal lahir tidak boleh lebih besar dari hari ini.\n")
        return input_tanggal_lahir()

    return tanggal_lahir.isoformat()


def today_date():
    """Mengembalikan string ISO YYYY-MM-DD untuk tanggal hari ini."""
    return dt.date.today().isoformat()


def input_jenis_kelamin():
    while True:
        jenis_kelamin = input("Jenis Kelamin (L/P)\t: ").upper().strip()
        if jenis_kelamin in ['L', 'P']:
            return jenis_kelamin
        else:
            print("Input tidak valid. Masukkan 'L' untuk Laki-laki atau 'P' untuk Perempuan.\n")


def input_skor(prompt):
    while True:
        try:
            skor = float(input(prompt))
            if 0 <= skor <= 100:
                # Simpan sebagai string dengan minimal 1 desimal agar format konsisten (misal "80.0")
                return f"{skor:.1f}"
            else:
                print("Skor harus antara 0 - 100. Coba lagi.\n")
        except ValueError:
            print("Input harus berupa angka. Silahkan coba lagi.\n")


def hitung_umur(tanggal_lahir_iso: str) -> int:
    """Terima tanggal_lahir dalam string ISO 'YYYY-MM-DD', kembalikan umur (tahun, int)."""
    tgl = dt.datetime.strptime(tanggal_lahir_iso, "%Y-%m-%d").date()
    hari_ini = dt.date.today()
    umur = hari_ini.year - tgl.year - ((hari_ini.month, hari_ini.day) < (tgl.month, tgl.day))
    return umur


# ----------------------
# CRUD
# ----------------------

def create_data():
    """Menambahkan satu record ke file DB (append). Format 11 kolom."""
    nama = input("Nama\t\t\t: ").strip()
    tanggal_lahir = input_tanggal_lahir()          # ISO string
    tanggal_input = today_date()                   # ISO string
    umur = hitung_umur(tanggal_lahir)
    jenis_kelamin = input_jenis_kelamin()
    posisi = input("Posisi\t\t\t: ").strip()
    skor_psikotes = input_skor("Skor Psikotes\t\t: ")
    skor_teknikal = input_skor("Skor Teknikal\t\t: ")
    skor_wawancara = input_skor("Skor Wawancara\t\t: ")

    kecocokan = (float(skor_psikotes) + float(skor_teknikal) + float(skor_wawancara)) / 3.0

    pk = str(random.randint(100000, 999999))

    data_str = (
        f"{pk}, {tanggal_input}, {nama}, {tanggal_lahir}, {umur}, "
        f"{jenis_kelamin}, {posisi}, {skor_psikotes}, {skor_teknikal}, {skor_wawancara}, {kecocokan:.2f}"
    )

    try:
        with open(db.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str + "\n")
    except Exception as e:
        print("Gagal menambahkan data ke database. Periksa izin penulisan file.\n")
        print("Error:", e)


def update_data(
    index,                # pk (string) yang diambil dari field[0]
    nama,
    tanggal_lahir,        # ISO string atau dt.date? Kita asumsikan ISO string (konsisten dengan input_tanggal_lahir)
    jenis_kelamin,
    posisi,
    skor_psikotes,
    skor_teknikal,
    skor_wawancara
):
    """
    Update record yang memiliki PK == index.
    Membaca seluruh file, rebuild baris yang diupdate, lalu tulis ulang file.
    """
    all_lines = read()
    if not all_lines:
        print("Database kosong atau tidak ditemukan. Tidak ada yang diupdate.")
        return False

    updated_list = []
    found = False

    for line in all_lines:
        fields = [f.strip() for f in line.split(",")]
        pk_field = fields[0]

        if pk_field == str(index):
            # gunakan tanggal_input lama (fields[1]) agar tidak berubah
            tanggal_input = fields[1]
            umur = hitung_umur(tanggal_lahir)
            kecocokan = (float(skor_psikotes) + float(skor_teknikal) + float(skor_wawancara)) / 3.0

            new_line = (
                f"{pk_field}, {tanggal_input}, {nama.strip()}, {tanggal_lahir.strip()}, {umur}, "
                f"{jenis_kelamin.strip()}, {posisi.strip()}, {float(skor_psikotes):.1f}, {float(skor_teknikal):.1f}, "
                f"{float(skor_wawancara):.1f}, {kecocokan:.2f}"
            )
            updated_list.append(new_line)
            found = True
        else:
            # pastikan baris lain tetap bersih (strip tiap field lalu gabung lagi agar konsisten spacing)
            cleaned = ", ".join([f.strip() for f in fields])
            updated_list.append(cleaned)

    if not found:
        print("PK tidak ditemukan. Tidak ada yang diupdate.")
        return False

    write_all(updated_list)
    return True

def delete_data(pk):
    temp_file_name = "data_tempt.txt"

    try:
        with open(db.DB_NAME, "r", encoding="utf-8") as file, \
             open(temp_file_name, "w", encoding="utf-8") as temp_file:

            for line in file:
                file_pk = line.split(",")[0].strip()  # Ambil pk di baris

                # Jika pk sama -> lewati baris (hapus)
                if file_pk == pk:
                    continue

                temp_file.write(line)

    except Exception as e:
        print(f"Database error: {e}")
        return

    os.replace(temp_file_name, db.DB_NAME)
