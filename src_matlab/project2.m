% Project 2: Unconstrained Optimization

%% for reproducibility initialize the random number generator
rng(42,"twister");

x = randn(100, 1);
% x = 2*ones(100,1);

max_iter=200;

%% fun1
[x_gd,hist_fx_gd,hist_fxfx1_gd]=gradientDescent(@fun1,@g_fun1,x,1e-5,max_iter);
% disp(hist_fx_gd(end))
fprintf("Optimum Value with GD: %f\n", hist_fx_gd(end))
fprintf("Iterations: %d\n", length(hist_fx_gd)-1)

figure
plot(1:length(hist_fx_gd), hist_fx_gd);
xlabel("iterations")
ylabel("f(x)")
title("Gradient Descent")
saveas(gcf,'fun1_gd.jpg')

[x_nm,hist_fx_nm,hist_fxfx1_nm]=newton(@fun1,@g_fun1,@h_fun1,x,1e-5,max_iter);
% disp(hist_fx_nm(end))
fprintf("Optimum Value with Newton: %f\n", hist_fx_nm(end))
fprintf("Iterations: %d\n", length(hist_fx_nm)-1)

figure
plot(1:length(hist_fx_nm), hist_fx_nm);
xlabel("iterations")
ylabel("f(x)")
title("Newton's Method")
saveas(gcf,'fun1_nm.jpg')

[x_qn,hist_fx_qn,hist_fxfx1_qn]=quasiNewton(@fun1,@g_fun1,@h_fun1,x,1e-5,1000);
% disp(hist_fx_qn(end))
fprintf("Optimum Value with Quasi-Newton: %f\n", hist_fx_qn(end))
fprintf("Iterations: %d\n", length(hist_fx_qn)-1)

figure
plot(1:length(hist_fx_qn), hist_fx_qn);
xlabel("iterations")
ylabel("f(x)")
title("Quasi-Newton Method")
saveas(gcf,'fun1_qn.jpg')


%% fun 2

[x_gd,hist_fx_gd,hist_fxfx1_gd]=gradientDescent(@fun2,@g_fun2,x,1e-5,max_iter);
% disp(hist_fx_gd(end))
fprintf("Optimum Value with GD: %f\n", hist_fx_gd(end))
fprintf("Iterations: %d\n", length(hist_fx_gd)-1)

figure
plot(1:length(hist_fx_gd), hist_fx_gd);
xlabel("iterations")
ylabel("f(x)")
title("Gradient Descent")
saveas(gcf,'fun2_gd.jpg')

[x_nm,hist_fx_nm,hist_fxfx1_nm]=newton(@fun2,@g_fun2,@h_fun2,x,1e-5,max_iter);
% disp(hist_fx_nm(end
fprintf("Optimum Value with Newton: %f\n", hist_fx_nm(end))
fprintf("Iterations: %d\n", length(hist_fx_nm)-1)

figure
plot(1:length(hist_fx_nm), hist_fx_nm);
xlabel("iterations")
ylabel("f(x)")
title("Newton's Method")
saveas(gcf,'fun2_nm.jpg')

[x_qn,hist_fx_qn,hist_fxfx1_qn]=quasiNewton(@fun2,@g_fun2,@h_fun2,x,1e-5,max_iter);
% disp(hist_fx_qn(end))
fprintf("Optimum Value with Quasi-Newton: %f\n", hist_fx_qn(end))
fprintf("Iterations: %d\n", length(hist_fx_qn)-1)

figure
plot(1:length(hist_fx_qn), hist_fx_qn);
xlabel("iterations")
ylabel("f(x)")
title("Quasi-Newton Method")
saveas(gcf,'fun2_qn.jpg')


%% fun 3
% x = [20;20];
x = randn(2,1);
[x_gd,hist_fx_gd,hist_fxfx1_gd]=gradientDescent(@fun3,@g_fun3,x,1e-5,max_iter);
% disp(hist_fx_gd(end))
fprintf("Optimum Value with GD: %f\n", hist_fx_gd(end))
fprintf("Iterations: %d\n", length(hist_fx_gd)-1)

figure
plot(1:length(hist_fx_gd), hist_fx_gd);
xlabel("iterations")
ylabel("f(x)")
title("Gradient Descent")
saveas(gcf,'fun3_gd.jpg')

[x_nm,hist_fx_nm,hist_fxfx1_nm]=newton(@fun3,@g_fun3,@h_fun3,x,1e-5,max_iter);
% disp(hist_fx_nm(end))
fprintf("Optimum Value with Newton: %f\n", hist_fx_nm(end))
fprintf("Iterations: %d\n", length(hist_fx_nm)-1)

figure
plot(1:length(hist_fx_nm), hist_fx_nm);
xlabel("iterations")
ylabel("f(x)")
title("Newton's Method")
saveas(gcf,'fun3_nm.jpg')

[x_qn,hist_fx_qn,hist_fxfx1_qn]=quasiNewton(@fun3,@g_fun3,@h_fun3,x,1e-5,max_iter);
% disp(hist_fx_qn(end))
fprintf("Optimum Value with Quasi-Newton: %f\n", hist_fx_qn(end))
fprintf("Iterations: %d\n", length(hist_fx_qn)-1)

figure
plot(1:length(hist_fx_qn), hist_fx_qn);
xlabel("iterations")
ylabel("f(x)")
title("Quasi-Newton Method")
saveas(gcf,'fun3_qn.jpg')

