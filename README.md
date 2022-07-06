# Pubchem-
基于python通过selenium、requests爬取pubchem网站中化合物（compound）、生物测定（bioassay）、物质（substance）三个主题类别下爬取序号从1开始的网页数据，包括二维结构图，以xml文件保存的数据

由于数据量大，需要布置多个服务器同时进行爬取，且每台服务器进行多线程运行。由于爬取的网址模板为”https://pubchem.ncbi.nlm.nih.gov/(substance、compound、bioassay)/“+”id“，具体为给每天服务器的程序分配序号（id）范围，例如服务器A分配序号（1-5000），服务器B分配序号（5001-10000）
