experiment = importdata('/Network/Servers/cp-file-home.cp-calpoly.edu/studentHome$/user/rmullen/PHYS202-S13/Week10/radioactivedecay.dat')
t = experiment.data(:,1);
N = experiment.data(:,2);

%Function to fit
fun = @(A, B, x) A .* exp(B .* x)
%Starting points for the parameters A and B
guess = fun(-0.3, 10, x);
%Fit the data
fittedmodel = fit(x', y', fun, 'StartPoint',[-0.3 10])
%Plot the result
figure(42)
plot(fittedmodel, 'r-');

%plot(t, N, '.b')