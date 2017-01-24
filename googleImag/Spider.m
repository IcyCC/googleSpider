function  Spider( keyWord )
%SPIDER 此处显示有关此函数的摘要
%   此处显示详细说明
OrgPath = cd;
spath2 = strcat(OrgPath,'\googleImag\googleImag');
cd(spath2);
f = fopen('in.txt','wt');
fprintf(f,'%s',keyWord);
system('python run_spider.py');
cd(OrgPath);
end

