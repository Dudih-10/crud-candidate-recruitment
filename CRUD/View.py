from . import Input

def read_console():
    data_file = Input.read()

    print("\n===================================================================================== DATA REKRUTMEN ====================================================================================\n")
    print(f"{'No':<5} | {'ID':<7} | {'Tanggal Input':<15} | {'Nama':<40} | {'Tanggal Lahir':<12} | {'Umur':<4} | {'JK':<3} | {'Posisi':<30} | {'Psikotes':<8} | {'Teknikal':<8} | {'Wawancara':<9} | {'Kecocokan':<9}")
    print("-"*185)

    for index, line in enumerate(data_file):
        fields = [f.strip() for f in line.split(",")]
        # pastikan ada 11 field (jaga safety)
        while len(fields) < 11:
            fields.append("")

        print(f"{index+1:<5} | {fields[0]:<7} | {fields[1]:<15} | {fields[2]:<40} | {fields[3]:<12}  | {fields[4]:<4} | {fields[5]:<3} | {fields[6]:<30} | {fields[7]:<8} | {fields[8]:<8} | {fields[9]:<9} | {fields[10] + ' %':<9} ")

    print("\n=========================================================================================================================================================================================\n")


def create_console():
    print("\n==================== CREATE DATA REKRUTMEN ====================\n")
    Input.create_data()
    print("\n==================== DATA BERHASIL DITAMBAHKAN ====================\n")


def update_console():
    print("Choose data to update by entering the (No)")
    read_console()

    # pilih nomor baris (No)
    while True:
        try:
            no = int(input("Enter nomor (No) to update: "))
            data_line = Input.read(index=no)
            if data_line:
                break
            else:
                print("Please enter a valid nomor (No) from the database.\n")
        except ValueError:
            print("Masukkan angka valid untuk nomor (No).\n")

    fields = [f.strip() for f in data_line.split(",")]
    # fields: [pk, date_created, nama, tanggal_lahir, umur, jk, posisi, skor_psikotest, skor_teknikal, skor_wawancara, kecocokan]
    pk = fields[0]
    nama = fields[2]
    tanggal_lahir = fields[3]
    jenis_kelamin = fields[5]
    posisi = fields[6]
    skor_psikotes = fields[7]
    skor_teknikal = fields[8]
    skor_wawancara = fields[9]

    while True:
        print("\nSilahkan pilih field yang ingin diupdate:")
        print(f"1. Nama\t\t\t: {nama}")
        print(f"2. Tanggal Lahir\t: {tanggal_lahir}")
        print(f"3. Jenis Kelamin\t: {jenis_kelamin}")
        print(f"4. Posisi\t\t: {posisi}")
        print(f"5. Skor Psikotes\t: {skor_psikotes}")
        print(f"6. Skor Teknikal\t: {skor_teknikal}")
        print(f"7. Skor Wawancara\t: {skor_wawancara}\n")

        field_option = input("Masukan opsi (1-7): ").strip()
        match field_option:
            case "1":
                nama = input("Nama Baru\t: ").strip()
            case "2":
                tanggal_lahir = Input.input_tanggal_lahir()
            case "3":
                jenis_kelamin = Input.input_jenis_kelamin()
            case "4":
                posisi = input("Posisi Baru\t: ").strip()
            case "5":
                skor_psikotes = Input.input_skor("Skor Psikotes Baru\t: ")
            case "6":
                skor_teknikal = Input.input_skor("Skor Teknikal Baru\t: ")
            case "7":
                skor_wawancara = Input.input_skor("Skor Wawancara Baru\t: ")
            case _:
                print("Opsi tidak valid, silahkan coba lagi.\n")

        is_done = input("Apakah sudah selesai mengupdate data (y/n)? ").strip().lower()
        if is_done == "y":
            break

    # Panggil update_data dengan PK sebagai index
    success = Input.update_data(
        index=pk,
        nama=nama,
        tanggal_lahir=tanggal_lahir,
        jenis_kelamin=jenis_kelamin,
        posisi=posisi,
        skor_psikotes=skor_psikotes,
        skor_teknikal=skor_teknikal,
        skor_wawancara=skor_wawancara
    )

    if success:
        print("\n==================== DATA BERHASIL DIUPDATE ====================\n")
    else:
        print("\nGagal mengupdate data.\n")
        
def delete_console():
    print("Choose data to delete by entering the (No)")
    read_console()

    # pilih nomor baris (No)
    while True:
        no = int(input("Enter nomor (No) to delete: "))
        data_line = Input.read(index=no)
        if data_line:
            fields = [f.strip() for f in data_line.split(",")]
            # fields: [pk, date_created, nama, tanggal_lahir, umur, jk, posisi, skor_psikotest, skor_teknikal, skor_wawancara, kecocokan]
            pk = fields[0]
            nama = fields[2]
            tanggal_lahir = fields[3]
            jenis_kelamin = fields[5]
            posisi = fields[6]
            skor_psikotes = fields[7]
            skor_teknikal = fields[8]
            skor_wawancara = fields[9]
                
            print("\nSilahkan pilih field yang ingin diupdate:")
            print(f"1. Nama\t\t\t: {nama}")
            print(f"2. Tanggal Lahir\t: {tanggal_lahir}")
            print(f"3. Jenis Kelamin\t: {jenis_kelamin}")
            print(f"4. Posisi\t\t: {posisi}")
            print(f"5. Skor Psikotes\t: {skor_psikotes}")
            print(f"6. Skor Teknikal\t: {skor_teknikal}")
            print(f"7. Skor Wawancara\t: {skor_wawancara}\n")
            is_confirm = input(f"Apakah anda yakin ingin menghapus data dengan nama '{nama}' (y/n)? ").strip().lower()
            if is_confirm == "y" or is_confirm == "Y":
                Input.delete_data(pk)
                break
        else:
            print("Please enter a valid nomor (No) from the database")
            