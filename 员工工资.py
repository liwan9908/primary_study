#请在____处写一行表达式
#请在…处写多行代码
#可以修改其他代码

members = {'张三':['人力部',5500],
            '李四':['后勤部',4500],
            '王三':['市场部',6500],
            '赵六':['开发部',8500]
           }
sal_dep = {}
for key in members:
    print('{}的工资是:{}, 部门是{}'.format(key,members[key][1],members[key][0]))
s=list(members.values())
s.sort(key=lambda x:x[1],reverse=True)
max_name=s[0][0]
max_val=s[0][1]
print('工资最高的部门是:{},该部门工资是:{}'.format(max_name,max_val))
