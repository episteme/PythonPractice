from random import randint

def main():
    nums = four_numbers()
    print(nums)
    inp = raw_input()
    if validate(inp, nums):
        try:
            ans = eval(inp)
        except SyntaxError:
            print "Invalid expr, most likely bracket issue"
            exit
        print(ans)
        if ans != 24:
            print "you lost"
        else:
            print "you won"
    
def four_numbers():
    return (str(randint(0,9)) + str(randint(0,9))
            + str(randint(0,9)) + str(randint(0,9))) 

def validate(expr, nums):
    valid = ['+','-','/','*']
    expr_clean = expr.replace("(", "").replace(")", "")
    nums_in_expr = []
    if len(expr_clean) != 7:
        print "invalid expr"
        return False
    for c in range(0, len(expr_clean)):
        if c % 2 == 0:
            nums_in_expr.append(expr_clean[c])
        else:
            if expr_clean[c] not in valid:
                print "invalid operator"
                return False
    if sorted(nums) != sorted(nums_in_expr):
        print "invalid nums"
        return False
    return True

main()
