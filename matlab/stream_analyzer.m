%get streams
stream1 = transpose(read_float_binary("/home/ben/Desktop/senior_design/gnuradio/data_files/stream1"));
csvwrite("/home/ben/Desktop/senior_design/gnuradio/data_files/stream1.csv",stream1(220000:240000))
stream2 = transpose(read_float_binary("/home/ben/Desktop/senior_design/gnuradio/data_files/stream2"));
csvwrite("/home/ben/Desktop/senior_design/gnuradio/data_files/stream2.csv",stream2(220000:240000))
stream3 = transpose(read_float_binary("/home/ben/Desktop/senior_design/gnuradio/data_files/stream3"));
csvwrite("/home/ben/Desktop/senior_design/gnuradio/data_files/stream3.csv",stream3(220000:240000))
stream4 = transpose(read_float_binary("/home/ben/Desktop/senior_design/gnuradio/data_files/stream4"));
csvwrite("/home/ben/Desktop/senior_design/gnuradio/data_files/stream4.csv",stream4(220000:240000))

filt_start = 223000;
filt_stop = 235000;
if filt_stop < length(stream1)
  filt = fliplr(stream1(filt_start:filt_stop));
  csvwrite("/home/ben/Desktop/senior_design/gnuradio/data_files/filt.txt",filt)
else
  filt = fliplr(stream1(1:1000));
end
  
filt_out1 = conv(filt,stream1);
filt_out2 = conv(filt,stream2);
filt_out3 = conv(filt,stream3);
filt_out4 = conv(filt,stream4);
find (filt_out1 == max(filt_out1))
find (filt_out2 == max(filt_out2))
find (filt_out3 == max(filt_out3))
find (filt_out4 == max(filt_out4))

pkg load signal;
crosscorr1 = xcorr(stream1,stream1);
crosscorr2 = xcorr(stream1,stream2);
crosscorr3 = xcorr(stream1,stream3);
crosscorr4 = xcorr(stream1,stream4);
find (crosscorr1 == max(crosscorr1))
find (crosscorr2 == max(crosscorr2))
find (crosscorr3 == max(crosscorr3))
find (crosscorr4 == max(crosscorr4))

figure(1)
subplot(1,4,1)
plot(stream1)
ylim([-1 1])
title("stream 1")
subplot(1,4,2)
plot(stream2)
ylim([-1 1])
title("stream 2")
subplot(1,4,3)
plot(stream3)
ylim([-1 1])
title("stream 3")
subplot(1,4,4)
plot(stream4)
ylim([-1 1])
title("stream 4")

figure(2)
plot(filt)
title("matched filter")

figure(3)
subplot(1,4,1)
plot(filt_out1)
ylim([-10 45])
title("filt out 1")
subplot(1,4,2)
plot(filt_out2)
ylim([-10 45])
title("filt out 2")
subplot(1,4,3)
plot(filt_out3)
ylim([-10 45])
title("filt out 3")
subplot(1,4,4)
plot(filt_out4)
ylim([-10 45])
title("filt out 4")

figure(4)
subplot(1,4,1)
plot(crosscorr1)
%ylim([-10 45])
title("crosscorr1")
subplot(1,4,2)
plot(crosscorr2)
%ylim([-10 45])
title("crosscorr2")
subplot(1,4,3)
plot(crosscorr3)
%ylim([-10 45])
title("crosscorr3")
subplot(1,4,4)
plot(crosscorr4)
%ylim([-10 45])
title("crosscorr4")
