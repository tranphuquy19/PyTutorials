test = "Hello baby"

# For Each
for charItem in test:
    print(charItem)

print('\n###############################')

# For normal
for charIndex in range(len(test)):
    if charIndex == 5:
        # pass      # IGNORE below
        continue    # IGNORE index == 5
        # break     # IGNORE index >= 5
    print(charIndex)
