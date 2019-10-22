import pickle
from singer import Singer

singer = Singer("I'll stand by you")

with open('/Users/ryusuke/Downloads/KTH/practice/pickle/singer.pickle', 'wb') as f:
    pickle.dump(singer, f)
