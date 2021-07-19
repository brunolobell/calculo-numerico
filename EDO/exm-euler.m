function d=der(t,y)
  m1=m2=m3=2; k1=k2=10; c1=c2=0.15;
  A=[0 0 0 1 0 0;0 0 0 0 1 0;0 0 0 0 0 1;-k1/m1 k1/m1 0 -c1/m1 c1/m1 0;k1/m2 -(k1+k2)/m2 k2/m2 c1/m2 -(c1+c2)/m2 c2/m2;0 k2/m3 -k2/m3 0 c2/m3 -c2/m3];
  B=[0;0;0;0;0;1/m3];
  u=0;
  d=A*y+B*u;
endfunction

function [vt,vy]=rk4(t0,tf,h,y0)
  i=1;
  vt(i)=t0;
  vy(i,:)=y0;
  t=t0;
  while t<=tf,
    y=y0+h*der(t,y0);
    t=t+h;
    i=i+1;
    vt(i)=t;
    vy(i,:)=y;
    y0=y;
  end,
endfunction


m1=m2=m3=2; k1=k2=10; c1=c2=0.15;
A=[0 0 0 1 0 0;0 0 0 0 1 0;0 0 0 0 0 1;-k1/m1 k1/m1 0 -c1/m1 c1/m1 0;k1/m2 -(k1+k2)/m2 k2/m2 c1/m2 -(c1+c2)/m2 c2/m2;0 k2/m3 -k2/m3 0 c2/m3 -c2/m3];
y0=[-0.5;0;0.5;0;0;0];
t0=0;tf=12;h=0.005
[vt,vy] = rk4(t0,tf,h,y0);

n=max(size(vt));
for i=1:n,
  vya(i,:)=expm(A*vt(i))*y0;
end

subplot(221)
plot(vt,vy,'b',vt,vya,'r')
axis([0 12 -1.5 1.5])
title("passo")
grid
subplot(222)
plot(vt,vya-vy,'g')
axis([0 12 -3e-9 3e-9])
title("erro")
grid