from mplsoccer import Pitch
import matplotlib.pyplot as plt
#this line is for where the shot from
x=[85,80,60,55]
y=[40,50,80,75]
#short reults(goal=1,miss=0)
result=[0,1,1,0]
Pitch=Pitch(pitch_type="statsbomb",pitch_color="grass",line_color="white")
fig,ax=Pitch.draw()
for i in range(len(x)):
    if result[i]==1:
        Pitch.scatter(x[i],y[i],ax=ax,color="green",s=200,label="goal")
    else:
        Pitch.scatter(x[i],y[i],ax=ax,color="white",s=200,label="missed")
plt.title("goal vs shot map")
plt.legend(loc="upper left")
plt.show()



