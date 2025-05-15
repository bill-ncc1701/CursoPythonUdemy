# Quebra de linha
# \r\n => LineEnd => Windows (CRLF)
# \n => LineEnd => Linux/Mac (LF)

print(12, 34, 1011, sep="-", end="#\n")
print(56, 78, sep=",", end="\n")
print(9, 10, sep="-", end="\n")

