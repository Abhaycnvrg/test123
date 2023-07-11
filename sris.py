#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:11:44 2023

@author: sp-01
"""

import os
import pandas as pd
abc = pd.read_csv('/home/sp-01/Downloads/sris.csv')
os.chdir('/home/sp-01/Downloads/')
abc.columns
roi = {'Google_Cost': 11.3,
       'Instagram_Cost': 0.3,
       'Facebook_Cost': 0.5,
       'Pinterest_Cost': 0.4,
       'Bing_Cost': 0.2,
       'Tiktok_Cost': 0.1}
for i in range(abc.shape[0]):
    print(i)
    a1 = abc['Instagram_Cost_sat'][i]
    a2 = abc['Bing_Cost_sat'][i]
    a3 = abc['Facebook_Cost_sat'][i]
    a4 = abc['Google_Cost_sat'][i]
    a5 = abc['Pinterest_Cost_sat'][i]
    a6 = abc['Tiktok Cost_sat'][i]
    if a1 <= 0.95 or a2 <= 0.95 or a3 <= 0.95 or a4 <= 0.95 or a5 <= 0.95 or a6 <= 0.95:
        if a1 >= 0.95:
            try:
                del roi['Instagram_Cost']
            except:
                print('already deleted')
            temp = abc['Instagram_Cost'][i]
            abc[max(roi, key=roi.get)][i] = abc[max(
                roi, key=roi.get)][i] + temp
            abc['Instagram_Cost'][i] = 0

        if a2 >= 0.95:
            try:
                del roi['Bing_Cost']
            except:
                print('already deleted')
            temp = abc['Bing_Cost'][i]
            abc[max(roi, key=roi.get)][i] = abc[max(
                roi, key=roi.get)][i] + temp
            abc['Bing_Cost'][i] = 0

        if a3 >= 0.95:
            try:
                del roi['Facebook_Cost']
            except:
                print('already deleted')
            temp = abc['Facebook_Cost'][i]
            abc[max(roi, key=roi.get)][i] = abc[max(
                roi, key=roi.get)][i] + temp
            abc['Facebook_Cost'][i] = 0
        if a4 >= 0.95:
            try:
                del roi['Google_Cost']
            except:
                print('already deleted')
            temp = abc['Google_Cost'][i]
            abc[max(roi, key=roi.get)][i] = abc[max(
                roi, key=roi.get)][i] + temp
            abc['Google_Cost'][i] = 0

        if a5 >= 0.95:
            try:
                del roi['Pinterest_Cost']
            except:
                print('already deleted')
            temp = abc['Pinterest_Cost'][i]
            abc[max(roi, key=roi.get)][i] = abc[max(
                roi, key=roi.get)][i] + temp
            abc['Pinterest_Cost'][i] = 0

        if a6 >= 0.95:
            try:
                del roi['Tiktok_Cost']
            except:
                print('already deleted')
            temp = abc['Tiktok Cost'][i]
            abc[max(roi, key=roi.get)][i] = abc[max(
                roi, key=roi.get)][i] + temp
            abc['Tiktok Cost'][i] = 0

    else:
        breaking_point = i
        break
abc.to_csv('file_sris.csv')
