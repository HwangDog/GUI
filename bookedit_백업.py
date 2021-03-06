from tkinter import*
import tkinter.messagebox as msgbox
from tkinter import filedialog

# 파일 불러오기 함수
def func_open():
    winedit.file = filedialog.askopenfile(title="파일 선택창")
    e_pic.insert(0, winedit.file.name)

# 파일 수정 함수
def func_edit():
    title = e_title.get()
    author = e_author.get()
    publisher = e_publish.get()
    price = e_price.get()
    link = e_link.get()
    ISBN = e_isbn.get()
    rental = e_pic.get()
    bookdescription = t_explain.get("1.0", END)

# 파일 취소 함수
def func_exit():
    response = msgbox.askyesno("도서수정", "정말 취소하시겠습니까?")
    if response == 1:
        winedit.destroy()
    else:
        pass

def Book_Edit(title, author, publisher, price, link, ISBN, rental, bookdescription):
    global winedit
    winedit = Toplevel()
    winedit.title("도서수정")
    winedit.geometry("380x370")
    winedit.resizable(0, 0)
    editframe = Frame(winedit, relief='flat', padx=10, pady=10)
    editframe.grid(row=0, column=0)

    # 제목 수정
    label_title = Label(editframe, text="도서명 : ")
    label_title.grid(row=0, column=0, pady=6)
    global e_title
    e_title = Entry(editframe, width=30)
    e_title.grid(row=0, column=1, pady=6)
    e_title.insert(0, title)

    # 저자 수정
    label_author = Label(editframe, text="저자 : ")
    label_author.grid(row=1, column=0, pady=6)
    global e_author
    e_author = Entry(editframe, width=30)
    e_author.grid(row=1, column=1, pady=6)
    e_author.insert(0, author)

    # 출판사 수정
    label_publish = Label(editframe, text="출판사 : ")
    label_publish.grid(row=2, column=0, pady=6)
    global e_publish
    e_publish = Entry(editframe, width=30)
    e_publish.grid(row=2, column=1, pady=6)
    e_publish.insert(0, publisher)

    # 가격 수정
    label_price = Label(editframe, text="가격 : ")
    label_price.grid(row=3, column=0, pady=6)
    global e_price
    e_price = Entry(editframe, width=30)
    e_price.grid(row=3, column=1, pady=6)
    e_price.insert(0, price)

    #  관련링크
    label_link = Label(editframe, text="관련링크 : ")
    label_link.grid(row=4, column=0, pady=6)
    global e_link
    e_link = Entry(editframe, width=30)
    e_link.grid(row=4, column=1, pady=6)
    e_link.insert(0, link)

    # ISBN 수정
    label_isbn = Label(editframe, text="ISBN : ")
    label_isbn.grid(row=5, column=0, pady=6)
    global e_isbn
    e_isbn = Entry(editframe, width=30)
    e_isbn.grid(row=5, column=1, pady=6)
    e_isbn.insert(0, ISBN)

    # 사진 수정
    label_pic = Label(editframe, text="사진 : ")
    label_pic.grid(row=6, column=0, pady=6)
    global e_pic
    e_pic = Entry(editframe, width=30)
    e_pic.grid(row=6, column=1, pady=6)
    e_pic.insert(0, rental)
    btn_pic = Button(editframe, text="파일 열기", bg="#0d47a1",
                     fg="white", command=func_open)
    btn_pic.grid(row=6, column=2, padx=8)

    # 도서설명 수정
    label_explain = Label(editframe, text="도서설명 : ")
    label_explain.grid(row=7, column=0, pady=6)
    global t_explain
    t_explain = Text(editframe, width=30, height=3)
    t_explain.grid(row=7, column=1, columnspan=2, sticky=E+W, pady=6)
    t_explain.insert(END, bookdescription)

    # 수정하기 버튼
    btn_edit = Button(editframe, text="수정하기", bg="#0d47a1",
                      fg="white", command=func_edit)
    btn_edit.grid(row=8, column=1, sticky=W, pady=15)

    # 취소 버튼
    btn_cancel = Button(editframe, text="취소", bg="#0d47a1",
                        fg="white", width=8, command=func_exit)
    btn_cancel.grid(row=8, column=2, sticky=W, pady=15)

    winedit.mainloop()
