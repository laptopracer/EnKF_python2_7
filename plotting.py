"""
plotting.py

File that plotts various figures

Written by Godwin Madho
"""
import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from param import m,nstep,inf,tend,dt,Eavg,Obsfile,stat,preA,obsA

def plotavg():
        
    # Plotting the average
    Et=[]
    Ex=[]
    Ey=[]
    Ez=[]
    Ot=[]
    Ox=[]
    Oy=[]
    Oz=[]
           
    # The average ensemble file
    avgsave=open(Eavg,'r')
    av=csv.reader(avgsave,delimiter=';')
    for line in av:
        Et.append(float(line[0]))
        Ex.append(float(line[1]))
        Ey.append(float(line[2]))
        Ez.append(float(line[3]))
            
    avgsave.close()
    
    # The observation file
    obs=open(Obsfile,'r')
    da=csv.reader(obs,delimiter=';')
        
    # This is for file created in python
    for line in da:
        fline=line[0]
        if float(fline)>float(tend):
            break
        Ot.append(float(line[0]))
        Ox.append(float(line[1]))
        Oy.append(float(line[2]))
        Oz.append(float(line[3]))
       
    obs.close()
    
    # plots the observations and average ensemble
    plt.figure(1)
    plt.subplot(3,1,1)
    plt.title("Observation and Ensemble average with an ensemble size of m = " +str(m)+ ", assim step = " +str(nstep)+ ", inflation = " +str(inf)+ ", dt = " +str(dt)+ " ,Blue=ensemble average, Red=truth", fontsize=16)
    plt.plot(Et,Ex,'b',linewidth=1.0)
    plt.plot(Ot,Ox,'r',linewidth=1.0)
    plt.xlim([0,tend])
    plt.ylim([-20,20])
    plt.ylabel("X",fontsize=20)
    plt.subplot(3,1,2)
    plt.plot(Et,Ey,'b',linewidth=1.0)
    plt.plot(Ot,Oy,'r',linewidth=1.0)
    plt.xlim([0,tend])
    plt.ylim([-30,30])
    plt.ylabel("Y",fontsize=20)
    plt.subplot(3,1,3)
    plt.plot(Et,Ez,'b',linewidth=1.0)
    plt.plot(Ot,Oz,'r',linewidth=1.0)
    plt.xlim([0,tend])
    plt.ylim([0,50])
    plt.ylabel("Z",fontsize=20)
    plt.xlabel("Time (t)",fontsize=20)
    
    
    prex=[]
    prey=[]
    prez=[]
    pret=[]
    posx=[]
    posy=[]
    posz=[]
    post=[]
    
    Ass=open(preA,'r')
    da=csv.reader(Ass,delimiter=';')
    for line in da:
        pret.append(float(line[0]))
        prex.append(float(line[1]))
        prey.append(float(line[2]))
        prez.append(float(line[3]))
    Ass.close()
       
    Ass=open(obsA,'r')
    da=csv.reader(Ass,delimiter=';')
    for line in da:
        post.append(float(line[0]))
        posx.append(float(line[1]))
        posy.append(float(line[2]))
        posz.append(float(line[3]))
    Ass.close()
    # plots the average ensemble before assimilation
    plt.figure(1)
    plt.subplot(3,1,1)
    plt.plot(post,posx,'.',color='black',markersize=7.0)
    plt.ylim([-20,20])
    plt.subplot(3,1,2)
    plt.plot(post,posy,'.',color='black',markersize=7.0)
    plt.ylim([-30,30])
    plt.subplot(3,1,3)
    plt.plot(post,posz,'.',color='black',markersize=7.0)
    plt.ylim([0,50])    
    
    # Plots the observation
    plt.figure(2)
    plt.subplot(3,1,1)
    plt.title("Observation and Ensemble with an ensemble size of m = " +str(m)+ ", assim step = " +str(nstep)+ ", inflation = " +str(inf)+ ", dt = " +str(dt)+" ,Blue=ensemble, Red=truth",fontsize=16)
    plt.plot(Ot,Ox,'r',linewidth=1.0)
    plt.xlim([0,tend])
    plt.ylim([-20,20])
    plt.ylabel("X",fontsize=20)
    plt.subplot(3,1,2)
    plt.plot(Ot,Oy,'r',linewidth=1.0)
    plt.xlim([0,tend])
    plt.ylim([-30,30])
    plt.ylabel("Y",fontsize=20)
    plt.subplot(3,1,3)
    plt.plot(Ot,Oz,'r',linewidth=1.0)
    plt.xlim([0,tend])
    plt.ylim([0,50])
    plt.ylabel("Z",fontsize=20)
    plt.xlabel("Time (t)",fontsize=20)
    
    # Plots the ensemble average
    plt.figure(3)
    plt.subplot(3,1,1)
    plt.title("Ensemble average and Ensemble with an ensemble size of m = " +str(m)+ ", assim step = " +str(nstep)+ ", inflation = " +str(inf)+ ", dt = " +str(dt)+" ,Blue=ensemble, Red=ensemble average",fontsize=16)
    plt.plot(Et,Ex,'r',linewidth=1.0)
    plt.xlim([0,tend])
    plt.ylim([-20,20])
    plt.ylabel("X",fontsize=20)
    plt.subplot(3,1,2)
    plt.plot(Et,Ey,'r',linewidth=1.0)
    plt.xlim([0,tend])
    plt.ylim([-30,30])
    plt.ylabel("Y",fontsize=20)
    plt.subplot(3,1,3)
    plt.plot(Et,Ez,'r',linewidth=1.0)
    plt.xlim([0,tend])
    plt.ylim([0,50])
    plt.ylabel("Z",fontsize=20)
    plt.xlabel("Time (t)",fontsize=20)
    

def plotens(m):
    
    # plots indivitual ensembles
    i=0
    while i<m:
        en=open('en%s.txt' % (str(i)),'r')
        
        av=csv.reader(en,delimiter=';')
        Ent=[]
        Enx=[]
        Eny=[]
        Enz=[]
        for line in av:
            Ent.append(float(line[0]))
            Enx.append(float(line[1]))
            Eny.append(float(line[2]))
            Enz.append(float(line[3]))
        en.close()
        
        plt.figure(2)
        plt.subplot(3,1,1)
        plt.plot(Ent,Enx,'b',markersize=1.0)
        plt.ylim([-20,20])
        plt.subplot(3,1,2)
        plt.plot(Ent,Eny,'b',markersize=1.0)
        plt.ylim([-30,30])
        plt.subplot(3,1,3)
        plt.plot(Ent,Enz,'b',markersize=1.0)
        plt.ylim([0,50])
                
        plt.figure(3)
        plt.subplot(3,1,1)
        plt.plot(Ent,Enx,'b',markersize=1.0)
        plt.ylim([-20,20])
        plt.subplot(3,1,2)
        plt.plot(Ent,Eny,'b',markersize=1.0)
        plt.ylim([-30,30])
        plt.subplot(3,1,3)
        plt.plot(Ent,Enz,'b',markersize=1.0)
        plt.ylim([0,50])
                
        i=i+1
def STD():
    # Plotting strandard deviation
    x=[]
    y=[]    
    z=[]
    t=[]
    avgsave=open(stat,'r')
    av=csv.reader(avgsave,delimiter=';')
    for line in av:
        t.append(float(line[0]))
        x.append(float(line[1]))
        y.append(float(line[2]))
        z.append(float(line[3]))
    avgsave.close()

    plt.figure(4)
    plt.subplot(3,1,1)
    plt.title("Standard Deviation with an ensemble size of m = " +str(m)+ ", assim step = " +str(nstep)+ ", inflation = " +str(inf)+ ", dt = " +str(dt),fontsize=16)
    plt.plot(t,x,'b',markersize=0.4,label='x')
    plt.xlim(min(t),max(t))
    plt.ylabel("X Standard Deviation",fontsize=20)
    plt.subplot(3,1,2)
    plt.plot(t,y,'r',markersize=0.4,label='y')
    plt.xlim(min(t),max(t))
    plt.ylabel("Y Standard Deviation",fontsize=20)
    plt.subplot(3,1,3)
    plt.plot(t,z,'g',markersize=0.4,label='z')
    plt.xlim(min(t),max(t))
    plt.ylabel("Z Standard Deviation",fontsize=20)
    plt.xlabel("Time (t)")        
    
def Prplot():
    # Plotting the average
    Et=[]
    sig=[]
    b=[]
    r=[]
    # The average ensemble file
    avgsave=open(Eavg,'r')
    av=csv.reader(avgsave,delimiter=';')
    for line in av:
        Et.append(float(line[0]))
        sig.append(float(line[4]))
        r.append(float(line[5]))
        b.append(float(line[6]))
    avgsave.close()
    
    plt.figure(5)
    plt.subplot(3,1,1)
    plt.title("Parameter variations with an ensemble size of m = " +str(m)+ ", assim step = " +str(nstep)+ ", inflation = " +str(inf)+ ", dt = " +str(dt),fontsize=16)
    plt.plot(Et,sig,'b',linewidth=1.0)
    plt.axhline(y=10.0,c="red",linewidth=2.0)
    plt.xlim([0,tend])
    plt.ylabel("$\sigma$",fontsize=20)
    plt.subplot(3,1,2)
    plt.plot(Et,r,'b',linewidth=1.0)
    plt.axhline(y=28.0,c="red",linewidth=2.0)
    plt.xlim([0,tend])
    plt.ylabel("r",fontsize=20)
    plt.subplot(3,1,3)
    plt.plot(Et,b,'b',linewidth=1.0)
    plt.axhline(y=8.0/3.0,c="red",linewidth=2.0)
    plt.xlim([0,tend])
    plt.ylabel("b",fontsize=20)
    plt.xlabel("Time (t)",fontsize=20)
    
    SD=np.std(sig)
    ME=np.mean(sig)
    plt.figure(6)
    plt.title("$\sigma$ distribution m = " +str(m)+ ", assim step = " +str(nstep)+ ", inflation = " +str(inf)+ ", dt = " +str(dt),fontsize=16)
    plt.hist(sig, bins='auto',normed=1)
    plt.ylabel("Frequency",fontsize=20)
    plt.xlabel("$\sigma$",fontsize=20)
    xs=[10.0]*100
    ys=np.linspace(0,0.15,100)
    plt.plot(xs,ys,c="red",linewidth=2.0)
    plt.text(0,0.15,'Mean =' +str("{0:.3f}".format(ME))+ '\n' +'SD ='+str("{0:.3f}".format(SD)) + '\n' + 'True value = 10.000',fontsize=15,bbox=dict(boxstyle='round', facecolor='white', alpha=1.0))
    plt.tight_layout()
    
    SD=np.std(r)
    ME=np.mean(r)
    plt.figure(7)
    plt.title("r distribution m = " +str(m)+ ", assim step = " +str(nstep)+ ", inflation = " +str(inf)+ ", dt = " +str(dt),fontsize=16)
    plt.hist(r, bins='auto',normed=1)
    plt.ylabel("Frequency",fontsize=20)
    plt.xlabel("r",fontsize=20)
    xs=[28.0]*100
    ys=np.linspace(0,0.4,100)
    plt.plot(xs,ys,c="red",linewidth=2.0)
    plt.text(30,0.30,'Mean =' +str("{0:.3f}".format(ME))+ '\n' +'SD ='+str("{0:.3f}".format(SD)) + '\n' + 'True value = 28.000',fontsize=15,bbox=dict(boxstyle='round', facecolor='white', alpha=1.0))
    plt.tight_layout()
    
    SD=np.std(b)
    ME=np.mean(b)
    plt.figure(8)
    plt.title("b distribution m = " +str(m)+ ", assim step = " +str(nstep)+ ", inflation = " +str(inf)+ ", dt = " +str(dt),fontsize=16)
    plt.hist(b, bins='auto',normed=1)
    plt.ylabel("Frequency",fontsize=20)
    plt.xlabel("b",fontsize=20)
    bval=8.0/3.0
    xs=[8.0/3.0]*100
    ys=np.linspace(0,0.5,100)
    plt.plot(xs,ys,c="red",linewidth=2.0)
    plt.text(4,0.6,'Mean =' +str("{0:.3f}".format(ME))+ '\n' +'SD ='+str("{0:.3f}".format(SD)) + '\n' + 'True value =' +str("{0:.3f}".format(bval)),fontsize=15,bbox=dict(boxstyle='round', facecolor='white', alpha=1.0))
    plt.tight_layout()