class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        
        res = 0
        for word, coef in zip(words, coefs):
            res += len(word) * coef
        return res


    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        
        res = 0
        for i in range(len(words)):
            res += len(words[i]) * coefs[i]
        return res


# if __name__ == "__main__":
#     words1 = ["Le", "Lorem", "Ipsum", "est", "simple"]
#     coefs1 = [1.0, 2.0, 1.0, 4.0, 0.5]
#     print(Evaluator.zip_evaluate(coefs1, words1))
    
#     words2 = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
#     coefs2 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
#     print(Evaluator.enumerate_evaluate(coefs2, words2))
