# Pubchem-
基于python通过selenium、requests、Beautifulsoup爬取pubchem网站中化合物（compound）、生物测定（bioassay）、物质（substance）三个主题类别下爬取序号从1开始的网页数据，包括二维结构图，以xml文件保存的数据

由于数据量大，需要布置多个服务器同时进行爬取，且每台服务器进行多线程运行。由于爬取的网址模板为”https://pubchem.ncbi.nlm.nih.gov/(substance、compound、bioassay)/“+”id“， 

具体为给每天服务器的程序分配序号（id）范围，例如服务器A分配序号（1-5000），服务器B分配序号（5001-10000）

同时在每个阶段会更新开始爬取序号，以免由于突发情况导致的程序停止，重新运行时避免重复运行，且保存了爬取数据时出现异常的日志，该日志是关于哪条网址在爬取时出现异常，还包括下载保存数据的存储位置，方便检查。

同时为了保证爬取效率，设置了隐式Chrome浏览器

python=3.7.10

requests=2.26.0

selenium=3.141.0
