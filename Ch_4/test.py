
n = int(input())
integer_list = map(int, input().split())

print(tuple(integer_list))
print(__builtins__.hash(tuple(integer_list)))
