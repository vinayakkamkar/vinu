def check(my_string):
    brackets = ['{}', '()', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
         my_string=my_string.replace(br, '')

string="{[()]}"
print(string, "-", "balanced"
      if check(string) else "unbalanced")
