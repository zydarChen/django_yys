# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=100)
    bi_an_hua = models.CharField(max_length=10)  # 彼岸花
    ci_mu = models.CharField(max_length=10)  # 茨木童子
    da_gou = models.CharField(max_length=10)  # 大天狗
    hua_niao = models.CharField(max_length=10)  # 花鸟卷
    huang = models.CharField(max_length=10)  # 荒
    huang_chuang = models.CharField(max_length=10)  # 荒川
    hui_ye_ji = models.CharField(max_length=10)  # 辉夜姬
    jiu_tun = models.CharField(max_length=10)  # 酒吞童子
    qing_deng = models.CharField(max_length=10)  # 青行灯
    xiao_lu = models.CharField(max_length=10)  # 小鹿男
    xue_tong_zi = models.CharField(max_length=10)  # 雪童子
    yan_mo = models.CharField(max_length=10)  # 阎魔
    yao_dao = models.CharField(max_length=10)  # 妖刀姬
    yi_mu = models.CharField(max_length=10)  # 一目连
    yu_zao_qian = models.CharField(max_length=10)  # 玉藻前

    def __unicode__(self):
        return self.name
