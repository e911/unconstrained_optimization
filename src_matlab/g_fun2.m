function dx = g_fun2(x)
    fid_A = fopen('Project2/fun2_A.txt','r');
    A = fscanf(fid_A,'%e ',[500,100]);
    fclose(fid_A);
    
    fid_b = fopen('Project2/fun2_b.txt','r');
    b = fscanf(fid_b,'%e ',[500,1]);
    fclose(fid_b);
    
    fid_c = fopen('Project2/fun2_c.txt','r');
    c = fscanf(fid_c,'%e ',[100,1]);
    fclose(fid_c);

    dx = c + A'*(1./(b - A*x));
end