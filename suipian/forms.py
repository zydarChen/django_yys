from django import forms
from models import Table


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'bi_an_hua', 'ci_mu', 'da_gou', 'hua_niao', 'huang', 'huang_chuang', 'hui_ye_ji', 'jiu_tun', 'qing_deng', 'xiao_lu', 'xue_tong_zi', 'yan_mo', 'yao_dao', 'yi_mu', 'yu_zao_qian']
