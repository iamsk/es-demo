es-demo
=======

elasticsearch demo for indexing zhihu rss and search in title

中文发行版：https://github.com/medcl/elasticsearch-rtf

启动 es 服务

	elasticsearch/bin/elasticsearch

es 默认使用本地文件系统存储索引，所以无需担心丢失

配置文件为
	
	elasticsearch/config/elasticsearch.yml

支持的类型有：
	
	mmapfs, simplefs, niofs 根据不同的 os 进行选择
	
	memory 用于存到内存，速度快，重启系统会丢失
	
索引数据的存储位置和日志位置均为 elasticsearch 的根目录，分别为 data 和 logs

下载本 demo，运行 demo

	python app.py
	
访问 http://localhost:9527/init 进行数据模型的定义，并索引已有数据

MySQL 和 es 的数据结构对照

	MySQL             elasticsearch
	-----			  -------------
	database          index
	table             type
	schema 			  mapping
	row               document
	field             field

访问 http://localhost:9527/search/iphone 进行搜索

REFs:

[中文文档](http://es-cn.medcl.net/)

[ElasticSearch入门笔记](http://www.qwolf.com/?p=1387)
