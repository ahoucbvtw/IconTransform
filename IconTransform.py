import PythonMagick
from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import filedialog
import sys, os

class Main(object):

	def __init__(self):

		# def resource_path(relative_path):
		# #Get absolute path to resource, works for dev and for PyInstaller
		# 	try:
		# # PyInstaller creates a temp folder and stores path in _MEIPASS
		# 		base_path = sys._MEIPASS
		# 	except Exception:
		# 		base_path = os.path.abspath(".")
		# 	return os.path.join(base_path, relative_path)

		# icon = resource_path("Calendar.ico")
		self.window = Tk()
		# self.window.iconbitmap(icon)
		self.window.title("IconTransform") #視窗名稱
		self.window.config(background = "#f0f0f0")#更該視窗背景顏色
		self.window.geometry("350x240+800+250") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
		self.window.resizable(0,0) #不可以更改大⼩
		Font = tkfont.Font(family = "新細明體", size = 10, weight = "bold")
		Font_path = tkfont.Font(family = "新細明體", size = 10)
		path = StringVar() #輸入路徑Entry用的變數
		size = StringVar() #Radiobutton所使用的共同變數，以了解目前使用者選擇哪個按鈕並輸出相對應字串值

		def selectpicture():
			file_path = filedialog.askopenfilename() #請使用者選擇檔案
			path.set(file_path)

		def transform():
			entryvalue = path_pic.get() #獲取Entry輸入的值
			imgfile_List = entryvalue.split("/") #使用"/"去分割成List
			imgfile = imgfile_List[-1] #尋找此List最後一個index必定為欲轉換檔案名稱(含附檔名)
			changeimgfile_List = imgfile.split(".") #使用"/"將檔案名稱去分割成List
			changeimgfile = changeimgfile_List[0] #尋找此List第一個index必定為欲轉換檔案名稱(不含附檔名)

			#.title()是將英文字母首字改成大寫，若非英文字母則使用原始檔名
			newfile = entryvalue.replace(imgfile,changeimgfile.title()) #使用原始選擇圖片路徑當做儲存路徑

			if entryvalue == "": #先判斷Entry輸入值是否為空值
				messagebox.showerror(title = "Error", message = "請選擇欲轉換的圖片！！")
			else:
				try: #利用Try判斷使用者是否選擇正確非圖片之檔案名稱
					img = PythonMagick.Image(entryvalue)
				except:
					messagebox.showerror(title = "Error", message = "請選擇正確圖片檔案！！")
					path_pic.delete(0, END)
				else:
					img.sample( size.get() ) #從Radiobutton獲得使用者欲轉換成何種大小
					img.write(newfile + ".ico")
					messagebox.showinfo(title = "Notice", message = "圖標已成功製作完成！！")
					path_pic.delete(0, END)

		frame = Frame(self.window)
		frame.grid(row = 0, padx = 10, pady = 10)

		selectpic = Label(frame, font = Font, text = "請選擇檔案：")
		selectpic.grid(row = 0, padx = 5, pady = 10)

		path_pic = Entry(frame, font = Font_path, textvariable = path, width = 20)
		path_pic.grid(row = 0, column = 1, pady = 10)

		selectbutton_pic = Button(frame, text = "選擇檔案", font = Font, bg = "skyblue", width = 10, height = 1, command = selectpicture)
		selectbutton_pic.grid(row = 0, column = 2, padx = 5, pady = 10)


		iconsizetitle = LabelFrame(self.window, text = "請選擇Icon大小", font = Font)
		iconsizetitle.grid(row = 1, column = 0, padx = 5, pady = 10)

		iconsizeselect1 = Radiobutton(iconsizetitle, text = "16x16", variable = size,value = "16x16")
		iconsizeselect1.grid(row = 0, padx = 5, pady = 10)

		iconsizeselect2 = Radiobutton(iconsizetitle, text = "24x24", variable = size,value = "24x24")
		iconsizeselect2.grid(row = 0, column = 1, padx = 5, pady = 10)

		iconsizeselect3 = Radiobutton(iconsizetitle, text = "32x32", variable = size,value = "32x32")
		iconsizeselect3.grid(row = 0, column = 2, padx = 5, pady = 10)

		iconsizeselect4 = Radiobutton(iconsizetitle, text = "48x48", variable = size,value = "48x48")
		iconsizeselect4.grid(row = 1, column = 0, padx = 5, pady = 10)

		iconsizeselect5 = Radiobutton(iconsizetitle, text = "64x64", variable = size,value = "64x64")
		iconsizeselect5.grid(row = 1, column = 1, padx = 5, pady = 10)

		iconsizeselect6 = Radiobutton(iconsizetitle, text = "128x128", variable = size,value = "128x128")
		iconsizeselect6.grid(row = 1, column = 2, padx = 5, pady = 10)

		#先預設選擇第一個Radiobutton
		iconsizeselect1.select()

		icontransform = Button(self.window, text = "轉換", font = Font, bg = "skyblue", width = 10, height = 1, command = transform)
		icontransform.grid(row = 2, columnspan = 3, padx = 5, pady = 10)


		self.window.mainloop()

if __name__ == '__main__':
	Main()
