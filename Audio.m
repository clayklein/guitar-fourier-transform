rec = audiorecorder(44100, 16, 1);

disp('Recording Started')
recordblocking(rec, 3);
disp('Recording Ended');

play(rec);

y = getaudiodata(rec);
figure()
plot(y);

n = length(y);

yfft = abs(fft(y));
%yfft = yfft/n; What is this line?
yfft = yfft(1:n/2+1);

fs = 44100;

f = fs*(0:n/2)/n;

figure()
plot(f, yfft);
xlim([0, 1000]);

f = transpose(f);

data = [f yfft];
csvwrite('d_chord.csv', data);