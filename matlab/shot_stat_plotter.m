 n = 12;
 l = 3;
 shot_matrix = cell(n, 1);
 z = 0
 for k = 1 : n
  for j = 1: l
    shot_matrix{k+z} = csvread(['/home/ben/Desktop/senior_design/gnuradio/data_files/in1fileAR15.50m.' num2str((k-1)*30) 'deg.shot' num2str(l) '.csv']);
    z = z+1;
    end
    z = z-1;
 end
 for g = 1:length(shot_matrix)
  shot_file = fopen(['/home/ben/Desktop/shot_csv_to_bin/bin_test' num2str(g) '.dat'],'wb');
  fwrite(shot_file,shot_matrix{g},'float32');
  fclose(shot_file);
  end
    length(shot_matrix)
 %for m = 1:(n*l)
  figure(1)
  %subplot(6,6,m)
  plot(shot_matrix{5})
  %end

