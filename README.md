# LotteryDraw
一零一国际部艺术节抽奖程序源代码和相关文件

下载代码方法：1）直接下载压缩包 2）注册GitHub账号添加ssh-key，然后终端执行“git clone git@github.com:Jasonyanyusong/LotteryDraw”。
使用方法：首先安装Visual Studio Code，并安装Python工具（百度一下）

第一步（准备阶段）：安装抽奖程序依赖库pygame
  打开终端（具体操作系统可以上网搜索一下），输入指令“pip install pygame”，等系统显示成功才可以进行下一步（有时候网络不好会失败，多尝试几次）

第二步（准备阶段）：在程序文件中添加老师/同学的信息
  观察LotteryDraw.py文件的第21、22行（也可以模仿LotteryDraw_2022Demo.py文件）
  形式如：BJ101IDMembers.append(BJ101IDMember("张三","张三的班名",1))
  其中，张三为学生的名字，将其改为学生的真名；张三的班名为国际部的英文班名（如Curie/Carver）；第三个参数（序号）为从1开始的整数，其目的是方便快速删除已经中奖的学生，不要重复
  例：BJ101IDMembers.append(BJ101IDMember("烟雨松","Curie",268))：表示Curie班的烟雨松在抽奖的名单中，序号为268

第三步（抽奖阶段）：
