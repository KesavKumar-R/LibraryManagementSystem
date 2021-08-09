import datetime
import os
# os.getcwd()
class LMS:
    """This class is used to keep record of books library.
    it has four modules:'dispplay books','issue books','return books','add books' """
    def __init__(self,list_of_books,library_name):
        self.list_of_books="List_of_books.txt"
        self.library_name=library_name
        self.books_dict={}
        Id=101
        with open(self.list_of_books) as bk:
            content=bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n"," "),
            "lender_name":"","Issue_data":"","Status":"available"}})
            Id=Id+1 
    def display_books(self):
        print("-------------------list of books---------------------")
        print("Books ID","\t","Title")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("Status"),"]")           

    def Issue_books(self):
        books_id=input('enter books id: ')
        current_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"]=="available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} \
                on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]["Status"]=="available":
                your_name= input("enter your name")
                self.books_dict[books_id]["lender_name"]=your_name
                self.books_dict[books_id]["Issue_date"]=current_date
                self.books_dict[books_id]["Status"]="already issued"
                print("Book Issued Succesfully !!!\n") 
            else:
                print("Book ID not found")
                return self.Issue_books() 
    def add_books(self):
        new_book=input("Enter The Book Title")
        if new_book=="":
            return self.add_books()
        elif len(new_book)>25:
            print('Book Title Length is too Long')
            return self.add_books()
        else:
            with open (self.list_of_books,'a') as bk:
                bk.writelines(f'\n{new_book}')
                self.books_dict.update({str(int(max(self.books_dict))+1):{"books_title":new_book,
                "lender_name":"","Issue_date":"","Status":"available"}})
                print(f"The book  '{new_book}' has been added succesfully !!!")
        
    def return_books(self):
        books_id=input("Enter the Book ID:   ")
        if books_id=="":
            return self.return_books()
        elif books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"]=="available":
                print("This Book is Already Available,Check your Book ID")
                return self.return_books()
            elif not self.books_dict[books_id]["Status"]=="available":
                self.books_dict[books_id]["lender_name"]=""
                self.books_dict[books_id]["Issue_date"]=""
                self.books_dict[books_id]["Status"]="available"
        else:
            print("Book ID not Found")
try:
    myLMS=LMS("List_of_books.txt","G.R.Damodaran Memorial Library")
    press_key_list={"D":"Display Books","I":"Issue Books","A":"Add Books","R":"Return Books","Q":"Quit"}
    key_press=False
    while not (key_press=="q"):
        print(f"\n----------Welcome to {myLMS.library_name} Library Management System---------\n")
        for key,value in press_key_list.items():
            print(f'For {value} Press {key}')  
        key_press=input("Enter your keyword:  ").lower() 
        if key_press=="i":
            print("\ncurrent selection: Issue Books\n")
            myLMS.Issue_books()
        elif key_press=="d":
            print("\ncurrent selection: Display Books\n")
            myLMS.display_books() 
        elif key_press=="a":
            print("\ncurrent selection:Add Books\n")
            myLMS.add_books()
        elif key_press=="r":
            print("\ncurrent selection: return books\n")
            myLMS.return_books()
        elif key_press=="q":
            break
        else:
            continue    
except Exception as e:
    print("Something Went Wrong in the Project")





l=LMS("List_of_books.txt","oxford")

l.display_books()
#print(LMS("List_of_books.txt","oxford"))        