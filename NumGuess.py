from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("NumGuess")

def main():
	global ran
	global tries
	global root

	ran = random.randint(1, 100)

	tries = 0

	hlp = Label(root, text="I picked a whole number between 1 to 100.\nGuess what is it:")
	hlp.pack()

	eyg = Entry(root)
	eyg.pack()
	
	def chk(guess):
		global ran
		global tries
		global root

		if float(guess) > 100 or float(guess) < 1:
			messagebox.showinfo("NumGuess", str(guess) + ", Your guess, is not between 1 to 100.\nPlease try another number.")
		elif float(guess) > float(ran):
			tries += 1
			messagebox.showinfo("NumGuess", "Your guess is too high.\nPlease, try again.")
		elif float(guess) < float(ran):
			tries += 1
			messagebox.showinfo("NumGuess", "Your guess is too low.\nPlease, try again.")
		elif float(guess) == float(ran):
			tries += 1
			messagebox.showinfo("NumGuess", "Your guess is correct!.\nNumber or tries: " + str(tries) + ".")
			pa = messagebox.askyesno("NumGuess", "Do you wanna play again?\nPress 'Yes or 'No'.")
			
			if pa == 1:
				hlp.pack_forget()
				eyg.pack_forget()
				snd.pack_forget()
				clr.pack_forget()

				main()
			elif pa == 0:
				root.destroy()
		else:
			messagebox.showinfo("NumGuess", str(guess) + ", Your guess, is unknown number.\nPlease try another number.")

	def dlt():
		eyg.delete(0, END)

	snd = Button(root, text="Guess", command=lambda: chk(eyg.get()))
	snd.pack()

	clr = Button(root, text="Clear", command=dlt)
	clr.pack()

	root.mainloop()

main()
