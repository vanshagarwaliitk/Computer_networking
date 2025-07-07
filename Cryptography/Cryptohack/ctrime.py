import requests
flag =""

printable_chars = ''.join([chr(i) for i in range(32, 127)])
# l= 68  Figure out the right value of l yourself
lengths = []
while len(flag)<33:
  #  print(i)
   temp = flag
   for c in printable_chars:
        plaintext = ""
        temp_text = (flag+c).encode().hex()
        # prev_len = 0
        check = False
        print(c,"no")
        # flag = False
        for j in range(9):
            plaintext+=temp_text
            # hex_input = temp_text.encode().hex()
            url = f"https://aes.cryptohack.org/ctrime/encrypt/{plaintext}/"
            response = requests.get(url)
            response = response.json()['ciphertext']
            if j==8 and  len(response)==l:
                # flag = True
                flag+=c
                print(c)
                lengths.append(l)
                check = True
   if temp==flag:
      l+=2
   if check:
       break
   print(flag)
print(plaintext)
