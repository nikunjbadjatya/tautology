tautology.py

A tautology verifier is a program that takes a "propositional statement" and verifies the statement
is a "tautology" or not.
A Tautology is a "propositional statement" which is true no matter what valuation is applied for
each of the variables in the “vocabulary” of the statement. A propositional statement is formed by
combining "propositional variables" with arbitrary logical operators. Vocabulary of the
propositional statement is the set of all the variables in the statement.
A propositional variable is one that can take truth values(true/false). Logical operators that we
consider for this exercise are "AND" represented by "&", "OR" represented by "|" and "NOT" by
"!".

Program to verify whether the given INPUT_PROPOSITION is a tautology or not.
Example of valid tautologies: 'a | !a' and '(a & (!b | b)) | (!a & (!b | b))'

How to Execute:
Modify INPUT_PROPOSITION as per your needs.
$python tautology.py

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
