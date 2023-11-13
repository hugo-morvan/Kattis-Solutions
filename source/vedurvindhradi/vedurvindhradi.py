wind = float(input())
wind = int(wind*10)
buckets = [0,2,15,33,54,79,107,138,171,207,244,284,326,2000]
names = ["Logn","Andvari","Kul","Gola","Stinningsgola","Kaldi","Stinningskaldi", "Allhvass vindur", "Hvassvidri", "Stormur", "Rok", "Ofsavedur", "Farvidri"]
for i in range(len(buckets)):
    if wind < buckets[i]:
        print(names[i-1])
        break