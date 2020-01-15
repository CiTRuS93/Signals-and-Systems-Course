
% create the signal in time and dft domains
N=1e6;
sig_rnd=wgn(N,1,0);
sig_rnd=sig_rnd/max(abs(sig_rnd));
Sig_rnd=fft(sig_rnd);

% build the desired shape in the dft domain
Desired=ones(N,1);
Desired(1:N/4)=1-4/N*(1:N/4);
Desired(3*N/4+1:N)=-3+4/N*(3*N/4+1:N);
stem(Desired,'Marker','none')

% build a "filter" - a vector that will make the random signal in the
% desired shape
Filt=abs(Desired)./abs(Sig_rnd);
Sig=Sig_rnd.*Filt;
sig=ifft(Sig);
sig_r_var=var(real(sig));
sig_i_var=var(imag(sig));
sig=real(sig);
Sig=fft(sig);

subplot(6,1,1:3);
plot(sig);
ylabel('signal in time');
subplot(6,1,4:6);
plot(abs(Sig));
ylabel('signal in freq');
xlabel('the horizontal label is not set up... ignore the values');

