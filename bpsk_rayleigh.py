
import numpy as np
import pandas as pd 
from numpy import random
import matplotlib.pyplot as plt
# import cmath



# the number of bits per frame, default 10000 bits per frame
bit_per_frame = 10000
# the number of frames
number_frame = 1000
# range of examined signal-to-noise ratio, in dB
SNR_array = np.array([0,5,10,20,30,40,50])
print(SNR_array)

BER_array = []

# a = np.random.rand(1,10)
# print(a)

for snr in SNR_array:
	# initialize the bit error counter per frame
	T_errors = 0
	# total bits transmitted
	T_bits = 0
	# print('check',snr)

	for i in range(number_frame):
		# print('check',i)
		uncoded_bits = np.round(random.rand(1,bit_per_frame))
		# print(uncoded_bits)
		tx_bpsk = 2*uncoded_bits - 1
		# print(tx_bpsk,len(tx_bpsk[0]))
		# noise variance
		N0 = 1/(10**(snr/10))
		# print(N0)
		# Rayleigh channel fading
		h = 1/np.sqrt(2)*(random.randn(1,bit_per_frame)+random.randn(1,bit_per_frame)*1j)
		# print(h)
		rx = tx_bpsk*h + np.sqrt(N0/2)*(random.randn(1,bit_per_frame)+random.randn(1,bit_per_frame)*1j)

		rx_remove_fading = rx/h
		# print(rx_remove_fading)

		rx_demodulated = (rx_remove_fading > 0)*1
		# print(rx_demodulated)

		diff = rx_demodulated - uncoded_bits
		# print(diff)
		T_errors = T_errors + np.sum(np.abs(diff))
		# print(T_errors)
		T_bits = T_bits + bit_per_frame
	BER_array.append(T_errors/T_bits)
	print('bit error probability =', T_errors/T_bits)

line_sim, = plt.scatter(SNR_array, BER_array, c='blue')


SNR_dec = 10**(SNR_array/10)
# print(SNR_dec)
theoryBer = 0.5*(1-np.sqrt(SNR_dec/(SNR_dec+1)))
# print(theoryBer)
line_theory, = plt.plot(SNR_array, theoryBer, c='red') # checked the calculation


plt.yscale('log')
plt.legend([line_sim, line_theory], ['Sim', 'Theory'])
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.grid(linewidth=0.2)



plt.show()




