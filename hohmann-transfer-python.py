"""
ホーマン遷移軌道をPythonで計算する｜衛星を別の軌道へ運ぶΔv

元記事: https://space.yurufuwa.work/learn/hohmann-transfer-python
ゆるふわ宇宙・航空 (space.yurufuwa.work) の解説記事から抜粋したコードです。
"""

import numpy as np

GM = 3.986e14
R_earth = 6.371e6

def hohmann(alt1_km, alt2_km):
    r1 = R_earth + alt1_km * 1000
    r2 = R_earth + alt2_km * 1000
    a = (r1 + r2) / 2                       # 遷移楕円の長半径

    v1 = np.sqrt(GM / r1)                   # 出発の円軌道速度
    v2 = np.sqrt(GM / r2)                   # 到着の円軌道速度
    v_peri = np.sqrt(GM * (2/r1 - 1/a))     # 楕円の近地点速度
    v_apo  = np.sqrt(GM * (2/r2 - 1/a))     # 楕円の遠地点速度

    dv1 = v_peri - v1                        # 1回目の噴射
    dv2 = v2 - v_apo                         # 2回目の噴射
    return dv1, dv2, dv1 + dv2

dv1, dv2, total = hohmann(400, 35786)       # LEO(400km) → GEO(静止軌道)
print(f"1回目Δv: {dv1:.0f} m/s")
print(f"2回目Δv: {dv2:.0f} m/s")
print(f"合計Δv : {total:.0f} m/s")

for name, alt in [("ISS高度", 400), ("中軌道", 10000), ("静止軌道", 35786)]:
    _, _, total = hohmann(400, alt)
    print(f"400km → {name}({alt}km): 合計Δv {total:.0f} m/s")
