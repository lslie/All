# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 图案.py 18-4-9 下午6:27
# SITE: https:www.jetbrains.com/pycharm/


if __name__ == "__main__":
    print("\n".join([''.join(['*' * ((x - y) % 3) if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (
                y * 0.1) ** 3 <= 0 else ' ' for x in range(-30, 30)]) for y in range(15, -15, -1)]))