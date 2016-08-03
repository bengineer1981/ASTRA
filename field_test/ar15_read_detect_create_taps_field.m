addpath("/home/ben/gnuradio/gr-utils/octave")
%             change file name here | |  (needs to be same as GR name)
%                                   v v
shot_bin = 9.*read_float_binary("audio_recordings/ar15");
shot_lin = transpose(shot_bin);
size(shot_bin)
shot = shot_lin(283800:288000);
shot_match_filt = fliplr(shot);
%     rename taps file here |  |  |
%                           v  v  v       
csvwrite("/home/ben/Desktop/senior_design/field_test/taps/ar15.txt",shot_match_filt)
shot(1:4)
shot_match_filt(1:4)
figure(1)
subplot(1,3,1)
plot(shot_bin)
title("shot from bin file")
subplot(1,3,2)
plot(shot)
title("truncated shot")
subplot(1,3,3)
plot(shot_match_filt)
title("matched filter (reversed shot)")
filtered_out = fftconv(shot_bin,shot_match_filt);
figure(2)
plot(filtered_out)
%figure(3)
%t = [1:length(shot_bin)];
%y = fftshift(fft(shot_bin));
%plot(t,y)