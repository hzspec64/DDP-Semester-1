import myModul
print("======Cara 1 menggunakan modul======")
myModul.pangkat(15, 22)
myModul.akar(2400)


import myModul as mtk
print("======Cara 2 menggunakan modul======")
mtk.pangkat(2,15)
mtk.akar(2)


from myModul import akar
print("======Cara 3 menggunakan modul sebagian fungsi======")
akar(20)

from myModul import *
print("======Cara 4 menggunakan modul all fungsi======")
pangkat(10,50)
akar(20)
perkalian(5,70)