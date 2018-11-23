# -*- coding:utf-8 -*-
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from collections import OrderedDict

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv(r'./shzf_gj_zm.csv', header=0, index_col=0)

# 分析国家在分组中的分布情况
country = OrderedDict()
country = {840:'美国', 356:'印度', 608:'菲律宾', 704:'越南', 586:'巴基斯坦',
	360:'印度尼西亚', 410:'韩国',392:'日本', 170:'哥伦比亚', 458:'马来西亚',
	178:'刚果（布）', 508:'莫桑比克',604:'秘鲁', 764:'泰国', 834:'坦桑尼亚',
	566:'尼日利亚', 144:'斯里兰卡', 36:'澳大利亚', 124:'加拿大', 496:'蒙古',
	642:'罗马尼亚', 364:'伊朗', 702:'新加坡', 40:"奥地利", 643:'俄罗斯联邦',
	208:'丹麦', 288:'加纳', 694:'塞拉利昂', 430:'利比里亚', 12:'阿尔及利亚',
	120:'喀麦隆', 100:'保加利亚', 4:'阿富汗', 826:'英国', 56:'比利时',
	792:'土耳其', 520:'瑙鲁', 752:'瑞典', 76:'巴西', 250:'法国', 408:'朝鲜',
	528:'荷兰', 324:'几内亚', 862:'委内瑞拉', 466:'马里', 480:'毛里求斯',
	188:'哥斯达黎加', 504:'摩洛哥', 108:'布隆迪', 484:'墨西哥',268:'格鲁吉亚',
	418:'老挝', 148:'乍得', 231:'埃塞俄比亚', 400:'约旦', 716:'津巴布韦',
	554:'新西兰', 584:'马绍尔群岛'}

# 罪名分布情况
zm = OrderedDict()
zm = {  '201':'盗窃罪', '124':'信用卡诈骗罪', '206':'职务侵占罪', '152':'合同诈骗罪',
		'316':'非法持有毒品罪', '200':'抢劫罪', '207':'挪用资金罪','86':'非国家工作人员受贿罪',
		'121':'票据诈骗罪', '4146':'妨害信用卡管理罪', '166':'强奸罪',
		'153':'非法经营罪','1':'无编码', '146':'销售侵权复制品罪', '102':'非法吸收公众存款罪',
		'271':'出售入境证件罪', '60':'生产销售伪劣产品罪', '116':'逃汇罪',
		'97':'持有,使用假币罪', '69':'走私罪', '202':'诈骗罪', '203':'抢夺罪', 
		'16':'放火罪', '200':'抢劫罪', '247':'赌博罪', '142':'销售假冒注册商标的商品罪',
		'233':'寻衅滋事罪', '169':'猥亵儿童罪', '170':'非法拘禁罪', '78':'走私普通货物、物品罪',
		'141':'假冒注册商标罪', '146':'销售侵权复制品罪','4151':'开设赌场罪',
		'268':'组织他人偷越国境罪', '330':'协助组织卖淫罪', '73':'走私文物罪',
		'163':'过失致人死亡罪', '122':'金融票证诈骗罪', '162':'故意杀人罪', '328':'组织卖淫罪',
		'316':'非法持有毒品罪', '164':"故意伤害罪", '214':'妨害公务罪', '171':'绑架罪',
		'166':'强奸罪', '209':"挪用资金罪", '340':'组织淫秽表演罪', '272':'运送他人偷越国境罪',
		'4':"分裂国家罪", '123':'信用证诈骗罪', '119':'集资诈骗罪'}

# 首先看国家的分布情况，用柱状图表示出国家和人数

def country_analysis():
	X = range(len(country))
	print(X)
	y = [df[df['gjdq'] == value]['gjdq'].count() for value in country]
	X_ticks = list(country.values())

	#　画柱状图
	plt.figure(figsize=(16,8))
	plt.title('国家比例分析')
	plt.xlabel('国家')
	plt.ylabel('人数')
	plt.xticks(X, X_ticks, rotation=60)
	plt.yticks(np.arange(1, 55, 2))
	b = plt.bar(X, y, width=0.6)
	for x, i in zip(X, b):
		plt.text(x, i.get_height(), "%d" % i.get_height(), ha='center', va='bottom')
	plt.tight_layout()
	plt.show()

country_analysis()