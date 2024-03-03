import numpy as np
import matplotlib.pyplot as plt

from sleep_stage_classifier.data_model.edf_file import EDFFile


class PSG(EDFFile):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_signal_labels(self):
        self.open()
        return self.file.getSignalLabels()

    def get_signal(self, label):
        self.open()
        signal_index = self.get_signal_labels().index(label)
        return self.file.readSignal(signal_index)

    def get_sampling_frequency(self, label):
        self.open()
        signal_index = self.get_signal_labels().index(label)
        return self.file.getSampleFrequency(signal_index)
    
    
    def plot_signal(self, label, start_time=0, end_time=None):
        self.open()
        signal_index = self.get_signal_labels().index(label)
        sampling_rate = self.get_sampling_frequency(label)
        
        signal = self.get_signal(label)
        times = np.arange(signal.size) / sampling_rate
        
        if end_time is not None:
            signal = signal[int(start_time*sampling_rate):int(end_time*sampling_rate)]
            times = times[int(start_time*sampling_rate):int(end_time*sampling_rate)]
        
        plt.figure(figsize=(15, 5))
        plt.plot(times, signal)
        plt.title(f'Signal: {label}')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.show()