import instaloader
import getpass

def search_instagram_jobs(hashtags=None, max_posts=5):
    if hashtags is None:
        hashtags = ["vagasfrota", "trabalhefrota", "vagasfleet", "empregosbrasil"]

    L = instaloader.Instaloader()

    # Prompt for login securely
    username = input("Instagram username: ")
    password = getpass.getpass("Instagram password: ")
    try:
        L.login(username, password)
    except Exception as e:
        print("Login failed:", e)
        return []

    results = []

    for tag in hashtags:
        try:
            posts = instaloader.Hashtag.from_name(L.context, tag).get_posts()
            count = 0
            for post in posts:
                caption = post.caption if post.caption else ""
                if "brasil" in caption.lower() or "sp" in caption.lower() or "rio" in caption.lower():
                    results.append({
                        "company": post.owner_username,
                        "role": caption.split('\n')[0] if caption else "Unknown",
                        "location": "Brazil",
                        "link": post.url,
                        "caption": caption
                    })
                    count += 1
                if count >= max_posts:
                    break
        except Exception as e:
            print(f"Error with hashtag {tag}: {e}")

    return results

if __name__ == "__main__":
    jobs = search_instagram_jobs(max_posts=5)
    print(f"Found {len(jobs)} Instagram fleet jobs:\n")
    for j in jobs:
        print(j["company"], "-", j["role"], "-", j["location"])
        print("Link:", j["link"])
        print("--------------------------")
