function a = backtrackingLineSearch(f, x, p, g, c, rho, a0)
    a = a0;
    while f(x+a*p) > f(x) + c*p'*g(x)*a
        a = rho*a;
    end
end