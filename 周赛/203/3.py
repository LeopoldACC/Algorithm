s ="10100"# "11111"#"10101"
def show(stri):
    c = stri.split('0')
    print(c)
    c = filter(lambda x: x, c)
    print(c)
show(s)
