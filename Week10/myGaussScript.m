x = -10:0.1:5;
sigma = 2;
y = exp(-x.^2/sigma^2);
plot(x,y)
xlabel('xaxis (m)')
ylabel('Gaussian')
title('myGaussian')