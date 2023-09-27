#Version 1
# s=input()
# m=input().split()
# ans = ''
# for word in m:
#     for let in s:
#         if let in word:
#             ans += '*'*len(word) + ' '
#             break
#     else:
#         ans += word + ' '
# print(ans)

#Version 2
# s,a=input(),''
# m=input().split()
# for w in m:a+='*'*len(w)+' 'if any(l in w for l in s)else w+' '
# print(a)

#Version 3
s=input()
print(' '.join([w,'*'*len(w)][any({*s}&{*w})]for w in input().split()))

#Version 4 also works
s=input()
print(' '.join(any({*s}&{*w})*'*'*len(w)or w for w in input().split()))
