# tüm kitaplıkları içe aktarma
from tkinter import *
from timeit import default_timer as timer
import random

# GUI kullanarak pencere oluşturma
window = Tk()

# pencerenin boyutu tanımlama
window.geometry("450x200")

x = 0

# test için fonksiyon tanımlama
def game():
	global x

	# pencereyi yok etmek için döngü
	# testten sonra
	if x == 0:
		window.destroy()
		x = x+1

	# test sonuçları için tanımlama işlevi
	def check_result():
		if entry.get() == words[word]:

			# burada başlama zamanı, pencerenin
			# açılır ve bitiş zamanı
			# pencere yok edildi
			end = timer()

		# başlangıç ​​zamanını sondan çıkarıyoruz
# zaman ve kullanarak sonuçları hesaplayın
# timeit işlevi
			print(end-start)
		else:
			print("Yanlış giriş!")

	words = ['Lorem ipsum dolor sit amet', 'Dogan Cuceloglu fen lisesi', 'Bilisim dersi',
			'consectetur adipiscing elit', 'python eglenceli', 'İstanbulda yasiyorum']

	# Kullanıcının hızını test etmek için rastgele kelimeler verin


	word = random.randint(0, (len(words)-1))

# timeit işlevini kullanarak zamanlayıcıyı başlatma
	start = timer()
	windows = Tk()
	windows.geometry("450x200")

# pencerede etiketlemek için tkinter'ın etiket yöntemini kullanma
	x2 = Label(windows, text=words[word], font="times 20")

	# pencerede etiketleme yeri
	x2.place(x=150, y=10)
	x3 = Label(windows, text="Yazmaya Başla", font="times 20")
	x3.place(x=10, y=50)

	entry = Entry(windows)
	entry.place(x=280, y=55)

	# çıktı göndermek ve sonuçları kontrol etmek için düğmeler


	b2 = Button(windows, text="Bitir",
				command=check_result, width=12, bg='grey')
	b2.place(x=150, y=100)

	b3 = Button(windows, text="Tekrar Dene",
				command=game, width=12, bg='grey')
	b3.place(x=250, y=100)
	windows.mainloop()


x1 = Label(window, text="Haydi Başlayalım!", font="times 20")
x1.place(x=10, y=50)

b1 = Button(window, text="Başla", command=game, width=12, bg='grey')
b1.place(x=150, y=100)

# arama penceresi


window.mainloop()
