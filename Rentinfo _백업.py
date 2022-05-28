from tkinter import*

global wininfo
#wininfo = Toplevel()
wininfo = Tk()
wininfo.title("대여정보")
wininfo.geometry("300x270")
wininfo.resizable(0, 0)
infoframe = Frame(wininfo, relief='flat', padx=10, pady=10)
infoframe.grid(row=0, column=0)

# 이름 정보
label_name = Label(infoframe, text="이름 : ")
label_name.grid(row=0, column=0, pady=4)
label_name = Label(infoframe, text="")
label_name.grid(row=0, column=1, pady=4)

# 전화번호 정보
label_phonenum = Label(infoframe, text="전화번호 : ")
label_phonenum.grid(row=1, column=0, pady=4)
label_phonenum = Label(infoframe, text="전화번호 : ")
label_phonenum.grid(row=1, column=1, pady=4)

# 도서명 정보
label_booktit = Label(infoframe, text="도서명 : ")
label_booktit.grid(row=2, column=0, pady=4)
label_booktit = Label(infoframe, text="도서명 : ")
label_booktit.grid(row=2, column=1, pady=4)

# ISBN 정보
label_ISBN = Label(infoframe, text="ISBN : ")
label_ISBN.grid(row=3, column=0, pady=4)
label_ISBN = Label(infoframe, text="ISBN : ")
label_ISBN.grid(row=3, column=1, pady=4)

# 대출일 정보
label_borrow = Label(infoframe, text="대출일 : ")
label_borrow.grid(row=4, column=0, pady=4)
label_borrow = Label(infoframe, text="대출일 : ")
label_borrow.grid(row=4, column=1, pady=4)

# 반납예정일 정보
label_return = Label(infoframe, text="반납예정일 : ")
label_return.grid(row=5, column=0, pady=4)
label_return = Label(infoframe, text="반납예정일 : ")
label_return.grid(row=5, column=1, pady=4)

# 반납여부
label_returnchk = Label(infoframe, text="반납여부 : ")
label_returnchk.grid(row=6, column=0, pady=4)
label_returnchk = Label(infoframe, text="반납여부 : ")
label_returnchk.grid(row=6, column=1, pady=4)

btn_return = Button(infoframe, text="반납", bg="#0d47a1", fg="white", width=8)
btn_return.grid(row=7, column=1, sticky=E, padx=24, pady=8)

wininfo.mainloop()
