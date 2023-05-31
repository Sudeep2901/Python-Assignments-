#Simple Program for Multiple Inheritance
'''
Parent Class 1 : Father
Parent Class 2 : Mother
Child class : Son >  inherit(Father, Mother)
'''
try:
    class Father:
        def hair_Col(self,h):
            print(f"Dad's Hair colour is {h}")

    class Mother:
        def eye_Col(self,e):
                print(f"Mom's Eye colour is {e}")

    class Son(Father, Mother):
        def me(self):
            print(f"My Hair Colour is Black & Eye Colour is Brown ")

    s = Son()
    s.hair_Col("Black")
    s.eye_Col("Brown")
    s.me()
except BaseException as ex:
    print(ex)