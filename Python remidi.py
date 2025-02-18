import random
from datetime import datetime

# Class untuk Step Skincare
class SkincareStep:
    def __init__(self, name):
        self.name = name
        self.id = random.randint(1000, 9999)
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "[✓]" if self.completed else "[ ]"
        return f"{status} {self.name} (ID: {self.id}, Created: {self.created_at})"

# Class untuk mengelola skincare routine
class SkincareRoutine:
    def __init__(self):
        self.steps = []

    def add_step(self, name):
        step = SkincareStep(name)
        self.steps.append(step)
        print(f"Langkah '{name}' berhasil ditambahkan!")

    def show_steps(self):
        if not self.steps:
            print("Tidak ada langkah skincare!")
        else:
            for step in self.steps:
                print(step)

    def complete_step(self, step_id):
        for step in self.steps:
            if step.id == step_id:
                step.mark_completed()
                print(f"Langkah '{step.name}' ditandai sebagai selesai!")
                return
        print("Langkah tidak ditemukan!")

    def delete_step(self, step_id):
        for step in self.steps:
            if step.id == step_id:
                self.steps.remove(step)
                print(f"Langkah '{step.name}' dihapus!")
                return
        print("Langkah tidak ditemukan!")

# Program Utama
def main():
    routine = SkincareRoutine()
    while True:
        print("\n=== Skincare Routine Harian ===")
        print("1. Tambah Langkah Skincare")
        print("2. Lihat Langkah Skincare")
        print("3. Tandai Langkah Selesai")
        print("4. Hapus Langkah Skincare")
        print("5. Keluar")

        choice = input("Pilih opsi: ")

        if choice == "1":
            name = input("Masukkan langkah skincare: ")
            routine.add_step(name)
        elif choice == "2":
            routine.show_steps()
        elif choice == "3":
            step_id = int(input("Masukkan ID langkah yang selesai: "))
            routine.complete_step(step_id)
        elif choice == "4":
            step_id = int(input("Masukkan ID langkah yang ingin dihapus: "))
            routine.delete_step(step_id)
        elif choice == "5":
            print("Keluar dari program. Semoga kulitmu sehat dan glowing!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

# Jalankan program
if __name__ == "__main__":
    main()
