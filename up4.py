n= input('input=>')
def v(n):
      vo = 'AEIOUaeiou'
      c = ''
      for i in n:
          if i in vo:
              c =c+ i
      print (len(c))
v(n)
