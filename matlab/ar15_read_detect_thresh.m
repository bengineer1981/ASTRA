#get sensor input -> x(t), create match filter-> s(t)
shot_bin = read_float_binary("sounds/ar15_close");
shot = shot_bin(1:5000);
shot_lin = transpose(shot);
shot_match_filt = fliplr(shot_lin);
sens_input = read_float_binary("ar15_crowd_shot");
sens_out = conv(sens_input,shot_match_filt);
#create delays and delayed signals
d1 = 10000
d2 = 20000
d3 = 30000
array_in1 = cat(1, sens_input(1:d1), sens_input(1:(length(sens_input)-d1)));
length(array_in1)
length(sens_input)
array_in2 = cat(1,sens_input(1:d2), sens_input(1:(length(sens_input)-d2)));
length(array_in2)
length(sens_input)
array_in3 = cat(1,sens_input(1:d3), sens_input(1:(length(sens_input)-d3)));
length(array_in3)
length(sens_input)

#plot input and delayed inputs
figure(1)
subplot(4,1,1)
plot(sens_input)
title("sens input")
subplot(4,1,2)
plot(array_in1)
title("array in1")
subplot(4,1,3)
plot(array_in2)
title("array in2")
subplot(4,1,4)
plot(array_in3)
title("array in3")

#convolve x(t) with s(t)
sens_out = conv(sens_input,shot_match_filt);

#plot input file, truncated input file, match filter taps,
#output of convolution of x(t) with s(t) 
figure(2)
subplot(2,3,1)
plot(shot_bin)
title("shot from bin file")
subplot(2,3,2)
plot(shot)
title("truncated shot")
subplot(2,3,3)
plot(shot_lin)
title("transposed var 'shot'")
subplot(2,3,4)
plot(shot_match_filt)
title("matched filter (reversed shot_lin)")
subplot(2,3,5)
plot(sens_input)
title("sensor input from crowd")
subplot(2,3,6)
plot(sens_out)
title("output of matched filter")

#run threshold to detect peaks on all signals
thresh = 200

for i = 1:length(sens_out)
  if sens_out(i) > thresh
    disp("hit at:")
    thresh_trig_t = i;
    thresh_trig_A = sens_out(i);
    i = i++;
  else
    i = i++; 
  end
end

[acor1,lag1] = xcorr(sens_input,array_in1);
[~,j] = max(abs(acor1));
lagdiff1 = lag1(j)
pkval_acor1 = max(abs(acor1))
[acor2,lag2] = xcorr(sens_input,array_in2);
[~,k] = max(abs(acor2));
lagdiff2 = lag2(k)
pkval_acor2 = max(abs(acor2))
[acor3,lag3] = xcorr(sens_input,array_in3);
[~,l] = max(abs(acor3));
lagdiff3 = lag3(l)
pkval_acor3 = max(abs(acor3))
disp("heres:")
j
disp("heres:")
k
disp("heres:")
l
figure(3)
n = [1:length(acor1)];
size(n)
size(acor1)
length(n)
subplot(4,1,1)
plot(sens_input,'y-')
subplot(4,1,2)
plot(n,acor1,'g-')
subplot(4,1,3)
plot(n, acor2,'b-')
subplot(4,1,4)
plot(n, acor3,'r-')

orig_hit_sig = zeros(length(sens_input),1);
orig_hit_sig(thresh_trig_t) = thresh_trig_A;
dly_hit_sig1 = zeros(length(sens_input),1);
dly_hit_sig1(thresh_trig_t-lagdiff1) = pkval_acor1;
dly_hit_sig2 = zeros(length(sens_input),1);
dly_hit_sig2(thresh_trig_t-lagdiff2) = pkval_acor2;
dly_hit_sig3 = zeros(length(sens_input),1);
dly_hit_sig3(thresh_trig_t-lagdiff3) = pkval_acor3;
m = [1:length(sens_input)];
figure(4)
plot(m,orig_hit_sig,m, dly_hit_sig1,m, dly_hit_sig2,m, dly_hit_sig3)

%% Time specifications:
   Fs = 44100;                      % samples per second
   dt = 1/Fs;                     % seconds per sample
   StopTime = 5000/44100;                  % seconds
   t = (0:dt:StopTime-dt)';
   N = size(t,1);
   %% Signal:
   #write shot to csv
   csvwrite("/home/ben/Desktop/senior_design/shot_taps/ar15_close.txt",shot_lin);
   #read shot from csv
   x = csvread("/home/ben/Desktop/senior_design/shot_taps/ar15_close_taps.txt");
   %% Fourier Transform:
   X = fftshift(fft(x));
   %% Frequency specifications:
   dF = Fs/N;                      % hertz
   f = -Fs/2:dF:Fs/2-dF;           % hertz
   %% Plot the spectrum:
   figure(5);
   plot(f,abs(X)/N);
   xlabel('Frequency (in hertz)');
   title('Magnitude Response');