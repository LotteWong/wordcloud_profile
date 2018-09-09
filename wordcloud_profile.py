#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'LotteWong'

import itchat
from itchat.content import TEXT
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.misc import imread
import os

info = {}


# 生成词云头像
def create_prof(user, time):
    img = imread(user + '/' + time + '.png')
    text = open(user + '/' + time + '.txt', encoding='utf-8', newline='\n').read()

    # 中文分词
    cut_text = ''.join(jieba.cut(text))

    # 生成词云
    wordcloud = WordCloud(background_color='white', mask=img, stopwords=STOPWORDS, font_path='PingFang-W1.ttc',
                   max_words=2000, max_font_size=75, random_state=21)
    wordcloud.generate(cut_text)
    wordcloud.recolor(color_func=ImageColorGenerator(img))

    # 保存词云
    wordcloud.to_file(user + '/' + 'wordcloud_profile_' + time + '.png')


# 获取用户头像和信息
@itchat.msg_register(TEXT, isFriendChat=True)
def get_info(msg):
    global info

    # msg基本信息
    time = str(msg['CreateTime'])
    user = itchat.search_friends(userName=msg['FromUserName'])
    nickname = user['NickName']
    remarkname = user['RemarkName']
    py = user['PYQuanPin']
    remarkpy = user['RemarkPYQuanPin']
    prov = user['Province']
    city = user['City']
    sign = user['Signature']
    intro = msg['Content']
    if user['Sex'] == '1':
        sex = '男'
    else:
        sex = '女'

    if 'Hello world!' in msg['Content']:
        os.makedirs(nickname, exist_ok=True)

        # 微信头像
        prof = itchat.get_head_img(userName=msg['FromUserName'])
        with open(nickname + '/' + time + '.png', 'wb') as f_prof:
            f_prof.write(prof)
        print(nickname + '头像保存成功')

        # 微信资料
        info.update(
            {
                'NickName': nickname, 'RemarkName': remarkname, 'PinYin': py,  'RPinYin': remarkpy,
                'Province': prov, 'City': city,
                'Signature': sign, 'Introduce': intro,
                'Sex': sex
            }
        )
        with open(nickname + '/' + time + '.txt', 'w+', encoding='utf-8', newline='\n') as f_text:
            for key in info:
                value = info[key]
                f_text.write(value + '\n')
        print(nickname + '资料保存成功')

        # 生成词云头像
        create_prof(nickname, time)

        itchat.send_image(nickname + '/' + 'wordcloud_profile_' + time + '.png', toUserName=msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)   # 扫码登录，支持热加载
    itchat.run()
