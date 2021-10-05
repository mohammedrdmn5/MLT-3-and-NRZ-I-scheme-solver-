bits = input("Enter your bits: ")
choices = ['##|', '|##']
prev = '#|#'
print('\nHow to use => middle:#|#\tbottom:|##\ttop:##|\n')
print('#|#\tSTART')
i = 0
for b in bits:
    i = i % 2
    if b == '1':
        print(choices[i] + "\t 1")
        prev = choices[i]
        i += 1
    else:
        print(prev + "\t 0")
print('#|#\tEND')
