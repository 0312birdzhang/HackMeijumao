#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年6月20日

@author: 0312birdzhang
@summary: Hack for meijumao.cc
'''
import m3u8

m3u8_obj = m3u8.load('http://ts.ystt.me/m3u8_Game_of_Thrones_S06E09-1.m3u8?pm3u8/0/expires/18000&e=1466426663&token=cPLJw_uAAGMXzHbzxCoqDtiTVD4LiTw6Oc19fxI2:NltqKTuWqRVo0TTdioXZdvBlmF0=')  # this could also be an absolute filename
m3u8_obj.dump("F:\\test\\test.playlist")
