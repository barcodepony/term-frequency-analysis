import preprocessing
import preprocessing_pseudo
X = [["hallo","wie","geht","es","dir","denn","so"],
     ["alle","meine","freunde","geht","es","gut"],
     ["das","ist","der","letze","test","satz"],
     ["alle", "meine", "freunde", "geht", "es", "gut"]
     ]

N = len(X)
k = 2

def test(X=X, N=N, k=k):
    x, y = preprocessing.preprocess(X, N, k)
    print(x)
    print(y)

if __name__ == "__main__":
    test()