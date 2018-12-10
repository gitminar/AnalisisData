"""
Program untuk menganalisis data dari suatu sumber,
diproses dan ditampilkan hasilnya
"""

from acquire import twitter
from process import decision_tree
from views import text

data = twitter.get_data() #acquire
result = decision_tree.process_data(data) #process
display = text.as_text(result) #views

print(display)
