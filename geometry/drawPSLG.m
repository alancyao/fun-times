function [pts, lines, lsg] = drawPSLG( pts, lines, lsg, varargin )
%DRAWPSLG Draw a planar straight-line graph of points, lines, and segments
%   pts is a Ax2 matrix of (x,y) positive coordinate pairs
%   lines is a Bx2 matrix of y=mx+b pairs of (m, x)
%   lsg is a Cx4 matrix of positive point pairs that define segments
%   an optional 4th parameter defines the color of lines.
%   this is useful for dualizing

% Draw points
figure(1); hold on;
if ~isempty(pts)
%    pts = pts / abs(max(pts(:)));
    scatter(pts(:,1), pts(:,2), 'k', 'filled');
end
if ~isempty(lsg)
%    lsg = lsg / abs(max(lsg(:)));
    scatter(lsg(:,1), lsg(:,2), 'b', 'filled');
    scatter(lsg(:,3), lsg(:,4), 'b', 'filled');
end

% Draw lines
maxln = max([abs(lines(:)); 1]);
linsp = -maxln:.1:maxln;
if ~isempty(lines)
%    lines = lines / abs(max(lines(:)));
    [N, ~] = size(lines);
    
    if length(varargin) > 0
        colors = varargin{1};
    else
        colors = repmat([1, 0, 0], N, 1);
    end
    for i = 1:N
        m = lines(i,1); b = lines(i,2);
        line(linsp, m*linsp+b, 'Color', colors(i,:));
    end
end

% Draw segments
if ~isempty(lsg)
    [N, ~] = size(lsg);
    for i = 1:N
        x1 = lsg(i,1); y1 = lsg(i,2); x2 = lsg(i,3); y2 = lsg(i,4);
        m = (y2-y1)/(x2-x1); b = y1 - m*x1;
        linsp = x1:(x2-x1)/100:x2;
        line(linsp, m*linsp+b, 'Color', colors(i,:));
    end
end
