immutable_var = (2,78,'V', 'f')
print(immutable_var)
#Изменение переменных невозможно, т.к кортежи используются  в качестве хранилища данных, это нужно, когда необходимо сохранить список в неизменяемом виде!
mutable_list=[23,'IT',1,'like']
print(mutable_list)
mutable_list.extend(['super'])
print(mutable_list)

