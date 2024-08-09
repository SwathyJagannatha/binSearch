# You can use this list video_titles in your Python code for further processing or manipulation.

# Task 1:

# Implement the binary search algorithm for searching videos by title.
# Task 2:

# Develop a REST API endpoint using Flask that allows users to search for videos by their titles using the binary search developed in Task 1. This API should accept a search query as input and return the matching videos, if any.
# Task 3:

# Test the video search functionality using Postman or a similar tool. Send requests to the API endpoint created in Task 2 with different search queries to verify its correctness and efficiency. Ensure that the API returns the expected results for both existing and non-existing videos.

from flask import Flask,request,jsonify

#www.127.0.0.1:5000/search_name?search_query=Exploring the Cosmos
app = Flask(__name__)

@app.route('/search_video',methods=['GET'])
def search_videos():
    video_query = request.args.get('search_query')
    print(search_video_bytitle(video_titles,video_query))
    return jsonify('success'),200

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

#binary search on title
def search_video_bytitle(video_titles,title):
    video_titles.sort()
    #print("after sorting")
    #print(video_titles)
    start = 0 
    end = len(video_titles)-1

    while start <= end:
        mid = (start+end)//2

        if video_titles[mid] == title:
            return f"Video with title {title} is found at position {mid}"
        elif title < video_titles[mid]:
            end = mid-1
        else:
            start = mid+1

    return f"Video with title {title} isnt found"



if __name__ == '__main__':
    app.run(debug=True)