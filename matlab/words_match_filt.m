words = read_float_binary("one_two_three");
word = transpose(words(31000:52000));
figure(1)
plot(words)
title("original words")
figure(2)
plot(word)
title("word 'one'")
%front_filt = word;
%max(front_filt)
%filt_out = conv(word,words);
%figure(3)
%plot(filt_out)
%title("filtered output")
word_match = fliplr(word);
size(word_match)
csvwrite("file.txt",word_match)
figure(4)
plot(word_match)
title("word match")
out = conv(word_match,words);
figure(5)
plot(out)
title("conv output")
r = dlmread("file.txt", ",");
size(r)
r(1:6)
figure(6)
plot(r)