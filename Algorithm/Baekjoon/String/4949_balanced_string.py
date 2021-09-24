import re
import sys

close_str: list = []
is_balanced: bool = True

while True:
    input_str: str = str(sys.stdin.readline().rstrip())
    if len(input_str) == 1 and input_str == '.':
        break
    else:
        input_str = re.sub('[a-zA-Z.]', '', input_str).replace(' ','')
        if len(input_str) == 0:
            pass
        else:
            input_str_list: list = list(input_str)

            while input_str_list:
                next_str: str = input_str_list.pop()

                if next_str == ')' or next_str == ']':
                    close_str.append(next_str)
                else:
                    if len(close_str) == 0:
                        is_balanced = False
                        break
                    else:
                        recent_str: str = close_str.pop()

                        if not ((recent_str == ')' and next_str == '(') or (recent_str == ']' and next_str == '[')):
                            is_balanced = False
                            break
        
        if len(close_str) >= 1:
            is_balanced = False
            
        print('yes') if is_balanced else print('no')
        is_balanced = True
        close_str.clear()