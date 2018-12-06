#++jpj==mangled code ==tt=018-12-06==
# ===python method parameters===
class MeDoink:
    def double_it(self,value):
        doubled_value=value*2
        return doubled_value
my_object=MeDoink()
print(my_object.double_it(2))
print(my_object.double_it(16))
print(my_object.double_it(3))
print(my_object.double_it(17))
# == demonstrated the implied self as first parameter in instance object ===

class MeLeetle_adder:
    def adder_do(self,x,y):
        add_menbr=x+y
        return add_menbr
my_ans=MeLeetle_adder()
print(my_ans.adder_do(6,7))
print(my_ans.adder_do(6,9))
print(my_ans.adder_do(6,5))
print(my_ans.adder_do(6,7))


      

        