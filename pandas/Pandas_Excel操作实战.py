import pandas as pd
# import xlrd
# import xlwt

month = 3
# 读取各基地CRM退货数据
goods_rejected_8010 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02011已处理CRM退货收货检验申请{month}(8010).xls')
goods_rejected_8012 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02011已处理CRM退货收货检验申请{month}(8012).xls')
goods_rejected_8020 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02011已处理CRM退货收货检验申请{month}(8020).xls')
goods_rejected_8030 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02011已处理CRM退货收货检验申请{month}(8030).xls')
goods_rejected_8040 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02011已处理CRM退货收货检验申请{month}(8040).xls')
goods_rejected_8050 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02011已处理CRM退货收货检验申请{month}(8050).xls')

# 拼接数据表
goods_rejected_all = pd.concat([goods_rejected_8010,
                                goods_rejected_8012,
                                goods_rejected_8020,
                                goods_rejected_8030,
                                goods_rejected_8040,
                                goods_rejected_8050]).reset_index(drop=True)

# 写入文件
file = pd.ExcelWriter(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02011已处理CRM退货收货检验申请(集团{month}月合计).xlsx')
goods_rejected_all.to_excel(file, index=False)
file.save()

print('拼接写入完成')

# 读取各基地LTC退货数据
goods_rejected_ltc_8010 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02013已处理LTC退货收货检验申请{month}(8010).xls')
goods_rejected_ltc_8012 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02013已处理LTC退货收货检验申请{month}(8012).xls')
goods_rejected_ltc_8020 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02013已处理LTC退货收货检验申请{month}(8020).xls')
goods_rejected_ltc_8030 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02013已处理LTC退货收货检验申请{month}(8030).xls')
goods_rejected_ltc_8040 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02013已处理LTC退货收货检验申请{month}(8040).xls')
goods_rejected_ltc_8050 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02013已处理LTC退货收货检验申请{month}(8050).xls')

# 拼接数据表
goods_rejected_ltc_all = pd.concat([goods_rejected_8010,
                                    goods_rejected_ltc_8012,
                                    goods_rejected_ltc_8020,
                                    goods_rejected_ltc_8030,
                                    goods_rejected_ltc_8040,
                                    goods_rejected_ltc_8050]).reset_index(drop=True)

# 写入文件
file = pd.ExcelWriter(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\退货\IQC02011已处理LTC退货收货检验申请(集团{month}月合计).xlsx')
goods_rejected_all.to_excel(file, index=False)
file.save()

print('拼接写入完成')
