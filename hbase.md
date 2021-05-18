1、hadoop安装
https://www.cnblogs.com/sea520/p/13530185.html
镜像：https://mirror-hk.koddos.net/apache/hadoop/common/hadoop-3.1.4/

2、hbase安装
https://baijiahao.baidu.com/s?id=1631231582763493960&wfr=spider&for=pc
https://www.jianshu.com/p/eb7097439e77

安装异常：https://www.cnblogs.com/barneywill/p/10283076.html
https://blog.csdn.net/weixin_45724219/article/details/105815916


<property>
   <name>hbase.rootdir</name>
   <value>file:///D:/Users/Desktop/java/bigData/hbase-2.2.6/root</value>
  </property>
  <property>
   <name>hbase.tmp.dir</name>
   <value>D:/Users/Desktop/java/bigData/hbase-2.2.6/tmp</value>
  </property>
  <property>
   <name>hbase.zookeeper.quorum</name>
   <value>127.0.0.1</value>
  </property>
  <property>
   <name>hbase.zookeeper.property.dataDir</name>
   <value>D:/Users/Desktop/java/bigData/hbase-2.2.6/zoo</value>
  </property>
  <property>
    <name>hbase.cluster.distributed</name>
    <value>false</value>
  </property>
  <property>
    <name>hbase.unsafe.stream.capability.enforce</name>
    <value>false</value>
  </property>


3、管理界面
localhost:16010/master-status  


4 操作
base op:https://hbase.apache.org/book.html#hadoop
修改列簇

https://blog.csdn.net/HYDMonster/article/details/80009950

Hbase添加和删除列族:
hbase> alter 'testspace:testtable1', {NAME => 'cf2', VERSIONS => 800}
hbase> alter 'testspace:testtable1',  {NAME => 'cf2', METHOD => 'delete'}

hbase ttl是过期吗

describe查看表的一些详细信息：

禁用与启用表： 在删除表和修改表的配置之前，我们需要先禁用表 （disable & enable & drop)

put命令
put 'testspace:testtable1','20190419_10001','f1:name','zhangsan'
put 'testspace:testtable1','20190419_10001','cf2:name','leo'
put 'testspace:testtable1','20190419_10001','cf2:age','15'

put 'testspace:testtable1','20190419_10001','f1:age','22'


 get 'testspace:testtable1', '20190419_10001'

put 'testspace:testtable1','20190419_10002','f1:name','lisi'

put 'testspace:testtable1','20190419_10003','f1:name','wangwu'

查看数据

客户端：
https://github.com/Observe-secretly/HbaseGUI/wiki


hbase默认配置属性：
https://www.cnblogs.com/junrong624/p/3582610.html