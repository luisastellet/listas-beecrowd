# #LISTA 1

# #EXERCÍCIO 1
# A, G, Ra, Rg = map(float, input().split())
# distA = Ra / A
# distG = Rg / G
# if distA > distG:
#     print('A')
# else:
#     print('G')

# #EXERCÍCIO 2
# N = int(input())
# M = int(input())
# print(N-M)


# #EXERCÍCIO 3
# Xm, Ym, Xr, Yr = map(int,input().split())
# dist = abs(Xr - Xm) + abs(Yr - Ym)
# print(dist)


# #EXERCICIO 4
# N = int(input())
# cont = 1
# V = []
# V.append(int(input()))
# for i in range(0,N-1):
#     V.append(int(input()))
#     if V[i+1] != V[i]:
#         cont += 1
# print(cont)


# #EXERCÍCIO 5:
# N = int(input())
# menor = float('inf')
# for i in range(N):
#     P, G = input().split()
#     P = float(P)
#     G = int(G)
#     valorgrama = P / G
#     if valorgrama < menor:
#         menor = valorgrama
# print(menor * 1000)


# #EXERCÍCIO 6
# n = list(map(int,input().split()))
# if n[0] > n[1] > n[2] > n[3] > n[4]:
#     print('D')
# elif n[0] < n[1] < n[2] < n[3] < n[4]:
#     print('C')
# else:
#     print('N')



# #LISTA 2

# #EXERCÍCIO 1
# X, Y = input().split()
# Xint = int(X)
# Yint = int(Y)
# maior = X
# if Yint > Xint:
#     maior = Yint
# print(maior)


# #EXERCÍCIO 2
# I, N = input().split()
# Iint = int(I)
# Nint = int(N) #número que aparecerá no for (númeor de vezes da análise)
# D = Iint
# E = Iint
# F = Iint
# print(D, E, F, Iint, Nint)
# for i in Nint:
#     operacao = input().split


# #EXERCÍCIO 3
# maximo = int(input())
# operacao = input().split()
# numero1 = int(operacao[0])
# numero2 = int(operacao[2])
# if operacao[1] == '+':
#     resultado = numero1 + numero2
#     if resultado <= maximo:
#         print("OK")
#     else:
#         print("OVERFLOW")
# elif operacao[1] == '*':
#     resultado = numero1 * numero2
#     if resultado <= maximo:
#         print("OK")
#     else:
#         print("OVERFLOW")


# #EXERCÍCIO 4
# bandejas = int(input())
# quebrados = 0
# for i in range(bandejas):
#     infos = input().split()
#     L = int(infos[0])
#     C = int(infos[1])
#     if L > C:
#         quebrados += C
#     L = 0
#     C = 0
# print(quebrados)


# #EXERCÍCIO 5
# bandejas = int(input())
# quebrados = 0
# for i in range(bandejas):
#     infos = input().split()
#     L = int(infos[0])
#     C = int(infos[1])
#     if L > C:
#         quebrados += C
#     L = 0
#     C = 0
# print(quebrados)


# #EXERCÍCIO 6
# n = list(map(int,input().split()))
# if n[0] > n[1] > n[2] > n[3] > n[4]:
#     print('D')
# elif n[0] < n[1] < n[2] < n[3] < n[4]:
#     print('C')
# else:
#     print('N')