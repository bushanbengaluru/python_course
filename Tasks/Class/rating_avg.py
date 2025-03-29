class Ratings:
    def __init__ (self, no_ratings, rating_given):
        self.no_ratings = no_ratings
        self.rating_given = rating_given
    def avg_rating(self):
        self.avg_rating = (self.no_ratings//self.rating_given)
        if self.avg_rating < 1:
            return ("*")
        elif (self.avg_rating > 1 & self.avg_rating < 5):
            return ("*" * self.avg_rating)
        else:
            return ("*****")
r = Ratings(8,4)
avg_rating = r.avg_rating()
print(avg_rating)