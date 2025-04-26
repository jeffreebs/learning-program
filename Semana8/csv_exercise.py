import csv


def add_video_games ():

    video_games = []

    x= int(input("How many video games do you want to add ??"))

    for i in range(x):
        name= input( "Please enter the video game name : ")
        gender = input ( "Please enter the video game gender :")
        developer = input (" Please enter the video game developer : ")
        classification = input ( "Please enter the classification : ")


        video_game = {
        "name" : name,
        "gender" : gender,
        "developer" : developer,
        "classification" : classification

        }

        video_games.append(video_game)


    return video_games

def save_in_csv(video_games ):
    with open ("video_games.csv", "w") as file:
        space = ["name","gender","developer", "classification"]
        writer = csv.DictWriter(file, fieldnames = space)


        writer.writeheader()
        writer.writerows(video_games)

    print("The video games data saved in 'video_games.csv ' ")


if __name__ == "__main__":
    video_games = add_video_games()
    save_in_csv(video_games)