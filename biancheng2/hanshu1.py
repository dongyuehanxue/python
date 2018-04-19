#-* coding=utf-8 -*-\
# def make_shirt(size,font):
#     print 'T恤的大小是'+size+',T恤上的字为'+font

# # 位置实参
# make_shirt('34','ufo')
# make_shirt(font='1234567',size='45')

# def make_shirt(size='大',font='I love Python'):
#     print 'T恤的大小是'+size+',T恤上的字为'+font

# make_shirt()
# make_shirt('中')
# make_shirt(font='其他字体')

# def describe_city(city,county='China'):
#     print city+' is in '+county
# describe_city('北京')
# describe_city('邯郸')
# describe_city('日本',county='Jaspan')

#返回字典
# def make_album(name,album,num=''):
#     albums = {'name':name,'album':album}
#     if num:
#         albums['num'] = num
#     return albums

# print make_album('周杰伦','十里香','20')
# print make_album('梁静茹','暖暖')
# print make_album('平安','洋葱')



# def show_magicians(magicians):
#     for i in magicians:
#         print '魔术师名字：'+i
# def make_great(old,magicians):
#     while old:
#         # old中的元素都移除，列表为空
#         current = old.pop()+'the Great'
#         magicians.append(current)


# old_magicians = ['张三','李四','王五']
# magicians = []

# # make_great(old_magicians,magicians)
# # 传递列表的副本
# make_great(old_magicians[:],magicians)
# # old中的元素都移除，列表为空
# show_magicians(old_magicians)
# show_magicians(magicians)

# *toppings空元祖，传递任意数量的实参
# **user_info字典 键值对
# def bulid_profile(first,last,**user_info):
#     # 创建一个空字典
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key,value in user_info.items():
#         profile[key] = value
#     return profile
# user = bulid_profile('李','si',age='23')
# print user

# def sandwich(*foods):
#     print 'the sandwich with the following toppings:'
#     for food in foods:
#         print '- '+food

# sandwich('洋葱')
# sandwich('洋葱','芝士','培根')

# def make_car(manu,model,**other):
#     car = {}
#     car['zhizaoshang'] = manu
#     car['xinghao'] = model
#     for key,value in other.items():
#         car[key] = value
#     return car

# car = make_car('subaru','outback',color='blue',tow_package=True)
# print car

# class Restaurant():
#     def __init__(self,reataurant_name,cuisine_type,num_served=0):
#         self.reataurant_name = reataurant_name
#         self.cuisine_type = cuisine_type
#         self.num_served = num_served
#     def describe_restaurant(self):
#         print self.reataurant_name,self.cuisine_type,'就餐人数:',self.num_served
#     def open_restaurant(self):
#         print '餐馆正在营业'
#     def set_number_served(self,num):
#         self.num_served = num
#     # 就餐人数递增
#     def increment_number_served(self,num_served):
#         self.num_served += num_served
    
# restaurant = Restaurant('第一家','a3')
# print restaurant.reataurant_name
# print restaurant.cuisine_type

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant.set_number_served(30)
# restaurant.describe_restaurant()
# # 第一天
# restaurant.increment_number_served(20)
# restaurant.describe_restaurant()
# # 第二天
# restaurant.increment_number_served(20)
# restaurant.describe_restaurant()

class User(object):
    def __init__(self,first_name,last_name,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
    def describe_user(self):
        print self.first_name,self.last_name,self.login_attempts
    def greet_user(self):
        print 'hello '+self.first_name+self.last_name
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

one = User('张','三',0)
one.describe_user()
one.greet_user()

one.increment_login_attempts()
one.describe_user()

one.increment_login_attempts()
one.describe_user()

one.reset_login_attempts()
one.describe_user()



