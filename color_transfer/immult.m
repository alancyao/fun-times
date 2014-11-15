function [ out ] = immult ( in, mat )
out = zeros(size(in));
for i = 1:3
    for j = 1:3
        clr = in(:,:,j);
        out(:,:,i) = out(:,:,i) + mat(i,j) * clr;
    end
end
end