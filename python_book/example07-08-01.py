# coding:utf-8
import tkinter as tk

class Ball:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def move(self, canvas):
        # いまの円を消す
        canvas.create_oval(self.x - 21, self.y - 21, self.x + 21, self.y + 21, fill="white", width=0)
        # X座標、Y座標を動かす
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        # 次の位置に円を描画する
        canvas.create_oval(self.x - 21, self.y - 21, self.x + 21, self.y + 21, fill=self.color, width=0)
        # 橋を越えていたら反対向きにする
        if self.x >= canvas.winfo_width():
            self.dx = -1
        if self.x <= 0:
            self.dx = 1
        if self.y >= canvas.winfo_height():
            self.dy = -1
        if self.y <= 0:
            self.dy = 1

#円をひとつ作る
b = Ball(400, 300, 1, 1, "red")

def loop():
    #　動かす
    b.move(canvas)
    # もう一回
    root.after(10,loop)

# ウィンドウを描く
root = tk.Tk()
root.geometry("800x600")

# canvasを置く
canvas = tk.Canvas(root, width = 800, height = 600, bg="white")
canvas.place(x = 0, y = 0)

# タイマーをセット
root.after(10,loop)

root.mainloop()