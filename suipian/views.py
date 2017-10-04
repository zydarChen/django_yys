# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from suipian.models import Table


def index(request):
    table_list = Table.objects.all()
    return render(request, 'index.html', context={'table_list': table_list})


def update(request):
    name = request.POST['name']
    bi_an_hua = request.POST['bi_an_hua']
    ci_mu = request.POST['ci_mu']
    da_gou = request.POST['da_gou']
    hua_niao = request.POST['hua_niao']
    huang = request.POST['huang']
    huang_chuang = request.POST['huang_chuang']
    hui_ye_ji = request.POST['hui_ye_ji']
    jiu_tun = request.POST['jiu_tun']
    qing_deng = request.POST['qing_deng']
    xiao_lu = request.POST['xiao_lu']
    xue_tong_zi = request.POST['xue_tong_zi']
    yan_mo = request.POST['yan_mo']
    yao_dao = request.POST['yao_dao']
    yi_mu = request.POST['yi_mu']
    yu_zao_qian = request.POST['yu_zao_qian']
    if Table.objects.filter(name=name).count() > 0:
        line = Table.objects.get(name=name)
        if bi_an_hua:
            line.bi_an_hua = bi_an_hua
        if ci_mu:
            line.ci_mu = ci_mu
        if jiu_tun:
            line.jiu_tun = jiu_tun
        if da_gou:
            line.da_gou = da_gou
        if hua_niao:
            line.hua_niao = hua_niao
        if huang:
            line.huang = huang
        if huang_chuang:
            line.huang_chuang = huang_chuang
        if hui_ye_ji:
            line.hui_ye_ji = hui_ye_ji
        if qing_deng:
            line.qing_deng = qing_deng
        if xiao_lu:
            line.xiao_lu = xiao_lu
        if xue_tong_zi:
            line.xue_tong_zi = xue_tong_zi
        if yan_mo:
            line.yan_mo = yan_mo
        if yao_dao:
            line.yao_dao = yao_dao
        if yi_mu:
            line.yi_mu = yi_mu
        if yu_zao_qian:
            line.yu_zao_qian = yu_zao_qian
        line.save()
    else:
        Table(name=name, bi_an_hua=bi_an_hua, ci_mu=ci_mu,
              da_gou=da_gou, hua_niao=hua_niao, huang=huang,
              huang_chuang=huang_chuang, hui_ye_ji=hui_ye_ji,
              jiu_tun=jiu_tun, qing_deng=qing_deng, xiao_lu=xiao_lu,
              xue_tong_zi=xue_tong_zi, yan_mo=yan_mo, yao_dao=yao_dao,
              yi_mu=yi_mu, yu_zao_qian=yu_zao_qian).save()
    return redirect('index.html')
