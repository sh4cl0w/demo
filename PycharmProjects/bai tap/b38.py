def extended_gcd(a, b):
    """
    Thuật toán Euclid mở rộng.
    Trả về bộ 3 số (g, x, y) sao cho a * x + b * y = g, trong đó g là ước số chung lớn nhất của a và b.
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, p):
    """
    Tìm nghịch đảo của a modulo p sử dụng thuật toán Euclid mở rộng.
    Nếu a và p không nguyên tố cùng nhau (gcd(a, p) != 1), thì không tồn tại nghịch đảo.
    """
    g, x, y = extended_gcd(a, p)
    print(x)
    print(p)
    if g != 1:
        raise ValueError(f"Không tồn tại nghịch đảo của {a} modulo {p}")
    else:
        return x % p

a = int(input("Nhập số a: "))
p = int(input("Nhập số nguyên tố p: "))

try:
    inverse = mod_inverse(a, p)
    print(f"Nghịch đảo của {a} trong trường 𝔽_{p} là: {inverse}")
except ValueError as e:
    print(e)
