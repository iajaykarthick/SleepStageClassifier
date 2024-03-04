import numpy as np
import matplotlib.pyplot as plt


def plot_signal_with_stages(psg_object, hypnogram_object, signal_label):
    psg_object.open()
    hypnogram_object.open()
    
    signal_data = psg_object.get_signal(signal_label)
    sampling_rate = psg_object.get_sampling_frequency(signal_label)
    signal_times = np.arange(signal_data.size) / sampling_rate

    hypno_onsets, hypno_durations, hypno_stages = hypnogram_object.get_annotations()

    

    hypno_stages = ['light' if stage in ['Sleep stage 1', 'Sleep stage 2']  else stage for stage in hypno_stages]
    hypno_stages = ['deep' if stage in ['Sleep stage 3', 'Sleep stage 4']  else stage for stage in hypno_stages]
    hypno_stages = ['rem' if stage == 'Sleep stage R'  else stage for stage in hypno_stages]
    hypno_stages = ['wake' if stage == 'Sleep stage W'  else stage for stage in hypno_stages]

    stage_mapping = {
        'wake': 4, 
        'rem': 3, 
        'light': 2, 
        'deep': 1
    }
    
    mapped_hypno_stages = [stage_mapping[stage] for stage in hypno_stages]


    hypno_plot_times = []
    hypno_plot_stages = []
    for onset, duration, stage in zip(hypno_onsets, hypno_durations, mapped_hypno_stages):
        hypno_plot_times.extend([onset, onset + duration])
        hypno_plot_stages.extend([stage, stage])

    fig, ax1 = plt.subplots(figsize=(15, 6))


    ax1.plot(signal_times, signal_data, 'b-')
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel(signal_label, color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.step(hypno_plot_times, hypno_plot_stages, where='post', color='r')
    ax2.set_ylabel('Sleep Stage', color='r')
    ax2.tick_params('y', colors='r')
    ax2.set_yticks(list(stage_mapping.values()))
    ax2.set_yticklabels(list(stage_mapping.keys()))

    plt.title(f'{signal_label} with sleep stages')
    fig.tight_layout()
    plt.show()


    psg_object.close()
    hypnogram_object.close()



def plot_all_signals_with_stages(psg_object, hypnogram_object):
    psg_object.open()
    hypnogram_object.open()
    
    signal_labels = psg_object.get_signal_labels()
    num_signals = len(signal_labels)
    fig, axs = plt.subplots(num_signals, 1, figsize=(15, num_signals * 3), sharex=True)
    
    hypno_onsets, hypno_durations, hypno_stages = hypnogram_object.get_annotations()
    

    hypno_stages = ['light' if stage in ['Sleep stage 1', 'Sleep stage 2']  else stage for stage in hypno_stages]
    hypno_stages = ['deep' if stage in ['Sleep stage 3', 'Sleep stage 4']  else stage for stage in hypno_stages]
    hypno_stages = ['rem' if stage == 'Sleep stage R'  else stage for stage in hypno_stages]
    hypno_stages = ['wake' if stage == 'Sleep stage W'  else stage for stage in hypno_stages]

    stage_mapping = {
        'wake': 4, 
        'rem': 3, 
        'light': 2, 
        'deep': 1
    }
    
    mapped_hypno_stages = [stage_mapping.get(stage, 5) for stage in hypno_stages] 

    hypno_plot_times = []
    hypno_plot_stages = []
    for onset, duration, stage in zip(hypno_onsets, hypno_durations, mapped_hypno_stages):
        hypno_plot_times.extend([onset, onset + duration])
        hypno_plot_stages.extend([stage, stage])

    for i, label in enumerate(signal_labels):
        signal_data = psg_object.get_signal(label)
        sampling_rate = psg_object.get_sampling_frequency(label)
        signal_times = np.arange(signal_data.size) / sampling_rate
        
        axs[i].plot(signal_times, signal_data, 'b-')  
        axs[i].set_ylabel(label)
        
        ax2 = axs[i].twinx()
        ax2.step(hypno_plot_times, hypno_plot_stages, where='post', color='r')
        ax2.set_ylabel('Sleep Stage', color='r')
        ax2.tick_params('y', colors='r')
        
        sorted_stage_items = sorted(stage_mapping.items(), key=lambda x: x[1])
        ax2.set_yticks([item[1] for item in sorted_stage_items])
        ax2.set_yticklabels([item[0] for item in sorted_stage_items])
    
    plt.xlabel('Time (seconds)')
    plt.tight_layout()
    plt.show()

    psg_object.close()
    hypnogram_object.close()