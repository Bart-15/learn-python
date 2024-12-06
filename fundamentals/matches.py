series = 'N-02'

match series:
  case "N-01":
    print('Samsung')
  case "N-02":
    print('Nokia')
  case "N-03":
    print("Motorola")
  case _:
    print('This product doesn\'t exists')