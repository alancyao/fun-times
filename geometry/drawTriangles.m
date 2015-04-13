function drawTriangles( fname )
node = dlmread([fname '.node']);
node = node(2:end, 2:3);
ele = dlmread([fname '.ele']);
ele = ele(2:end, 2:4);
figure(1);
hold on;
title('given triangulation');
triplot(ele, node(:,1), node(:,2));
figure(2);
hold on;
title('reference tri');
triplot(delaunayTriangulation(node));
end

