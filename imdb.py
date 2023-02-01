import json
with open("imdb_movies_1985to2022.json", "r") as f:
    num_movies_hj = 0
    rating_total_hj = 0
    num_movies_rr = 0
    rating_total_rr = 0
    for line in f:
        this_movie = json.loads(line)
        for actor in this_movie['actors']:
            if actor == "Hugh Jackman":
                num_movies_hj += 1
                rating_total_hj += this_movie['rating']["avg"]
            if actor == "Ryan Reynolds":
                num_movies_rr +=1 
                rating_total_rr += this_movie['rating']["avg"]
        
    avg_rating_hj = float(rating_total_hj)/float(num_movies_hj)
    avg_rating_rr = float(rating_total_rr)/float(num_movies_rr)
    print("Hugh Jackman Avg Rating: ", avg_rating_hj)
    print("Ryan Reynolds Avg Rating: ", avg_rating_rr)       
    
   