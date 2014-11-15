function [ out_img ] = transfer( from, to )
%TRANSFER the color map of from onto to

in = imread(from);
out = imread(to);
inlab = im2lab(in);
outlab = im2lab(out);
out_img = zeros(size(outlab));
for n = 1:3
    o = outlab(:,:,n);
    o(~isfinite(o)) = mean(o(isfinite(o)));
    stdo = std(o(:));
    i = inlab(:,:,n);
    i(~isfinite(i)) = mean(i(isfinite(i)));
    stdi = std(i(:));
    out_img(:,:,n) = (o-mean(o(:))).*(stdi/stdo)+mean(i(:));
end
out_img = lab2rgb(out_img);
end

function [ out ] = im2lab ( in )
% Ensure in is a RGB double
in = im2double(in);
inlms = rgb2lms(in);

% Convert to log space 
loglms = log(inlms);

% Convert to LAB
lms2lab = [0.577350269189626,0.577350269189626,0.577350269189626;0.408248290463863,0.408248290463863,-0.816496580927726;0.707106781186548,-0.707106781186548,0];
out = immult(loglms, lms2lab);
end

function [ out ] = lab2rgb ( in )
lab2lms = [0.577350269189626,0.408248290463863,0.707106781186548;0.577350269189626,0.408248290463863,-0.707106781186548;0.577350269189626,-0.816496580927726,0];
loglms = immult(in, lab2lms);
lms = exp(loglms);
out = lms2rgb(lms);
end

function [ out ] = rgb2lms ( in )
rgb2lmsmat = [0.381100000000000,0.578300000000000,0.040200000000000;0.196700000000000,0.724400000000000,0.078200000000000;0.024100000000000,0.128800000000000,0.844400000000000];
out = immult( in, rgb2lmsmat ) ;
end

function [ out ] = lms2rgb ( in )
lms2rgbmat = [4.467900000000000,-3.587300000000000,0.119300000000000;-1.218600000000000,2.380900000000000,-0.162400000000000;0.049700000000000,-0.243900000000000,1.204500000000000];
% Convert to LMS space
out = immult( in, lms2rgbmat );
end

function [ out ] = immult ( in, mat )
out = zeros(size(in));
for i = 1:3
    for j = 1:3
        clr = in(:,:,j);
        out(:,:,i) = out(:,:,i) + mat(i,j) * clr;
    end
end
end
