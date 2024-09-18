import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def findavg(smoothdata):
    smoothdata = smoothdata.reshape(24, 60)
    avg = np.mean(smoothdata, axis = 1)
    return avg

def main():
    np.random.seed(0)
    trafficdata = np.random.poisson(size = 1440)
    noise = np.random.normal(0, 5, 1440)

    noisyd = trafficdata + noise

    # smoothdata = []
    smoothdata = savgol_filter(noisyd, window_length=100, polyorder = 2)
    
    plt.figure(1)
    plt.plot(noisyd, smoothdata)
    plt.xlabel("Noisy Data")
    plt.ylabel("Smooth Data")
    plt.show()

    avg = findavg(smoothdata)                           
    print(f"average number of vehicles: {avg}")

    plt.figure(2)
    plt.plot(noisyd, label='noisydata')
    plt.plot(smoothdata, label='smoothdata')
    plt.xlabel("time")
    plt.ylabel("no of vehicles")
    plt.title("vehical distribution graph")
    plt.show()

    exceed100=np.where(smoothdata> 100)[0]
                               
main()



    

    
    

    

        
        

        

    
