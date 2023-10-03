# Fungsi untuk menyelesaikan problem advance yang diberikan
def SolveAdvanceProblems():
    # Mengambil value dari input dan di tampung oleh variable input_number
    input_number = int(input("Input number of cube : "))
    
    # Melakukan perulangan for berdasarkan jumlah dari input_number untuk dilakukan iterasi
    for i in range(input_number):
        # Menampilkannya pada console dan melakukan operasi "**" sebagai pemangkatan dengan 3 
        # untuk setiap i ditambah 1 karena range itu dimulai dari 0 maka kita tambahkan 1
        print(f"Current Number is {i+1} and the cube is {(i+1)**3}")
        
# Memanggil Fungsi SolveAdvanceProblems untuk dijalankan
SolveAdvanceProblems()