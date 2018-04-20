一个简单的拼接多个 .flv 合并的程序

原因：
	起初想用爬虫爬取 B 站的视频，经过一段时间的摸索发现自己功力不够，只得乖乖的下载 win10 客户端程序。发现下载下来的视频是不连续的 .flv 文件，这可忍不了。发现网上有一个神器 FFMPEG(推荐) 可用来拼接视频。但工作量太大且有重复，于是就有了这个 python 脚本。

过程：
	1. 如何用 ffmpeg(神器) 拼接视频 ？
		1.1 命令行: ffmpeg -f concat -safe 0 - i one.txt -c copy one.mp4
			说明：
				不加 "-safe 0" 会报错，提示 unsafe file
		1.2 one.txt 文件编写格式:
			file '路径(绝对或相对) + 想要拼接文件'
			file '路径(绝对或相对) + 想要拼接文件'
			file '路径(绝对或相对) + 想要拼接文件'

	2. 编写 python 文件遇到的坑
		2.1 python 自定义排序的编写 (坑)
			python3 去除了 sorted 的 cmp 参数。
			解决方案：
				可选用以下方案替代
				from functools import cmp_to_key
				def cmp(a, b):
					pass
				sorted(listToSort, key=cmp_to_key(cmp))
		2.2 python os 模块操作
			os.listdir()
			os.path.join()
			os.isdir()
			os.getsize()
			os.chdir()
			os.path.pardir


			



		
	

