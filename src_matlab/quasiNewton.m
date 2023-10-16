function [x,hist] = quasiNewton(f, g, h, x, eps, max_iter)
    c=0.1;
    rho=0.5;
    a0=1;

    hist=zeros(max_iter+1,1);
    hist(k) = f(x);

    C=inv(h(x));
    
    for k=2:max_iter+1
        x0 = x;
        % p=C\(-g(x0));
        [p, ~] = linsolve(C,-g(x0));
        a=backtrackingLineSearch(c, rho, a0, f, x0, p, g);
        x=x0+a*p;

        %update C here
        y = g(x) - g(x0);
        s = x-x0;
        C = C - ((C*(y*y')*C)/(y'*c*y)) + ((s*s')/(y'*s));

        hist(k) = f(x);
        if abs(f(x)-f(x0)) < eps
            hist=hist(1:k);
            break
        end
    end
end