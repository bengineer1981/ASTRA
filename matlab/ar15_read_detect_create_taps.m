shot_bin = 9.5.*read_float_binary("/home/ben/Desktop/senior_design/field_test/audio_recordings/ar15_uphigh");
shot = shot_bin(135000:142000);
shot_lin = transpose(shot);
shot_match_filt = fliplr(shot_lin);
sens_input = read_float_binary("ar15_crowd_shot");
sens_out = conv(sens_input,shot_match_filt);
csvwrite("/home/ben/Desktop//senior_design/field_test/taps/ar15_uphigh.txt",shot_match_filt)
(fliplr(shot_lin))(1:6)
shot_match_filt(1:6)
size(shot_bin)
size(shot)
size(shot_lin)
size(shot_match_filt)
size(sens_input)
size(sens_out)
figure(1)
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
figure(2)
subplot(1,3,1)
plot(sens_input)
title("sensor input signal from microphone")
subplot(1,3,2)
plot(shot_match_filt)
title("filter that signal is run through")
subplot(1,3,3)
plot(sens_out)
title("sensor output")
r = dlmread("ar15_close_taps.txt", ",");
size(r)
r(1:6)
figure(6)
plot(r)
thresh = 200
for i = 1:length(sens_out)
  if sens_out(i) > thresh
    disp("hit at:\n")
    i
    i = i++;
  else
    i = i++; 
  end
end