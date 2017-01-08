''' tautology.py

Program to verify whether the given INPUT_PROPOSITION is a tautology or not.
Example of valid tautologies: 'a | !a' and '(a & (!b | b)) | (!a & (!b | b))'

How to Execute:
Modify INPUT_PROPOSITION as per your needs below.
python tautology.py

Algorithm:
1. Parse the input string and count the number of variables. This is vars_list.
2. Transform the input string so that '!' is converted to 'not' as python does not have boolean !.
3. Generate all valid subsets (subs) of the vars_list. Ex. vars_list = [a,b,c], subs = [[], [a], [b], [c], [a,b], [b,c], [a,c], [a,b,c]]
   This is equivalent for [000,100, 010, 001, 110, 011, 101, 111] 
4. Use subs to evaluate the input proposition. Ex. if subs == [a], that means keep a=True rest all False.
   if subs = [a,b], keep a and b True rest all False.

Assumptions:
1. All statements that are given as input will be syntactically valid. (You dont need to handle
invalid sentences).
2. All propositional variables will be single letter alphabets and no more than 10 variables will be
there in any statement. (ie., cardinality of the vocabulary <= 10).
3. The propositional statement can be arbitrarily nested.
4. You can expected sentences to be well bracketed in case of binary operations. for ex: a | b will
always be (a | b) even if it is the only operation in the statement. (You dont need to worry about
associativity)
5. Whitespace can appear anywhere in the statement.
6. Only &, |, ! will be used as logical operators.
7. ! operator will always associate with the immediate right proposition.

Requirements:
Python2.7 or greater
Tested on Python2.7

Limitations:
None

Author:
Nikunj Badjatya
https://in.linkedin.com/in/celebratetech


'''
from itertools import combinations
import re

INPUT_PROPOSITION = "(!a | (b & !a))"
#(a & (!b | b)) | (!a & (!b | b))
#(!a | (a & a))
# (!a | (b & !a))
# a & (b | c)



class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def infixToPostfix(infixexpr):
    prec = {}
    prec["!"] = 3
    prec["&"] = 2
    prec["|"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = [char for char in list(infixexpr) if char != ' ']

    for token in tokenList:
        if token in "abcdefghij":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postfixEval(postfixExpr, current_val):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "abcdefghij":
            operandStack.push(token)
        else:
            if token == '!':
                operand1 = operandStack.pop()
                operand2 = None
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
            result = doMath(token,current_val[operand1],current_val[operand2])
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    print(op, op1, op2)
    if op == "!":
        return not op1
    elif op == "|":
        return op1 | op2
    elif op == "&":
        return op1 & op2


def find_propositional_variables():
    '''
    This function is used to return the number of variables in the INPUT_PROPOSITION. It does this in O(n) time.
    '''

    vars_list = set()
    for char in INPUT_PROPOSITION:
        if char in 'abcdefghij': # since input vars are not greater than 10 as given in question
            vars_list.add(char)
    return vars_list


def get_subsets(vars_list):
    '''
    This is used to generate all valid subsets of a given list.
    Ex. vars_list = [a,b,c], subs = [[], [a], [b], [c], [a,b], [b,c], [a,c], [a,b,c]]
    It uses built in combinations method. Ex. combinations('ABCD', 2) => AB AC AD BC BD CD
    '''

    return [set()] + [set(j) for i in range(len(vars_list)) for j in combinations(vars_list, i+1)]

#print(postfixEval('7 8 + 3 2 + /'))

def main():
    vars_list = find_propositional_variables()

    subset_list = get_subsets(vars_list)
    print('subsets %s' % subset_list)
    postfixExpr = infixToPostfix(INPUT_PROPOSITION)
    print(postfixExpr)

    # Evaluate the expression for different values of thse variables

    initial_val = {}
    for propositional_variable in vars_list:
        initial_val[propositional_variable] = False
    print(initial_val)

    result = []
    for subset in subset_list:
        current_val = dict(initial_val)
        for propositional_variable in subset:
            current_val[propositional_variable] = True
        print(current_val)
        result.append(postfixEval(postfixExpr, current_val))
    print result


if __name__ == '__main__':
    main()
