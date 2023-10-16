% Project 2: Unconstrained Optimization

x = randn(100, 1);
max_iter=100;

%fun1
[x_gd,hist_gd]=gradientDescent(@fun1,@g_fun1,x,1e-5,100);

[x_nm,hist_nm]=newton(@fun1,@g_fun1,@h_fun1,x,1e-5,100);

[x_qn,hist_qn]=quasiNewton(@fun1,@g_fun1,@h_fun1,x,1e-5,100);


%fun 2
fid_A = fopen('Project2/fun2_A.txt','r');
A = fscanf(fid_A,'%e ',[500,100]);
fclose(fid_A);

fid_b = fopen('Project2/fun2_b.txt','r');
b = fscanf(fid_b,'%e ',[500,1]);
fclose(fid_b);

fid_c = fopen('Project2/fun2_c.txt','r');
c = fscanf(fid_c,'%e ',[100,1]);
fclose(fid_c);


[x_gd,hist_gd]=gradientDescent(@fun2,@g_fun2,x,1e-5,100);

[x_nm,hist_nm]=newton(@fun2,@g_fun2,@h_fun2,x,1e-5,100);

[x_qn,hist_qn]=quasiNewton(@fun2,@g_fun2,@h_fun2,x,1e-5,100);


%fun 3
[x_gd,hist_gd]=gradientDescent(@fun3,@g_fun3,x,1e-5,100);

[x_nm,hist_nm]=newton(@fun3,@g_fun3,@h_fun3,x,1e-5,100);

[x_qn,hist_qn]=quasiNewton(@fun3,@g_fun3,@h_fun3,x,1e-5,100);

%plotting
figure
plot(1:length(hist_nm), hist_nm);
xlabel("iterations")
ylabel("f(x)")
title("Convergence")
% saveas(gcf,'Convergence.jpg')
