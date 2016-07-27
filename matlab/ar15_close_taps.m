w = (wavread("ar15.wav"));
size(w)
w = (w(:,1));
figure(2)
plot(w)
%wavwrite(w,44100,16,"AR15_close_mono.wav");
%w = (wavread("AR15_close_mono.wav"));
%size(w)
%w = w(1:30000);
%w = transpose(w);
%taps = fliplr(w);
%csvwrite("AR15_close_taps.txt",w);
%x = wavread("crowd_shot.wav");
%size(w)
%size(x)
%size(taps)
%w(length(w)-5:length(w))
%fliplr(taps(1:6))
%out = conv(taps,x);
figure(1)
subplot(2,2,1)
plot(w)
subplot(2,2,2)
plot(taps)
subplot(2,2,3)
plot(x)
subplot(2,2,4)
%plot(out)
%figure(3)
%f = [1 : length(taps)];
%size(f)
%a = fft(taps);
%z = fftshift(a);
%size(z)
%plot(f,z)