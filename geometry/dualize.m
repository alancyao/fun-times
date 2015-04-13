function [ pts2, lines2, linecolors ] = dualize( pts, lines, lsg )
%DUALIZE Summary of this function goes here
%   Detailed explanation goes here
pts2 = []; lines2 = []; linecolors = [];

if ~isempty(pts)
    lines2 = [pts(:,1) -pts(:,2)];
end

if ~isempty(lines)
    [N, ~] = size(lines);
    pts2 = [lines(:,1) -lines(:,2)];
    linecolors = repmat([1, 0, 0], N, 1);
end

if ~isempty(lsg)
    [N, ~] = size(lsg);
    for i = 1:N
        color = rand(1, 3);
        x1 = lsg(i,1); y1 = lsg(i,2); x2 = lsg(i,3); y2 = lsg(i,4);
        m = (y2-y1)/(x2-x1); b = y1 - m*x1;
        linsp = x1:(x2-x1)/100:x2;
        lines2 = [lines2; linsp' (m*linsp+b)'];
        linecolors = [linecolors; repmat(color, 101, 1)]; 
    end
end

