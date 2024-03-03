import numpy as np
import matplotlib.pyplot as plt


def plot_signal_with_stages(psg_object, hypnogram_object, signal_label):
    psg_object.open()
    hypnogram_object.open()
    
    signal_data = psg_object.get_signal(signal_label)
    sampling_rate = psg_object.get_sampling_frequency(signal_label)
    signal_times = np.arange(signal_data.size) / sampling_rate

    hypno_onsets, hypno_durations, hypno_stages = hypnogram_object.get_annotations()

    
    stage_mapping = {'Sleep stage W': 0, 'Sleep stage 1': 1, 'Sleep stage 2': 2, 
                     'Sleep stage 3': 3, 'Sleep stage 4': 3, 'Sleep stage R': 4, 
                     'Movement time': 5, 'Sleep stage ?': 6}
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

    plt.title('Signal and Hypnogram')
    fig.tight_layout()
    plt.show()


    psg_object.close()
    hypnogram_object.close()

