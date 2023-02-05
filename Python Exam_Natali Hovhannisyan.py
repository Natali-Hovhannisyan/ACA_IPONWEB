#!/usr/bin/env python
# coding: utf-8

# ### Problem 1

# In[22]:


class PatientError(Exception):
    def __init__(self, message, value):
        self._message = message
        self._value = value
        super().__init__(f"{message}: {value}")
        
        
class Patient:
    def __init__(self, name, surname, age, gender):
        if age < 18 or age > 100:
            raise PatientError("Age should be between 18 and 100", age)
            
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        
    def __repr__(self):
        return f"{self.name} {self.surname} - {self.gender}, {self.age} years old"
    
    def __ne__(self, other):
        return self.name != other.name and self.surname != other.surname and self.age != other.age and self.gender != other.gender
        
        


# In[23]:


patient1 = Patient("Natali", 'Hovhannisyan', 17 , "F")


# In[24]:


patient1 = Patient("Natali", 'Hovhannisyan', 19 , "F")


# In[25]:


patient2 = Patient("Petros","Petrosyan", 20, "M")


# In[26]:


patient1 != patient2


# In[27]:


patient3 = Patient("Natali", 'Hovhannisyan', 19 , "F")


# In[28]:


patient1 != patient3


# In[8]:


#from datetime import timedelta, datetime


# In[18]:


# class Doctor:
    
#     def __init__(self, name, surname, schedule):
#         self.name = name
#         self.surname = surname
#         self.schedule = schedule
        
#     def __repr__(self):
#         return f"Doctor {self.name} {self.name} schedule \n {self.schedule}"
    
#     def is_registered(self, patient):
#         if patient in self.schedule.values():
#             return True
#         else:
#             return False
        
#     def if_free(self, datetime):
        
        


# In[9]:


# d = datetime(2023,5,2,12,0)


# In[ ]:


# print(d)


# In[ ]:


# schedule = {d: patient1, datetime(2023,5,2,12,30): patient2}


# In[ ]:


# doct1 = Doctor("Armen","Hakobyan", schedule)


# In[ ]:


# doct1.is_registered(patient1)


# ### This is the correct solution for Doctor class

# In[34]:


from datetime import datetime, timedelta

class Doctor:
    def __init__(self, name, surname, schedule = {}):
        self.name = name
        self.surname = surname
        self.schedule = schedule
        
    def __repr__(self):
        
        return f"Doctor {self.name} {self.name} schedule \n {self.schedule}"
    
    
#     def register_patient(self, patient, datetime_):
        
#         date_object = datetime.strptime(datetime_, "%Y-%m-%d %H:%M")
#         datetime_ = date_object.strftime("%Y-%m-%d %H:%M")
        
#         if patient in list(self.schedule.values()) and datetime_ in self.schedule:
#             print(f"Patient {patient} is already registered")
#         else:
#             self.schedule[datetime_] = patient
#             print(f"Patient {patient} successfully registered at {datetime_}")         
        
    def is_free(self, time_string):
        time = datetime.strptime(time_string, "%Y-%m-%d %H:%M")
        for appointment_time_str, patient in self.schedule.items():
            print(appointment_time_str)
            appointment_time = datetime.strptime(appointment_time_str, "%Y-%m-%d %H:%M")
            appointment_end = appointment_time + timedelta(minutes=30)
            if appointment_time <= time <= appointment_end:
                return False
        return True
            
        
    def is_registered(self, patient):
        if patient in list(self.schedule.values()):
            return False
            print(f"Patient {patient} is already registered")
        else:
            return True
            print(f"Patient {patient} is not registered")
            
    def register_patient(self, patient, datetime_):
        
        date_object = datetime.strptime(datetime_, "%Y-%m-%d %H:%M")
        datetime_ = date_object.strftime("%Y-%m-%d %H:%M")
        
        if self.is_free(datetime_) and not self.is_registered(patient):
            self.schedule[datetime_] = patient
        else:
            return f"Patient {patient} already registered or Datetime {datetime_} is not free"


# In[40]:


d = "2023-5-2 12:30"


# In[41]:


schedule = {d: patient1, "2023-5-2 12:30": patient2}


# In[42]:


doct1 = Doctor("Armen","Hakobyan", schedule)


# In[43]:


doct1.is_free("2023-5-2 12:30")


# In[44]:


doct1.register_patient(patient3, "2023-5-2 12:25")


# ### Problem 2

# In[12]:


class ProductError(Exception):
    def __init__(self, message, value):
        self._message = message
        self._value = value
        super().__init__(f"{message}: {value}")
        
        
class Product:
    
    def __init__(self, price, ID, quantity):
        self.price = price
        self.ID = ID
        self.quantity = quantity
        
    def __repr__(self):
        return f"Product {self.ID}, Price is {self.price}, quantity {self.quantity}"
    
    def buy(self, count):
        if count > self.quantity:
            raise ProductError("Don't have enough quantity", self.quantity)
        else:
            self.quantity -= count
            
    
    
    


# In[13]:


product1 = Product(12, 1, 3)


# In[14]:


product2 = Product(5, 4, 4)


# In[15]:


product1.buy(5)


# In[16]:


product1.buy(1)


# In[17]:


product1.quantity


# In[18]:


class Inventory:
    
    def __init__(self, products):
        self.products = products
        
    def __repr__(self):
        return f"The inventory consists of {self.products}"
    
    def get_by_id(self, id_):
        for i in self.products:
            if i.ID == id_:
                return i
    
    def sum_of_products(self):
        sum_ = 0
        value = 0
        for i in self.products:
            sum_ += i.quantity
            value += i.quantity*i.price
            
        return f"We have {sum_} products, which have value of {value}"


# In[19]:


inv = Inventory([product1, product2])


# In[20]:


inv.get_by_id(1)


# In[21]:


inv.sum_of_products()


# ### Problem 3

# In[1]:


class Passenger:
    
    def __init__(self, name, city, rooms):
        self.__name = name
        self.__city = city
        self.__rooms = rooms
        
    def __repr__(self):
        return f"Passenger {self.__name} going to {self.__city} has occupied {self.__rooms}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, value):
        self.__city = value
    
    @property
    def rooms(self):
        return self.__rooms
    
    @rooms.setter
    def rooms(self, value):
        self.__rooms = value
    


# In[2]:


passenger1 = Passenger("Natali", "New York", {"penthouse": 0})


# In[4]:


passenger1.city


# In[9]:


class Hotel:
    
    def __init__(self, city, rooms):
        self.__city = city
        self.__rooms = rooms
        
    def __repr__(self):
        return f"The hotel in city {self.__city} has these available rooms {self.__rooms}"
    
    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, value):
        self.__city = value
    
    def free_rooms_list(self, room_type):
        return self.__rooms[room_type]
    
    def reserve_rooms(self, type_ , count):
        if self.__rooms[type_] >= count:
            self.__rooms[type_] -= count
        else:
            print("Not enough available rooms")
        


# In[10]:


hotel1 = Hotel("New York", {"penthouse": 2, "single": 1, "double":0})


# In[12]:


hotel1.free_rooms_list("penthouse")


# In[13]:


hotel1.reserve_rooms("single", 1)


# In[14]:


hotel1.free_rooms_list("single")


# In[16]:


hotel1.reserve_rooms("double", 1)

