function  Spider( keyWord )
%SPIDER �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
OrgPath = cd;
spath2 = strcat(OrgPath,'\googleImag\googleImag');
cd(spath2);
f = fopen('in.txt','wt');
fprintf(f,'%s',keyWord);
system('python run_spider.py');
cd(OrgPath);
end

