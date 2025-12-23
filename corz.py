cor={

}
c=None
while True:
  val=str(input("What currency you want to use?")).lower()
  match val:
    case 'dollars'|'dollar':
      break
    case 'rubles'|'ruble':
      break
    case 'euros'|'euro':
      break
    case 'yuans'|'yuan':
      break
    case _:
      print("wrong currency, try again")
      continue
sum=0
while c!='yes':
  a=str(input("What do you want to buy? "))
  b=int(input(f"How much it cost? {val}: "))
  sum+=b
  with open('corz.txt', 'a') as file:
    file.write(f'{a} it costs:{b} {val}\n')
  cor[a]=b
  print(f"Your list of products: {cor}")
  c=str(input('Do you want to stop making list?(yes for exit, no for standing here) '))
else:
  with open('corz.txt', 'a') as file:
    file.write(f"So you need to bring {sum} {val} for shopping")
  print("Check your corz.txt file!")