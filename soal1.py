print("******kredit keaktivan mahasiswa******")
print("STUDENT ACTIVITIES CREDIT")
print("1.Menambahkan Kegiatan")
print("2. menampilkan Jumlah poin")
print("3.keluar")
print("---------------------------------")

activity_data = []

def add_activity(activity, date, category, points):
    activity_data.append({
        "activity": activity,
        "date": date,
        "category": category,
        "points": points
    })

def main():
    while True:
        action = int(input("Silahkan masukkan Pilihan Anda:"))

        if action == 1:
            activity = input("nama kegiatan: ")
            date = input("Tanggal kegiatan: ")
            print("pilihan Kategori kegiatan:")
            print("prestasi")
            print("- organisasi")
            print("- kepanitiaan")
            print("- rekognisi")

            category = input("Masukkan kategori Pilihan kategori kegiatan: ")
            points = int(input("Masukkan jumlah poin kegiatan: "))
            print("kegiatan berhasil ditambahkan..")
            existing_activity = next((data for data in activity_data if data["activity"] == activity), None)
            if existing_activity:
                print("Kegiatan sudah pernah diinput. Tidak boleh double claim!")
            else:
                add_activity(activity, date, category, points)
            
           
        elif action == 2 :
            print("Nama Kegiatan       Tanggal      Kategori     Poin")
           
            total_points = 0
            for data in activity_data:                
                print(print(f"{data['activity']} ({data['date']}): {data['category']} poin ({data['points']})"))
                total_points += data['points']
            print(f"Jumlah Poin Total      : {total_points}")
            break
        else:
            print("sistem berhenti...")

if __name__ == '__main__':
    main()