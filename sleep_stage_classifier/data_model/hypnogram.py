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
        
        plt.figure(figsize=(15, 3))
        plt.step(hypno_onsets, mapped_hypno_stages, where='post')
        plt.yticks(list(stage_mapping.values()), list(stage_mapping.keys()))
        plt.title('Hypnogram')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Sleep Stage')
        plt.show()