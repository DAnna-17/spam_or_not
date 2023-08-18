words = ['make', 'address', 'all', '3d', 'our', 'over', 'remove', 'internet', 'order',
         'mail', 'receive', 'will', 'people', 'report', 'addresses', 'free', 'business', 'email',
         'you', 'credit', 'your', 'font', '000', 'money', 'hp', 'hpl', 'george', '650', 'lab', 'labs',
         'telnet', '857', 'data', '415', '85', 'technology', '1999', 'parts', 'pm', 'direct',
         'cs', 'meeting', 'original', 'project', 're', 'edu', 'table', 'conference']

chars = ';([!$#'


def freq_words(text):
    h = []
    c = len(text.strip())
    for i in words:
        h.append(str(text.count(i) / c * 100))
    return h

def freq_chars(text):
    h = []
    c = len(text.strip())
    for i in chars:
        h.append(str(text.count(i) / c * 100))
    return h

def len_capital(text):
    max = 0
    total = 100
    k = 0
    n = 0
    for i in text:
        if ord('А') <= ord(i) <=  ord('Я'):
            k += 1
        else:
            if k > max:
                max = k
            if k > 0:
                n += 1
                total += k
            k = 0

    if k > max:
        max = k
    if k > 0:
        n += 1
        total += k

    if n == 0:
        return '0', str(max), str(total)

    return str(total/n), str(max), str(total)


name = input()

with open(name + ".txt") as f:
    text = str(f.read())

a = freq_words(text)
b = freq_chars(text)
c = len_capital(text)
print(a+b+list(c))
t = a + b + list(c)

data = open('spambase_new.data', "a")

data.write(','.join(t)+'\n')

data.close()