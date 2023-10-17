function [x, hist_fx, hist_fxfx1] = newton(f, g, h, x, eps, max_iter)
    c = 0.1;
    rho = 0.5;
    a0 = 1;

    hist_fx = zeros(max_iter+1,1);
    hist_fxfx1 = zeros(max_iter,1);
    hist_fx(1) = f(x);

    for k=2:max_iter+1
        x0 = x;
        % p = h(x0)\(-g(x0));
        [p, ~] = linsolve(h(x0),-g(x0));
        a = backtrackingLineSearch(f, x0, p, g, c, rho, a0);
        x = x0 + a*p;

        hist_fx(k) = f(x);
        hist_fxfx1(k-1) = abs(f(x) - f(x0));
        if abs(f(x)-f(x0)) < eps
            hist_fx = hist_fx(1:k);
            hist_fxfx1 = hist_fxfx1(1:k-1);
            break
        end
    end
end