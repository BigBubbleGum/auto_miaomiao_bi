#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 本程序以三星s7手机为例，屏幕分辨率1080*1920
# 使用的是绝对坐标，分辨率相同的安卓手机可以直接使用，其他分辨率手机需要手动修改坐标
# 仅限安卓，iphone不适用
# 使用前请先安装adb，然后进去淘宝的“618理想大赢家”界面

import os
import time
from PIL import Image


def screencap():
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')


def qu_guang_dian():
    print('====== 进入领喵币中心,去逛店 ======')
    for i in range(1, 50):
        os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
        os.system('adb shell input tap 900 1670')  # 点击领喵币
        print('第{}次去逛店...'.format(i))
        time.sleep(1)
        os.system('adb shell input tap 900 870')  # 点击去逛店，然后等15s
        print('进入店铺,浏览页面中，请等待15s...')
        time.sleep(15)

        screencap()
        img = Image.open('screen.png')
        # print(img.getpixel((970, 1128)))
        if img.getpixel((970, 1128)) == (241, 196, 201, 255):
            os.system('adb shell input tap 970 1130')  # 点击得喵币
            print('已点击喵币，返回中...')
            time.sleep(1)
            os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
            time.sleep(1)
        else:
            print('已完成50次去逛店任务')
            break
    print('已完成去逛店领取喵币任务')
    os.system('adb shell input keyevent KEYCODE_BACK')  # 返回


def kan_zhi_bo():
    print('====== 进入领喵币中心，看直播 ======')
    for i in range(1, 4):
        os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
        os.system('adb shell input tap 900 1670')  # 点击下方领喵币
        screencap()
        img = Image.open('screen.png')
        # print(img.getpixel((111, 1824)))
        if img.getpixel((111, 1824)) == (248, 239, 237, 255):
            print('第{}次去看直播...'.format(i))
            time.sleep(1)
            os.system('adb shell input tap 900 1800')  # 点击去看直播，然后等12s
            print('观看直播中，请等待20s...')
            time.sleep(20)
            os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
        else:
            print('3次看直播任务已完成')
            break
    print('已完成去看直播领取喵币任务')
    os.system('adb shell input tap 996 136')  # 点击右上角关闭


def liu_lan_hui_chang():
    print('====== 进入领喵币中心，浏览会场 ======')
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 900 1670')  # 点击下方领喵币
    for i in range(1, 4):
        screencap()
        img = Image.open('screen.png')
        # print(img.getpixel((856, 1050)))
        if img.getpixel((856, 1050)) == (244, 60, 74, 255):
            os.system('adb shell input tap 900 1050')
            print('第{}次去浏览会场...'.format(i))
            time.sleep(6)
            os.system('adb shell input tap 150 960')  # 点击去会场
            print('浏览会场中，请等待15s...')
            time.sleep(15)
            os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
            os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
        else:
            break
            print('会场任务已完成')
    print('已完成浏览会场领取喵币任务')
    os.system('adb shell input tap 996 136')  # 点击右上角关闭


kan_zhi_bo()
liu_lan_hui_chang()
qu_guang_dian()
