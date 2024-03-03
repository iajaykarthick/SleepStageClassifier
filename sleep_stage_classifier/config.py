import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'sleep-edf-database-expanded-1.0.0', 'edf')
PARTICIPANT_SHEET_XLS = {
        "SC": os.path.join(BASE_DIR, 'data', 'sleep-edf-database-expanded-1.0.0', 'SC-participants.xls'),
        "ST": os.path.join(BASE_DIR, 'data', 'sleep-edf-database-expanded-1.0.0', 'ST-participants.xls'),
}

PARTICIPANT_SHEET = os.path.join(BASE_DIR, 'data', 'sleep-edf-database-expanded-1.0.0', 'participants.csv')