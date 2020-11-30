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

	hlp = Label(root, text="Hi there!\nI picked a number between 1 to 100.\nEnter your guess:")
	hlp.pack()

	eyg = Entry(root)
	eyg.pack()

	def chk(guess):
		global ran
		global tries
		global root

		if int(guess) > int(ran):
			tries += 1
			messagebox.showinfo("NumGuess", "Your guess is too high.\nPlease, try again.")
		elif int(guess) < int(ran):
			tries += 1
			messagebox.showinfo("NumGuess", "Your guess is too low.\nPlease, try again.")
		elif int(guess) == int(ran):
			tries += 1
			messagebox.showinfo("NumGuess", "Your guess is correct!.\nNumber or tries: " + str(tries) + ".")
			pa = messagebox.askyesno("NumGuess", "Do you wanna play again?\nPress 'Yes or 'No'.")
			
			if pa == 1:
				hlp.pack_forget()
				eyg.pack_forget()
				snd.pack_forget()

				main()
			elif pa == 0:
				root.destroy()

	snd = Button(root, text="Guess", command=lambda: chk(eyg.get()))
	snd.pack()

	root.mainloop()

main()