# Video Sorting with Merge Sort
# Objective: The objective of this assignment is to implement the merge sort algorithm to sort a list of videos based on their titles.

# Problem Statement: You are tasked with developing a video sorting function that sorts a list of videos alphabetically by their titles using the merge sort algorithm. This application will help users organize their video collections more efficiently. You should use the previous assignment project.

# Task 1:

# Implement the merge sort algorithm in Python to sort videos by their titles..
# Task 2:

# Develop another REST API endpoint using Flask that allows users to fetch a list of videos sorting alphabetically by their titles using the merge sort developed in Task 1.
# Task 3:

# Test the video sorting functionality using Postman or a similar tool. Send requests to the API endpoint created in Task 2 and verify its correctness and efficiency. Ensure that the API returns the expected results.


# Task 1:

# Implement the merge sort algorithm in Python to sort videos by their titles..
# Task 2:

# Develop another REST API endpoint using Flask that allows users to fetch a list of videos sorting alphabetically by their titles using the merge sort developed in Task 1.
# Task 3:

# Test the video sorting functionality using Postman or a similar tool. Send requests to the API endpoint created in Task 2 and verify its correctness and efficiency. Ensure that the API returns the expected results.

from flask import Flask,request,jsonify

#www.127.0.0.1:5000/search_name
app = Flask(__name__)

@app.route('/search_video',methods=['GET'])
def search_videos():
    sort_by_title(video_titles)
    print(video_titles)
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

def sort_by_title(videos):
    if len(videos) > 1:
        mid = len(videos)//2
        left_side = videos[:mid]
        right_side= videos[mid:]

        sort_by_title(left_side)
        sort_by_title(right_side)

        i=0
        j=0
        k=0

        while j< len(left_side) and k < len(right_side):
            if left_side[j] < right_side[k]:
                videos[i] = left_side[j]
                i = i+1
                j += 1
            else:
                videos[i] = right_side[k]
                i +=1
                k +=1

        while j < len(left_side):
            videos[i] = left_side[j]
            i +=1
            j +=1

        while k < len(right_side):
            videos[i] = right_side[k]
            i +=1
            k +=1


if __name__ == '__main__':
    app.run(debug=True)