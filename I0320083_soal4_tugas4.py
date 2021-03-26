# Program Pendaftaran Kursus Online

# input time library
import time
start_time = time.time()

print("Pendaftaran Kursus Online")
print(" ")

# input usia
usia = int(input("Berapa usia Anda saat ini? " ))

# output usia >=21
if usia >= 21:
    status_ujian = input ("Apakah Anda lulus ujian kualifikasi? [Y/T]: ")
    if status_ujian == "Y":
        print("Anda dapat mendaftar di kursus.")
    elif status_ujian == "T":
        print("Anda tidak dapat mendaftar di kursus.")

# output usia <21
else:
    print("Anda tidak dapat mendaftar di kursus.")

print(" ")
print("Terima kasih telah berkunjung")
print(" ")
print("Waktu runtime adalah", time.time() - start_time, "detik")
