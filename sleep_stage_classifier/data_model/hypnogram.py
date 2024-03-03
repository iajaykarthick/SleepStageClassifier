import matplotlib.pyplot as plt

from sleep_stage_classifier.data_model.edf_file import EDFFile


class Hypnogram(EDFFile):
    def __init__(self, file_path):
        super().__init__(file_path)
    
    def get_annotations(self):
        self.open()
        annotations = self.file.readAnnotations()
        return annotations

    
    def plot_stages(self):
        annotations = self.get_annotations()
        hypno_onsets, _, hypno_stages = annotations

        # Convert stages to integers for plotting
        stage_mapping = {'Sleep stage W': 0, 'Sleep stage 1': 1, 'Sleep stage 2': 2, 'Sleep stage 3': 3, 'Sleep stage 4': 3, 'Sleep stage R': 4, 'Movement time': 5, 'Sleep stage ?': 6}
        mapped_hypno_stages = [stage_mapping[stage] for stage in hypno_stages]
        
        plt.figure(figsize=(15, 3))
        plt.step(hypno_onsets, mapped_hypno_stages, where='post')
        plt.yticks(list(stage_mapping.values()), list(stage_mapping.keys()))
        plt.title('Hypnogram')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Sleep Stage')
        plt.show()