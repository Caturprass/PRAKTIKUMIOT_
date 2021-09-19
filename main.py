from gpio import *
from time import *
#GPIO (General Purpose Input/Output) merupakan library yang digunakan untuk mengontrol GPIO Raspberry
#Pi menggunakan Python. GPIO merupakan pin atau tempat yang digunakan sebagai input dan output 
#Fungsi digitalRead berguna untuk membaca input pada pin yang ditentukan. digitalRead(0) berarti program membaca input pada pin 0 (D0). 
#Fungsi digitalWrite berguna untuk menyetel nilai pada pin yang ditentukan (high atau low). Nilai ini akan terus ada, sampai nilai tersebut diubah lagi.  
 
# untuk mendeklarasikan fungsi handleSensorData
def handleSensorData():
	 # mendeklarasikan inputan dari sensor digitalRead
	value = digitalRead(0)
	if value == 0:
		customWrite(2, '0')
		digitalWrite(1, LOW)
		print("Tidak ada gerakan")
		#jika tidak ada gerakan maka pintu garasi tidak akan terbuka
	else:
		customWrite(2, '1')
		digitalWrite(1, HIGH)
		print("Ada gerakan")
		#jika kita mendekatkan cursor kita maka pintu garasi akan terbuka.
		
		
def main():
	add_event_detect(0, handleSensorData)
	
	while True:
		delay(1000)
		
		# jika fungsi main dijalankan maka akan menjalankan programnya
if __name__ == "__main__":
	main()