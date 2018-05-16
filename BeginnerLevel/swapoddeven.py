s=raw_input()
f=''.join([c[1] + c[0] for c in zip(s[::2],s[1::2])])
print(f)
