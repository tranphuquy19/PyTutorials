stringA = "Ahihi"

# # stringA[0:2] = "abc"    # does not support
# stringA[:3] = 'abc'
# print(stringA)
# stringA[:2] = '12345'
# print(stringA)

stringA = stringA[:len(stringA)] + ' 12345'[0:4]  # Ahihi 123
print(stringA)

print(r'trần Phú \nQuy')
print(' Trần Phú Quy '.center(50, '*'))
