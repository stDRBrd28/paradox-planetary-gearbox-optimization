import numpy as np

# 関数定義


def inv(a):
    inv = np.tan(a) - a
    return inv


def i_inv(i, eps):
    a = 1  # 初期値
    error = i - inv(a)
    while (1):
        a = a - error/(1-1/(np.cos(a))**2)
        error = i - inv(a)
        if np.abs(error) < eps:
            return a


# 条件
eps = 1.0e-6  # inv関数の逆関数を求める際の許容誤差
sk = 0.0001  # 歯先の厚さの限界値(転位すると歯先幅が小さくなるので限界値を定めておく)

# 歯面の摩擦係数(効率の計算に使うだけ．最適設計自体には無関与)
mu = 0.1

###################################################################################
# パラメータ
###################################################################################

# モジュール
mod = 0.8

# 歯数
za = 12
zb = 12
zc = 36
zd = 39

# 圧力角
a_a = 20 * np.pi / 180
a_b = 20 * np.pi / 180
a_c = 20 * np.pi / 180
a_d = 20 * np.pi / 180

# 噛み合い率
eps_c = 1.4
eps_d = 1.4
eps_a0 = 1.1

# 転位係数
xd = 0
xb = 0.5

########################################################
# 計算

eps_1c = eps_c/2
eps_2c = eps_c/2

# 基礎円半径
r_g_a = mod*za*np.cos(a_a)/2
r_g_b = mod*zb*np.cos(a_b)/2
r_g_c = mod*zc*np.cos(a_c)/2
r_g_d = mod*zd*np.cos(a_d)/2

inv_a_bd = 2*np.tan(a_c)*(xd-xb)/(zd-zb) + inv(a_c)
a_bd = i_inv(inv_a_bd, eps)
cos_a_ba = (za+zb)/(zd-zb)*np.cos(a_bd)
a_ba = np.arccos(cos_a_ba)
cos_a_bc = (zc-zb)/(zd-zb)*np.cos(a_bd)
a_bc = np.arccos(cos_a_bc)

# print('a_bd={:f}'.format(a_bd*180/np.pi))
# print('a_ba={:f}'.format(a_ba*180/np.pi))
# print('a_bc={:f}'.format(a_bc*180/np.pi))

xc = (zc-zb)/(2*np.tan(a_c))*(inv(a_bc) - inv(a_c)) + xb
# print('xc={:f}'.format(xc))

# xcが歯先とがりを起こしていないかの確認
r_h_c = (zc*mod/2 + mod*(1+xc))
a_h_c = np.arccos(r_g_c/r_h_c)
if r_h_c*(np.pi/2/zc + 2*xc*np.tan(a_c)/zc + (inv(a_c) - inv(a_h_c))) < sk:
    print('{:f} < {:f}'.format(r_h_c*(np.pi/2/zc + 2*xc *
          np.tan(a_c)/zc + (inv(a_c) - inv(a_h_c))), sk))
    print('Cの歯車に歯先とがりあり')
    exit()

# xbが歯先とがりを起こしていないかの確認
r_h_b = (zb*mod/2 + mod*(1+xb))
a_h_b = np.arccos(r_g_b/r_h_b)
if r_h_b*(np.pi/2/zb + 2*xb*np.tan(a_b)/zb + (inv(a_b) - inv(a_h_b))) < sk:
    print('{:f} < {:f}'.format(r_h_b*(np.pi/2/zb + 2*xb *
          np.tan(a_b)/zb + (inv(a_b) - inv(a_h_b))), sk))
    print('Bの歯車に歯先とがりあり')
    exit()

# bとcの噛み合いについて
r_k_c = r_g_c*np.sqrt((np.tan(a_bc) - np.pi*eps_c/zc)**2 + 1)
r_k_bc = r_g_b*np.sqrt((np.pi*eps_c/zb + np.tan(a_bc))**2 + 1)

# a_k_bc =
r_h_k_bc = r_k_bc

eps_0c = 1 - eps_1c - eps_2c + eps_1c**2 + eps_2c**2
nu_c = 1 - mu*np.pi*(1/zb-1/zc)*eps_0c
# print(nu_c)

r_k_d = r_g_d*np.sqrt((np.tan(a_bd) - np.pi*eps_d/zd)**2 + 1)
r_k_bd = r_g_b*np.sqrt((np.pi*eps_d/zb + np.tan(a_bd))**2 + 1)

eps_0d = 1 - eps_d + eps_d**2/4
nu_d = 1 - mu*np.pi*(1/zb-1/zd)*eps_0d
# print(nu_d)

eps_1a = zb/2/np.pi*(np.sqrt((r_h_b/r_g_b)**2 - 1) - np.tan(a_ba))
if eps_1a + 0.5 >= eps_a0:
    eps_2a = 0.5
else:
    print('eps_1a+0.5= {:f} < {:f}'.format(eps_1a+0.5, eps_a0))
    print('最適設計じゃないのでやり直し')
    exit()

r_k_a = r_g_a*np.sqrt((2*np.pi*eps_2a/za + np.tan(a_ba))**2 + 1)

eps_0a = 1 - eps_1a - eps_2a + eps_1a**2 + eps_2a**2
nu_a = 1 - mu*np.pi*(1/zb+1/za)*eps_0a
# print(nu_a)

xa = (za+zb)/(2*np.tan(a_c))*(inv(a_ba) - inv(a_c)) - xb

nu = (1-zc/zd)/(1-zc/zd*nu_c*nu_d)*(1+zc/za*nu_a*nu_c)/(1+zc/za)
print('この不思議遊星歯車列の効率は{:f}%です'.format(nu*100))

print('噛み合いピッチ円直径 a_ba:{:f}'.format(r_g_a/np.cos(a_ba)))
print('噛み合いピッチ円直径 b_ba:{:f}'.format(r_g_b/np.cos(a_ba)))
print('噛み合いピッチ円直径 b_bc:{:f}'.format(r_g_b/np.cos(a_bc)))
print('噛み合いピッチ円直径 c_bc:{:f}'.format(r_g_c/np.cos(a_bc)))
print('噛み合いピッチ円直径 d_bd:{:f}'.format(r_g_d/np.cos(a_bd)))
print('xa={:f}'.format(xa))
print('xb={:f}'.format(xb))
print('xc={:f}'.format(xc))
print('xd={:f}'.format(xd))
