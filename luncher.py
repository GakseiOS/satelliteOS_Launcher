import tkinter as tk
root = tk.Tk()


#----ランチャーのウィンドウサイズ、位置の調整----
#モニターの縦、横のピクセル数を取得
monitor_width = root.winfo_screenwidth()
monitor_height = root.winfo_screenheight()
print(monitor_width)
print(monitor_height)

#モニターのピクセル数÷3(小数点切り捨て)をし、ランチャーのウィンドウサイズを計算する
window_width = monitor_width//3
window_height = monitor_height//3
print(window_width)
print(window_height)

#ランチャーのウィンドウサイズ、ウィンドウ位置を調整する
windowsize = str(window_width) + "x" + str(window_height) + "+" + str(window_width) + "+" + str(window_height)
print(windowsize)
root.geometry(windowsize)

#タイトルバーを非表示にする
#root.overrideredirect(True)


root.mainloop()
