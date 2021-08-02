import xlrd
xl=xlrd.open_workbook('D:\\Desktop\\12月份衣服销售数据.xls')    #文件格式修改为xls
cl=xl.sheet_by_name('12月份各种服饰销售情况')
money=0     #总销售额
sum=0   #总库存
psum=0  #总销量
cth=['羽绒服','牛仔裤','风衣','皮草','T血','衬衫']
sth=[0,0,0,0,0,0]   #对应cth每种服饰销量
print(' -------------12月份服饰销售数据-------------')
print('\t日期\t服装名称\t价格/件\t库存数量\t销售量/每日')
for i in range(1,cl.nrows):
    for j in range(0,cl.ncols):
        print('\t',cl.cell(i,j).value,end='')
    print()
    money+= float(cl.cell(i, 2).value) * float(cl.cell(i, 4).value)
    sum+=int(cl.cell(i,3).value)
    psum+=int(cl.cell(i,4).value)
    for k in range(0,6):
        if cth[k]==cl.cell(i,1).value:
            sth[k]+=cl.cell(i,4).value

print('12月衣服库存总数：',sum,'总销售额：','%.2f'%money,'平均每日销售量：','%.2f'%(psum/30),'\n各服装每月销售占比：')
for i in range(0,6):
    print(cth[i],':\t','%.2f%%'%(sth[i]/psum))