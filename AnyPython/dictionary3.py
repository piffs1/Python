picnicItems = {"apples" : 5, "cups" : 2}
print( "I am bringing " + str(picnicItems.get("cups", 0)) + " cups ." )
print( "I am bringing " + str(picnicItems.get("bubs", -1)) + " bubs ." )
# template<class T, class C> T dictionary::get(T key, C output)
# if (this->find(key)!=this->end()) return value;
# else return output;
# Поиск по ключу, если ключ не найден, то выводится значение аргумента C
spam = {"name" : "Pooka" , "age" : 5}
if "color" not in spam: # analogue setdefault
	spam["color"] = "black"
print(spam)

spam.setdefault("color1","black")
print(spam)