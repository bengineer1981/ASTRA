%% Time specifications:
   Fs = 44100;                      % samples per second
   dt = 1/Fs;                     % seconds per sample
   StopTime = 5000/44100;                  % seconds
   t = (0:dt:StopTime-dt)';
   N = size(t,1);
   %% Signal:
   x = csvread("/home/ben/Downloads/desert_eagle_357_read_detect_create_taps.txt");
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