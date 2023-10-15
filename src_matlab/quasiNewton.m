function [x,hist] = quasiNewton(f, g, h, x, s, max_iter)
    c=0.1;
    rho=0.5;
    a0=1;

    hist=zeros(max_iter,1);
    
    figure;
    % hold on;
    % plot(x(1),x(2),'ro');

    C=inv(h(x));
    
    for k=1:max_iter
        x0 = x;
        p=C\(-g(x0));
        a=backtrackingLineSearch(c, rho, a0, f, x0, p, g);
        x=x0+a*p;

        hold on;
        % plot(x(1),x(2),'ro');
        plot([x(1) x0(1)],[x(2) x0(2)],'r');

        %update C here
        y = g(x) - g(x0);
        s = x-x0;
        C = C - ((C*(y*y')*C)/(y'*c*y)) + ((s*s')/(y'*s));

        hist(k) = f(x)-f(x0);
        if abs(f(x)-f(x0)) < s(1) | abs(x-x0) < s(2)
            hist=hist(1:k);
            break
        end
        % break
    end
    % while (abs(f(x)-f(x0)) < s(0) && abs(x-x_hat) < s(1)) || (iter<=max_iter)
    %     p=-1*g(x);
    %     a=backtrackingLineSearch(c, rho, a0, f, x, p, g);
    %     x_hat=x+a*p;
    % end

    %plot here
    [X,Y] = meshgrid(-100:1:100);
    % Z = f_quadratic([X Y]);
    Z = X.^2 + 10.*Y.^2;
    contour(X,Y,Z,40);
    axis([-100 100 -100 100]);
    axis square;
    grid on;
    title('Quasi Newton');
    xlabel('x');
    ylabel('y');
    hold off;

end