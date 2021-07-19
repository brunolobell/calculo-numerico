function d=der(t,y)
  m=2; c=0.5; k=10;
  A=[0 1;-k/m -c/m];
  B=[0;1/m];
  u=0;
  d=A*y+B*u;
endfunction

function [vt,vy]=inteuler(t0,tf,h,y0)
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

m=2; k=10; c=0.5;
A=[0 1;-k/m -c/m];
y0=[0.5;0];
t0=0; tf=9; h=0.01;
[vt,vy]=inteuler(t0,tf,h,y0);
n=max(size(vt));
for i=1:n,
  vya(i,:)=expm(A*vt(i))*y0;
end,
subplot(221);
plot(vt,vy,'b',vt,vya,'r')
axis([0 9 -1.1 1])
grid