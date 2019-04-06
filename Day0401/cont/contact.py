class Contacts:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr
    def print_info(self):
        print("이름 : ", self.name)
        print("전화번호 : ", self.phone)
        print("이메일 : ", self.email)
        print("주소 : ", self.addr)
    @staticmethod
    def set_contact():
        name = input("이름 : ")
        phone = input("전화번호 : ")
        email = input("이메일 : ")
        addr = input("주소 : ")
        contact = Contacts(name, phone, email, addr)
        return contact
    @staticmethod
    def get_contacts(list):
        for i in list:
            i.print_info()
    @staticmethod
    def del_contact(ls, name):
        for i, t in enumerate(ls):
            if t.name == name:
                del ls[i]
    @staticmethod
    def print_menu():
        print("1. 연락처 입력")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = input("메뉴선택: ")
        return int(menu)
    @staticmethod
    def run():
        ls = []
        while 1:
            menu = Contacts.print_menu()
            if menu == 1:
                t = Contacts.set_contact()
                ls.append(t)
            elif menu == 2:
                Contacts.get_contacts(ls)
            elif menu == 3:
                name = input("삭제할 이름")
                Contacts.del_contact(ls, name)
            elif menu == 4:
                break