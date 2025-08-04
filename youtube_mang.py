import json
import timer



def load_data():
    try:
        with open('youtube.txt','r')as file:
            test= json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []
    

def save_data_help(videos):
    with open('youtube.txt','w')as file:
        json.dump(videos,file)

        
    
def list_all_videos(videos):
    # for index,video in enumerate(videos,start=1):
    # #     print(f"{index}")
    # for vid in videos:
    #     print(f"{vid}.")
    for index,video in enumerate(videos, start=1):
        print("\n")
        print("*"  * 70)
        print(f"{index}.{video['name']}, Duration :{video['time']}")
        print("*"  * 70)

def add_videos(videos):
    name=input("enter video name:")
    time=input("enter video time:")
    videos.append({'name':name,'time':time})
    save_data_help(videos)



def update_videos(videos):
    list_all_videos(videos)
    x=input("enter the video number to update")
    if 1<=x<=len(videos):
        name=inpput("enter the movie")
        time=input("enter the new video")
        videos[x-1]={'name':name, 'time':time
        }
        save_data_help(videos)
    else:
        print("invalid index selector")

    
def delete_videos(videos):
    list_all_videos(videos)
    index=int(input("enter the video number to be deleted"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_help(videos)
    else:
        print("invalid video index")

    pass

def main():
    videos=load_data()

    while True:
        print("\n Youtube Manager | choose an option" )
        print(" 1 .List all Favourite videos")
        print(" 2 .Add a youtube video")
        print(" 3 .Update a Youtube Details")
        print(" 4. Delete a Youtube Video")
        print(" 5 .Exit the app")
        
        print(videos)

        choice=input("enter You choice")

        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("invalid choice")

            
if __name__ == "__main__":
    main()



