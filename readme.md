# Prerequisites
* Refer to PRAW [Quick Start](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html#quick-start)

# Usage
1. Download the project as a `.zip`, extract it
2. Replace `client_id`, `client_secret`, `user_agent` with your values
    ```
    reddit = praw.Reddit(client_id="##replace_me##",
                        client_secret="##replace_me##",
                        user_agent="##replace_me##")
    ```
3. Change `linkIds` to your desired post(s)
    ```
    linkIds = ['jshxam', '...', '...']
    ```
4. Open terminal inside the directory and run 
    ```
    python3 posts.py
    ```
5. Your files are outputted to the working directory, with the link ID as the file name

---
### Please note that this version does not have any error-handling and has not been tested at scale. On average, a post with ~2000 comments takes 45 seconds