function [x,hist] = gradientDescent(f, g, x, eps, max_iter)
    c=0.1;
    rho=0.5;
    a0=1;

    hist=zeros(max_iter+1,1);
    hist(1) = f(x);
    
    for k=2:max_iter+1
        x0 = x;
        p=-1*g(x0);
        a=backtrackingLineSearch(c, rho, a0, f, x0, p, g);
        x=x0+a*p;

        hist(k) = f(x);
        if abs(f(x)-f(x0)) < eps
            hist=hist(1:k);
            break
        end
    end
end