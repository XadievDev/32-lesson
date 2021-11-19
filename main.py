#XadievDev
#32-lesson.Dunder metodlar

#-------------------------------------------------------------#

# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1

#     def __repr__(self):
#         """Mashina haqida ma'lumotlar"""
#         return f"Avto: {self.make} {self.model}"

#     def __eq__(self,boshqa_avto):
#         """Mashina narhini tengligini tekshiradi"""
#         return self.narh == boshqa_avto.narh
    
#     def __lt__(self,boshqa_avto):
#         """Mashina narhini kichikligini tekshiradi"""
#         return self.narh < boshqa_avto.narh

#     def __le__(self,boshqa_avto):
#         """Mashina narhini kichik yoki teng tekshiradi"""
#         return self.narh <= boshqa_avto.narh
    
# avto1 = Avto('GM','Malibu','Qora',2021,30000)
# avto2 = Avto('BMW','X6','Oq',2020,50000)
# avto3 = Avto('GM','Gentra','Qora',2021,10000)
# avto4 = Avto("Honda","Accord","Oq",2017,40000)

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         """Avtosalon haqida ma'lumot"""
#         return f"{self.name} avtosaloni"
    
#     def add_avto(self,avto):
#         """Mashinani qo'shadi"""
#         if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
#             self.avtolar.append(avto)
#         else:
#             print("Avto obyketini kiriting")

#     def __getitem__(self,index):
#         """Listdan avtoni chiqaradi"""
#         return self.avtolar[index]

#     def __setitem__(self,index,value):
#         if isinstance(value,Avto):
#             self.avtolar[index]=value

# salon1 = AvtoSalon("MaxAvto")
# salon1.add_avto(avto1)
# salon1.add_avto(avto2)

#-------------------------------------------------------------#
#Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling.
#Obyekt haqida ma'lumot (__rerp__)
#Talabalarni bosqichi bo'yicha solishtirish (__lt__, __eg__ va hokazo)

# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def __repr__(self):
#         return f"{self.familiya.title()} {self.ism.title()} {self.tyil}-yil.Passport: {self.passport}."
    


#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

#-------------------------------------------------------------------------------------#

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def __repr__(self):
#         return f"Talaba:{self.familiya.title()} {self.ism.title()}. {self.tyil}-yil {self.bosqich}-bosqich talabasi"

    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1

#     def __eq__(self,boshqa_talaba):
#         return self.bosqich == boshqa_talaba
    
#     def __gt__(self,boshqa_talaba):
#         return self.bosqich > boshqa_talaba
    
#     def __le__(self,boshqa_talaba):
#         return self.bosqich <= boshqa_talaba

# talaba1 = Talaba('Amirbek','Xadiev',2006)
# talaba2 = Talaba('Alisher','Xadiev',1998)
# talaba3 = Talaba('Timur','Xadiev',2001)
# talaba4 = Talaba('Muhammadrizo','Jumayev',2007)
# talaba5 = Talaba('Akmal','Ravshanov',2006)

#-------------------------------------------------------------#

#Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.


# class Fan():
#     """Talabalar qo'shilgan fan"""
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.__talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.__talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def get_talabalar(self):
#         return self.__talabalar

#     def get_talabalar_soni(self):
#         return self.talabalar_soni

#     def __getitem__(self,index):
#         return self.__talabalar[index]
    
#     def __setitem__(self,index,value):
#         if isinstance(value,Talaba):
#             self.__talabalar[index]=value

#     def __len__(self):
#         return self.talabalar_soni

#     def __add__(self,talaba):
#         self.__talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def __sub__(self,value):
#         return self.__talabalar.remove(value)

# math = Fan('Matematika')
# math.add_student(talaba1)
# math.add_student(talaba2)
# math.add_student(talaba3)
# math.add_student(talaba4)
