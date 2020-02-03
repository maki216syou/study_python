# coding:utf-8
import tkinter as tk

root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

labell = tk.Label(root, text="数を入力してね")
labell.place(x = 20,y = 20)

root.mainloop()