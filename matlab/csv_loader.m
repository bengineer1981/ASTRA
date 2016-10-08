x = [];
for i = 1:3
  x[i] = csvread(['/home/ben/Desktop/senior_design/gnuradio/data_files/in1fileAR15.50m.0deg.shot' num2str(i) '.csv']);
  end
length(x(1))
plot(x(1))