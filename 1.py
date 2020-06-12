import os							# built-in library
import shutil						# pip install pytest-shutil
from tkinter import *				# built-in library
import pygame						# built-in library
from PIL import ImageTk, Image 		# pip install Pillow

isDir = os.path.isdir('D:/uytyfd/')
#print(isFile)

if isDir is True:
	shutil.rmtree('D:/uytyfd/')
 

os.mkdir('D:/uytyfd')
d="D:/uytyfd/"
i=0
for root, dirs, files in os.walk('D:/'):
	for file in files:
		if (file.endswith('.mp3') and root!="D:/uytyfd/"):
			#print(os.path.join(root,file))
			try:
				shutil.copy(os.path.join(root,file), d)
			except shutil.SameFileError:
				continue

os.chdir("D:/uytyfd")
songlist=os.listdir()

songlist.sort(reverse=True)

player=Tk()
player.title("Music Player")
player.geometry('700x700')
player.resizable(False,False)

frame=Frame(player,width=700,height=30).grid(row=0,columnspan=2)

im= ImageTk.PhotoImage(Image.open("D:/codes/Music/Asset 1.png")) #‪C:\Users\Asus\Desktop\1.png
pan = Label(frame, image = im,width=700)
pan.grid(row=0,columnspan=2,pady=10)

playlist=Listbox(frame,highlightcolor="blue",selectmode=SINGLE,width=100,height=25)
for item in songlist:
	pos=0
	playlist.insert(pos,item)
	pos +=1

pygame.init()
pygame.mixer.init()

x=0

def Mplay():
	pygame.mixer.music.load(playlist.get(ACTIVE))
	var.set(playlist.get(ACTIVE))
	pygame.mixer.music.play()

def Mpause():
	global x
	if (x%2==0):
		pygame.mixer.music.pause()
		#print  (x)
	if (x%2==1):
		pygame.mixer.music.unpause()
		#print(x)
	x+=1

var= StringVar()

songtitle=Label(frame,textvariable=var,font=("arial",9,"bold"))

playlist.grid(row=1,columnspan=2)



canvas=Canvas(player,width=700,height=3,background='SlateGray3')
#line=canvas.create_line(0,5,400,5,width=5,fill="SlateGray3")
canvas.grid(row=2,columnspan=2,pady=7)

pause_but=Button(player,text="Pause/Resume",width=25,height=2,bd=5,bg="skyblue3",font=("arial",12,"bold"),command=Mpause).grid(row=3,pady=10)
play_but=Button(player,text="Play",width=25,height=2,bd=5,bg="skyblue3",font=("arial",12,"bold"),command=Mplay).grid(row=3,column=1,pady=10)


songtitle.grid(row=4,columnspan=2)

player.mainloop()

