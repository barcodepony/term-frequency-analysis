import preprocessing

X = [["hallo","wie","geht","es","dir","denn","so"],
     ["alle","meine","freunde","geht","es","gut"],
     ["das","ist","der","letze","test","satz"],
     ["alle", "meine", "freunde", "geht", "es", "gut"]
     ]

N = len(X)
k = 2

def test(X=X, N=N, k=k):
    preprocessing.preprocess(X, N, k)

if __name__ == "__main__":
    test()