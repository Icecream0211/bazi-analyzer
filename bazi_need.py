#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 钉钉、抖音或微信pythontesting 钉钉群21734177
# CreateDate: 2019-2-21

import argparse
import collections
import pprint
import datetime
import json

from lunar_python import Lunar, Solar
from colorama import init

from datas import *
from sizi import summarys
from common import *
from yue import months



 
def get_shens(gans, zhis, gan_, zhi_,me):
    
    all_shens = []
    for item in year_shens:
        if zhi_ in year_shens[item][zhis.year]:    
            all_shens.append(item)
                
    for item in month_shens:
        if gan_ in month_shens[item][zhis.month] or zhi_ in month_shens[item][zhis.month]:     
            all_shens.append(item)
                
    for item in day_shens:
        if zhi_ in day_shens[item][zhis.day]:     
            all_shens.append(item)
                
    for item in g_shens:
        if zhi_ in g_shens[item][me]:    
            all_shens.append(item) 
    if all_shens:  
        return "  神:" + ' '.join(all_shens)
    else:
        return ""
                
def jin_jiao(first, second):
    return True if Zhi.index(second) - Zhi.index(first) == 1 else False

def is_ku(zhi):
    return True if zhi in "辰戌丑未" else False  

def zhi_ku(zhi, items):
    return True if is_ku(zhi) and min(zhi5[zhi], key=zhi5[zhi].get) in items else False
 
 

 


## 返回八字相关必要信息
def get_bazi_need(year:int,month:int,day:int,time:int,isSolar:bool=True,isRunYuer:bool=False,gender:bool=True):

    print(year,month,day,time,isSolar,isRunYuer,gender)
    Gans = collections.namedtuple("Gans", "year month day time")
    Zhis = collections.namedtuple("Zhis", "year month day time")

    result = {}
    result["is_solar"] = "公历" if isSolar else "农历"
    result["is_run_yuer"] = "闰月" if isRunYuer else "非闰月"
    result["gender"] = "男" if gender else "女"
    ## 是否公公历
    if isSolar:
        solar = Solar.fromYmdHms(int(year), int(month), int(day), int(time), 0, 0)
        lunar = solar.getLunar()
    else:
        month_ = int(month)*-1 if isRunYuer else int(month)
        lunar = Lunar.fromYmdHms(int(year), month_, int(day),int(time), 0, 0)
        solar = lunar.getSolar()

    day = lunar
    ba = lunar.getEightChar() 
    gans = Gans(year=ba.getYearGan(), month=ba.getMonthGan(), day=ba.getDayGan(), time=ba.getTimeGan())
    zhis = Zhis(year=ba.getYearZhi(), month=ba.getMonthZhi(), day=ba.getDayZhi(), time=ba.getTimeZhi())
    yun = ba.getYun(1 if gender else 0 )

    me = gans.day
    month = zhis.month
    zhus = [item for item in zip(gans, zhis)]



    result["solar_date"] = "{}年{}月{}日".format(solar.getYear(), solar.getMonth(), solar.getDay())
    result["lunar_date"] = "{}年{}月{}日".format(lunar.getYear(), lunar.getMonth(), lunar.getDay())

    gan_shens = []
    for seq, item in enumerate(gans):    
        if seq == 2:
            gan_shens.append('--')
        else:
            gan_shens.append(ten_deities[me][item])

    zhi_shens = [] # 地支的主气神
    for item in zhis:
        d = zhi5[item]
        zhi_shens.append(ten_deities[me][max(d, key=d.get)])


    shens = gan_shens + zhi_shens

    zhi_shens2 = [] # 地支的所有神，包含余气和尾气, 混合在一起
    zhi_shen3 = [] # 地支所有神，字符串格式
    for item in zhis:
        d = zhi5[item]
        tmp = ''
        for item2 in d:
            zhi_shens2.append(ten_deities[me][item2])
            tmp += ten_deities[me][item2]
        zhi_shen3.append(tmp)
    shens2 = gan_shens + zhi_shens2
        

    ## 八字计算
    bazi  = {'year': '', 'month': '', 'day': '','hour':''}
    bazi['year'] = gans.year+zhis.year
    bazi['month'] = gans.month+zhis.month
    bazi['day'] = gans.day+zhis.day
    bazi['hour'] = gans.time+zhis.time
    
    result["bazi"] = bazi


    ## 五行分值
    scores = {"金":0, "木":0, "水":0, "火":0, "土":0}
    ## 干支分值
    gan_scores = {"甲":0, "乙":0, "丙":0, "丁":0, "戊":0, "己":0, "庚":0, "辛":0,
                "壬":0, "癸":0}   

    for item in gans:  
        scores[gan5[item]] += 5
        gan_scores[item] += 5
    for item in list(zhis) + [zhis.month]:  
        for gan in zhi5[item]:
            scores[gan5[gan]] += zhi5[item][gan]
            gan_scores[gan] += zhi5[item][gan]

    result["wuxing_scores"] = scores
    result["gan_scores"] = gan_scores

    ##强弱计算
    weak = True
    me_status = []
    for item in zhis:
        me_status.append(ten_deities[me][item])
        if ten_deities[me][item] in ('长', '帝', '建'):
            weak = False
    if weak:
        if shens.count('比') + me_status.count('库') >2:
            weak = False
    # 网上的计算
    me_attrs_ = ten_deities[me].inverse

    remark = "通常>29为强，需要参考月份、坐支等"
    strong = gan_scores[me_attrs_['比']] + gan_scores[me_attrs_['劫']] + gan_scores[me_attrs_['枭']] + gan_scores[me_attrs_['印']]

    strong_weak_score =  {"strong":strong,"weak":weak,"remark":remark}

    result["strong_weak_score"] = strong_weak_score
 
    ##大运计算
    seq = Gan.index(gans.year)
    #女
    if not gender:
        if seq % 2 == 0:
            direction = -1
        else:
            direction = 1
    else: #男
        if seq % 2 == 0:
            direction = 1
        else:
            direction = -1

    dayuns = []
    gan_seq = Gan.index(gans.month)
    zhi_seq = Zhi.index(zhis.month)
    for i in range(12):
        gan_seq += direction
        zhi_seq += direction
        dayuns.append(Gan[gan_seq%10] + Zhi[zhi_seq%12])

    result["da_yun"] = dayuns

    statuses = [ten_deities[me][item] for item in zhis]
    
    
    me_lu = ten_deities[me].inverse['建']

    me_jue = ten_deities[me].inverse['绝']
    me_tai = ten_deities[me].inverse['胎']
    me_di = ten_deities[me].inverse['帝']
    shang = ten_deities[me].inverse['伤']
    shang_lu = ten_deities[shang].inverse['建']
    shang_di = ten_deities[shang].inverse['帝']
    yin = ten_deities[me].inverse['印']
    yin_lu = ten_deities[yin].inverse['建']
    xiao = ten_deities[me].inverse['枭']
    xiao_lu = ten_deities[xiao].inverse['建']
    cai = ten_deities[me].inverse['财']
    cai_lu = ten_deities[cai].inverse['建']
    cai_di = ten_deities[cai].inverse['帝']
    piancai = ten_deities[me].inverse['才']
    piancai_lu = ten_deities[piancai].inverse['建']
    piancai_di = ten_deities[piancai].inverse['帝']
    guan = ten_deities[me].inverse['官']
    guan_lu = ten_deities[guan].inverse['建']
    guan_di = ten_deities[guan].inverse['帝']
    sha = ten_deities[me].inverse['杀']
    sha_lu = ten_deities[sha].inverse['建']
    sha_di = ten_deities[sha].inverse['帝']

    jie = ten_deities[me].inverse['劫']
    shi = ten_deities[me].inverse['食']
    shi_lu = ten_deities[shi].inverse['建']
    shi_di = ten_deities[shi].inverse['帝']

    ##调侯计算
    y_th = tiaohous['{}{}'.format(me, zhis[1])]
    result["tiao_hou"] = y_th
    ##金不换大运
    y_jbh=jinbuhuan['{}{}'.format(me, zhis[1])]
    result["jin_bu_huan"] = y_jbh


    ##格局
    y_gj = [ges[ten_deities[me]['本']][zhis[1]]]
    if len(set('寅申巳亥')&set(zhis)) == 0:
        y_gj.append("缺四生：一生不敢作为")
    if len(set('子午卯酉')&set(zhis)) == 0:
        y_gj.append("缺四柱地支缺四正，一生避是非")
    if len(set('辰戌丑未')&set(zhis)) == 0:
        y_gj.append("四柱地支缺四库，一生没有潜伏性凶灾。")
    if ( '甲', '戊', '庚',) in (tuple(gans)[:3], tuple(gans)[1:]):
        y_gj.append("地上三奇：白天生有申佳，需身强四柱有贵人。")
    if ( '辛', '壬', '癸',) in (tuple(gans)[:3], tuple(gans)[1:]):
        y_gj.append("人间三奇，需身强四柱有贵人。")
    if ( '乙', '丙', '丁',) in (tuple(gans)[:3], tuple(gans)[1:]):
        y_gj.append("天上三奇：晚上生有亥佳，需身强四柱有贵人。")
    if zhi_shens2.count('亡神') > 1:
        y_gj.append("二重亡神，先丧母；")
        
    if get_empty(zhus[2],zhis.time):
        y_gj.append("时坐空亡，子息少。 母法P24-41 母法P79-4：损破祖业，后另再成就。")
        
    if zhis.count(me_jue) + zhis.count(me_tai) > 2:
        y_gj.append("胎绝超过3个：夭或穷。母法P24-44 丁未 壬子 丙子 戊子")
    
    not_yang = False if Gan.index(me) % 2 == 0 else True
    if not_yang and zhi_ku(zhis[2], (me,jie)) and zhi_ku(zhis[3], (me,jie)):
        y_gj.append("阴日主时日支入比劫库：性格孤独，难发达。母法P28-112 甲申 辛未 辛丑 己丑 母法P55-11 为人孤独，且有灾疾")


    result["ge_ju"] = y_gj


    ##温度分数
    temps_scores = temps[gans.year] + temps[gans.month] + temps[me] + temps[gans.time] + temps[zhis.year] + temps[zhis.month]*2 + temps[zhis.day] + temps[zhis.time]
    remark = "正为暖燥，负为寒湿，正常区间[-6,6]"
    result["temp_scores"] = {"temps_scores":temps_scores,"remark":remark}



    dy_byYear = []
    dy_tenYear = []
    for dayun in yun.getDaYun()[1:]:
        ten_dayun = {}
        gan_ = dayun.getGanZhi()[0]
        zhi_ = dayun.getGanZhi()[1]
        fu = '*' if (gan_, zhi_) in zhus else " "
        zhi5_ = ''
        for gan in zhi5[zhi_]:
            zhi5_ = zhi5_ + "{}{}　".format(gan, ten_deities[me][gan]) 
        
        zhi__ = set() # 大运地支关系
        
        for item in zhis:
        
            for type_ in zhi_atts[zhi_]:
                if item in zhi_atts[zhi_][type_]:
                    zhi__.add(type_ + ":" + item)
        zhi__ = '  '.join(zhi__)
        
        empty = chr(12288)
        if zhi_ in empties[zhus[2]]:
            empty = '空'        
        
        jia = ""
        if gan_ in gans:
            for i in range(4):
                if gan_ == gans[i]:
                    if abs(Zhi.index(zhi_) - Zhi.index(zhis[i])) == 2:
                        jia = jia + "  --夹：" +  Zhi[( Zhi.index(zhi_) + Zhi.index(zhis[i]) )//2]
                    if abs( Zhi.index(zhi_) - Zhi.index(zhis[i]) ) == 10:
                        jia = jia + "  --夹：" +  Zhi[(Zhi.index(zhi_) + Zhi.index(zhis[i]))%12]
        
        ten_dayun["start_age"] = dayun.getStartAge()
        ten_dayun["gan_zhi"] = dayun.getGanZhi()
       
        out = "{1:<4d}{2:<5s}{3} {15} {14} {13}  {4}:{5}{8}{6:{0}<6s}{12}{7}{8}{9} - {10:{0}<10s} {11}".format(
            chr(12288), dayun.getStartAge(), '', dayun.getGanZhi(),ten_deities[me][gan_], gan_,check_gan(gan_, gans), 
            zhi_, yinyang(zhi_), ten_deities[me][zhi_], zhi5_, zhi__,empty, fu, nayins[(gan_, zhi_)], ten_deities[me][zhi_]) 
    
        gan_index = Gan.index(gan_)
        zhi_index = Zhi.index(zhi_)
        out = out + jia + get_shens(gans, zhis, gan_, zhi_,me)
        ten_dayun["remark"] = out
        ten_dayun["liunian"] = []
        zhis2 = list(zhis) + [zhi_]
        gans2 = list(gans) + [gan_]
        for liunian in dayun.getLiuNian():
            liunian_dayun = {}
            gan2_ = liunian.getGanZhi()[0]
            zhi2_ = liunian.getGanZhi()[1]
            fu2 = '*' if (gan2_, zhi2_) in zhus else " "
            #print(fu2, (gan2_, zhi2_),zhus)
            
            zhi6_ = ''
            for gan in zhi5[zhi2_]:
                zhi6_ = zhi6_ + "{}{}　".format(gan, ten_deities[me][gan])        
            
            # 大运地支关系
            zhi__ = set() # 大运地支关系
            for item in zhis2:
            
                for type_ in zhi_atts[zhi2_]:
                    if type_ == '破':
                        continue
                    if item in zhi_atts[zhi2_][type_]:
                        zhi__.add(type_ + ":" + item)
            zhi__ = '  '.join(zhi__)
            
            empty = chr(12288)
            if zhi2_ in empties[zhus[2]]:
                empty = '空'       
            out = "{1:>3d} {2:<5d}{3} {15} {14} {13}  {4}:{5}{8}{6:{0}<6s}{12}{7}{8}{9} - {10:{0}<10s} {11}".format(
                chr(12288), liunian.getAge(), liunian.getYear(), gan2_+zhi2_,ten_deities[me][gan2_], gan2_,check_gan(gan2_, gans2), 
                zhi2_, yinyang(zhi2_), ten_deities[me][zhi2_], zhi6_, zhi__,empty, fu2, nayins[(gan2_, zhi2_)], ten_deities[me][zhi2_]) 
            
            liunian_dayun["age"] = liunian.getAge()
            liunian_dayun["year"] = liunian.getYear()
            liunian_dayun["gan_zhi"] = liunian.getGanZhi()
            liunian_dayun["gan_zhi_2"] = gan2_+zhi2_

            jia = ""
            if gan2_ in gans2:
                for i in range(5):
                    if gan2_ == gans2[i]:
                        zhi1 = zhis2[i]
                        if abs(Zhi.index(zhi2_) - Zhi.index(zhis2[i])) == 2:
                            # print(2, zhi2_, zhis2[i])
                            jia = jia + "  --夹：" +  Zhi[( Zhi.index(zhi2_) + Zhi.index(zhis2[i]) )//2]
                        if abs( Zhi.index(zhi2_) - Zhi.index(zhis2[i]) ) == 10:
                            # print(10, zhi2_, zhis2[i])
                            jia = jia + "  --夹：" +  Zhi[(Zhi.index(zhi2_) + Zhi.index(zhis2[i]))%12]  

                        if (zhi1 + zhi2_ in gong_he) and (gong_he[zhi1 + zhi2_] not in zhis):
                            jia = jia + "  --拱：" + gong_he[zhi1 + zhi2_]
                            
            out = out + jia + get_shens(gans, zhis, gan2_, zhi2_,me)
            all_zhis = set(zhis2) | set(zhi2_)
            if set('戌亥辰巳').issubset(all_zhis):
                out = out + "  天罗地网：戌亥辰巳"
            if set('寅申巳亥').issubset(all_zhis) and len(set('寅申巳亥')&set(zhis)) == 2 :
                out = out + "  四生：寅申巳亥"   
            if set('子午卯酉').issubset(all_zhis) and len(set('子午卯酉')&set(zhis)) == 2 :
                out = out + "  四败：子午卯酉"  
            if set('辰戌丑未').issubset(all_zhis) and len(set('辰戌丑未')&set(zhis)) == 2 :
                out = out + "  四库：辰戌丑未"  
                ##result = [item.strip() for item in out.split() if item.strip()]
                ##print(result)
            liunian_dayun["remark"] = out
            ten_dayun["liunian"].append(liunian_dayun)
        dy_byYear.append(ten_dayun)
    result["liunian_dayun"] = dy_byYear
    return result







description = '''


parser = argparse.ArgumentParser(description=description,
                                formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('year', action="store", help=u'year')
parser.add_argument('month', action="store", help=u'month')
parser.add_argument('day', action="store", help=u'day')
parser.add_argument('time', action="store",help=u'time')    
parser.add_argument("--start", help="start year", type=int, default=1850)
parser.add_argument("--end", help="end year", default='2030')
parser.add_argument('-b', action="store_true", default=False, help=u'直接输入八字')
parser.add_argument('-g', action="store_true", default=False, help=u'是否采用公历')
parser.add_argument('-r', action="store_true", default=False, help=u'是否为闰月，仅仅使用于农历')
parser.add_argument('-n', action="store_true", default=False, help=u'是否为女，默认为男')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0 Rongzhong xu 2022 06 15')
options = parser.parse_args()
  

result = get_bazi_need(options.year, options.month, options.day, options.time,options.g,options.r,options.n)


print(json.dumps(result,ensure_ascii=False))
'''