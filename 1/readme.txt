һ���򵥵�ƴ�Ӷ�� .flv �ϲ��ĳ���

ԭ��
	�������������ȡ B վ����Ƶ������һ��ʱ������������Լ�����������ֻ�ùԹԵ����� win10 �ͻ��˳��򡣷���������������Ƶ�ǲ������� .flv �ļ�������̲��ˡ�����������һ������ FFMPEG(�Ƽ�) ������ƴ����Ƶ����������̫�������ظ������Ǿ�������� python �ű���

���̣�
	1. ����� ffmpeg(����) ƴ����Ƶ ��
		1.1 ������: ffmpeg -f concat -safe 0 - i one.txt -c copy one.mp4
			˵����
				���� "-safe 0" �ᱨ����ʾ unsafe file
		1.2 one.txt �ļ���д��ʽ:
			file '·��(���Ի����) + ��Ҫƴ���ļ�'
			file '·��(���Ի����) + ��Ҫƴ���ļ�'
			file '·��(���Ի����) + ��Ҫƴ���ļ�'

	2. ��д python �ļ������Ŀ�
		2.1 python �Զ�������ı�д (��)
			python3 ȥ���� sorted �� cmp ������
			���������
				��ѡ�����·������
				from functools import cmp_to_key
				def cmp(a, b):
					pass
				sorted(listToSort, key=cmp_to_key(cmp))
		2.2 python os ģ�����
			os.listdir()
			os.path.join()
			os.isdir()
			os.getsize()
			os.chdir()
			os.path.pardir


			



		
	

