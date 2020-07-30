# NCUT_GPA_calculator 北方工业大学 GPA 计算器
    
    百分制 -> GPA 
    Convert 100 to GPA 0-4 

## How to compute manually ? [page](http://yjsy.ncut.edu.cn/yjsy/73/20190701/094754347509949.html)
对应表 Reference table :
> |百分制(100 scores)|GPA 分数（GPA points)|
> |:-:|:-:|
> |86~100|4|
> |81~85|3.7|
>|77~80|3.3|
>|73~76|3|
>|69~72|2.5|
>|65~68|2|
>|60~64|1|
>|0~59|0|

计算公式 Formula: 
> GPA = sum( course credit * gpa point ) / sum(course credit) <br>
> GPA = sum( 单科学分 * 单科GPA分数 ) / sum(单科学分)



## Usage
1. Get Grade Sheet
 Login to jxxx.ncut.edu.cn -> Grade -> export Full Grade Sheet -> F12 Developer Tool -> Open Element Tab and Copy Source Code
2. Save Source Code into __test.html__
3. run `python gpa_convert.py`


## 用法
1. 登录 jxxx.ncut.edu.cn -> 成绩 -> 打印完整成绩单 -> F12 开发者工具 -> 元素选项卡中选取所有的元素
2. 保存到 test.html
3. 运行 `python gpa_convert.py`


## 需要的安装包 Requirements
- numpy
- bs4 
