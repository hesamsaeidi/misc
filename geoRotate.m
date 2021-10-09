function [longriR latgriR] = geoRotate(rotPole, gridLat, gridLon, rotAlpha) 
%rotate A about the pole in geographical coordinate

R = 6371;
longriR = [];
latgriR = [];
alpha = deg2rad(rotAlpha);
disp(gridLat)
for i = 1:size(gridLat,1)
  for j = 1:size(gridLat,2)
    Alambda = deg2rad(90 - rad2deg(gridLat(i,j))); Aphi = gridLon(i,j);
    xA = R*sin(Alambda)*cos(Aphi);
    yA = R*sin(Alambda)*sin(Aphi);
    zA = R*cos(Alambda);
%     fprintf('x: %d\ny: %d\nz: %d\n',xA, yA, zA)
    Plambda = deg2rad(90 -  rotPole(1)); Pphi = deg2rad(rotPole(2));
    xP = R*sin(Plambda)*cos(Pphi);
    yP = R*sin(Plambda)*sin(Pphi);
    zP = R*cos(Plambda);
%     fprintf('xp: %d\nyp: %d\nzp: %d\n',xP,yP,zP)
    newxA = xA - xP; newyA = yA - yP; newzA = zA - zP;
    Arot = [cos(alpha) -sin(alpha) 0; sin(alpha) cos(alpha) 0; 0 0 1] * [newxA; newyA; newzA];
%     fprintf('newx: %d\nnewy: %d\nnewz: %d\n',newxA, newyA, newzA)
disp(Arot(1))
    xR = Arot(1) + xP; yR = Arot(2) + yP; zR = Arot(3) + zP;
    lonR = atan(yR/xR); latR = deg2rad(90 - rad2deg(atan(sqrt(xR^2 + yR^2)/zR)));
    latgriR(i,j) = latR;
    longriR(i,j) = lonR;
    
%     
    
  end
end