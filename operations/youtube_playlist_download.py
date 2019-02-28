# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:33:28 2019
Used to Download full youtube playlist of a channel 
Youtube channel videos download
@author: ayuvaram

Note: need pre-installed pytube library
"""

from pytube import Playlist
'''
Please provide the link of youtube which consists of full playlist
'''
playlist_link = 'https://www.youtube.com/playlist?list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0'
pl = Playlist(playlist_link)
pl.populate_video_urls()
print(pl.video_urls)
print ("List size is %s:" % len(pl.video_urls))
pl.download_all()
print ("----DOWNLOAD COMPLETED-----")
